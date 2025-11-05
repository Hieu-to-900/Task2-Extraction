from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from llama_index.core import StorageContext, VectorStoreIndex, Document
from llama_index.core import Settings

# Import Qwen3 embedding từ rag_system
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag_system import Qwen3EmbeddingLlamaIndex

# get credentials
host = os.environ.get("ES_HOST", "http://localhost:9200")
index_name = os.environ.get("INDEX_NAME", "test-index-documents")

print("=" * 60)
print("Elasticsearch Vector Store Test with Qwen3 Embedding")
print("=" * 60)

# Create Qwen3 embeddings (local model)
print("\n1. Creating Qwen3 embeddings...")
print("   Loading Qwen3-Embedding-0.6B model (this may take a moment)...")
try:
    import torch
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        print(f"   Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("   Using CPU")
except:
    use_cuda = False

embeddings = Qwen3EmbeddingLlamaIndex(
    model_name_or_path="Qwen/Qwen3-Embedding-0.6B",
    use_fp16=True,
    use_cuda=use_cuda,
    max_length=8192,
    embed_batch_size=32 if use_cuda else 8
)

# set global settings
Settings.embed_model = embeddings
Settings.chunk_size = 512

print("✓ Qwen3 Embeddings configured")

# Create some sample documents
print("\n2. Creating sample documents...")
documents = [
    Document(
        text="Python is a high-level programming language known for its simplicity and readability. "
             "It was created by Guido van Rossum and first released in 1991. "
             "Python supports multiple programming paradigms including procedural, object-oriented, and functional programming."
    ),
    Document(
        text="Machine Learning is a subset of artificial intelligence that focuses on algorithms and statistical models. "
             "It enables computer systems to learn and improve from experience without being explicitly programmed. "
             "Common applications include image recognition, natural language processing, and recommendation systems."
    ),
    Document(
        text="Elasticsearch is a distributed search and analytics engine built on Apache Lucene. "
             "It provides a RESTful API for storing, searching, and analyzing data in real-time. "
             "Elasticsearch is widely used for log analytics, full-text search, and business intelligence."
    ),
    Document(
        text="Vector databases are specialized databases designed to store and query high-dimensional vectors. "
             "They are essential for machine learning applications like similarity search, recommendation systems, "
             "and semantic search. Popular vector databases include Pinecone, Weaviate, and Milvus."
    ),
    Document(
        text="RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with language generation. "
             "It retrieves relevant documents from a knowledge base and uses them as context for generating more accurate responses. "
             "RAG systems are commonly used in question-answering applications and chatbots."
    ),
]

print(f"✓ Created {len(documents)} documents")

# Create Elasticsearch vector store
print("\n3. Setting up Elasticsearch vector store...")
vector_store_kwargs = {
    "index_name": index_name,
    "es_url": host
}

vector_store = ElasticsearchStore(**vector_store_kwargs)
print(f"✓ Vector store configured for index: {index_name}")

# Create StorageContext
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create index from documents (this will create the index if it doesn't exist)
print("\n4. Creating index from documents...")
print("   This may take a moment as documents are being embedded and stored...")
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    show_progress=True,
)
print("✓ Index created successfully")

# Verify index was created
print("\n5. Verifying index creation...")
try:
    from elasticsearch import Elasticsearch
    es_client_kwargs = {"hosts": [host]}
    
    es_client = Elasticsearch(**es_client_kwargs)
    index_exists = es_client.indices.exists(index=index_name)
    if index_exists:
        # Get document count
        stats = es_client.count(index=index_name)
        print(f"✓ Index exists with {stats['count']} documents")
        
        # Try to flush and refresh to ensure persistence
        try:
            es_client.indices.flush(index=index_name)
            es_client.indices.refresh(index=index_name)
            print("✓ Index flushed and refreshed - data persisted to disk")
        except Exception as e:
            print(f"⚠ Could not flush/refresh: {e}")
    else:
        print("⚠ Index not found in Elasticsearch")
except Exception as e:
    print(f"⚠ Could not verify index: {e}")

# Create retriever (chỉ retrieval, không generate response)
print("\n6. Creating retriever...")
retriever = index.as_retriever(similarity_top_k=3)
print("✓ Retriever ready")

# Test queries - chỉ retrieve documents, không generate
print("\n" + "=" * 60)
print("7. Testing Retrieval (Top 3 Results)")
print("=" * 60)

test_queries = [
    "What is Python?",
    "Tell me about machine learning",
    "What is Elasticsearch used for?",
    "Explain vector databases",
    "What is RAG?",
]

for i, query in enumerate(test_queries, 1):
    print(f"\nQuery {i}: {query}")
    print("-" * 60)
    try:
        # Retrieve relevant documents
        nodes = retriever.retrieve(query)
        print(f"Found {len(nodes)} relevant documents:")
        for j, node in enumerate(nodes, 1):
            print(f"\n  Document {j} (Score: {node.score:.4f if hasattr(node, 'score') else 'N/A'}):")
            # Print first 200 chars of each document
            text_preview = node.text[:200] + "..." if len(node.text) > 200 else node.text
            print(f"  {text_preview}")
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 60)
print("Test completed!")
print("=" * 60)