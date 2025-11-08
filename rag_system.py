import os
import re
import logging
from typing import List, Dict, Tuple, Optional, Union
from datetime import datetime
import torch
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
import warnings
warnings.filterwarnings("ignore")

# LlamaIndex imports
from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    Settings,
    Document
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.retrievers import VectorIndexRetriever, BaseRetriever
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from elasticsearch import Elasticsearch
from llama_index.retrievers.bm25 import BM25Retriever

# Import question classifier
from question_classifier import QuestionClassifier

# Import reranker
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'testing-features'))
from qwen3_reranker_transformers import Qwen3Reranker

class RAGConfig:
    """Configuration for RAG system"""
    # Model configurations
    EMBEDDING_MODEL = "Qwen/Qwen3-Embedding-0.6B"
    GENERATION_MODEL = "Qwen/Qwen3-0.6B"
    
    # RAG parameters
    TOP_K = 6
    CHUNK_SIZE = 400
    CHUNK_OVERLAP = 50
    
    # File paths
    DOCUMENT_PATH = "documents"
    QUESTIONS_PATH = "Question-Bank-GD4.csv"
    TRUE_RESULTS_PATH = "Answer-for-question-bank-gd4.md"
    
    # Elasticsearch configuration
    ELASTICSEARCH_URL = "http://localhost:9200"  # Hoặc Elastic Cloud URL
    ELASTICSEARCH_INDEX = "vietnamese_mcq_rag"   # Index name
    ELASTICSEARCH_USER = None  # Nếu có authentication
    ELASTICSEARCH_PASSWORD = None  # Nếu có authentication
    
    # Hybrid retrieval parameters
    HYBRID_ALPHA = 0.5  # 0.0 = chỉ keyword, 1.0 = chỉ vector, 0.5 = balanced
    HYBRID_TOP_K = 10    # Số kết quả từ mỗi method trong hybrid search (10 vector + 10 keyword = 20)
    HYBRID_COMBINED_TOP_K = 10  # Số kết quả sau khi combine (từ 20 → 10)
    
    # Query reformulation parameters
    REFORMULATION_ENABLED = True  # Enable/disable query reformulation
    REFORMULATION_TEMPERATURE = 0.7  # Temperature for reformulation generation
    REFORMULATION_MAX_TOKENS = 1024  # Maximum tokens for reformulated query
    
    # Reranker parameters
    RERANKER_MODEL = "Qwen/Qwen3-Reranker-0.6B"
    RERANKER_ENABLED = True  # Enable/disable reranker
    RERANKER_MAX_LENGTH = 2048  # Maximum length for reranker input
    RERANKER_TOP_K = 5  # Số kết quả sau rerank (từ 10 → 5)
    RERANKER_INSTRUCTION = "Given the user query, retrieve the relevant passages that answer the query"

class Qwen3EmbeddingLlamaIndex(BaseEmbedding):
    """Custom Qwen3 Embedding class integrated with LlamaIndex"""
    
    def __init__(self, 
                 model_name_or_path: str = "Qwen/Qwen3-Embedding-0.6B",
                 instruction: str = None,
                 use_fp16: bool = True,
                 use_cuda: bool = True,
                 max_length: int = 8192,
                 embed_batch_size: int = 32,
                 **kwargs):
        
        # Initialize parent class first with only recognized parameters
        super().__init__(embed_batch_size=embed_batch_size, **kwargs)
        
        # Store custom attributes in a separate dict to avoid field validation issues
        if instruction is None:
            instruction = 'Given a web search query, retrieve relevant passages that answer the query'
        
        # Use __dict__ to bypass field validation
        self.__dict__['qwen_instruction'] = instruction
        self.__dict__['qwen_max_length'] = max_length
        self.__dict__['qwen_device'] = "cuda:0" if use_cuda and torch.cuda.is_available() else "cpu"
        
        # Load model with optimizations
        qwen_model = AutoModel.from_pretrained(
            model_name_or_path, 
            trust_remote_code=True, 
            torch_dtype=torch.float16 if use_fp16 else torch.float32
        )
        
        # Move to device and store
        self.__dict__['qwen_model'] = qwen_model.to(self.__dict__['qwen_device'])
        
        # Load tokenizer
        self.__dict__['qwen_tokenizer'] = AutoTokenizer.from_pretrained(
            model_name_or_path, 
            trust_remote_code=True, 
            padding_side='left'
        )
    
    def last_token_pool(self, last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
        """Last token pooling strategy for Qwen3"""
        left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
        if left_padding:
            return last_hidden_states[:, -1]
        else:
            sequence_lengths = attention_mask.sum(dim=1) - 1
            batch_size = last_hidden_states.shape[0]
            return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]
    
    def get_detailed_instruct(self, task_description: str, query: str) -> str:
        """Format instruction for query according to Qwen3 requirements"""
        if task_description is None:
            task_description = self.__dict__['qwen_instruction']
        return f'Instruct: {task_description}\nQuery: {query}'
    
    def _embed_batch(self, texts: List[str], is_query: bool = False) -> List[List[float]]:
        """Internal method to embed a batch of texts"""
        # Format queries with instruction prefix
        if is_query:
            texts = [self.get_detailed_instruct(self.__dict__['qwen_instruction'], text) for text in texts]
        
        # Tokenize
        inputs = self.__dict__['qwen_tokenizer'](
            texts, 
            padding=True, 
            truncation=True, 
            max_length=self.__dict__['qwen_max_length'], 
            return_tensors='pt'
        )
        
        # Move to device
        inputs = {k: v.to(self.__dict__['qwen_device']) for k, v in inputs.items()}
        
        with torch.no_grad():
            model_outputs = self.__dict__['qwen_model'](**inputs)
            embeddings = self.last_token_pool(
                model_outputs.last_hidden_state, 
                inputs['attention_mask']
            )
            # L2 normalize
            embeddings = F.normalize(embeddings, p=2, dim=1)
        
        return embeddings.cpu().numpy().tolist()
    
    def _get_query_embedding(self, query: str) -> List[float]:
        """Get embedding for a single query"""
        return self._embed_batch([query], is_query=True)[0]
    
    def _get_text_embedding(self, text: str) -> List[float]:
        """Get embedding for a single document text"""
        return self._embed_batch([text], is_query=False)[0]
    
    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Get embeddings for multiple document texts"""
        return self._embed_batch(texts, is_query=False)
    
    async def _aget_query_embedding(self, query: str) -> List[float]:
        """Async version of get_query_embedding - fallback to sync"""
        return self._get_query_embedding(query)
    
    async def _aget_text_embedding(self, text: str) -> List[float]:
        """Async version of get_text_embedding - fallback to sync"""
        return self._get_text_embedding(text)
    
    async def _aget_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Async version of get_text_embeddings - fallback to sync"""
        return self._get_text_embeddings(texts)
    
    @property
    def _model_name(self) -> str:
        return "Qwen3-Embedding-0.6B"

