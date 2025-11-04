# Public_568

# Giới thiệu

Công nghệ dán bề mặt (Surface Mount technology - SMT) là một công nghệ tiên tiến giúp gắn kết nhanh và chính xác các linh kiện điện tử hay vi xử lý lên các bảng mạch điện - điều khiển [1]. Cách mạng công nghiệp 4.0 đòi hỏi lượng lớn nhu cầu về các hệ thống tự động được kiểm soát bởi các bộ điều khiển với các mạch điện tử tinh xảo bên trong [2]. Ngày nay, các mạch điện tử như vậy thông thường được tạo ra bởi các dây chuyền thuộc SMT. Đây là công nghệ thay thế kỹ thuật đục lỗ trên bảng mạch điện tử truyền thống, cải thiện năng suất sản xuất và nâng cao tính tự động hóa cho quy trình sản xuất mạch điện tử [3]. Một dây chuyền lắp ráp mạch điện tử hoàn chỉnh theo công nghệ SMT cơ bản cần có bốn công đoạn chính: Quét hợp kim hàn dạng kem lên bảng mạch; gắp thả các linh kiện điện tử và mạch; gia nhiệt giúp chảy kem hàn; và kiểm tra chất lượng mạch sau gia công [4]. Về cơ bản, trong một dây chuyền tự động hóa hoàn toàn, mỗi công đoạn cần một cơ cấu máy khác nhau, tuy nhiên, độ chính xác của các mạch điện tử khi gia công phụ thuộc nhiều vào độ chính xác của cơ cấu gắp thả và đặt linh kiện điện tử trên bảng mạch [1].
Máy lắp ráp linh kiện điện tử (máy SMT-P&P) là hệ thống quan trọng và cần thiết nhất trong giai đoạn gắp thả và định vị các linh kiện điện - điện tử trong dây chuyền SMT [5]. Tốc độ lắp ráp mạch hoàn chỉnh, định vị độ chính xác rất cao. Tuy nhiên, chúng thường đòi hỏi lượng lớn chi phí đầu tư ban đầu, điều này lại là trở ngại lớn cho nền công nghiệp sản xuất vừa và nhỏ như ở Việt Nam [11]. Chính vì vậy, các mô hình máy có kích thước nhỏ, chi phí thấp là điều phù hợp hơn trong các mục đích sử dụng để sản xuất đơn chiếc hoặc số lượng nhỏ cũng như dùng cho sản xuất mạch điện – điện tử phục vụ cho công việc nghiên cứu. Tại Việt Nam, máy SMT-P&P chủ yếu là nhập khẩu như Hình 1. Các doanh nghiệp nhỏ thường chọn giải pháp đặt hàng yêu cầu gia công mạch ở nước ngoài với số lượng nhất định để giảm thiểu chi phí. Vì vậy việc hiểu được quy trình thiết kế và tạo ra máy SMT-P&P trong điều kiện của nước ta với giá thành hợp lý sẽ tiết kiệm đáng kể chi phí và thời gian.
|<image_1>|
_Hình 1. Máy SMT-P&P dán cỡ nhỏ thông dụng [12]_

# Yêu cầu hệ thống máy P&P

