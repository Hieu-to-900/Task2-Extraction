# Public_478

# GIỚI THIỆU VỀ LỌC SỐ SỐ

Lọc số (Digital Filtering) là kỹ thuật xử lý tín hiệu rời rạc nhằm triệt tiêu hoặc giảm thiểu thành phần nhiễu, tăng cường thành phần mong muốn.

Trong lĩnh vực xử lý tín hiệu, thiết kế bộ lọc số chiếm vai trò then chốt với các ứng dụng từ âm thanh, hình ảnh đến thông tin vô tuyến và điều khiển tự động.

MATLAB cung cấp nhiều công cụ mạnh mẽ như Signal Processing Toolbox để xây dựng, mô phỏng và đánh giá hiệu năng của các bộ lọc FIR và IIR.

# NỘI DUNG CHI TIẾT HƯỚNG DẪN MÔ PHỎNG

## Yêu cầu trước khi thực hành 
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><p>Một số yêu cầu bao gồm:</p>
<ul>
<li><p>Nắm bắt kiến thức cơ bản về tín hiệu rời rạc và hệ thống
LTI.</p></li>
<li><p>Hiểu khái niệm biến đổi z và biến đổi Fourier rời rạc.</p></li>
<li><p>Sử dụng thành thạo MATLAB và Signal Processing Toolbox.</p></li>
<li><p>Có kinh nghiệm đọc đồ thị đáp ứng tần số và nhóm pha.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Mục đích của phần thực hành
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><ul>
<li><p>Xây dựng và so sánh bộ lọc FIR và IIR cho bài toán loại bỏ
nhiễu.</p></li>
<li><p>Thiết kế cửa sổ Hamming, Kaiser và thuật toán
Parks–McClellan.</p></li>
<li><p>Đánh giá đáp ứng tần số, đáp ứng bước và độ ổn định của bộ
lọc.</p></li>
<li><p>Phân tích ảnh hưởng của tham số thiết kế lên đặc tính
lọc.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Tóm tắt lý thuyết 

Bộ lọc số được chia thành hai họ chính: FIR (Finite Impulse Response) và IIR (Infinite Impulse Response).

FIR có đáp ứng xung hữu hạn, dễ đạt pha tuyến tính; IIR có đáp ứng xung vô hạn, đạt đặc tính biên dải sắc với bậc thấp nhưng pha thường không tuyến tính.

Quy trình thiết kế tiêu chuẩn gồm xác định yêu cầu phổ, lựa chọn loại bộ lọc (thấp, cao, băng, dừng), xác lập tần số cắt và gợn râu, sau đó chọn phương pháp thiết kế phù hợp và kiểm chứng ổn định, thực thi.

## Định nghĩa các hệ thống lọc cơ bản

  * FIR (đáp ứng hữu hạn):
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><ol>
<li></li>
</ol></th>
<th><math><semantics><mrow><mi>y</mi><mo>[</mo><mi>n</mi><mo>]</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mi>M</mi></munderover><msub><mi>b</mi><mi>k</mi></msub><mo>⋅</mo><mi>x</mi><mo>[</mo><mi>n</mi><mo>−</mo><mi>k</mi><mo>]</mo></mrow><annotation>y\lbrack n\rbrack = \sum_{k = 0}^{M}b_{k} \cdot x\lbrack n - k\rbrack</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 
  * IIR (đáp ứng vô hạn):
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><ol>
<li></li>
</ol></th>
<th><blockquote>
<p><math><semantics><mrow><mi>y</mi><mo>[</mo><mi>n</mi><mo>]</mo><mo>=</mo><munderover><mo>∑</mo><mrow></mrow><mrow></mrow></munderover><mrow><mi>k</mi><mo>=</mo><msup><mn>0</mn><mi>M</mi></msup><msub><mi>b</mi><mi>k</mi></msub></mrow><mo>⋅</mo><mi>x</mi><mo>[</mo><mi>n</mi><mo>−</mo><mi>k</mi><mo>]</mo><mo>−</mo><munderover><mo>∑</mo><mrow></mrow><mrow></mrow></munderover><mrow><mi>k</mi><mo>=</mo><msup><mn>1</mn><mi>N</mi></msup><msub><mi>a</mi><mi>k</mi></msub></mrow><mo>⋅</mo><mi>y</mi><mo>[</mo><mi>n</mi><mo>−</mo><mi>k</mi><mo>]</mo></mrow><annotation>y\lbrack n\rbrack = \sum_{}^{}{k = 0^{M}b_{k}} \cdot x\lbrack n - k\rbrack - \sum_{}^{}{k = 1^{N}a_{k}} \cdot y\lbrack n - k\rbrack</annotation></semantics></math></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 
  * Bộ lọc thấp (Low-pass): Cho phép tần số ≤$f_{c}$.

  * Bộ lọc cao (High-pass): Cho phép tần số ≥ $f_{c}$.

  * Bộ lọc băng (Band-pass): Cho phép f₁ ≤ f ≤ f₂.

  * Bộ lọc dừng (Band-stop): Chặn f₁ ≤ f ≤ f₂.