class Logger:
    """Enhanced logging system for RAG performance tracking"""
    
    def __init__(self, log_file: str = "rag_system.log"):
        self.log_file = log_file
        self.setup_logging()
        self.metrics = {
            "total_questions": 0,
            "correct_answers": 0,
            "partial_answers": 0,
            "wrong_answers": 0,
            "processing_times": [],
            "errors": []
        }
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def log_info(self, message: str):
        self.logger.info(message)
    
    def log_error(self, message: str, exception: Exception = None):
        error_msg = f"{message}"
        if exception:
            error_msg += f" - Exception: {str(exception)}"
        self.logger.error(error_msg)
        self.metrics["errors"].append({
            "timestamp": datetime.now().isoformat(),
            "message": error_msg
        })
    
    def log_question_result(self, question_idx: int, predicted: str, actual: str, 
                          score: float, processing_time: float):
        """Log individual question processing result"""
        self.metrics["total_questions"] += 1
        self.metrics["processing_times"].append(processing_time)
        
        if score == 1.0:
            self.metrics["correct_answers"] += 1
            status = "CORRECT"
        elif score == 0.5:
            self.metrics["partial_answers"] += 1
            status = "PARTIAL"
        else:
            self.metrics["wrong_answers"] += 1
            status = "WRONG"
        
        self.log_info(f"Q{question_idx}: {status} | Predicted: {predicted} | Actual: {actual} | Score: {score} | Time: {processing_time:.2f}s")
    
    def get_summary(self) -> Dict:
        """Get performance summary"""
        total = self.metrics["total_questions"]
        if total == 0:
            return {"error": "No questions processed"}
        
        accuracy = (self.metrics["correct_answers"] + 0.5 * self.metrics["partial_answers"]) / total * 100
        avg_time = sum(self.metrics["processing_times"]) / len(self.metrics["processing_times"]) if self.metrics["processing_times"] else 0
        
        return {
            "total_questions": total,
            "accuracy": accuracy,
            "correct_answers": self.metrics["correct_answers"],
            "partial_answers": self.metrics["partial_answers"],
            "wrong_answers": self.metrics["wrong_answers"],
            "average_processing_time": avg_time,
            "total_errors": len(self.metrics["errors"])
        }


