"""
Question Classifier Module
Phân loại câu hỏi để áp dụng chiến lược xử lý phù hợp
"""

import re
from typing import Dict, List


class QuestionClassifier:
    """Phân loại câu hỏi để áp dụng chiến lược xử lý phù hợp"""
    
    def __init__(self):
        # Định nghĩa các pattern cho từng loại câu hỏi
        # Thứ tự quan trọng - kiểm tra từ specific đến general
        self.patterns = {
            'calculation': [
                r'hãy\s+tính',  # Match: "Hãy tính giá trị X"
                r'tính\s+.*\s+bao nhiêu|tính\s+.*\s+giá trị|tính\s+.*\s+kết quả',  # Match: "Tính giá trị X", "Tính bao nhiêu", "Tính kết quả"
                r'bao nhiêu.*tính|giá trị.*tính|kết quả.*tính',  # Match: "Giá trị tính toán là gì", "Kết quả tính"
                r'tỉ lệ.*được giữ|phần trăm.*được giữ|tỉ lệ.*giữ lại',  # Match: "Tỉ lệ được giữ là bao nhiêu", "Phần trăm được giữ"
                r'\d+\s*[+\-×÷*/]\s*\d+',  # Match: "10 + 5", "20 - 3", "5 × 2", "10 / 2" (phép tính số học)
                r'λ\d+|eigenvalue|trị riêng|ma trận|matrix',  # Match: "λ1", "eigenvalue", "trị riêng", "ma trận", "matrix" (toán học)
                r'công thức.*tính|formula.*tính|tính toán.*theo',  # Match: "Công thức tính", "Formula tính", "Tính toán theo"
                r'=\s*\d+|bằng\s*\d+|kết quả\s*=\s*\d+',  # Match: "= 10", "bằng 5", "kết quả = 20" (kết quả số)
                r'tính\s+.*\s+theo\s+công\s+thức',  # Match: "Tính X theo công thức Y"
            ],
            'table_data': [
                r'bảng\s*\d+\.?\d*|theo\s+bảng|dựa\s+vào\s+bảng',  # Match: "Bảng 1", "Bảng 2.5", "Theo bảng", "Dựa vào bảng"
                r'bảng.*cho\s+biết|bảng.*cung\s+cấp',  # Match: "Bảng cho biết", "Bảng cung cấp thông tin"
                r'table\s*\d+|theo\s+table',  # Match: "Table 1", "Theo table" (tiếng Anh)
            ],
            'document_comprehension': [
                # Pattern ưu tiên: match "Public_xxx" hoặc "Public xxx" (với số)
                r'public_\d+',  # Match: "Public_172", "Public_633", "public_123" (tài liệu cụ thể với underscore)
                r'public\s+\d+',  # Match: "Public 172", "Public 633", "public 123" (tài liệu cụ thể với space)
                
                # Pattern match "Theo tài liệu" (có thể có hoặc không có số)
                r'theo\s+tài\s+liệu',  # Match: "Theo tài liệu", "theo tài liệu" (không cần số)
                r'theo\s+tài\s+liệu\s+\d+',  # Match: "Theo tài liệu 123", "theo tài liệu 456" (có số)
                r'theo\s+văn\s+bản',  # Match: "Theo văn bản", "theo văn bản"
                r'trong\s+tài\s+liệu',  # Match: "Trong tài liệu", "trong tài liệu"
            ],
            'definition': [
                r'là\s+gì\s*$|định nghĩa.*là|khái niệm.*là',  # Match: "X là gì", "Định nghĩa X là", "Khái niệm Y là"
                r'viết\s+tắt.*là|tên\s+gọi.*là|được\s+gọi\s+là',  # Match: "Viết tắt của X là", "Tên gọi của Y là", "Được gọi là Z"
                r'được\s+định\s+nghĩa|được\s+hiểu|được\s+ký\s+hiệu',  # Match: "Được định nghĩa", "Được hiểu", "Được ký hiệu"
                r'định\s+nghĩa\s+của|khái\s+niệm\s+của',  # Match: "Định nghĩa của X", "Khái niệm của Y"
            ],
            'comparison': [
                r'khác\s+nhau.*ở|giống\s+nhau.*ở',  # Match: "Khác nhau ở điểm nào", "Giống nhau ở đâu"
                r'khác\s+.*\s+ở\s+những\s+điểm|giống\s+.*\s+ở\s+những\s+điểm',  # Match: "X khác Y ở những điểm", "X giống Y ở những điểm"
                r'so\s+sánh.*và|điểm\s+khác|điểm\s+chung',  # Match: "So sánh X và Y", "Điểm khác", "Điểm chung"
                r'khác\s+biệt.*giữa|sự\s+khác\s+biệt',  # Match: "Khác biệt giữa X và Y", "Sự khác biệt"
            ],
            'procedure': [
                r'bước\s+đầu\s+tiên|bước\s+nào|thứ\s+tự.*bước',  # Match: "Bước đầu tiên", "Bước nào", "Thứ tự các bước"
                r'quy\s+trình.*gồm|quy\s+trình.*bao\s+nhiêu',  # Match: "Quy trình gồm", "Quy trình bao nhiêu bước"
                r'tcvn|iso|theo.*quy\s+định|theo.*tiêu\s+chuẩn',  # Match: "TCVN", "ISO", "Theo quy định", "Theo tiêu chuẩn"
                r'sắp\s+xếp.*bước|thực\s+hiện.*bước',  # Match: "Sắp xếp các bước", "Thực hiện bước"
                r'quy\s+trình.*là\s+gì',  # Match: "Quy trình là gì"
            ],
            'explanation': [
                r'giải\s+thích.*nguyên\s+lý|mô\s+tả.*nguyên\s+lý',  # Match: "Giải thích nguyên lý", "Mô tả nguyên lý hoạt động"
                r'nguyên\s+lý.*hoạt\s+động|cơ\s+chế.*hoạt\s+động',  # Match: "Nguyên lý hoạt động", "Cơ chế hoạt động"
                r'hoạt\s+động.*như\s+thế\s+nào|vai\s+trò.*là\s+gì',  # Match: "Hoạt động như thế nào", "Vai trò là gì"
                r'trình\s+bày.*cách|mô\s+tả.*cách',  # Match: "Trình bày cách", "Mô tả cách hoạt động"
            ],
            'identification': [
                r'đâu\s+là.*đúng|đâu\s+không\s+phải',  # Match: "Đâu là đúng", "Đâu không phải", "Đâu là phương án đúng"
                r'thành\s+phần\s+nào|mô\s+hình\s+nào',  # Match: "Thành phần nào", "Mô hình nào"
                r'công\s+nghệ\s+nào|thuật\s+toán\s+nào',  # Match: "Công nghệ nào", "Thuật toán nào"
                r'phương\s+pháp\s+nào|đơn\s+vị\s+nào',  # Match: "Phương pháp nào", "Đơn vị nào"
            ],
            'application': [
                r'ứng\s+dụng.*là\s+gì|sử\s+dụng.*để\s+làm',  # Match: "Ứng dụng là gì", "Sử dụng để làm gì"
                r'dùng\s+để\s+làm\s+gì|mục\s+đích.*là\s+gì',  # Match: "Dùng để làm gì", "Mục đích là gì"
                r'được\s+dùng|được\s+sử\s+dụng|vai\s+trò',  # Match: "Được dùng", "Được sử dụng", "Vai trò"
            ],
            'reason': [
                r'tại\s+sao|vì\s+sao|lý\s+do.*là',  # Match: "Tại sao", "Vì sao", "Lý do là gì"
                r'nguyên\s+nhân.*là|vì.*nên|do.*nên',  # Match: "Nguyên nhân là", "Vì X nên Y", "Do X nên Y"
            ],
        }
    
    def classify(self, question: str) -> str:
        """
        Phân loại câu hỏi thành các loại
        
        Args:
            question: Câu hỏi cần phân loại
            
        Returns:
            Loại câu hỏi (calculation, table_data, document_comprehension, 
                         definition, comparison, procedure, explanation, 
                         identification, application, reason, hoặc general)
        """
        if not question or not question.strip():
            return 'general'
        
        question_lower = question.lower()
        
        # Kiểm tra từng loại theo thứ tự ưu tiên
        # Thứ tự quan trọng vì một câu hỏi có thể match nhiều pattern
        priority_order = [
            'table_data',           # Kiểm tra bảng trước (rất specific)
            'document_comprehension', # Kiểm tra tài liệu cụ thể
            'calculation',          # Tính toán
            'definition',          # Định nghĩa
            'comparison',          # So sánh
            'procedure',           # Quy trình
            'explanation',         # Giải thích
            'identification',      # Nhận dạng
            'application',         # Ứng dụng
            'reason',              # Lý do
        ]
        
        for q_type in priority_order:
            if q_type in self.patterns:
                for pattern in self.patterns[q_type]:
                    if re.search(pattern, question_lower):
                        return q_type
        
        # Mặc định là general
        return 'general'
    
    def get_confidence(self, question: str, q_type: str) -> float:
        """
        Tính độ tin cậy của phân loại
        
        Args:
            question: Câu hỏi
            q_type: Loại câu hỏi đã phân loại
            
        Returns:
            Độ tin cậy từ 0.0 đến 1.0
        """
        if not question or q_type == 'general':
            return 0.5
        
        question_lower = question.lower()
        matches = 0
        total_patterns = len(self.patterns.get(q_type, []))
        
        if total_patterns == 0:
            return 0.0
        
        for pattern in self.patterns.get(q_type, []):
            if re.search(pattern, question_lower):
                matches += 1
        
        # Tính tỷ lệ pattern match
        confidence = matches / total_patterns
        
        # Nếu có nhiều pattern match, confidence cao hơn
        if matches > 1:
            confidence = min(1.0, confidence * 1.2)
        
        return confidence
    
    def get_all_matches(self, question: str) -> Dict[str, float]:
        """
        Trả về tất cả các loại có thể match và confidence của chúng
        
        Args:
            question: Câu hỏi
            
        Returns:
            Dictionary với key là loại câu hỏi và value là confidence
        """
        if not question:
            return {'general': 0.5}
        
        question_lower = question.lower()
        matches = {}
        
        for q_type, pattern_list in self.patterns.items():
            match_count = 0
            for pattern in pattern_list:
                if re.search(pattern, question_lower):
                    match_count += 1
            
            if match_count > 0:
                confidence = match_count / len(pattern_list)
                if match_count > 1:
                    confidence = min(1.0, confidence * 1.2)
                matches[q_type] = confidence
        
        if not matches:
            matches['general'] = 0.5
        
        return matches