## Phân loại hệ thống lọc số
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Loại lọc</strong></th>
<th><strong>Đặc điểm chính</strong></th>
<th><strong>Minh họa</strong></th>
<th><strong>Ứng dụng chính</strong></th>
<th><strong>Tính nhân quả</strong></th>
<th><strong>Tính ổn định</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>FIR</td>
<td>Pha tuyến tính; đáp ứng nhanh</td>
<td>|<image_1>|</td>
<td>Xử lý âm thanh, đo lường</td>
<td>Có</td>
<td>Luôn ổn định</td>
</tr>
<tr>
<td>IIR</td>
<td>Tiết kiệm bậc; pha không tuyến tính</td>
<td>|<image_2>|</td>
<td>Điều khiển, liên lạc</td>
<td>Có hoặc không</td>
<td>Tùy hệ số</td>
</tr>
<tr>
<td>Thấp (Low-pass)</td>
<td>Chặn thành phần tần số cao</td>
<td></td>
<td>Làm mượt tín hiệu, khử nhiễu</td>
<td>Có</td>
<td>Luôn ổn định</td>
</tr>
<tr>
<td>Cao (High-pass)</td>
<td>Chặn thành phần tần số thấp</td>
<td></td>
<td>Phát hiện cạnh, phân tích</td>
<td>Có</td>
<td>Tùy thiết kế</td>
</tr>
<tr>
<td>Băng thông (Band-pass)</td>
<td>Cho phép dải tần xác định</td>
<td></td>
<td>Xử lý vô tuyến, phân tích</td>
<td>Có</td>
<td>Tùy thiết kế</td>
</tr>
<tr>
<td>Băng dừng (Band-stop)</td>
<td>Chặn dải tần xác định</td>
<td></td>
<td>Loại bỏ tạp âm cụ thể</td>
<td>Có</td>
<td>Tùy thiết kế</td>
</tr>
</tbody>
</table> 

## Phương pháp thiết kế bộ lọc số

