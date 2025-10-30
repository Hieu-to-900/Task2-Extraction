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
    StorageContext,
    load_index_from_storage,
    Document
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import BaseNode, TextNode
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.base.embeddings.base import BaseEmbedding


class RAGConfig:
    """Configuration for RAG system"""
    # Model configurations
    EMBEDDING_MODEL = "Qwen/Qwen3-Embedding-0.6B"
    GENERATION_MODEL = "Qwen/Qwen3-0.6B"
    
    # RAG parameters
    TOP_K = 2
    CHUNK_SIZE = 200
    CHUNK_OVERLAP = 50
    
    # File paths
    DOCUMENT_PATH = "documents"
    QUESTIONS_PATH = "question.csv"
    TRUE_RESULTS_PATH = "true_result.md"
    
    # Storage
    INDEX_STORAGE_PATH = "./storage"


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
        vietnamese_instruction = 'Tìm kiếm đoạn văn bản tiếng Việt có chứa thông tin trả lời câu hỏi'
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
            chunk_size=400,  # Smaller for MCQ context
            chunk_overlap=50,
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
        """Create or load vector index with native LlamaIndex storage"""
        
        try:
            # Try to load existing index
            if not force_rebuild and os.path.exists(self.config.INDEX_STORAGE_PATH):
                self.logger.log_info("Loading existing vector index...")
                storage_context = StorageContext.from_defaults(persist_dir=self.config.INDEX_STORAGE_PATH)
                self.index = load_index_from_storage(storage_context)
                self.logger.log_info("Vector index loaded successfully")
                return
        except Exception as e:
            self.logger.log_info(f"Could not load existing index ({str(e)}), creating new one...")
        
        self.logger.log_info("Creating new vector index with hierarchical chunking...")
        
        # Setup optimal chunking
        self.setup_chunking()

        # Create index with automatic transformations
        # Documents will be processed through MarkdownNodeParser -> SentenceSplitter pipeline
        self.index = VectorStoreIndex.from_documents(
            documents,
            show_progress=True,
            # transformations are applied automatically from Settings
        )
        
        # Persist index to storage directory
        self.index.storage_context.persist(persist_dir=self.config.INDEX_STORAGE_PATH)
        self.logger.log_info("Vector index created and persisted successfully")
    
    def setup_query_engine(self):
        """Setup query engine - bypass LlamaIndex LLM, use retrieval only"""
        self.logger.log_info("Setting up query engine with custom Qwen3 retriever...")
        
        try:
            # Set global LLM to None to disable OpenAI and bypass LLM complexity
            Settings.llm = None
            
            # Create retriever with custom Qwen3 embedding (instruction formatting handled automatically)
            retriever = VectorIndexRetriever(
                index=self.index,
                similarity_top_k=self.config.TOP_K,
            )
            
            # Store retriever for manual context extraction
            self.retriever = retriever
            
            self.logger.log_info("Query engine setup completed - using custom Qwen3 embeddings")
            
        except Exception as e:
            self.logger.log_error("Failed to setup query engine", e)
            raise
    
    def generate_answer_with_qwen3(self, context: str, question: str, options: Dict[str, str]) -> str:
        """Generate answer using Qwen3-0.6B model with chat format"""
        
        # Format options
        options_text = ", ".join([f"{k}: {v}" for k, v in options.items()])
        
        # Create messages in chat format for Qwen3
        messages = [
            {
                "role": "user",
                "content": f"""Bạn là một trợ lý AI chuyên trả lời câu hỏi trắc nghiệm tiếng Việt.

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
            }
        ]
        
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
    
    def parse_answer(self, response: str) -> List[str]:
        """Parse model response to extract answer choices from enhanced format"""
        
        # Handle empty or None response
        if not response or not response.strip():
            return []
        
        try:
            # Enhanced regex patterns for new format
            patterns = [
                # New format patterns
                r"Đáp án đúng:\s*([A-D,\s]+)",
                r"đáp án đúng:\s*([A-D,\s]+)",
                r"KẾT LUẬN:\s*.*?Đáp án đúng:\s*([A-D,\s]+)",
                r"\*\*KẾT LUẬN:\*\*\s*.*?Đáp án đúng:\s*([A-D,\s]+)",
                
                # Fallback patterns
                r"Đáp án:\s*([A-D,\s]+)",
                r"đáp án:\s*([A-D,\s]+)",
                r"Chọn:\s*([A-D,\s]+)",
                r"chọn:\s*([A-D,\s]+)",
                
                # Final fallback - any sequence of A-D with commas (fixed pattern)
                r"[A-D](?:\s*,\s*[A-D])*",
            ]
            
            for pattern in patterns:
                try:
                    match = re.search(pattern, response, re.DOTALL | re.IGNORECASE)
                    if match:
                        if match.groups():  # If pattern has groups
                            answer_text = match.group(1).strip()
                        else:  # If pattern has no groups (like the fixed final fallback)
                            answer_text = match.group(0).strip()
                        
                        # Extract individual letters
                        answers = re.findall(r'[A-D]', answer_text.upper())
                        if answers:
                            return sorted(list(set(answers)))  # Remove duplicates and sort
                except re.error as regex_err:
                    # Log regex error and continue to next pattern
                    continue
            
            # If no pattern matches, try to find any A-D letters in conclusion section
            try:
                conclusion_match = re.search(r"KẾT LUẬN:.*", response, re.DOTALL | re.IGNORECASE)
                if conclusion_match:
                    conclusion_text = conclusion_match.group(0)
                    letters = re.findall(r'[A-D]', conclusion_text.upper())
                    if letters:
                        return sorted(list(set(letters)))
            except re.error:
                pass
            
            # Final fallback - any A-D letters in response
            try:
                letters = re.findall(r'[A-D]', response.upper())
                if letters:
                    return sorted(list(set(letters)))
            except re.error:
                pass
                
        except Exception as e:
            # Log parsing error but don't crash
            self.logger.log_error(f"Error parsing answer from response: {str(e)}")
        
        return []
    
    def answer_mcq(self, question: str, options: Dict[str, str]) -> List[str]:
        """Answer a single MCQ question using retrieval + custom generation"""
        
        try:
            # Retrieve relevant context using our custom Qwen3 retriever
            # Query will be automatically formatted with instruction prefix in the embedding model
            nodes = self.retriever.retrieve(question)
            
            # Combine context from retrieved nodes
            context_parts = []
            for node in nodes:
                context_parts.append(node.text)
            
            context = "\n\n".join(context_parts)
            
            # Generate answer using Qwen3 model
            response = self.generate_answer_with_qwen3(context, question, options)
            
            # Parse answer
            answers = self.parse_answer(response)
            
            return answers
            
        except Exception as e:
            self.logger.log_error(f"Error answering MCQ: {str(e)}")
            return []
    
    def answer_mcq_debug(self, question: str, options: Dict[str, str]) -> Dict:
        """Answer MCQ question with debug information"""
        
        try:
            # Retrieve relevant context using custom Qwen3 retriever
            # Query formatting with instruction prefix is handled automatically
            nodes = self.retriever.retrieve(question)
            
            # Combine context and collect metadata
            context_parts = []
            retrieved_chunks = []
            
            for node in nodes:
                context_parts.append(node.text)
                
                # Get similarity score (if available)
                score = getattr(node, 'score', 0.0)
                retrieved_chunks.append((node.text, score))
            
            context = "\n\n".join(context_parts)
            
            # Generate answer using Qwen3 model
            raw_response = self.generate_answer_with_qwen3(context, question, options)
            
            # Parse answer
            parsed_answers = self.parse_answer(raw_response)
            
            return {
                'retrieved_chunks': retrieved_chunks,
                'context': context,
                'raw_response': raw_response,
                'parsed_answers': parsed_answers
            }
            
        except Exception as e:
            self.logger.log_error(f"Error in debug MCQ: {str(e)}")
            return {
                'retrieved_chunks': [],
                'context': "",
                'raw_response': f"Error: {str(e)}",
                'parsed_answers': []
            }
    
    def retrieval_debug(self, question: str) -> None:
        """Retrieve relevant chunks for a question with debug info"""
        
        try:
            # Retrieve relevant context using custom Qwen3 retriever
            # Query formatting with instruction prefix is handled automatically
            nodes = self.retriever.retrieve(question)
            
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
        self.setup_generation_model()
        
        # Load and process documents
        documents = self.load_documents()
        
        # Create vector index
        self.create_vector_index(documents, force_rebuild_index)
        
        # Setup query engine
        self.setup_query_engine()
        
        self.logger.log_info("RAG system initialization completed successfully!")


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
