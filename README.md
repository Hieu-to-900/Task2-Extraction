# Vietnamese MCQ RAG System

Hệ thống RAG (Retrieval-Augmented Generation) để trả lời câu hỏi trắc nghiệm tiếng Việt dựa trên tài liệu lớn.

## Yêu cầu hệ thống

- Python 3.10+
- NVIDIA GPU (RTX 3090 hoặc tương tự) với CUDA support
- RAM: 16GB+
- Disk space: 10GB+ (cho models và vector database)

## Cài đặt

### 1. Cài đặt PyTorch với GPU support (Critical)

```bash
# Uninstall CPU-only PyTorch nếu đã cài
pip uninstall torch torchvision torchaudio

# Install PyTorch với CUDA support cho RTX 3090
pip install torch>=2.0.0+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 2. Cài đặt dependencies chính

```bash
pip install llama-index==0.14.7
pip install llama-index-vector-stores-elasticsearch>=0.1.0  # Thêm package này
pip install llama-index-retrievers-bm25>=0.1.0

pip install elasticsearch>=8.0.0

pip install accelerate>=0.24.0
```

Sau khi chạy main.py nó báo thiếu gì thì pip install là được

### 3. Run docker container elasticsearch

```bash
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.11.0

OR

docker run -d \
  --name elasticsearch \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
  docker.elastic.co/elasticsearch/elasticsearch:8.11.0
```
Tested trên Docker Desktop, nếu dùng mỗi engine thì tự tìm lệnh để start/stop

## Sử dụng

### 1. Chạy evaluation đầy đủ

```bash
python main.py evaluate
python main.py evaluate --workers 4 --limit 200 --random
python main.py evaluate --workers 4 --range "100-200"
```



### 2. Test với một câu hỏi

```bash
python main.py debug 3
```


## Output Files

- `predictions.csv`: Kết quả dự đoán theo format yêu cầu
- `predictions_evaluation.json`: Chi tiết đánh giá hiệu suất
- `rag_system.log`: Log file với thông tin debug


## Logs và Monitoring


Check `rag_system.log` để theo dõi chi tiết.