Trong MATLAB, thường sử dụng ba nhóm phương pháp:

  * Cửa sổ (Window Method): Hamming, Hanning, Kaiser.

  * Equiripple (Parks–McClellan): Tối ưu theo Chebyshev.

  * Thiết kế IIR cổ điển: Butterworth, Chebyshev I/II, Elliptic.
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Phương pháp thiết kế</strong></th>
<th><strong>Băng thông cắt</strong></th>
<th><strong>Độ gợn râu trong (dB)</strong></th>
<th><strong>Độ gợn râu dừng (dB)</strong></th>
<th><strong>Độ dốc (dB/oct)</strong></th>
<th><strong>Độ phức tạp tính toán</strong></th>
<th><strong>Ghi chú</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Window Hamming</td>
<td>Xác định thủ công</td>
<td>~0.02</td>
<td>~50</td>
<td>Trung bình</td>
<td>Thấp</td>
<td>Dễ cài đặt, pha gần tuyến tính</td>
</tr>
<tr>
<td>Window Kaiser</td>
<td>Điều chỉnh β</td>
<td>Tùy β</td>
<td>Tùy β</td>
<td>Cao</td>
<td>Trung bình</td>
<td>Linh hoạt, cân bằng gợn râu–độ dốc</td>
</tr>
<tr>
<td>Parks–McClellan</td>
<td>Tùy yêu cầu</td>
<td>Thiết lập rõ ràng</td>
<td>Thiết lập rõ ràng</td>
<td>Cao</td>
<td>Cao</td>
<td>Equiripple, tối ưu chặt chẽ</td>
</tr>
<tr>
<td>Butterworth (IIR)</td>
<td>Tự nhiên</td>
<td>–3</td>
<td>~20</td>
<td>Thấp</td>
<td>Thấp</td>
<td>Pha không tuyến tính</td>
</tr>
<tr>
<td>Chebyshev I (IIR)</td>
<td>Tự nhiên</td>
<td>0</td>
<td>~65</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table> 

## Quy trình thiết kế chi tiết

### Đặc tả yêu cầu phổ:

  * Loại: Thấp, cao, băng thông, băng dừng.

  * Tần số: Chỉ rõ $\omega_{p},\omega_{s}$(hoặc $f_{p},f_{s}$).

  * Độ gợn râu: Đặt $A_{p}$(dB) và $A_{s}$(dB).

  * Ràng buộc pha/độ trễ: Xác định yêu cầu tuyến tính pha nếu có.


### Chọn họ bộ lọc:

  * FIR nếu cần pha tuyến tính, ổn định vô điều kiện, chấp nhận bậc cao.

  * IIR nếu cần biên sắc với bậc thấp, chấp nhận méo pha.


### Chọn phương pháp thiết kế:

  * FIR–Window:

* Ưu tiên: Triển khai nhanh, dễ điều chỉnh; dùng Hamming/Hann cho gợn râu thấp, Kaiser khi cần tinh chỉnh.

* Bước tính: Ước lượng bậc từ suy hao dải dừng và vùng chuyển tiếp; tiền xử lý chuẩn hóa tần số; tạo bộ hệ số.

  * FIR–Equiripple:

* Ưu tiên: Tối ưu hóa cao, bậc tối thiểu; chỉ định trọng số từng dải để cân bằng lỗi.

  * IIR–Prototype:

* Butterworth/Chebyshev/Elliptic: Xác định bậc từ ($A_{p}$, $A_{s}$, $\omega_{p}$, $\omega_{s}$); tiền biến dạng tần số; dùng biến đổi song tuyến tính; phân rã thành biquad.


### Kiểm chứng miền tần số:

  * Biên độ: Đáp ứng dải thông trong [−$A_{p}$,+ $A_{p}$] dB; dải dừng dưới −$A_{s}$ dB.

  * Pha/độ trễ nhóm: Với FIR tuyến tính pha, xác minh $\tau_{g}$ gần hằng trên dải thông.


### Đánh giá miền thời gian:

  * Đáp ứng bước/xung: Kiểm tra vượt đỉnh, gợn sóng, thời gian xác lập.

  * Tín hiệu thực tế: Áp dụng trên dữ liệu để đánh giá nhiễu tồn dư, méo biên dạng.


### Ràng buộc thực thi:

  * Độ dài/độ trễ: FIR dài gây trễ; cân nhắc decimation hoặc cấu trúc phân pha (polyphase).

  * Số học cố định: Dùng biquad, chuẩn hóa thang, chống tràn; lượng tử hóa hệ số.


### Tinh chỉnh tham số:

  * FIR: Điều chỉnh bậc, loại cửa sổ, trọng số equiripple.

  * IIR: Điều chỉnh bậc, gợn râu, tần số cắt; chọn cấu trúc trực tiếp II–transposed/biquad để ổn định số học.