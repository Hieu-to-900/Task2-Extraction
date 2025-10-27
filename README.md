# Vietnamese MCQ RAG System

Hệ thống RAG (Retrieval-Augmented Generation) để trả lời câu hỏi trắc nghiệm tiếng Việt dựa trên tài liệu lớn.

## Yêu cầu hệ thống

- Python 3.8+
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
pip install -r requirements.txt
```

### 3. Cài đặt Flash Attention (Medium priority)

```bash
# Flash Attention để tối ưu tốc độ (có thể bỏ qua nếu gặp lỗi)
pip install flash-attn>=2.3.0 --no-build-isolation
```

### 4. Verify GPU setup

```python
import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
print("GPU memory:", f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}GB" if torch.cuda.is_available() else "No GPU")
```

## Cấu trúc file

```
├── answer_template_small_part.md  # Tài liệu nguồn (40k+ dòng)
├── question.csv                   # Câu hỏi test (format: Question,A,B,C,D)
├── true_result.md                 # Kết quả đúng (format: num_correct,answers)
├── main.py                        # Script chính
├── rag_system.py                  # Core RAG system
├── mcq_processor.py               # MCQ processor và evaluation
└── requirements.txt               # Dependencies
```

## Sử dụng

### 1. Chạy evaluation đầy đủ

```bash
python main.py evaluate
```

### 2. Chạy với custom files

```bash
python main.py evaluate --questions my_questions.csv --ground-truth my_results.md --output my_predictions.csv
```

### 3. Rebuild vector index (khi thay đổi tài liệu)

```bash
python main.py evaluate --rebuild-index
```

### 4. Test với một câu hỏi

```bash
python main.py test
```

### 5. Chạy với nhiều workers (parallel processing)

```bash
python main.py evaluate --workers 4
python main.py evaluate --limit 200 --workers 8 --top-k 4
```

## Output Files

- `predictions.csv`: Kết quả dự đoán theo format yêu cầu
- `predictions_evaluation.json`: Chi tiết đánh giá hiệu suất
- `rag_system.log`: Log file với thông tin debug
- `./chroma_db/`: Vector database
- `./storage/`: LlamaIndex storage

## Hệ thống chấm điểm

- **100% (1 điểm)**: Trả lời hoàn toàn chính xác
- **50% (0.5 điểm)**: Thiếu 1 đáp án đúng
- **0% (0 điểm)**: Thiếu 2+ đáp án đúng HOẶC chọn sai

Điểm cuối = (Tổng điểm / Tổng câu) × 100

## Troubleshooting

### CUDA out of memory
```bash
# Giảm batch size trong config
# Hoặc sử dụng sequential processing
python main.py evaluate --workers 1
```

### Model không tải được
```bash
# Kiểm tra kết nối internet và disk space
# Restart và thử lại
```

### Performance thấp
- Kiểm tra embedding model có load đúng không
- Verify document chunking quality
- Check log file để debug

## Performance Benchmarks

Trên RTX 3090:
- Initialization: ~2-3 phút (lần đầu)
- Processing: ~5-10 giây/câu hỏi
- Memory usage: ~8-12GB GPU RAM

## Advanced Usage

### Custom Configuration

```python
from rag_system import RAGConfig

config = RAGConfig()
config.TOP_K = 5  # Tăng số documents retrieve
config.CHUNK_SIZE = 500  # Tăng chunk size
```

### Batch Processing Optimization

```python
# Disable parallel processing for stability
processor.batch_process_questions(df, max_workers=1)
```

## Logs và Monitoring

System tự động log:
- Question processing results
- Error details
- Performance metrics
- Retrieval quality

Check `rag_system.log` để theo dõi chi tiết.