#coding:utf8
import os
from typing import Dict, Optional, List, Union
import torch
from torch import nn
import torch.nn.functional as F

from torch import Tensor
from transformers import AutoTokenizer, AutoModel
from transformers.utils import is_flash_attn_2_available
import numpy as np
from collections import defaultdict

class Qwen3Embedding():
    def __init__(self, model_name_or_path, instruction=None,  use_fp16: bool = True, use_cuda: bool = True, max_length=8192):
        if instruction is None:
            instruction = 'Given a web search query, retrieve relevant passages that answer the query'
        self.instruction = instruction
        if is_flash_attn_2_available() and use_cuda:
            self.model = AutoModel.from_pretrained(model_name_or_path, trust_remote_code=True, attn_implementation="flash_attention_2", torch_dtype=torch.float16)
        else:
            self.model = AutoModel.from_pretrained(model_name_or_path, trust_remote_code=True, torch_dtype=torch.float16)
        if use_cuda:
            self.model = self.model.cuda()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True, padding_side='left')
        self.max_length=max_length
    
    def last_token_pool(self, last_hidden_states: Tensor,
        attention_mask: Tensor) -> Tensor:
        left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
        if left_padding:
            return last_hidden_states[:, -1]
        else:
            sequence_lengths = attention_mask.sum(dim=1) - 1
            batch_size = last_hidden_states.shape[0]
        return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]

    def get_detailed_instruct(self, task_description: str, query: str) -> str:
        if task_description is None:
            task_description = self.instruction
        return f'Instruct: {task_description}\nQuery:{query}'

    def encode(self, sentences: Union[List[str], str], is_query: bool = False, instruction=None, dim: int = -1):
        if isinstance(sentences, str):
            sentences = [sentences]
        if is_query:
            sentences = [self.get_detailed_instruct(instruction, sent) for sent in sentences]
        inputs = self.tokenizer(sentences, padding=True, truncation=True, max_length=self.max_length, return_tensors='pt')
        inputs.to(self.model.device)
        with torch.no_grad():
            model_outputs = self.model(**inputs)
            output = self.last_token_pool(model_outputs.last_hidden_state, inputs['attention_mask'])
            if dim != -1:
                output = output[:, :dim]
            output  = F.normalize(output, p=2, dim=1)
        return output
    
    def get_top_relevant_documents(self, queries: Union[List[str], str], documents: List[str], 
                                 top_k: int = 1, instruction=None, dim: int = -1):
        """
        Tìm top k tài liệu liên quan nhất cho mỗi truy vấn
        
        Args:
            queries: Danh sách truy vấn hoặc một truy vấn đơn
            documents: Danh sách tài liệu để tìm kiếm
            top_k: Số lượng tài liệu top cần trả về cho mỗi truy vấn
            instruction: Hướng dẫn tùy chỉnh cho truy vấn
            dim: Số chiều embedding
            
        Returns:
            List[Dict]: Danh sách kết quả cho mỗi truy vấn, mỗi phần tử chứa:
                - query: Truy vấn gốc
                - top_documents: Danh sách top k tài liệu với điểm số
        """
        if isinstance(queries, str):
            queries = [queries]
        
        # Encode queries và documents
        query_outputs = self.encode(queries, is_query=True, instruction=instruction, dim=dim)
        doc_outputs = self.encode(documents, dim=dim)
        
        # Tính điểm similarity
        scores = (query_outputs @ doc_outputs.T) * 100
        
        results = []
        for i, query in enumerate(queries):
            # Lấy điểm số cho truy vấn hiện tại
            query_scores = scores[i].cpu().numpy()
            
            # Tìm top k tài liệu
            top_indices = np.argsort(query_scores)[::-1][:top_k]
            
            top_documents = []
            for idx in top_indices:
                top_documents.append({
                    'document_index': int(idx),
                    'document': documents[idx],
                    'score': float(query_scores[idx])
                })
            
            results.append({
                'query': query,
                'top_documents': top_documents
            })
        
        return results

