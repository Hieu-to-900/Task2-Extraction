# Public_503

# Thuật toán (Algorithm)

## Khái niệm

  * Thuật toán là khái niệm cơ sở của toán học và tin học.

  * Thuật toán là phương pháp thể hiện lời giải của vấn đề – bài toán.

  * Thuật toán là dãy các thao tác, các hướng dẫn rõ ràng, được sắp xếp theo một trình tự xác định, sao cho 2 bộ xử lý (người/máy) khác nhau, với cùng điều kiện đầu vào như nhau thì sau một số bước hữu hạn thực hiện, sẽ cho kết quả giống nhau mà không cần biết ý nghĩa của các thao tác này. Cần chú ý là không phải mọi dãy thao tác, chỉ dẫn nào cũng đều tạo ra thuật toán. Phương pháp nấu ăn, cách dùng thuốc,… đều không phải là thuật toán do các thao tác, các chỉ dẫn là không xác định, không rõ ràng.


## Các đặc trưng của thuật toán

_Tính xác định: Các thao tác của thuật toán phải xác định, không được nhập nhằng, mơ hồ để có thể dễ dàng cài đặt trên một hệ tự động hóa.
_Tính dừng: Thuật toán phải dừng sau một số hữu hạn bước thực hiện.
_Tính đúng đắn: Thuật toán phải cho kết quả đúng theo yêu cầu của bài toán đặt ra.
_Tính phổ dụng: Thuật toán có thể được sử dụng lại để giải một lớp bài toán tương tự.
_Tính hiệu quả: Thuật toán cần tối ưu về sử dụng bộ nhớ và đáp ứng yêu cầu của bài toán trong thời gian ngắn nhất có thể được. Thực tế rất khó đạt được cả 2 yêu cầu này trong một thuật toán.

## Các công cụ biểu diễn thuật toán

Ngôn ngữ tự nhiên : là ngôn ngữ liệt kê các bước, mô tả thuật toán theo ngôn ngữ tự nhiên của con người.
Ví dụ: Thuật toán xác định trị lớn nhất trong 5 số nguyên.
B1. Gọi a, b, c, d, e là 5 biến lưu trữ các trị nguyên cho trước (nhập từ bàn
phím).
B2. Gọi max là biến lưu trữ trị lớn nhất trong 5 số nguyên trên, và giả sử a có trị lớn nhất.
B3. Lần lượt so sánh trị của max với các biến b, c, d, e còn lại. Nếu trị của max nhỏ hơn bất kỳ biến nào thì gán trị của biến đó cho max.
B4. Xuất kết quả trị biến max ra màn hình
Lưu đồ thuật toán hay sơ đồ khối (Flow chart) : là công cụ cho phép biểu diễn thuật toán một cách trực quan. Thường chỉ có thể dùng công cụ lưu đồ đối với các thuật toán tương đối ngắn, có thể được biểu diễn trong một trang giấy. Các hình cơ bản sử dụng trong lưu đồ:
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>Hình oval mô tả điểm xuất phát /</p>
<p>kết thúc.</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>Hình chữ nhật mô tả một hay</p>
<p>nhiều chỉ thị máy cần thực hiện.</p>
</blockquote></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Hình bình hành mô tả thao tác</p>
<p>nhập/xuất dữ liệu.</p>
</blockquote></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>Hình thoi mô tả sự rẻ nhánh, lựa</p>
<p>chọn, phép kiểm tra điều kiện</p>
</blockquote></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p><em>Mũi tên chỉ hướng lưu chuyển</em></p>
<p><em>của các thao tác.</em></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table> 

Mã giả (Pseudo code) gần giống như ngôn ngữ tự nhiên, nhưng có sử dụng các cấu trúc chuẩn hóa (khai báo biến, chú thích, cấu trúc điều khiển, . . .) do người thiết kế quy định.
Ngôn ngữ lập trình (Programming language) là hệ thống các ký hiệu cho phép mô tả các quy trình tính toán dưới dạng văn bản.

# Ngôn ngữ lập trình (NNLT)

Các thành phần cơ bản của NNLT bao gồm:

  * Bộ kí tự (character set) hay bảng chữ cái dùng để viết chương trình.

  * Cú pháp (syntax) là bộ quy tắc để viết chương trình.

  * Ngữ nghĩa (semantic) xác định ý nghĩa các thao tác, hành động cần phải thực hiện, ngữ cảnh (context) của các câu lệnh trong chương trình.


Hiện đã có hàng nghìn NNLT được thiết kế, và hàng năm lại có thêm nhiều NNLT mới xuất hiện. Sự phát triển của NNLT gắn liền với sự phát triển của ngành tin học. Mỗi loại NNLT phù hợp với một số lớp bài toán nhất định.
Phân loại NNLT:

  *Ngôn ngữ máy(machine language) hay còn gọi là NNLT cấp thấp có tập lệnh phụ thuộc vào một hệ máy cụ thể. Chương trình viết bằng ngôn ngữ máy sử dụng bảng chữ cái chỉ gồm 2 kí tự 0, 1. Chương trình ngôn ngữ máy được nạp trực tiếp vào bộ nhớ và thực hiện ngay.

  *Ngôn ngữ lập trình cấp caonói chung không phụ thuộc vào loại máy tính cụ thể. Chương trình viết bằng NNLT cấp cao sử dụng bộ kí tự phong phú hơn, và phải được chuyển đổi sang dạng mã máy để máy tính có thể hiểu được bằng chương trình dịch. Một số NNLT cấp cao thông dụng hiện nay: Pascal, C, C++, Java, Smalltalk, Basic, Ruby, Fortran, Algol, Lisp, Prolog, Cobol, ...


# Chương trình (máy tính)

Là tập hợp hữu hạn các chỉ thị máy được bố trí, sắp xếp theo một trật tự xác định, nhằm giải quyết yêu cầu của bài toán đặt ra. Chương trình được viết bằng một NNLT cụ thể nào đó.
Các chương trình C/C++ (trong môi trường DOS) được tạo ra bằng 1 trình soạn thảo văn bản (EDITOR) như: SK, NC Editor, VRES. . . Hiện nay, các chương trình dịch đều tích hợp sẵn editor riêng cho phép USER soạn thản, biên dịch, kiểm lỗi, liên kết và thực hiện chương trình một cách dễ dàng.
Các chương trình này (mã nguồn – source code), thực chất là ở dạng ngôn ngữ tự nhiên, do đó phải được biên dịch lại dưới dạng mã máy (object code) mà máy tính có thể hiểu được. Việc này được thực hiện bởi chương trình dịch.
Có 2 loại chương trình dịch:

  * Trình thông dịch (interpreter) : mỗi lệnh được dịch sang mã máy và cho thực hiện ngay.

  * Trình biên dịch (compiler): toàn bộ chương trình nguồn được dịch sang mã máy (tập tin.obj), sau đó trình liên kết (linker) sẽ kết nối các module chương trình để tạo thành tập tin EXE.