class VietnameseMCQRAG:
    """Main RAG system for Vietnamese MCQ answering"""
    
    def __init__(self, config: RAGConfig = None):
        self.config = config or RAGConfig()
        self.logger = Logger()
        self.index = None
        self.retriever = None  # Add retriever attribute
        self.query_engine = None
        self.generation_model = None
        self.tokenizer = None
        self._classifier = None  # Lazy initialization of question classifier
        self.reranker = None  # Reranker model
        
    def setup_embedding_model(self):
        """Setup custom Qwen3 embedding model with GPU optimization"""
        self.logger.log_info(f"Loading Qwen3 embedding model: {self.config.EMBEDDING_MODEL}")
        
        # Detect GPU availability
        device_available = torch.cuda.is_available()
        self.logger.log_info(f"CUDA available: {device_available}")
        
        if device_available:
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
            self.logger.log_info(f"GPU detected: {gpu_name} ({gpu_memory:.1f}GB)")
        
        # Vietnamese-optimized instruction
        vietnamese_instruction = 'Given a web search query, retrieve relevant passages that answer the query'
        # Setup custom Qwen3 embedding model
        embed_model = Qwen3EmbeddingLlamaIndex(
            model_name_or_path=self.config.EMBEDDING_MODEL,
            instruction=vietnamese_instruction,
            use_fp16=True,
            use_cuda=device_available,
            max_length=8192,
            embed_batch_size=32 if device_available else 8
        )
        
        # Configure global settings
        Settings.embed_model = embed_model
        Settings.chunk_size = self.config.CHUNK_SIZE
        Settings.chunk_overlap = self.config.CHUNK_OVERLAP
        
        self.logger.log_info("Custom Qwen3 embedding model setup completed")
        return embed_model
    
    def setup_reranker(self):
        """Setup Qwen3 Reranker model"""
        if not self.config.RERANKER_ENABLED:
            self.logger.log_info("Reranker is disabled in config")
            return
        
        try:
            self.logger.log_info(f"Loading reranker model: {self.config.RERANKER_MODEL}")
            
            # Check GPU availability
            device_available = torch.cuda.is_available()
            if device_available:
                gpu_name = torch.cuda.get_device_name(0)
                self.logger.log_info(f"Reranker will use GPU: {gpu_name}")
            
            # Initialize reranker
            self.reranker = Qwen3Reranker(
                model_name_or_path=self.config.RERANKER_MODEL,
                max_length=self.config.RERANKER_MAX_LENGTH,
                instruction=self.config.RERANKER_INSTRUCTION
            )
            
            self.logger.log_info("Reranker model loaded successfully")
            
        except Exception as e:
            self.logger.log_error(f"Failed to load reranker model: {str(e)}")
            self.logger.log_info("Continuing without reranker...")
            self.reranker = None
    
    def setup_generation_model(self):
        """Setup Qwen3-0.6B generation model"""
        self.logger.log_info(f"Loading generation model: {self.config.GENERATION_MODEL}")
        
        try:
            # Check GPU availability
            device = "cuda:0" if torch.cuda.is_available() else "cpu"
            torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
            
            if torch.cuda.is_available():
                self.logger.log_info("Using GPU with FP16 precision")
            else:
                self.logger.log_info("Using CPU with FP32 precision")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.config.GENERATION_MODEL,
                trust_remote_code=True
            )
            
            # Load model with optimizations
            if torch.cuda.is_available():
                self.generation_model = AutoModelForCausalLM.from_pretrained(
                    self.config.GENERATION_MODEL,
                    torch_dtype=torch_dtype,
                    device_map="auto",
                    trust_remote_code=True
                )
            else:
                self.generation_model = AutoModelForCausalLM.from_pretrained(
                    self.config.GENERATION_MODEL,
                    torch_dtype=torch_dtype,
                    trust_remote_code=True
                ).to(device)
            
            # Set to eval mode
            self.generation_model.eval()
            
            self.logger.log_info(f"Generation model loaded successfully on device: {device}")
            
        except Exception as e:
            self.logger.log_error("Failed to load generation model", e)
            raise
    
    def setup_chunking(self):
        """Optimal chunking workflow"""
        from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter

        # Step 1: Structure-aware parsing
        markdown_parser = MarkdownNodeParser()

        # Step 2: Sentence-level splitting
        sentence_splitter = SentenceSplitter(
            chunk_size=self.config.CHUNK_SIZE,  # Smaller for MCQ context
            chunk_overlap=self.config.CHUNK_OVERLAP,
            paragraph_separator="\n\n",
            secondary_chunking_regex="[.!?。！？]"  # Vietnamese support
        )

        # Set transformation pipeline
        Settings.transformations = [
            markdown_parser,
            sentence_splitter
        ]

        self.logger.log_info("Optimal chunking strategy configured")

    def load_documents(self) -> List:
        """Load and process documents"""
        self.logger.log_info(f"Loading documents from: {self.config.DOCUMENT_PATH}")
        
        try:
            # Check if document exists
            if not os.path.exists(self.config.DOCUMENT_PATH):
                raise FileNotFoundError(f"Document not found: {self.config.DOCUMENT_PATH}")
            
            # Count files in directory
            md_files = [f for f in os.listdir(self.config.DOCUMENT_PATH) if f.endswith('.md')]
            self.logger.log_info(f"Found {len(md_files)} markdown files in document directory")

            # Load documents from directory
            documents = SimpleDirectoryReader(
                input_dir=self.config.DOCUMENT_PATH,
                recursive=False,  # Don't search subdirectories,
                required_exts=[".md"],  # Specify markdown reader
            ).load_data()
            
            self.logger.log_info(f"Loaded {len(documents)} documents from {len(md_files)} files")
            
            # Log file distribution
            file_counts = {}
            for doc in documents:
                filename = doc.metadata.get('file_name', 'unknown')
                file_counts[filename] = file_counts.get(filename, 0) + 1
            
            for filename, count in file_counts.items():
                self.logger.log_info(f"  {filename}: {count} initial chunks")
            
            return documents
            
        except Exception as e:
            self.logger.log_error("Failed to load documents", e)
            raise
    
    def create_vector_index(self, documents: List, force_rebuild: bool = False):
        """Create or load vector index with Elasticsearch"""
        self.create_elasticsearch_index(documents, force_rebuild)
    
    def setup_query_engine(self):
        """Setup query engine with hybrid retrieval"""
        self.logger.log_info("Setting up query engine with hybrid retrieval (Elasticsearch)...")
        
        try:
            # Set global LLM to None
            Settings.llm = None
            
            # Create hybrid retriever
            self.retriever = self.create_hybrid_retriever()
            
            self.logger.log_info("Hybrid query engine setup completed")
            
        except Exception as e:
            self.logger.log_error("Failed to setup query engine", e)
            raise
    
    def generate_answer_with_qwen3(self, context: str, question: str, 
                                   options: Dict[str, str], 
                                   custom_prompt: str = None) -> str:
        """Generate answer using Qwen3-0.6B model with chat format"""
        
        # Sử dụng custom prompt nếu có, nếu không dùng prompt mặc định
        if custom_prompt is None:
            # Format options
            options_text = ", ".join([f"{k}: {v}" for k, v in options.items()])
            
            # Create messages in chat format for Qwen3
            messages = [{"role": "user",
                "content": 
                    f"""Bạn là một trợ lý AI chuyên trả lời câu hỏi trắc nghiệm tiếng Việt.
                    Context thông tin:
                    {context}

                    Câu hỏi: {question}
                    Các lựa chọn: {options_text}

                    Hướng dẫn:
                    1. Đọc kỹ context và câu hỏi
                    2. Phân tích từng lựa chọn dựa trên thông tin trong context
                    3. Trả lời theo định dạng chính xác: "Đáp án đúng: [danh sách các đáp án]" (ví dụ: "Đáp án đúng: A, C")
                    4. Nếu không tìm thấy thông tin trong context, trả lời: "Không có thông tin đủ để trả lời"
                    """
                }]
        else:
            messages = [{"role": "user", "content": custom_prompt}]
        
        try:
            # Apply chat template
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            # Tokenize input
            inputs = self.tokenizer(text, return_tensors="pt")
            
            # Count tokens
            input_token_count = inputs['input_ids'].shape[1]
            self.logger.log_info(f"Input token count for generation: {input_token_count}")

            # Move to device
            device = next(self.generation_model.parameters()).device
            inputs = {k: v.to(device) for k, v in inputs.items()}
            
            # Generate response
            with torch.no_grad():
                outputs = self.generation_model.generate(
                    **inputs,
                    max_new_tokens=32768,
                    temperature=0.7,
                    do_sample=True,
                    #top_p=0.9,
                    pad_token_id=self.tokenizer.eos_token_id
                )
                
                # Decode only the new tokens
                input_length = inputs['input_ids'].shape[1]
                new_tokens = outputs[:, input_length:]
                
                response = self.tokenizer.decode(
                    new_tokens[0], 
                    skip_special_tokens=True
                )

            # Count output tokens
            output_token_count = new_tokens.shape[1]
            self.logger.log_info(f"Output token count from generation: {output_token_count}")
            
            # Clear GPU cache after generation
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            return response.strip()
            
        except Exception as e:
            self.logger.log_error(f"Error in generation: {str(e)}")
            # Provide a simple fallback
            return "Tôi không thể xử lý câu hỏi này do lỗi kỹ thuật."
    
    def reformulate_query(self, question: str, options: Dict[str, str] = None) -> str:
        """Reformulate query to extract key concepts and keywords for better retrieval"""
        
        # If reformulation is disabled, return original question
        if not self.config.REFORMULATION_ENABLED:
            return question
        
        # Check if generation model is available
        if self.generation_model is None or self.tokenizer is None:
            self.logger.log_info("Generation model not available, skipping reformulation")
            return question
        
        try:
            # Format options if provided
            options_text = ""
            if options:
                options_text = "\nCác lựa chọn: " + ", ".join([f"{k}: {v}" for k, v in options.items()])
            
            # Create reformulation prompt in Vietnamese
            messages = [{"role": "user",
                "content": 
                    f"""Bạn là một trợ lý AI chuyên tối ưu hóa câu hỏi tìm kiếm cho hệ thống RAG.
                    Nhiệm vụ của bạn là tạo ra một câu hỏi tìm kiếm được tối ưu hóa từ câu hỏi trắc nghiệm gốc.
                    
                    Câu hỏi gốc: {question}{options_text}
                    
                    Hướng dẫn:
                    1. Trích xuất các từ khóa và khái niệm chính từ câu hỏi
                    2. Nếu câu hỏi đã đủ ngắn gọn, thì không cần tối ưu hóa thêm
                    3. Tạo câu hỏi tìm kiếm ngắn gọn, tập trung vào giữ nguyên ý nghĩa và ngữ cảnh của câu hỏi gốc
                    
                    Chỉ trả về câu hỏi tìm kiếm đã được tối ưu hóa, không có giải thích thêm.
                """
            }]
            
            # Apply chat template
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            # Tokenize input
            inputs = self.tokenizer(text, return_tensors="pt")
            
            # Move to device
            device = next(self.generation_model.parameters()).device
            inputs = {k: v.to(device) for k, v in inputs.items()}
            
            # Generate reformulated query
            with torch.no_grad():
                outputs = self.generation_model.generate(
                    **inputs,
                    max_new_tokens=self.config.REFORMULATION_MAX_TOKENS,
                    temperature=self.config.REFORMULATION_TEMPERATURE,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
                
                # Decode only the new tokens
                input_length = inputs['input_ids'].shape[1]
                new_tokens = outputs[:, input_length:]
                
                reformulated_query = self.tokenizer.decode(
                    new_tokens[0], 
                    skip_special_tokens=True
                ).strip()
            
            # Clear GPU cache after generation
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            # Log reformulation result
            self.logger.log_info(f"Query reformulation: '{question}' -> '{reformulated_query}'")
            
            # Fallback to original if reformulation is empty or too short
            if not reformulated_query or len(reformulated_query) < 5:
                self.logger.log_info("Reformulated query too short, using original question")
                return question
            
            return reformulated_query
            
        except Exception as e:
            self.logger.log_error(f"Error in query reformulation: {str(e)}")
            # Fallback to original question on error
            return question
    
    def classify_question(self, question: str) -> str:
        """Phân loại câu hỏi"""
        if self._classifier is None:
            self._classifier = QuestionClassifier()
        return self._classifier.classify(question)
    
    def adaptive_retrieval(self, question: str, q_type: str, 
                          reformulated_query: str = None) -> List:
        """Retrieval thích ứng theo loại câu hỏi"""
        
        if reformulated_query is None:
            reformulated_query = question
        
        try:
            # Điều chỉnh TOP_K theo loại câu hỏi
            if q_type == 'calculation':
                # Tăng TOP_K cho câu hỏi tính toán để tìm công thức
                top_k = min(self.config.TOP_K * 2, 20)
                nodes = self.retriever.retrieve(reformulated_query)
                # Sắp xếp lại theo mức độ chứa số liệu
                nodes = sorted(nodes, key=lambda n: self._has_numbers(n.text), reverse=True)
                nodes = nodes[:top_k]
                # Rerank với reranker
                nodes = self.rerank_nodes(nodes, reformulated_query)
                return nodes
            
            elif q_type == 'table_data':
                # Tìm chunks chứa từ khóa "bảng", "table"
                query = f"{reformulated_query} bảng table"
                nodes = self.retriever.retrieve(query)
                # Ưu tiên chunks có từ "bảng"
                nodes = sorted(nodes, key=lambda n: self._has_table_keywords(n.text), reverse=True)
                nodes = nodes[:self.config.TOP_K * 2]  # Lấy nhiều hơn để rerank
                # Rerank với reranker
                nodes = self.rerank_nodes(nodes, reformulated_query)
                return nodes[:self.config.TOP_K]
            
            elif q_type == 'document_comprehension':
                # Tìm tên tài liệu cụ thể (Public_XXX)
                doc_match = re.search(r'public_(\d+)', question.lower())
                if doc_match:
                    doc_id = doc_match.group(1)
                    # Tìm chunks từ tài liệu cụ thể
                    nodes = self._retrieve_by_document(doc_id, reformulated_query)
                    if nodes:
                        # Rerank với reranker
                        nodes = self.rerank_nodes(nodes, reformulated_query)
                        return nodes[:self.config.TOP_K]
                
                # Nếu không tìm thấy tài liệu cụ thể, dùng retrieval thông thường
                top_k = min(self.config.TOP_K * 2, 20)
                nodes = self.retriever.retrieve(reformulated_query)
                nodes = nodes[:top_k]
                # Rerank với reranker
                nodes = self.rerank_nodes(nodes, reformulated_query)
                return nodes
            
            elif q_type == 'definition':
                # Ưu tiên chunks ngắn, chứa định nghĩa
                nodes = self.retriever.retrieve(reformulated_query)
                # Sắp xếp theo độ dài (định nghĩa thường ngắn) và có từ khóa định nghĩa
                nodes = sorted(nodes, key=lambda n: (
                    -self._has_definition_keywords(n.text),
                    len(n.text)
                ))
                nodes = nodes[:self.config.TOP_K * 2]  # Lấy nhiều hơn để rerank
                # Rerank với reranker
                nodes = self.rerank_nodes(nodes, reformulated_query)
                return nodes[:self.config.TOP_K]
            
            elif q_type == 'explanation':
                # Tăng TOP_K cho câu hỏi giải thích để có đủ context
                top_k = min(self.config.TOP_K * 2, 20)
                nodes = self.retriever.retrieve(reformulated_query)
                nodes = nodes[:top_k]
                # Rerank với reranker
                nodes = self.rerank_nodes(nodes, reformulated_query)
                return nodes
            
            else:
                # Retrieval thông thường
                nodes = self.retriever.retrieve(reformulated_query)
                nodes = nodes[:self.config.TOP_K * 2]  # Lấy nhiều hơn để rerank
                # Rerank với reranker
                nodes = self.rerank_nodes(nodes, reformulated_query)
                return nodes[:self.config.TOP_K]
                
        except Exception as e:
            self.logger.log_error(f"Error in adaptive retrieval: {str(e)}")
            # Fallback to normal retrieval
            nodes = self.retriever.retrieve(reformulated_query)
            nodes = nodes[:self.config.TOP_K * 2]  # Lấy nhiều hơn để rerank
            # Rerank với reranker
            nodes = self.rerank_nodes(nodes, reformulated_query)
            return nodes[:self.config.TOP_K]
    
    def _has_numbers(self, text: str) -> int:
        """Đếm số lượng số trong text"""
        numbers = re.findall(r'\d+\.?\d*', text)
        return len(numbers)
    
    def _has_table_keywords(self, text: str) -> int:
        """Đếm số lượng từ khóa liên quan đến bảng"""
        keywords = ['bảng', 'table', 'bảng \d+', 'table \d+']
        count = 0
        text_lower = text.lower()
        for keyword in keywords:
            count += len(re.findall(keyword, text_lower))
        return count
    
    def _has_definition_keywords(self, text: str) -> int:
        """Đếm số lượng từ khóa định nghĩa"""
        keywords = ['định nghĩa', 'là', 'được gọi', 'khái niệm', 'nghĩa là']
        count = 0
        text_lower = text.lower()
        for keyword in keywords:
            count += len(re.findall(keyword, text_lower))
        return count
    
    def _retrieve_by_document(self, doc_id: str, query: str) -> List:
        """Retrieve chunks từ tài liệu cụ thể"""
        try:
            # Tìm tất cả nodes
            all_nodes = []
            if hasattr(self.index, 'storage_context') and hasattr(self.index.storage_context, 'docstore'):
                for node_id in self.index.storage_context.docstore.docs:
                    node = self.index.storage_context.docstore.get_node(node_id)
                    if node and hasattr(node, 'metadata'):
                        # Kiểm tra metadata có chứa doc_id không
                        metadata = node.metadata
                        if isinstance(metadata, dict):
                            file_name = metadata.get('file_name', '')
                            if f'public_{doc_id}' in file_name.lower() or f'public-{doc_id}' in file_name.lower():
                                all_nodes.append(node)
            
            # Nếu tìm thấy nodes từ tài liệu cụ thể, retrieve từ đó
            if all_nodes:
                # Tạo retriever tạm thời từ nodes này
                from llama_index.core.retrievers import VectorIndexRetriever
                temp_retriever = VectorIndexRetriever(
                    index=self.index,
                    similarity_top_k=min(len(all_nodes), self.config.TOP_K * 2)
                )
                nodes = temp_retriever.retrieve(query)
                # Lọc chỉ lấy nodes từ tài liệu cụ thể
                filtered_nodes = []
                for n in nodes:
                    metadata = getattr(n, 'metadata', {})
                    if isinstance(metadata, dict):
                        file_name = str(metadata.get('file_name', '')).lower()
                        if f'public_{doc_id}' in file_name or f'public-{doc_id}' in file_name:
                            filtered_nodes.append(n)
                return filtered_nodes if filtered_nodes else nodes
            
            return []
        except Exception as e:
            self.logger.log_error(f"Error retrieving by document: {str(e)}")
            return []
    
    def rerank_nodes(self, nodes: List, query: str, instruction: str = None) -> List:
        """
        Rerank nodes using Qwen3Reranker
        
        Args:
            nodes: List of nodes to rerank
            query: Original query/question
            instruction: Optional custom instruction for reranker
            
        Returns:
            Reranked list of nodes sorted by relevance score
        """
        # If reranker is not enabled or not available, return original nodes
        if not self.config.RERANKER_ENABLED or self.reranker is None:
            return nodes
        
        if not nodes:
            return nodes
        
        try:
            # Prepare query-document pairs for reranker
            pairs = [(query, node.text) for node in nodes]
            
            # Use custom instruction if provided, otherwise use default
            reranker_instruction = instruction or self.config.RERANKER_INSTRUCTION
            
            # Compute reranking scores
            scores = self.reranker.compute_scores(pairs, instruction=reranker_instruction)
            
            # Combine nodes with scores
            nodes_with_scores = list(zip(nodes, scores))
            
            # Sort by score (descending)
            nodes_with_scores.sort(key=lambda x: x[1], reverse=True)
            
            # Update node scores with reranker scores
            reranked_nodes = []
            for node, score in nodes_with_scores:
                node.score = score  # Update score attribute
                reranked_nodes.append(node)
            
            # Apply TOP_K if specified
            if self.config.RERANKER_TOP_K is not None:
                reranked_nodes = reranked_nodes[:self.config.RERANKER_TOP_K]
            
            self.logger.log_info(f"Reranked {len(nodes)} nodes, keeping top {len(reranked_nodes)}")
            
            return reranked_nodes
            
        except Exception as e:
            self.logger.log_error(f"Error in reranking: {str(e)}")
            # Fallback: return original nodes
            return nodes
    
    def generate_adaptive_prompt(self, question: str, q_type: str, 
                                context: str, options: Dict[str, str]) -> str:
        """Tạo prompt thích ứng theo loại câu hỏi"""
        
        # Format options
        options_text = ", ".join([f"{k}: {v}" for k, v in options.items()])
        
        base_prompt = f"""Bạn là một trợ lý AI chuyên trả lời câu hỏi trắc nghiệm tiếng Việt.
Context thông tin:
{context}

Câu hỏi: {question}
Các lựa chọn: {options_text}
"""
        
        # Hướng dẫn theo loại câu hỏi
        type_specific_instructions = {
            'calculation': """
Hướng dẫn đặc biệt cho câu hỏi TÍNH TOÁN:
1. Tìm công thức hoặc phương pháp tính trong context
2. Xác định các giá trị đã cho trong câu hỏi
3. Thay thế các giá trị vào công thức
4. Thực hiện tính toán cẩn thận từng bước
5. So sánh kết quả với các lựa chọn (chú ý làm tròn số)
6. Chọn đáp án có giá trị gần nhất hoặc khớp chính xác
7. Trả lời theo định dạng: "Đáp án đúng: [danh sách]" (ví dụ: "Đáp án đúng: A")
""",
            
            'table_data': """
Hướng dẫn đặc biệt cho câu hỏi BẢNG DỮ LIỆU:
1. Tìm bảng hoặc dữ liệu số liệu trong context
2. Đọc chính xác giá trị từ bảng (chú ý đơn vị)
3. Thực hiện phép tính nếu cần (tổng, trung bình, phần trăm)
4. So sánh kết quả với các lựa chọn
5. Chọn đáp án khớp với dữ liệu trong bảng
6. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'document_comprehension': """
Hướng dẫn đặc biệt cho câu hỏi HIỂU TÀI LIỆU:
1. Tìm nội dung chính của tài liệu được đề cập trong context
2. Tóm tắt ý chính, không đi vào chi tiết quá mức
3. So sánh với các lựa chọn để tìm mô tả phù hợp nhất
4. Chọn đáp án mô tả đúng nội dung chính của tài liệu
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'comparison': """
Hướng dẫn đặc biệt cho câu hỏi SO SÁNH:
1. Tìm thông tin về cả hai đối tượng cần so sánh trong context
2. Liệt kê điểm giống và khác nhau
3. Chọn đáp án mô tả chính xác sự khác biệt hoặc điểm giống nhau
4. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'definition': """
Hướng dẫn đặc biệt cho câu hỏi ĐỊNH NGHĨA:
1. Tìm định nghĩa chính xác trong context
2. Không suy luận, chỉ dựa vào thông tin có sẵn trong context
3. So sánh từng lựa chọn với định nghĩa trong context
4. Chọn đáp án khớp chính xác với định nghĩa
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'procedure': """
Hướng dẫn đặc biệt cho câu hỏi QUY TRÌNH:
1. Tìm các bước, thứ tự, quy trình trong context
2. Đọc kỹ thứ tự các bước
3. So sánh với các lựa chọn để tìm thứ tự đúng
4. Chọn đáp án mô tả đúng quy trình
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'explanation': """
Hướng dẫn đặc biệt cho câu hỏi GIẢI THÍCH:
1. Tìm thông tin về nguyên lý, cơ chế hoạt động trong context
2. Phân tích chi tiết cách hoạt động
3. So sánh với các lựa chọn để tìm mô tả đúng nhất
4. Chọn đáp án giải thích chính xác nhất
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'identification': """
Hướng dẫn đặc biệt cho câu hỏi NHẬN DẠNG:
1. Tìm thông tin về thành phần, mô hình, công nghệ trong context
2. Xác định đặc điểm của từng lựa chọn
3. So sánh với thông tin trong context
4. Chọn đáp án đúng hoặc loại bỏ đáp án sai (nếu câu hỏi là "đâu không phải")
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'application': """
Hướng dẫn đặc biệt cho câu hỏi ỨNG DỤNG:
1. Tìm thông tin về ứng dụng, mục đích sử dụng trong context
2. Xác định vai trò, chức năng của từng lựa chọn
3. So sánh với thông tin trong context
4. Chọn đáp án mô tả đúng ứng dụng
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
            
            'reason': """
Hướng dẫn đặc biệt cho câu hỏi LÝ DO:
1. Tìm thông tin về nguyên nhân, lý do trong context
2. Phân tích mối quan hệ nhân quả
3. So sánh với các lựa chọn
4. Chọn đáp án giải thích đúng lý do
5. Trả lời theo định dạng: "Đáp án đúng: [danh sách]"
""",
        }
        
        instruction = type_specific_instructions.get(q_type, """
Hướng dẫn chung:
1. Đọc kỹ context và câu hỏi
2. Phân tích từng lựa chọn dựa trên thông tin trong context
3. Chọn đáp án đúng nhất dựa trên thông tin có sẵn
4. Trả lời theo định dạng chính xác: "Đáp án đúng: [danh sách các đáp án]" (ví dụ: "Đáp án đúng: A, C")
5. Nếu không tìm thấy thông tin đủ trong context, trả lời: "Không có thông tin đủ để trả lời"
""")
        
        return base_prompt + instruction
    
    def parse_answer(self, response: str) -> List[str]:
        """Parse model response to extract answer choices from enhanced format"""
        
        # Handle empty or None response
        if not response or not response.strip():
            return ['E']  # Return E for debug if empty
        
        try:
            # Patterns to find "Đáp án đúng: B, C" format
            patterns = [
                r"Đáp án đúng:\s*([A-D,\s]+)",
                r"đáp án đúng:\s*([A-D,\s]+)",
                r"KẾT LUẬN:\s*.*?Đáp án đúng:\s*([A-D,\s]+)",
                r"\*\*KẾT LUẬN:\*\*\s*.*?Đáp án đúng:\s*([A-D,\s]+)",
            ]
            
            # Try each pattern and find ALL matches, use the LAST one (usually conclusion)
            for pattern in patterns:
                try:
                    matches = list(re.finditer(pattern, response, re.DOTALL | re.IGNORECASE))
                    if matches:
                        # Use the last match (usually the final conclusion)
                        match = matches[-1]
                        answer_text = match.group(1).strip()
                        
                        # Extract individual letters A-D
                        answers = re.findall(r'[A-D]', answer_text.upper())
                        if answers:
                            return sorted(list(set(answers)))  # Remove duplicates and sort
                except re.error as regex_err:
                    # Log regex error and continue to next pattern
                    continue
            
            # If no pattern matches, return E for debug
            self.logger.log_info(f"Could not parse answer from response. Returning E for debug.")
            return ['E']
                
        except Exception as e:
            # Log parsing error but don't crash
            self.logger.log_error(f"Error parsing answer from response: {str(e)}")
            return ['E']  # Return E for debug on error
    
    def answer_mcq(self, question: str, options: Dict[str, str]) -> List[str]:
        """Answer a single MCQ question using adaptive retrieval + custom generation"""
        
        try:
            # 1. Phân loại câu hỏi
            q_type = self.classify_question(question)
            self.logger.log_info(f"Question classified as: {q_type}")
            
            # 2. Reformulate query for better retrieval
            reformulated_query = self.reformulate_query(question, options)
            
            # 3. Adaptive retrieval theo loại câu hỏi
            nodes = self.adaptive_retrieval(question, q_type, reformulated_query)
            
            # 4. Combine context from retrieved nodes
            context_parts = []
            for node in nodes:
                context_parts.append(node.text)
            
            context = "\n\n".join(context_parts)
            
            # 5. Tạo prompt thích ứng theo loại câu hỏi
            adaptive_prompt = self.generate_adaptive_prompt(question, q_type, context, options)
            
            # 6. Generate answer using Qwen3 model với prompt thích ứng
            response = self.generate_answer_with_qwen3(context, question, options, adaptive_prompt)
            
            # 7. Parse answer
            answers = self.parse_answer(response)
            
            return answers
            
        except Exception as e:
            self.logger.log_error(f"Error answering MCQ: {str(e)}")
            return []
    
    def answer_mcq_debug(self, question: str, options: Dict[str, str]) -> Dict:
        """Answer MCQ question with debug information"""
        
        try:
            # 1. Phân loại câu hỏi
            q_type = self.classify_question(question)
            self.logger.log_info(f"Question classified as: {q_type}")
            
            # Reformulate query for better retrieval
            reformulated_query = self.reformulate_query(question, options)
            
            # Adaptive retrieval
            nodes = self.adaptive_retrieval(question, q_type, reformulated_query)
            
            # Combine context and collect metadata
            context_parts = []
            retrieved_chunks = []
            
            for node in nodes:
                context_parts.append(node.text)
                
                # Get similarity score (if available)
                score = getattr(node, 'score', 0.0)
                retrieved_chunks.append((node.text, score))
            
            context = "\n\n".join(context_parts)
            
            # Generate adaptive prompt
            adaptive_prompt = self.generate_adaptive_prompt(question, q_type, context, options)
            
            # Generate answer using Qwen3 model
            raw_response = self.generate_answer_with_qwen3(context, question, options, adaptive_prompt)
            
            # Parse answer
            parsed_answers = self.parse_answer(raw_response)
            
            return {
                'original_query': question,
                'question_type': q_type,
                'reformulated_query': reformulated_query,
                'retrieved_chunks': retrieved_chunks,
                'context': context,
                'raw_response': raw_response,
                'parsed_answers': parsed_answers
            }
            
        except Exception as e:
            self.logger.log_error(f"Error in debug MCQ: {str(e)}")
            return {
                'original_query': question,
                'reformulated_query': question,  # Fallback to original on error
                'retrieved_chunks': [],
                'context': "",
                'raw_response': f"Error: {str(e)}",
                'parsed_answers': []
            }
    
    def retrieval_debug(self, question: str) -> None:
        """Retrieve relevant chunks for a question with debug info"""
        
        try:
            # Reformulate query for better retrieval
            reformulated_query = self.reformulate_query(question)
            
            # Display original and reformulated queries
            print(f"Original Query: {question}")
            print(f"Reformulated Query: {reformulated_query}")
            print("-" * 50)
            
            # Retrieve relevant context using custom Qwen3 retriever
            # Query formatting with instruction prefix is handled automatically
            nodes = self.retriever.retrieve(reformulated_query)
            
            retrieved_chunks = []
            for node in nodes:
                score = getattr(node, 'score', 0.0)
                retrieved_chunks.append((node.text, score))
            
            print("Retrieved Chunks and Similarity Scores:")
            for idx, (chunk, score) in enumerate(retrieved_chunks):
                print(f"Chunk {idx+1} (Score: {score:.4f}):\n{chunk}\n{'-'*40}")
            
        except Exception as e:
            self.logger.log_error(f"Error in retrieval debug: {str(e)}")
            return None

    def initialize(self, force_rebuild_index: bool = False):
        """Initialize the complete RAG system"""
        self.logger.log_info("Initializing Vietnamese MCQ RAG system...")
        
        # Setup models
        self.setup_embedding_model()
        self.setup_reranker()
        self.setup_generation_model()
        
        documents = self.load_documents()
        
        # Create vector index
        self.create_vector_index(documents, force_rebuild_index)
        
        # Setup query engine
        self.setup_query_engine()
        
        self.logger.log_info("RAG system initialization completed successfully!")

    def setup_elasticsearch_client(self):
        """Setup Elasticsearch client connection"""
        self.logger.log_info("Connecting to Elasticsearch...")
        
        try:
            # Tạo Elasticsearch client
            es_client_kwargs = {
                "hosts": [self.config.ELASTICSEARCH_URL],
            }
            
            # Add authentication nếu có
            if self.config.ELASTICSEARCH_USER and self.config.ELASTICSEARCH_PASSWORD:
                es_client_kwargs["basic_auth"] = (
                    self.config.ELASTICSEARCH_USER,
                    self.config.ELASTICSEARCH_PASSWORD
                )
            
            es_client = Elasticsearch(**es_client_kwargs)
            
            # Test connection
            if not es_client.ping():
                raise ConnectionError("Cannot connect to Elasticsearch")
            
            self.logger.log_info(f"Connected to Elasticsearch: {self.config.ELASTICSEARCH_URL}")
            return es_client
            
        except Exception as e:
            self.logger.log_error("Failed to connect to Elasticsearch", e)
            raise

    def create_elasticsearch_index(self, documents: List, force_rebuild: bool = False):
        """Create or load Elasticsearch index with hybrid retrieval support"""
        
        # Setup Elasticsearch client - đảm bảo luôn được khởi tạo
        es_client = self.setup_elasticsearch_client()
        
        try:
            # Kiểm tra index đã tồn tại chưa
            index_exists = es_client.indices.exists(index=self.config.ELASTICSEARCH_INDEX)
            
            if index_exists and not force_rebuild:
                # Index đã được load ở initialize(), không cần làm gì thêm
                self.logger.log_info(f"Index already loaded in initialize()")
                return
                
            elif index_exists and force_rebuild:
                self.logger.log_info(f"Deleting existing index: {self.config.ELASTICSEARCH_INDEX}")
                es_client.indices.delete(index=self.config.ELASTICSEARCH_INDEX)
            
        except Exception as e:
            self.logger.log_info(f"Could not check existing index ({str(e)}), creating new one...")
        
        # Validate documents required for new index
        if documents is None or len(documents) == 0:
            raise ValueError("Documents are required for creating new index")
        
        self.logger.log_info("Creating new Elasticsearch index with hybrid retrieval support...")
        
        # Setup optimal chunking
        self.setup_chunking()
        
        # Tạo ElasticsearchStore với custom mapping để hỗ trợ hybrid search
        vector_store = ElasticsearchStore(
            index_name=self.config.ELASTICSEARCH_INDEX,
            es_client=es_client,  # Đảm bảo es_client đã được khởi tạo
            # Elasticsearch sẽ tự động lưu cả text và vector
            # text_field: lưu text content
            # vector_field: lưu embedding vector
        )
        
        # Create index từ documents
        # Documents sẽ được chunked và embedded tự động
        self.index = VectorStoreIndex.from_documents(
            documents,
            vector_store=vector_store,
            show_progress=True,
            # transformations are applied automatically from Settings
        )

        # Flush và refresh index để đảm bảo dữ liệu được lưu vào disk
        try:
            if es_client.indices.exists(index=self.config.ELASTICSEARCH_INDEX):
                es_client.indices.flush(index=self.config.ELASTICSEARCH_INDEX)
                es_client.indices.refresh(index=self.config.ELASTICSEARCH_INDEX)
                self.logger.log_info("Elasticsearch index flushed and refreshed - data persisted to disk")
            else:
                self.logger.log_info("Index not found, skipping flush/refresh")
        except Exception as e:
            self.logger.log_error(f"Could not flush/refresh index: {str(e)}")
        
        self.logger.log_info("Elasticsearch index created successfully with hybrid retrieval support")

    def create_hybrid_retriever(self):
        """Create hybrid retriever combining vector search and keyword search"""
        
        # Vector retriever (semantic search)
        vector_retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=self.config.HYBRID_TOP_K,
        )
        
        # BM25 retriever (keyword search) - lấy nodes từ index
        nodes = []
        try:
            # Với Elasticsearch, cần lấy nodes từ docstore hoặc từ Elasticsearch
            if hasattr(self.index, 'storage_context') and hasattr(self.index.storage_context, 'docstore'):
                for node_id in self.index.storage_context.docstore.docs:
                    node = self.index.storage_context.docstore.get_node(node_id)
                    if node:
                        nodes.append(node)
            else:
                # Fallback: nếu không có docstore, chỉ dùng vector retriever
                self.logger.log_info("No docstore available, using vector retriever only")
                return vector_retriever
        except Exception as e:
            self.logger.log_error(f"Error getting nodes for BM25: {str(e)}")
            # Fallback: nếu lỗi, chỉ dùng vector retriever
            return vector_retriever
        
        if not nodes:
            self.logger.log_info("No nodes found, using vector retriever only")
            return vector_retriever
        
        # Tạo BM25 retriever từ nodes
        bm25_retriever = BM25Retriever.from_defaults(
            nodes=nodes,
            similarity_top_k=self.config.HYBRID_TOP_K,
        )
        
        # Tạo hybrid retriever với weighted combination
        class HybridRetriever(BaseRetriever):
            def __init__(self, vector_retriever, bm25_retriever, alpha=0.5, top_k=10):
                super().__init__()
                self.vector_retriever = vector_retriever
                self.bm25_retriever = bm25_retriever
                self.alpha = alpha  # 0.5 = balanced, 0.0 = only keyword, 1.0 = only vector
                self.top_k = top_k  # Truyền top_k vào
            
            def _retrieve(self, query_bundle):
                # Retrieve từ cả 2 methods
                vector_nodes = self.vector_retriever.retrieve(query_bundle)
                keyword_nodes = self.bm25_retriever.retrieve(query_bundle)
                
                # Combine results với weighted scoring
                combined_nodes = {}
                
                # Add vector results
                for node in vector_nodes:
                    node_id = node.node_id
                    score = getattr(node, 'score', 0.0)
                    combined_nodes[node_id] = {
                        'node': node,
                        'vector_score': score * self.alpha,
                        'keyword_score': 0.0
                    }
                
                # Add keyword results
                for node in keyword_nodes:
                    node_id = node.node_id
                    score = getattr(node, 'score', 0.0)
                    if node_id in combined_nodes:
                        combined_nodes[node_id]['keyword_score'] = score * (1 - self.alpha)
                    else:
                        combined_nodes[node_id] = {
                            'node': node,
                            'vector_score': 0.0,
                            'keyword_score': score * (1 - self.alpha)
                        }
                
                # Calculate combined scores
                for node_id, data in combined_nodes.items():
                    combined_score = data['vector_score'] + data['keyword_score']
                    data['node'].score = combined_score
                
                # Sort by combined score và return top K
                sorted_nodes = sorted(
                    combined_nodes.values(),
                    key=lambda x: x['vector_score'] + x['keyword_score'],
                    reverse=True
                )
                
                # Return top K nodes
                return [item['node'] for item in sorted_nodes[:self.top_k]]
        
        hybrid_retriever = HybridRetriever(
            vector_retriever=vector_retriever,
            bm25_retriever=bm25_retriever,
            alpha=self.config.HYBRID_ALPHA,
            top_k=self.config.HYBRID_COMBINED_TOP_K  # Số kết quả sau khi combine (10 từ 20)
        )
        
        return hybrid_retriever




if __name__ == "__main__":
    # Test initialization
    rag_system = VietnameseMCQRAG()
    rag_system.initialize(force_rebuild_index=False)
    
    # 1. Interactive loop for testing questions and retrieving relevant chunks
    while True:
        print("\n" + "="*50)
        question = input("Enter your question (or 'quit' to exit): ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("Exiting...")
            break
        
        if not question:
            print("Please enter a valid question.")
            continue
        
        print(f"\nProcessing question: {question}")
        print("-" * 30)
        
        # Retrieve and display relevant chunks
        rag_system.retrieval_debug(question)