if __name__ == "__main__":
    model_path = "Qwen/Qwen3-Embedding-0.6B"
    model = Qwen3Embedding(model_path)
    queries = ['điện toán đám mây là gì?', 'Thủ đô của Trung Quốc là gì?']
    documents = [
        """
Điện toán đám mây là một nhóm tài nguyên máy tính được chia sẻ sẵn sàng cung cấp nhiều loại dịch vụ điện toán ở các cấp độ khác nhau, từ cơ sở hạ tầng đến các dịch vụ ứng dụng phức tạp nhất, dễ dàng phân bổ và phát hành hoặc tương tác với nhà cung cấp dịch vụ. Trên thực tế, nó quản lý tài nguyên máy tính, lưu trữ và truyền thông được nhiều người dùng chia sẻ trong một môi trường ảo hóa và cô lập. (MR Alam, MBI Reaz và MAM Ali, 2018).
IoT và nhà thông minh có thể tận dụng được các lợi ích từ các tài nguyên và chức năng rộng lớn của đám mây để bù đắp hạn chế của nó trong lưu trữ, xử lý, giao tiếp, hỗ trợ theo nhu cầu, sao lưu và phục hồi. Ví dụ: đám mây có thể hỗ trợ quản lý, dịch vụ IoT và thực thi các ứng dụng bổ sung bằng cách sử dụng dữ liệu do nó tạo ra. Nhà thông minh có thể được cô đọng, chỉ tập trung vào các chức năng cơ bản và quan trọng, do đó, giảm thiểu tài nguyên cục bộ do dựa vào các khả năng tài nguyên đám mây. Nhà thông minh và IoT sẽ tập trung vào thu thập dữ liệu, xử lý cơ bản và truyền thông tin lên đám mây để xử lý tiếp. Với các thách thức bảo mật, đám mây bảo mật cao với dữ liệu riêng tư và các dữ liệu khác sẽ công khai. (A. Bassi và G. Horn, Internet of things năm 2020).
        """,
        """
### Ngôn ngữ xử lý sự kiện

Xử lý sự kiện liên quan đến việc nắm bắt và quản lý các sự kiện được xác định trước theo thời gian thực. Nó bắt đầu từ việc quản lý các thực thể của các sự kiện ngay từ khi sự kiện xảy ra, thậm chí xác định, thu thập dữ liệu, liên kết quy trình và kích hoạt hành động phản hồi. Để cho phép xử lý sự kiện nhanh chóng và linh hoạt, một ngôn ngữ xử lý sự kiện được sử dụng, cho phép cấu hình nhanh các tài nguyên cần thiết để xử lý chuỗi hoạt động dự kiến cho mỗi loại sự kiện. Nó bao gồm hai mô-đun, ESP và CEP. ESP xử lý hiệu quả sự kiện, phân tích nó và chọn sự kiện thích hợp. CEP xử lý các sự kiện tổng hợp. Ngôn ngữ sự kiện mô tả các kiểu sự kiện phức tạp được áp dụng trên bản ghi sự kiện. (N. Panwar, S. Sharma, S. Mehrotra, L. Krzywiecki và N. Venkatasubramanian, 2019).
        """,
        "The capital of China is Beijing.",
        "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."
    ]
    dim = 1024
    
    # Phương pháp cũ: tính toán thủ công
    print("=== PHƯƠNG PHÁP CŨ ===")
    query_outputs = model.encode(queries, is_query=True, dim=dim)
    doc_outputs = model.encode(documents, dim=dim)
    print('query outputs shape:', query_outputs.shape)
    print('doc outputs shape:', doc_outputs.shape)
    scores = (query_outputs @ doc_outputs.T) * 100
    print('All scores:', scores.tolist())
    
    print("\n=== PHƯƠNG PHÁP MỚI: TOP 1 TÀI LIỆU LIÊN QUAN ===")
    # Sử dụng method mới để tìm top 1 tài liệu liên quan
    results = model.get_top_relevant_documents(queries, documents, top_k=1, dim=dim)
    
    for i, result in enumerate(results):
        print(f"\nTruy vấn {i+1}: '{result['query']}'")
        print("Top 1 tài liệu liên quan:")
        for j, doc_info in enumerate(result['top_documents']):
            print(f"  Thứ hạng {j+1}:")
            print(f"    - Chỉ số tài liệu: {doc_info['document_index']}")
            print(f"    - Điểm số: {doc_info['score']:.2f}")
            print(f"    - Nội dung: {doc_info['document'][:100]}...")
    
    print("\n=== DEMO TOP 3 TÀI LIỆU LIÊN QUAN ===")
    # Demo với top 3 để thấy rõ hơn
    results_top3 = model.get_top_relevant_documents(queries, documents, top_k=3, dim=dim)
    
    for i, result in enumerate(results_top3):
        print(f"\nTruy vấn {i+1}: '{result['query']}'")
        print("Top 3 tài liệu liên quan:")
        for j, doc_info in enumerate(result['top_documents']):
            print(f"  Thứ hạng {j+1}: Điểm số {doc_info['score']:.2f} - Tài liệu {doc_info['document_index']}")