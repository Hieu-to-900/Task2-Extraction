"""
Vietnamese MCQ RAG System
Core RAG implementation with LlamaIndex, multilingual embedding, and Phi-3 generation
"""

import os
import re
import json
import logging
import pandas as pd
from typing import List, Dict, Tuple, Optional
from datetime import datetime
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings
warnings.filterwarnings("ignore")

# LlamaIndex imports
from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    Settings,
    StorageContext,
    load_index_from_storage
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.prompts import PromptTemplate
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever

import chromadb


class RAGConfig:
    """Configuration for RAG system"""
    # Model configurations
    EMBEDDING_MODEL = "intfloat/multilingual-e5-small"
    GENERATION_MODEL = "microsoft/Phi-3-mini-4k-instruct"
    
    # RAG parameters
    TOP_K = 3
    CHUNK_SIZE = 400  # Let LlamaIndex optimize based on model
    CHUNK_OVERLAP = 50
    
    # File paths
    DOCUMENT_PATH = "answer_template.md"
    QUESTIONS_PATH = "question.csv"
    TRUE_RESULTS_PATH = "true_result.md"
    
    # Storage
    CHROMA_DB_PATH = "./chroma_db"
    INDEX_STORAGE_PATH = "./storage"


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
        """Setup multilingual embedding model with GPU optimization"""
        self.logger.log_info(f"Loading embedding model: {self.config.EMBEDDING_MODEL}")
        
        # Detect GPU availability
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.logger.log_info(f"Using device for embedding: {device}")
        
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
            self.logger.log_info(f"GPU detected: {gpu_name} ({gpu_memory:.1f}GB)")
        
        # Setup embedding model with GPU optimization
        embed_model = HuggingFaceEmbedding(
            model_name=self.config.EMBEDDING_MODEL,
            device=device,
            trust_remote_code=True,
            embed_batch_size=64 if torch.cuda.is_available() else 8,  # Larger batch for GPU
            query_instruction="query: ",  # Prefix for questions
            text_instruction="passage: ",  # Prefix for document chunks
            normalize=True  # L2 normalization as required
            # pooling="cls" removed - deprecated parameter
        )
        
        # Configure global settings
        Settings.embed_model = embed_model
        Settings.chunk_size = self.config.CHUNK_SIZE
        Settings.chunk_overlap = self.config.CHUNK_OVERLAP
        
        return embed_model
    
    def setup_generation_model(self):
        """Setup Phi-3 generation model with GPU optimization"""
        self.logger.log_info(f"Loading generation model: {self.config.GENERATION_MODEL}")
        
        try:
            # Check GPU availability
            if torch.cuda.is_available():
                device = "cuda:0"
                torch_dtype = torch.float16  # Use FP16 for RTX 3090 optimization
                self.logger.log_info("Using GPU with FP16 precision")
            else:
                device = "cpu"
                torch_dtype = torch.float32
                self.logger.log_info("Using CPU with FP32 precision")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.config.GENERATION_MODEL,
                trust_remote_code=True
            )
            
            # Set pad token if not exists
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load model with GPU optimization
            model_kwargs = {
                "torch_dtype": torch_dtype,
                "trust_remote_code": True
            }
            
            if torch.cuda.is_available():
                model_kwargs.update({
                    "device_map": "auto"  # Automatic device mapping
                    # "attn_implementation": "flash_attention_2"  # Removed - compilation issues on Windows
                })
            
            self.generation_model = AutoModelForCausalLM.from_pretrained(
                self.config.GENERATION_MODEL,
                **model_kwargs
            )
            
            # Move to device if not using device_map
            if not torch.cuda.is_available():
                self.generation_model = self.generation_model.to(device)
            
            self.logger.log_info("Generation model loaded successfully")
            
        except Exception as e:
            self.logger.log_error("Failed to load generation model", e)
            raise
    
    def load_documents(self) -> List:
        """Load and process documents"""
        self.logger.log_info(f"Loading documents from: {self.config.DOCUMENT_PATH}")
        
        try:
            # Check if document exists
            if not os.path.exists(self.config.DOCUMENT_PATH):
                raise FileNotFoundError(f"Document not found: {self.config.DOCUMENT_PATH}")
            
            # Load documents
            documents = SimpleDirectoryReader(
                input_files=[self.config.DOCUMENT_PATH]
            ).load_data()
            
            self.logger.log_info(f"Loaded {len(documents)} documents")
            return documents
            
        except Exception as e:
            self.logger.log_error("Failed to load documents", e)
            raise
    
    def create_vector_index(self, documents: List, force_rebuild: bool = False):
        """Create or load vector index with ChromaDB"""
        
        try:
            # Try to load existing index
            if not force_rebuild and os.path.exists(self.config.INDEX_STORAGE_PATH):
                self.logger.log_info("Loading existing vector index...")
                storage_context = StorageContext.from_defaults(persist_dir=self.config.INDEX_STORAGE_PATH)
                self.index = load_index_from_storage(storage_context)
                self.logger.log_info("Vector index loaded successfully")
                return
        except:
            self.logger.log_info("Could not load existing index, creating new one...")
        
        self.logger.log_info("Creating new vector index with ChromaDB...")
        
        # Initialize ChromaDB
        chroma_client = chromadb.PersistentClient(path=self.config.CHROMA_DB_PATH)
        chroma_collection = chroma_client.get_or_create_collection("vietnamese_mcq")
        
        # Create vector store
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        # Setup node parser for optimal chunking
        node_parser = SentenceSplitter(
            chunk_size=self.config.CHUNK_SIZE,
            chunk_overlap=self.config.CHUNK_OVERLAP,
        )
        Settings.node_parser = node_parser
        
        # Create index
        self.index = VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            show_progress=True
        )
        
        # Persist index
        self.index.storage_context.persist(persist_dir=self.config.INDEX_STORAGE_PATH)
        self.logger.log_info("Vector index created and persisted successfully")
    
    def setup_query_engine(self):
        """Setup query engine - bypass LlamaIndex LLM, use retrieval only"""
        self.logger.log_info("Setting up query engine...")
        
        try:
            # Set global LLM to None to disable OpenAI and bypass LLM complexity
            Settings.llm = None
            
            # Create simple retriever for context extraction
            retriever = VectorIndexRetriever(
                index=self.index,
                similarity_top_k=self.config.TOP_K,
            )
            
            # Store retriever for manual context extraction
            self.retriever = retriever
            
            self.logger.log_info("Query engine setup completed - using retrieval only approach")
            
        except Exception as e:
            self.logger.log_error("Failed to setup query engine", e)
            raise
    
    def generate_answer_with_phi3(self, context: str, question: str, options: Dict[str, str]) -> str:
        """Generate answer using Phi-3 model with GPU optimization"""
        
        # Format options
        options_text = ", ".join([f"{k}: {v}" for k, v in options.items()])
        
        # Create prompt
        prompt = f"""Bạn là một trợ lý AI chuyên trả lời câu hỏi trắc nghiệm tiếng Việt.

Context thông tin:
{context}

Câu hỏi: {question}
Các lựa chọn: {options_text}

Hướng dẫn:
1. Đọc kỹ context và câu hỏi
2. Phân tích từng lựa chọn dựa trên thông tin trong context
3. Trả lời theo định dạng chính xác: "Đáp án đúng: [danh sách các đáp án]" (ví dụ: "Đáp án đúng: A, C")
4. Nếu không tìm thấy thông tin trong context, trả lời: "Không có thông tin đủ để trả lời"

Trả lời:"""
        
        try:
            # Tokenize with proper device handling
            inputs = self.tokenizer(
                prompt, 
                return_tensors="pt", 
                truncation=True, 
                max_length=3000,
                padding=True
            )
            
            # Move to same device as model
            if hasattr(self.generation_model, 'device'):
                device = next(self.generation_model.parameters()).device
                inputs = {k: v.to(device) for k, v in inputs.items()}
            
            # Generate with optimized settings
            with torch.no_grad():
                outputs = self.generation_model.generate(
                    **inputs,
                    max_new_tokens=100,
                    temperature=0.1,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    use_cache=True  # Enable KV cache for faster generation
                )
            
            # Decode response
            response = self.tokenizer.decode(
                outputs[0][inputs['input_ids'].shape[1]:], 
                skip_special_tokens=True
            )
            
            # Clear GPU cache after generation
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            return response.strip()
            
        except Exception as e:
            self.logger.log_error(f"Error in generation: {str(e)}")
            return "Lỗi trong quá trình sinh câu trả lời"
    
    def parse_answer(self, response: str) -> List[str]:
        """Parse model response to extract answer choices"""
        
        # Multiple regex patterns to catch different response formats
        patterns = [
            r"Đáp án đúng:\s*([A-D,\s]+)",
            r"đáp án đúng:\s*([A-D,\s]+)", 
            r"Đáp án:\s*([A-D,\s]+)",
            r"đáp án:\s*([A-D,\s]+)",
            r"([A-D](?:\s*,\s*[A-D])*)",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response)
            if match:
                answer_text = match.group(1).strip()
                # Extract individual letters
                answers = re.findall(r'[A-D]', answer_text.upper())
                return sorted(list(set(answers)))  # Remove duplicates and sort
        
        # If no pattern matches, try to find any A-D letters
        letters = re.findall(r'[A-D]', response.upper())
        if letters:
            return sorted(list(set(letters)))
        
        return []
    
    def answer_mcq(self, question: str, options: Dict[str, str]) -> List[str]:
        """Answer a single MCQ question using retrieval + custom generation"""
        
        try:
            # Add query prefix for better retrieval
            query_with_prefix = f"query: {question}"
            
            # Retrieve relevant context using our retriever
            nodes = self.retriever.retrieve(query_with_prefix)
            
            # Combine context with passage prefix
            context_parts = []
            for node in nodes:
                # Add passage prefix for embedding consistency
                context_parts.append(f"passage: {node.text}")
            
            context = "\n\n".join(context_parts)
            
            # Generate answer using our custom Phi-3 model
            response = self.generate_answer_with_phi3(context, question, options)
            
            # Parse answer
            answers = self.parse_answer(response)
            
            return answers
            
        except Exception as e:
            self.logger.log_error(f"Error answering MCQ: {str(e)}")
            return []
    
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
    rag_system.initialize()
    
    # Test with a sample question
    test_question = "Các thành phần chính của nhà thông minh trước năm 2010 là gì?"
    test_options = {
        "A": "Cảm biến",
        "B": "Bộ xử lý", 
        "C": "API",
        "D": "Tất cả"
    }
    
    result = rag_system.answer_mcq(test_question, test_options)
    print(f"Question: {test_question}")
    print(f"Predicted answers: {result}")