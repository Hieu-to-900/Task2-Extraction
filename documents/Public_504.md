# Public_504

# Thiết kế và mô phỏng mô hình thiết bị thực nghiệm trong phòng thí nghiệm

Quá trình thiết kế và mô phỏng được thực hiện nhằm đảm bảo mô hình hoạt động chính xác, đồng thời giảm thiểu rủi ro trước khi chế tạo thực tế. Các bước triển khai bao gồm:

  * Xác định yêu cầu kỹ thuật: Mạch phải phát hiện nhanh hiện tượng chạm đất với độ nhạy cao, thời gian đáp ứng nhỏ hơn 10 ms và đảm bảo độ tin cậy khi vận hành trong môi trường phòng thí nghiệm.

  * Lựa chọn cấu hình mô hình: Hệ thống được thiết kế trên cơ sở mạng điện 3 pha quy đổi từ điện áp 6 kV sang 400 VAC, bảo đảm an toàn khi thử nghiệm.

  * Mô phỏng trên phần mềm: Sử dụng phần mềm chuyên dụng (như MATLAB/Simulink, Proteus hoặc Multisim) để xây dựng mô hình lý thuyết. Các thành phần chính gồm nguồn xoay chiều 3 pha, tải, mạch phát hiện chạm đất, và khối hiển thị kết quả.

  * Phân tích kết quả mô phỏng: Các dạng sóng điện áp và dòng điện được theo dõi để xác định sự khác biệt giữa trạng thái bình thường và khi có sự cố chạm đất. Tín hiệu ngõ ra được kiểm chứng nhằm đánh giá khả năng tác động của mạch.


Mục tiêu của giai đoạn này là đảm bảo thiết kế có tính khả thi, đồng thời cung cấp cơ sở dữ liệu cho bước chế tạo thực nghiệm.

# Thử nghiệm tại phòng thí nghiệm

Sơ đồ nguyên lý đóng vai trò then chốt trong việc quyết định khả năng phát hiện sự cố của thiết bị. Việc lựa chọn được tiến hành theo các tiêu chí:

  * Nguyên tắc phát hiện : Dựa trên việc so sánh điện áp các pha với điểm trung tính hoặc với nhau để phát hiện sự mất cân bằng khi xảy ra chạm đất.

  * Cấu trúc mạch : Bao gồm bộ chỉnh lưu tín hiệu điện áp, mạch lọc, mạch so sánh và rơ le tác động. Sơ đồ được thiết kế sao cho tín hiệu ra có độ trễ nhỏ nhất, đồng thời giảm thiểu ảnh hưởng của nhiễu.

  * Độ nhạy và an toàn : Các linh kiện chọn phải có khả năng chịu điện áp và dòng điện phù hợp, đồng thời vẫn đảm bảo an toàn khi thử nghiệm trong phòng thí nghiệm.

  * Khả năng mở rộng : Sơ đồ cho phép tích hợp thêm các module hiển thị hoặc kết nối máy tính để giám sát và ghi nhận dữ liệu.


Qua quá trình phân tích, sơ đồ nguyên lý được lựa chọn nhằm đáp ứng đầy đủ yêu cầu kỹ thuật, vừa đơn giản trong chế tạo, vừa hiệu quả trong phát hiện sự cố.

Các kết quả thử nghiệm
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Mô phỏng</strong></th>
<th><strong>Thực nghiệm</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>|<image_1>|</td>
<td>|<image_2>|</td>
</tr>
</tbody>
</table> 

Hình 4.11. Tín hiệu trước chỉnh lưu
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Mô phỏng</strong></th>
<th><strong>Thực nghiệm</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>|<image_3>|</td>
<td>|<image_4>|</td>
</tr>
</tbody>
</table> 

Hình 4.12. Tín hiệu sau chỉnh lưu của mỗi pha
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Mô phỏng</strong></th>
<th><strong>Thực nghiệm</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>|<image_5>|</p>
</blockquote></td>
<td>|<image_6>|</td>
</tr>
</tbody>
</table> 

Hình 4.13. Tín hiệu hiệu điện áp giữa các pha khi không có sự cố

|<image_7>|

Hình 4.15. Hình ảnh thể hiện chạm đất pha B

|<image_8>|

Hình 4.16. Dạng sóng đo được khi thử chạm đất pha A
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th rowspan="2"><blockquote>
<p><strong>STT</strong></p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p><strong>Điện trở rò (Ω)</strong></p>
</blockquote></th>
<th colspan="2"><strong>Đồ thị dạng sóng</strong></th>
<th rowspan="2"><blockquote>
<p><strong>Thời gian phát hiện (ms); kết luận</strong></p>
</blockquote></th>
</tr>
<tr>
<th><p>Mô phỏng</p>
<blockquote>
<p>Yêu cầu thời gian tác động ≤ 2ms do trong mô phỏng không có phần tử
Rơ le</p>
</blockquote></th>
<th><blockquote>
<p>Thực nghiệm Yêu cầu thời gian tác</p>
<p>động của Rơ le ≤ 10ms</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>10</td>
<td>|<image_9>|</td>
<td>|<image_10>|</td>
<td rowspan="3"><p>10</p>
<blockquote>
<p>Đạt</p>
</blockquote></td>
</tr>
<tr>
<td>2</td>
<td>20</td>
<td><blockquote>
<p>|<image_11>|</p>
</blockquote></td>
<td>|<image_12>|</td>
</tr>
<tr>
<td>3</td>
<td>26</td>
<td><blockquote>
<p>|<image_13>|</p>
</blockquote></td>
<td>|<image_14>|</td>
</tr>
<tr>
<td>4</td>
<td>27</td>
<td><blockquote>
<p>|<image_15>|</p>
</blockquote></td>
<td>|<image_16>|</td>
<td><p>10</p>
<blockquote>
<p>Tác động không chắc chắn</p>
</blockquote></td>
</tr>
<tr>
<td>5</td>
<td>30</td>
<td><blockquote>
<p>|<image_17>|</p>
</blockquote></td>
<td>|<image_18>|</td>
<td><blockquote>
<p>Không phát hiện được pha chạm đất</p>
</blockquote></td>
</tr>
</tbody>
</table> 

Bảng 4.3. Kết quả thực nghiệm xác định thời gian phát hiện pha chạm đất

# Nhận xét

  * Các dạng sóng mô phỏng và thực nghiệm là tương tự. Sự sai lệch do sai số linh kiện, các điện trở và tụ điện trong thực tế có sai số ±5%, trong khi đó các linh kiện mô phỏng là lý tưởng.

  * Mạch có khả năng phát hiện pha chạm đất.

  * Đối với mạng quy đổi từ điện áp 6kV sang 400VAC, mạch có khả năng phát hiện pha rò với điện trở rò không quá 26.6Ω và tác động đến rơ le với tổng thời gian không vượt quá 10m.