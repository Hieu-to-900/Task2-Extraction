"""
Script để phân chia Question-Bank-GD4.csv thành nhiều file nhỏ
theo question type từ QuestionClassifier
"""

import csv
import os
import sys
from collections import defaultdict
from question_classifier import QuestionClassifier

# Set UTF-8 encoding for stdout on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def split_questions_by_category(csv_path: str, output_dir: str = "categories"):
    """
    Phân chia file CSV thành nhiều file theo question type
    
    Args:
        csv_path: Đường dẫn đến file CSV gốc
        output_dir: Thư mục để lưu các file đã phân chia
    """
    print("="*80)
    print("Phan chia cau hoi theo category")
    print("="*80)
    
    # Tạo thư mục output nếu chưa có
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ Đã tạo thư mục: {output_dir}/")
    else:
        print(f"📁 Sử dụng thư mục có sẵn: {output_dir}/")
    
    # Khởi tạo classifier
    print("\n🔄 Đang khởi tạo QuestionClassifier...")
    classifier = QuestionClassifier()
    
    # Đọc file CSV
    print(f"\n📖 Đang đọc file: {csv_path}")
    try:
        questions_data = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                questions_data.append(row)
        
        total_questions = len(questions_data)
        print(f"✅ Đã đọc {total_questions} câu hỏi")
    except Exception as e:
        print(f"❌ Lỗi khi đọc file CSV: {str(e)}")
        return
    
    # Kiểm tra columns
    if questions_data:
        required_columns = ['Question', 'A', 'B', 'C', 'D']
        if not all(col in questions_data[0].keys() for col in required_columns):
            print(f"❌ File CSV thiếu các cột cần thiết: {required_columns}")
            return
    
    # Phân loại từng câu hỏi
    print("\n🔍 Đang phân loại câu hỏi...")
    category_counts = defaultdict(int)
    
    for row in questions_data:
        question = row.get('Question', '')
        category = classifier.classify(question)
        row['category'] = category
        category_counts[category] += 1
    
    print(f"\n[STATS] Thong ke phan loai:")
    print("-" * 80)
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_questions) * 100
        print(f"  {category:25s}: {count:4d} cau ({percentage:5.2f}%)")
    print("-" * 80)
    print(f"  {'Tong cong':25s}: {total_questions:4d} cau (100.00%)")
    
    # Lưu các file CSV theo category
    print(f"\n[INFO] Dang luu cac file CSV theo category...")
    saved_files = []
    
    # Nhóm câu hỏi theo category
    questions_by_category = defaultdict(list)
    for row in questions_data:
        category = row['category']
        questions_by_category[category].append(row)
    
    # Lấy header từ câu hỏi đầu tiên (bỏ cột category)
    if questions_data:
        header = [col for col in questions_data[0].keys() if col != 'category']
    
    # Lưu từng category
    for category in sorted(questions_by_category.keys()):
        category_questions = questions_by_category[category]
        
        # Tên file
        filename = f"Question-Bank-GD4-{category}.csv"
        filepath = os.path.join(output_dir, filename)
        
        # Lưu file
        try:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                for row in category_questions:
                    # Xóa cột category trước khi ghi
                    row_to_write = {k: v for k, v in row.items() if k != 'category'}
                    writer.writerow(row_to_write)
            
            saved_files.append((filename, len(category_questions)))
            print(f"  [OK] {filename:40s} - {len(category_questions):4d} cau hoi")
        except Exception as e:
            print(f"  [ERROR] Loi khi luu {filename}: {str(e)}")
    
    # Tạo file summary
    summary_path = os.path.join(output_dir, "summary.txt")
    try:
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("THỐNG KÊ PHÂN CHIA CÂU HỎI THEO CATEGORY\n")
            f.write("="*80 + "\n\n")
            f.write(f"Tổng số câu hỏi: {total_questions}\n")
            f.write(f"Số lượng category: {len(category_counts)}\n\n")
            f.write("-"*80 + "\n")
            f.write("PHÂN BỐ THEO CATEGORY:\n")
            f.write("-"*80 + "\n")
            
            for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / total_questions) * 100
                f.write(f"{category:25s}: {count:4d} câu ({percentage:5.2f}%)\n")
            
            f.write("-"*80 + "\n")
            f.write(f"{'Tổng cộng':25s}: {total_questions:4d} câu (100.00%)\n\n")
            f.write("="*80 + "\n")
            f.write("DANH SÁCH FILE ĐÃ TẠO:\n")
            f.write("="*80 + "\n")
            
            for filename, count in saved_files:
                f.write(f"  {filename:40s} - {count:4d} câu hỏi\n")
        
        print(f"\n[OK] Da tao file summary: {summary_path}")
    except Exception as e:
        print(f"[ERROR] Loi khi tao file summary: {str(e)}")
    
    # Tổng kết
    print("\n" + "="*80)
    print("[OK] HOAN THANH!")
    print("="*80)
    print(f"[INFO] Thu muc output: {output_dir}/")
    print(f"[INFO] So file da tao: {len(saved_files)}")
    print(f"[INFO] Tong so cau hoi: {total_questions}")
    print(f"[INFO] File summary: {summary_path}")
    print("="*80)


if __name__ == "__main__":
    # Đường dẫn file CSV gốc
    csv_path = "Question-Bank-GD4.csv"
    
    # Kiểm tra file tồn tại
    if not os.path.exists(csv_path):
        print(f"[ERROR] Khong tim thay file: {csv_path}")
        print("   Vui long dam bao file CSV nam trong cung thu muc voi script nay.")
        exit(1)
    
    # Chạy phân chia
    split_questions_by_category(csv_path, output_dir="categories")