Về cơ bản, một hệ máy SMT-P&P cần đảm bảo các vấn đề về năng suất, độ chính xác, tính ổn định, khả năng sử dụng linh hoạt, chi phí chế tạo phù hợp với quy mô sản xuất của máy và khả năng thay thế dể dàng các thành phần. Đầu tiên, nguyên lý động học máy và đặc điểm chuyển động máy cần lựa chọn đơn giản, hiệu quả nhằm mục đích giảm sai số vận hành, tăng hiệu suất và dễ dàng thay thế các thành phần khi hỏng hóc. Bên cạnh các yêu cầu chính xác về khoảng cách giữa các bộ phận, kết cấu máy cần đảm bảo cứng vững và hạn chế tối đa các tác nhân gây rung động không muốn do đặc điểm thiết kế thực tế [13], [14]. Hơn nữa, hệ thống mạch điện và thuật toán điều khiển [14] cũng cần được quan tâm; chúng phải đủ khả năng điều khiển đồng bộ nhiều hệ thống cùng lúc, phối hợp tốt để gắp và thả các linh kiện một cách chính xác, đúng lúc. Việc gắp và nhả nhanh chóng các linh kiện với các kích thước linh hoạt cũng phụ thuộc nhiều vào độ nhạy của cơ cấu chấp hành cuối – đầu hút chân không của máy. Ngoài ra, các hệ máy SMT-P&P cỡ nhỏ và chi phí thấp thường không đi kèm với các hệ thống giám sát hình ảnh, điều này dẫn đến việc phải cân chỉnh thủ công máy trong mỗi lần chạy máy. Do đó, trong máy SMT-P&P, hệ thống giám sát hoạt động là cần thiết để tăng độ chính xác khi hoạt động máy. Tương quan các yêu cầu hoạt động và khả năng đáp ứng của các bộ phận máy SMT-P&P được giới thiệu ở Bảng 1, khả năng làm việc linh hoạt của máy với các linh kiện khác nhau được giới thiệu ở Bảng 2.
_Bảng 1. Tương quan đặc điểm hoạt động của máy SMT-P&P và tác động của các thành phần tạo nên máy_
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>Đặc điểm</p>
</blockquote></th>
<th><blockquote>
<p>Nguyên nhân</p>
</blockquote></th>
<th><blockquote>
<p>Thành phần máy</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>Độ chính xác máy</p>
</blockquote></td>
<td><ul>
<li><p>Dao động hệ thống</p></li>
<li><p>Sai số cấu trúc</p></li>
<li><p>Sai số điều khiển</p></li>
<li><p>Sai số góc và vị trí của linh kiện được lắp ráp trên
mạch</p></li>
</ul></td>
<td><ul>
<li><p>Cấu trúc khung máy</p></li>
<li><p>Động học/ động lực học máy</p></li>
<li><p>Động cơ điện và cơ cấu truyền động</p></li>
<li><p>Hệ thống giám sát sai số</p></li>
</ul></td>
</tr>
<tr>
<td><blockquote>
<p>Năng suất máy</p>
</blockquote></td>
<td><ul>
<li><p>Tốc độ chạy máy</p></li>
<li><p>Thời gian và số lượt di chuyển</p></li>
<li><p>Tốc độ gắp và thả linh kiện</p></li>
<li><p>Tốc độ điều khiển và xử lý hình ảnh</p></li>
</ul></td>
<td><ul>
<li><p>Hệ thống cung cấp khí nén &amp; đầu hút</p></li>
<li><p>Động cơ điện</p></li>
<li><p>Hệ thống mạch điện và điều khiển</p></li>
<li><p>Hệ thống camera giám sát</p></li>
</ul></td>
</tr>
<tr>
<td><blockquote>
<p>Chi phí vận hành và sửa chữa</p>
</blockquote></td>
<td><ul>
<li><p>Cấu trúc đơn giản hay phức tạp.</p></li>
<li><p>Nguồn cung cấp linh kiện cho máy</p></li>
</ul></td>
<td><ul>
<li><p>Cấu trúc tổng thể máy</p></li>
<li><p>Hệ thống phần mềm quản lý chung của máy</p></li>
</ul></td>
</tr>
</tbody>
</table> 

_Bảng 2. Một số loại kinh kiện có thể thao tác được với máy_
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>Mã hiệu</p>
</blockquote></th>
<th><blockquote>
<p>Loại</p>
</blockquote></th>
<th><blockquote>
<p>Kích thước (Dài x Rộng)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>0402</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>Tụ dán</p>
</blockquote></td>
<td><blockquote>
<p>1,0 x 0,5 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>0603</p>
</blockquote></td>
<td><blockquote>
<p>1,6 x 0,8 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>0805</p>
</blockquote></td>
<td><blockquote>
<p>2,0 x 1,2 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>1206</p>
</blockquote></td>
<td><blockquote>
<p>3,2 x 1,6 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>2512</p>
</blockquote></td>
<td><blockquote>
<p>6,4 x 3,2 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>SOIC-8-N</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>Chip dán (Surface mount IC package)</p>
</blockquote></td>
<td><blockquote>
<p>4,8 x 3,8 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>TSOP6</p>
</blockquote></td>
<td><blockquote>
<p>1,5 x 2,9 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>SSOP8</p>
</blockquote></td>
<td><blockquote>
<p>5,3 x 12 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>32 pins -LQFP</p>
</blockquote></td>
<td><blockquote>
<p>5 x 5 (mm)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Microstar 64 pins - BGA</p>
</blockquote></td>
<td><blockquote>
<p>8 x 8 (mm)</p>
</blockquote></td>
</tr>
</tbody>
</table>