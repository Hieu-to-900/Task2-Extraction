# Public_605

Bảng dưới đây mô tả tính năng và tiêu chí, chỉ tiêu kỹ thuật đối với từng tính năng cụ thể. Đối với tính năng có một tiêu chí, chỉ tiêu kỹ thuật thì việc đánh giá là đạt khi giải pháp cung cấp được tính năng đó, không đạt nếu giải pháp không cung cấp được tính năng đó.

Đối với tính năng có nhiều tiêu chí, chỉ tiêu kỹ thuật khác nhau thì tính năng đó đạt khi tất cả các tiêu chí, chỉ tiêu kỹ thuật đều đạt, không đạt khi một trong các tiêu chí, chỉ tiêu kỹ thuật không đạt.
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>STT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tên tính năng</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tiêu chí, chỉ tiêu kỹ thuật</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3"><ol>
<li><p><strong>Máy ảo</strong></p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Tạo máy ảo</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp 03 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Tạo máy ảo mới thông qua giao diện đồ họa (GUI).</p></li>
<li><p>Tạo máy ảo mới thông qua giao diện dòng lệnh (CLI).</p></li>
<li><p>Tạo máy ảo mới thông qua giao diện lập trình ứng dụng (API) tích
hợp với hệ thống khác.</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Tạo nhiều máy ảo cùng một lúc</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng tạo nhiều máy ảo một lúc với số lượng tối
thiểu 02 máy / 1 lần tạo.</p></li>
<li><p>Cho phép người dùng tạo nhiều máy ảo một lúc với số lượng loại hệ
điều hành khác nhau, tối thiểu 02 hệ điều hành khác nhau / 1 lần
tạo.</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Tùy biến máy ảo</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp 04 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng tạo máy ảo từ tệp tin hệ điều hành mà hệ
thống hỗ trợ.</p></li>
<li><p>Cho phép người dùng tùy biến máy ảo muốn tạo và lưu lại máy ảo
sau khi tùy biến thành tệp tin hệ điều hành.</p></li>
<li><p>Lưu trữ tệp tin hệ điều hành do người dùng tạo ra trong nhóm tệp
tin hệ điều hành tùy biến.</p></li>
<li><p>Cho phép người dùng chọn tệp tin hệ điều hành trên giao diện cổng
thông tin quản trị (web portal) để tạo máy ảo tùy ý.</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Nhập / xuất máy ảo</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp 03 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng tải lên và tạo máy ảo từ những tệp tin hệ
điều hành có định dạng là VHD, VMDK, QCOW2 hoặc tương đương.</p></li>
<li><p>Lưu lại máy ảo đang chạy thành các tệp tin hệ điều hành có định
dạng là VHD, VMDK, QCOW2 hoặc tương đương.</p></li>
<li><p>Cho phép người dùng tải xuống các tệp tin hệ điều hành.</p></li>
</ol></td>
</tr>
<tr>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Chuyển đổi định dạng tệp tin hệ điều hành</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng chuyển đổi qua lại
các định dạng tệp tin hệ điều hành là VHD, VMDK, QCOW2 hoặc tương đương
cùng một lúc.</p>
</blockquote></td>
</tr>
<tr>
<td>6</td>
<td><blockquote>
<p>Triển khai máy ảo có cấu hình cao</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Hỗ trợ triển khai các máy ảo có số lượng lớn nhân xử lý và có bộ
nhớ kích thước lớn mà nặng về bộ nhớ (memory- intensive) hoặc nặng về
nhân xử lý (processor-intensive).</p></li>
<li><p>Hỗ trợ ít nhất 64 vCPU và 128 GB RAM</p></li>
</ol></td>
</tr>
<tr>
<td>7</td>
<td>Thay đổi cấu hình phần cứng máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng thay đổi cấu hình phần cứng máy ảo trong khi
các máy ảo đang chạy, không yêu cầu đối với trường hợp giảm kích thước ổ
cứng.</p></li>
<li><p>Thông báo cho người dùng ngay lập tức khi cần phải khởi động lại
máy ảo để áp dụng thay đổi.</p></li>
</ol></td>
</tr>
<tr>
<td>8</td>
<td>Di chuyển máy ảo giữa các máy chủ vật lý</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng di chuyển dữ liệu của một máy ảo đang
chạy từ máy vật lý này sang máy vật lý khác mà không phải tắt hoặc khởi
động lại máy ảo.</p>
</blockquote></td>
</tr>
<tr>
<td>9</td>
<td>Di chuyển dữ liệu máy ảo giữa các bộ lưu trữ khác nhau</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng di chuyển dữ liệu của một máy ảo đang
chạy từ thiết bị lưu trữ này sang thiết bị lưu trữ khác mà không phải
tắt hoặc khởi động lại.</p>
</blockquote></td>
</tr>
<tr>
<td>10</td>
<td>Khôi phục máy ảo sau khi có lỗi xảy ra</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng khôi phục / khởi động lại tự động máy ảo
(khi cơ sở hạ tầng vật lý phát sinh lỗi) mà phải thỏa mãn 02 điều kiện
sau:</p>
</blockquote>
<ol>
<li><p>Phát hiện được có lỗi đã xảy ra khi hệ thống gặp sư cố.</p></li>
<li><p>Tự động khởi động lại máy ảo khi phát hiện lỗi.</p></li>
</ol></td>
</tr>
<tr>
<td>11</td>
<td>Tính năng phân bổ máy ảo trên các máy vật lý khác nhau
(anti-affinity)</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng cấu hình các thông
số trên máy ảo để xác định vị trí triển khai các máy ảo khác nhau trên
các máy vật lý hoặc trung tâm dữ liệu khác nhau (nhằm phòng tránh sự ảnh
hưởng của vấn đề nào đó về phần cứng hoặc cơ sở hạ tầng đối với tất cả
các máy ảo cùng một lúc).</p>
</blockquote></td>
</tr>
<tr>
<td>12</td>
<td>Tính năng hỗ trợ tự động thay đổi cấu hình hệ thống mức cơ bản</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<p>Tính năng hỗ trợ tự động thay đổi theo chiều ngang thông qua 03 cách
bao gồm bật / tắt máy ảo; tạo ra các máy ảo mới dựa theo kế hoạch được
lập thủ công trước đó; thiết lập cấu hình tài nguyên cho máy ảo theo cấu
hình được định nghĩa trước.</p></td>
</tr>
<tr>
<td>13</td>
<td>Tính năng phân bổ máy ảo trên cùng máy vật lý (affinity)</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng định nghĩa các quy tắc hợp tác trao đổi dữ
liệu giữa các máy ảo.</p></li>
<li><p>Hỗ trợ triển khai các máy ảo thường xuyên trao đổi dữ liệu với
nhau trên cùng một máy vật lý.</p></li>
</ol></td>
</tr>
<tr>
<td>14</td>
<td>Truy cập vào máy ảo thông qua giao diện bảng điều khiển
(console)</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng truy cập vào máy ảo thông qua giao diện bảng
điều khiển (console)</p></li>
<li><p>Cung cấp giao diện bảng điều khiển (console) tương thích với các
trình duyệt phổ biến.</p></li>
</ol></td>
</tr>
<tr>
<td>15</td>
<td>Gắn các tệp tin định dạng ISO trên máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng Gắn các tệp tin định dạng ISO trên máy
ảo (các tệp tin định dạng ISO có thể nằm trên một kho dữ liệu riêng của
giải pháp).</p>
</blockquote></td>
</tr>
<tr>
<td>16</td>
<td>Sao lưu/khôi phục máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp 05 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng sao lưu máy ảo thành các bản chụp (snapshot)
theo kế hoạch được lập thủ công hoặc định kỳ trước đó.</p></li>
<li><p>Lưu trữ bản chụp (snapshot) được tạo ra dựa theo thông tin về
thời điểm tạo.</p></li>
<li><p>Cho phép người dùng sao lưu máy ảo thông qua cổng thông tin quản
trị hoặc CLI.</p></li>
<li><p>Cho phép người dùng sao lưu ít nhất 07 phiên bản khác nhau của
một máy ảo.</p></li>
<li><p>Cho phép người dùng khôi phục máy ảo từ bản chụp
(snapshot).</p></li>
</ol></td>
</tr>
<tr>
<td>17</td>
<td>Giới hạn IOPS và băng thông ổ đĩa của máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người quản trị và người dùng giới hạn IOPS của máy
ảo.</p></li>
<li><p>Cho phép người quản trị và người dùng giới hạn băng thông ổ đĩa
của máy ảo.</p></li>
</ol></td>
</tr>
<tr>
<td>18</td>
<td>Giới hạn băng thông mạng của máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng giới hạn băng thông
mạng của máy ảo cho cả hai luồng lưu lượng mạng vào / ra.</p>
</blockquote></td>
</tr>
<tr>
<td>19</td>
<td>Triển khai máy ảo cần sử dụng các công nghệ tăng tốc
(accelerator)</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng hỗ trợ <u>cấu hình NUMA</u> and
Transparent Hugepage, PCI Pass through, SR-IOV, OVS- DPDK, CPU pinning,
DPDK và Direct I/O, khi triển khai các máy ảo cần sử dụng các công nghệ
tăng tốc (accelerator).</p>
</blockquote></td>
</tr>
<tr>
<td>20</td>
<td>Tự động chọn máy chủ vật lý khi tạo một máy ảo mới</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép tự động chọn máy chủ vật lý để
triển khai máy ảo mới tạo nhằm cân bằng tải giữa các máy chủ vật lý.</p>
</blockquote></td>
</tr>
<tr>
<td>21</td>
<td>Thiết lập hoặc thiết lập lại mật khẩu cho tài khoản quản trị của máy
ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép quản trị viên nhập mật khẩu cho
tài khoản quản trị của máy ảo.</p>
</blockquote></td>
</tr>
<tr>
<td>22</td>
<td>Định nghĩa, cấu hình và khởi tạo cụm gồm nhiều máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng định nghĩa một
cluster mới tùy ý.</p>
</blockquote>
<p>- Ví dụ: một cụm máy chủ ảo 3 tầng gồm 06 máy ảo (02 máy chạy ứng
dụng ở mạng công cộng, 02 máy chạy các dịch vụ backend ở mạng cục bộ và
02 máy chạy cơ sở dữ liệu ở mạng cục bộ) có thể được tích hợp với tính
năng tự động thay đổi cấu hình hệ thống.</p></td>
</tr>
<tr>
<td colspan="3"><strong>2. Thiết bị lưu trữ</strong></td>
</tr>
<tr>
<td>1</td>
<td>Tích hợp các thiết bị lưu trữ truyền thống và giải pháp lưu trữ bằng
phần mềm</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Hỗ trợ giải pháp lưu trữ bằng phần mềm (SDS-Software- Defined
Storage).</p></li>
<li><p>Hỗ trợ tích hợp các thiết bị SAN (Storage Area Network) và NAS
(Network-Attached Storage).</p></li>
</ol></td>
</tr>
<tr>
<td>2</td>
<td>Tích hợp các dịch vụ lưu trữ</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Hỗ trợ lưu trữ dạng khối (block storage)</p></li>
<li><p>Hỗ trợ lưu trữ dạng đối tượng (object storage) và lưu trữ dạng
tệp tin (file storage)</p></li>
</ol></td>
</tr>
<tr>
<td>3</td>
<td>Áp dụng chính sách đối với các dịch vụ lưu trữ phân tầng</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng thiết lập chính sách
đối với các dịch vụ lưu trữ phân tầng.</p>
<p>- Ví dụ: một quản trị viên về việc lưu trữ dữ liệu có thể lập kế
hoạch lưu những dữ liệu không thường xuyên sử dụng trên thiết bị SATA
chậm hơn và ít tốn kém hơn.</p>
</blockquote></td>
</tr>
<tr>
<td>4</td>
<td>Gắn bộ nhớ trên nhiều máy ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Gắn một ổ cứng ảo (từ SAN hoăc SDS) trên nhiều máy ảo ổ cứng ảo
có thể ở chế độ chỉ đọc.</p></li>
<li><p>Gắn một hệ thống tệp tin chia sẻ dùng chung trên nhiều máy
ảo.</p></li>
</ol></td>
</tr>
<tr>
<td>5</td>
<td>Quản lý, phân bổ các tham số hiệu năng của ổ cứng ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng chọn một phân lớp
hiệu năng cho các ổ cứng ảo.</p>
<p>- Ví dụ: IOPS hoặc băng thông (đo bằng Mbps).</p>
</blockquote></td>
</tr>
<tr>
<td>6</td>
<td>Tự động phân bổ dữ liệu trên vùng lưu trữ</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng tự động phân bổ dữ liệu trên vùng lưu
trữ để phân tải cho các ổ đĩa.</p>
</blockquote></td>
</tr>
<tr>
<td>7</td>
<td>Mở rộng vùng lưu trữ</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng tăng dung lượng của
một vùng lưu trữ đã có sẵn.</p>
</blockquote></td>
</tr>
<tr>
<td>8</td>
<td>Mở rộng các ổ cứng ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng tăng kích thước của
một ổ cứng ảo (ổ cứng ảo của thiết bị SAN hoặc SDS) đã có sẵn mà không
phải cấp thêm ổ cứng ảo mới hoặc sao chép dữ liệu sang ổ cứng ảo
mới.</p>
</blockquote></td>
</tr>
<tr>
<td>9</td>
<td>Di dời dữ liệu giữa các vùng lưu trữ khi hệ thống đang vận hành</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép quản trị viên di chuyển dữ liệu
giữa các vùng lưu trữ khi hệ thống đang vận hành.</p>
</blockquote></td>
</tr>
<tr>
<td>10</td>
<td>Sao lưu ổ cứng ảo</td>
<td><blockquote>
<p>Giải pháp cung cấp 03 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng sao lưu ổ cứng ảo tại một thời điểm bất kỳ
thành các bản chụp (snapshot) thông qua các cách thức tự thao tác
(self-service.)</p></li>
<li><p>Sử dụng các bản chụp (snapshot) thông qua cách thức tự thao tác
(self-service) với mục đích để cấp thêm máy ảo mới</p></li>
</ol></td>
</tr>
<tr>
<td>11</td>
<td>Khả năng cung cấp lưu trữ dạng đối tượng (Object storage)</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng hỗ trợ khả năng cung cấp lưu trữ dạng
đối tượng (Object storage) mà phải thỏa mãn các điều kiện sau:</p>
</blockquote>
<ol>
<li><p>Lưu trữ và truy xuất dữ liệu thông qua API trên dịch vụ
web.</p></li>
</ol>
<blockquote>
<p>Hỗ trợ khả năng thay đổi đối với từng đối tượng đơn lẻ và toàn bộ lưu
trữ dạng đối tượng (Object storage).</p>
</blockquote></td>
</tr>
<tr>
<td>12</td>
<td>Mã hóa dữ liệu</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng mã hóa dữ liệu hoặc
cấu trúc dữ liệu.</p>
</blockquote></td>
</tr>
<tr>
<td>14</td>
<td>Sao lưu đối tượng</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép người dùng sao lưu đối tượng thành nhiều phiên bản tại
những thời điểm khác nhau nhằm mục đích phòng ngừa việc mất mát dữ liệu
do ghi đè hoặc xóa đối tượng.</p></li>
<li><p>Cho phép người dùng cấu hình việc sao lưu thông qua CLI, GUI hoặc
API đối với từng đối tượng.</p></li>
</ol></td>
</tr>
<tr>
<td colspan="3"><strong>3. Mạng và mạng định nghĩa bằng phần mềm
(Software-Defined Networking - SDN)</strong></td>
</tr>
<tr>
<td>1</td>
<td>Quản lý hiệu năng mạng</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng quản lý hiệu năng
đối với từng mạng mà máy ảo kết nối đến bao gồm việc giới hạn băng
thông, độ trễ, quản lý chất lượng dịch vụ (QoS).</p>
</blockquote></td>
</tr>
<tr>
<td>2</td>
<td><blockquote>
<p>Tích hợp</p>
<p>nhiều cổng</p>
</blockquote>
<p>giao tiếp mạng ảo trên vNIC một máy ảo</p></td>
<td><blockquote>
<p>Giải pháp cung cấp 04 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép nhiều địa chỉ IP khác nhau được gán cho một máy ảo thông
qua tích hợp nhiều cổng giao tiếp mạng ảo trên vNIC với địa chỉ MAC khác
nhau cho máy ảo đó.</p></li>
<li><p>Cho phép người dùng sử dụng kết hợp cả địa chỉ IP public và địa
chỉ IP private để gán cho máy ảo, ngoại trừ trường hợp hệ điều hành máy
ảo mà không hỗ trợ.</p></li>
<li><p>Cho phép người dùng định nghĩa nhiều phân đoạn mạng ảo mà không
cần dùng phần mềm bên thứ ba.</p></li>
</ol>
<blockquote>
<p>Cho phép người dùng định nghĩa nhiều mạng con cho mỗi mạng ảo.</p>
</blockquote></td>
</tr>
<tr>
<td>3</td>
<td>Hỗ trợ khả năng dự phòng từ mức vật lý cho các mạng mà máy ảo kết
nối đến</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng hỗ trợ kiến trúc thiết kế đảm bảo khả
năng dự phòng mà phải thỏa mãn 02 điều kiện sau:</p>
</blockquote>
<ol>
<li><p>Hỗ trợ từ mức vật lý (ít nhất ở mức cổng vật lý – NIC) cho các
mạng mà máy ảo kết nối đến (ví dụ: nếu một máy chủ vật lý có 02 cổng / 1
NIC thì khi một cổng gặp sự cố cũng không ảnh hưởng đến kết nối mạng của
máy ảo).</p></li>
<li><p>Hoạt động ở mức active-active hoặc active-standby để cải thiện
băng thông và bảo đảm tính sẵn sàng.</p></li>
</ol></td>
</tr>
<tr>
<td>4</td>
<td>Cấp phát địa chỉ IP</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép một máy ảo được gán địa chỉ IP động và địa chỉ IP này
phải luôn không đổi giá trị trong suốt quá trình hoạt động của máy
ảo.</p></li>
<li><p>Cho phép một máy ảo được gán địa chỉ IP tĩnh (bao gồm cả địa chỉ
IP public và private).</p></li>
</ol></td>
</tr>
<tr>
<td>5</td>
<td>Liên kết với bộ chuyển mạch và bộ định tuyến thông thường</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng SDN hoặc Liên kết với các bộ chuyển mạch
và bộ định tuyến thông thường của nhiều hãng khác nhau.</p>
</blockquote></td>
</tr>
<tr>
<td>6</td>
<td>Phòng chống tấn công giả mạo địa chỉ IP và giả mạo gói tin ARP</td>
<td>Giải pháp cung cấp tính năng phòng chống tấn công giả mạo địa chỉ IP
và giả mạo gói tin ARP đối với mạng nội bộ của máy ảo hoặc các mạng mà
máy ảo và máy vật lý kết nối đến.</td>
</tr>
<tr>
<td>7</td>
<td>Hỗ trợ VLAN và VXLAN</td>
<td>Giải pháp cung cấp tính năng cho phép người dùng định nghĩa các mạng
ảo bao gồm cả VLAN và VXLAN.</td>
</tr>
<tr>
<td>8</td>
<td>Hỗ trợ bộ định tuyến ảo</td>
<td>Giải pháp cung cấp tính năng cho phép người dùng sử dụng các chức
năng của bộ định tuyến (NAT, định tuyến giữa các VLAN,…) để quản lý kết
nối giữa các mạng.</td>
</tr>
<tr>
<td>9</td>
<td>Tích hợp dịch vụ cân bằng tải</td>
<td>Giải pháp cung cấp tính năng cho phép người dùng sử dụng dịch vụ cân
bằng tải đã được tích hợp sẵn (dịch vụ bao gồm các chức năng cấu hình
giám sát, cấu hình cho thiết bị đầu cuối và tương thích với nhiều máy ảo
đang kết nối với nhiều mạng ảo khác nhau).</td>
</tr>
<tr>
<td>10</td>
<td><blockquote>
<p>Cấu hình</p>
</blockquote>
<p>chính sách truy cập cho từng cổng trên máy ảo</p></td>
<td>Giải pháp cung cấp tính năng cho phép người dùng cấu hình chính sách
truy cập cho từng cổng (thuộc cổng giao tiếp mạng ảo trên vNIC) trên
những máy ảo đang chạy.</td>
</tr>
<tr>
<td>11</td>
<td><blockquote>
<p>Tích hợp dịch vụ tường lửa</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng cho phép người dùng sử dụng dịch vụ
tường lửa đã được tích hợp sẵn (dịch vụ phải hoạt động bình thường trên
tầng IP và Domain).</td>
</tr>
<tr>
<td>12</td>
<td><blockquote>
<p>Hỗ trợ IPv6 cho cả mạng vật lý và mạng ảo</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng hỗ trợ máy ảo hoặc cổng kết nối (ví dụ:
bộ cân bằng tải) sử dụng IPv6 trên cả mạng vật lý và mạng ảo.</td>
</tr>
<tr>
<td>13</td>
<td><blockquote>
<p>Tách biệt các mạng ảo với nhau</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng tách biệt hoàn toàn các mạng ảo khác
nhau.</td>
</tr>
<tr>
<td>14</td>
<td><blockquote>
<p>Đảm bảo sự hao phí băng thông đường truyền kết nối giữa các mạng
không vượt quá 10%</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng đảm bảo sự hao phí băng thông đường
truyền kết nối giữa máy ảo với máy ảo và máy ảo với thành phần bên ngoài
không vượt quá 10%.</p>
</blockquote>
<p>- Ví dụ: nếu thiết lập 02 mạng VXLAN cho 02 máy ảo khác nhau trong
mạng vật lý có băng thông là 10 Gbps thì băng thông thực tế của đường
truyền kết nối giữa các máy ảo này phải &gt; 9 Gbps.</p></td>
</tr>
<tr>
<td>15</td>
<td><blockquote>
<p>Đảm bảo hạ tầng kỹ thuật cho máy vật lý và máy ảo có tính sẵn sàng
cao</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng đảm bảo máy vật lý và máy ảo chạy trên
hạ tầng kỹ thuật có tính sẵn sàng cao, đảm bảo tính nguyên vẹn và tính
bí mật của dữ liệu.</p>
</blockquote></td>
</tr>
<tr>
<td>16</td>
<td><blockquote>
<p>Hỗ trợ cấu trúc liên kết mạng có tính phân cấp do người dùng định
nghĩa</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng cho phép người dùng tự thiết kế các
thành phần và sơ đồ mạng bao gồm tường lửa ảo, VLAN / VXLAN / GRE, mạng
con, NAT, bộ cân bằng tải ảo.</td>
</tr>
<tr>
<td>17</td>
<td><blockquote>
<p>Hỗ trợ tính năng tạo bộ chuyển mạch ảo</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng tạo bộ chuyển mạch ảo và bộ định tuyến
ảo</td>
</tr>
<tr>
<td>18</td>
<td><blockquote>
<p>Tách biệt các mặt phẳng SDN với nhau</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng tách biệt các mặt phẳng điều khiển, mặt
phẳng chuyển tiếp và mặt phẳng quản trị với nhau.</td>
</tr>
<tr>
<td>19</td>
<td><blockquote>
<p>Hỗ trợ Open Flow hoặc tương đương</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng hỗ trợ OpenFlow cho SDN hoặc tương
đương.</td>
</tr>
<tr>
<td>20</td>
<td><blockquote>
<p>Tính năng tích hợp nền tảng điện toán đám mây</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng hỗ trợ API sử dụng nền tảng điện toán
đám mây để tạo bộ chuyển mạch ảo và bộ định tuyến ảo</td>
</tr>
<tr>
<td>21</td>
<td><blockquote>
<p>Quản trị và điều khiển bộ chuyển mạch ảo và bộ định tuyến ảo</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng quản trị và điều khiển bộ chuyển mạch
ảo và bộ định tuyến ảo</td>
</tr>
<tr>
<td>22</td>
<td><blockquote>
<p>Tự động tạo và quản trị bộ chuyển mạch ảo và bộ định tuyến ảo</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng tự động tạo và quản trị bộ chuyển mạch
ảo và bộ định tuyến ảo</td>
</tr>
<tr>
<td>23</td>
<td><blockquote>
<p>Hỗ trợ AAA</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng cho phép xác thực, phân quyền, ghi log
hoạt động (authenticate, authorize, account – AAA) người dùng.</td>
</tr>
<tr>
<td>24</td>
<td>Tính năng quản trị các thành phần trong mạng</td>
<td>Giải pháp cung cấp tính năng cho phép người dùng sử dụng SNMP,
Netconf hoặc tương đương có chức năng quản trị các thành phần khác trong
mạng.</td>
</tr>
<tr>
<td>25</td>
<td>Tính năng hỗ trợ đảm bảo bộ điều khiển có tính sẵn sàng cao</td>
<td>Giải pháp cung cấp tính năng đảm bảo bộ điều khiển cho SDN có tính
sẵn sàng cao.</td>
</tr>
<tr>
<td>26</td>
<td><blockquote>
<p>Tính năng hỗ trợ Jumbo Frame</p>
</blockquote>
<p>(khuyến nghị áp dụng)</p></td>
<td>Giải pháp cung cấp tính năng sử dụng Jumbo Frame trong việc truyền
tải gói tin.</td>
</tr>
<tr>
<td>27</td>
<td><blockquote>
<p>Tính năng tích hợp CLI và GUI</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng cho phép người dùng cấu hình, quản lý
các thành phần trong mạng, bộ điều khiển cho SDN thông qua CLI và
GUI.</td>
</tr>
<tr>
<td>28</td>
<td><blockquote>
<p>Tính năng hỗ trợ bộ chuyển mạch ảo và bộ định tuyến ảo</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp 09 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Hỗ trợ SPAN, RSPAN hoặc tương đương.</p></li>
<li><p>Hỗ trợ LACP (mode 1, 2, 3, 4) từ máy ảo, máy vật lý.</p></li>
<li><p>Hỗ trợ 802.1Q VLAN with trunking.</p></li>
<li><p>Hỗ trợ multicast snooping.</p></li>
<li><p>Hỗ trợ LLDP.</p></li>
<li><p>Hỗ trợ STP, RSTP hoặc tương đương.</p></li>
<li><p>Hỗ trợ quản lý chất lượng dịch vụ (QoS).</p></li>
<li><p>Hỗ trợ áp dụng chính sách lưu lượng cho từng máy ảo.</p></li>
</ol>
<p>Hỗ trợ VXLAN.</p></td>
</tr>
<tr>
<td colspan="3"><strong>4. Máy vật lý</strong></td>
</tr>
<tr>
<td>1</td>
<td><blockquote>
<p>Tự động cài đặt hệ điều hành và phần mềm giám sát máy ảo</p>
</blockquote>
<p>(hypervisor)</p></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng tự động cài đặt hệ điều hành và phần mềm
giám sát máy ảo sau khi có những thiết bị (ảo hoặc vật lý) mới truy cập
mạng. Cho phép người dùng hoặc các thiết bị khác trong mạng có thể sử
dụng, giao tiếp với chúng.</p>
</blockquote></td>
</tr>
<tr>
<td>2</td>
<td><p>Triển khai</p>
<p>nhiều phiên bản hệ điều hành Windows và Linux cho máy vật lý</p></td>
<td><blockquote>
<p>Giải pháp cung cấp 07 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Hỗ trợ triển khai các phiên bản hệ điều hành Windows 8 và
10.</p></li>
<li><p>Hỗ trợ triển khai các phiên bản hệ điều hành Windows Server 2012
và 2016.</p></li>
<li><p>Hỗ trợ triển khai các phiên bản hệ điều hành Ubuntu 14.04,16.04
và 18.04.</p></li>
<li><p>Hỗ trợ triển khai các phiên bản hệ điều hành CentOS 6.x và
7.x.</p></li>
<li><p>Hỗ trợ triển khai các phiên bản hệ điều hành RHEL 6 và
7.</p></li>
<li><p>Hỗ trợ triển khai các phiên bản hệ điều hành Oracle Linux 6 và
7.</p></li>
<li><p>Hỗ trợ các phiên bản hệ điều hành windows, ubuntu, centos, rhel,
oracle linux, linux hiện hành.</p></li>
</ol></td>
</tr>
<tr>
<td>3</td>
<td>Quản trị qua kênh truyền tín hiệu riêng biệt</td>
<td><blockquote>
<p>Giải pháp cung cấp tính quản trị qua kênh truyền tín hiệu riêng biệt
thông qua giao diện quản lý nền tảng thông minh (IPMI), sử dụng một
trong các giao diện: iRMC, iLO, IDRAC, UCS hoặc tương đương.</p>
</blockquote></td>
</tr>
<tr>
<td>4</td>
<td><blockquote>
<p>Truy cập vào máy vật lý thông qua giao diện bảng điều
khiển(console</p>
</blockquote>
<p>)</p></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng truy cập vào máy vật
lý thông qua giao diện bảng điều khiển(console)</p>
</blockquote></td>
</tr>
<tr>
<td>5</td>
<td><blockquote>
<p>Cấu hình cơ chế dự phòng cho ổ cứng (RAID -</p>
<p>Redundant Arrays of Independent Disks) trên máy vật lý</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng cho phép người dùng cấu hình RAID trên
máy vật lý.</td>
</tr>
<tr>
<td colspan="3"><strong>5. Quản trị và vận hành</strong></td>
</tr>
<tr>
<td>1</td>
<td><blockquote>
<p>Định nghĩa các hành động sau khi tạo hoặc xóa máy ảo</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng cho phép quản trị viên định nghĩa các
hành động sau khi tạo hoặc xóa máy ảo.</td>
</tr>
<tr>
<td>2</td>
<td><blockquote>
<p>Thực hiện một hành động do người dùng chỉ định sẵn sau khi quá trình
khởi</p>
<p>động hoàn thành</p>
</blockquote></td>
<td>Giải pháp cung cấp tính năng thực hiện một hành động do người dùng
chỉ định sẵn thông qua cách thức tự hành (self- service) sau khi quá
trình khởi động lần đầu hoàn thành đối với máy ảo mới tạo.</td>
</tr>
<tr>
<td>3</td>
<td><blockquote>
<p>Hỗ trợ quản trị cấu hình</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng hỗ trợ quản trị cấu hình (thông qua
Ansible, Puppet, Chef hoặc SaltStack) mà phải thỏa mãn 03 điều kiện
sau:</p>
</blockquote>
<ol>
<li><p>Hoạt động như một dịch vụ được tích hợp sẵn để cho phép người
dùng quản lý, kiểm tra các cấu hình và quy trình triển khai.</p></li>
<li><p>Tự động hóa toàn bộ quy trình triển khai, nâng cấp, cập nhật và
vá lỗi.</p></li>
<li><p>Tích hợp các thành phần vận hành tự động có khả năng được cấu
hình thông qua các ngôn ngữ lập trình (như YAML,…).</p></li>
</ol></td>
</tr>
<tr>
<td>4</td>
<td>Quản lý tài nguyên</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Cho phép quản trị viên giám sát, đánh giá lịch sử sử dụng tài
nguyên của các máy ảo.</p></li>
<li><p>Đưa ra các khuyến nghị về việc cấp thêm tài nguyên khi cần
thiết.</p></li>
</ol></td>
</tr>
<tr>
<td>5</td>
<td>Quản lý bản vá</td>
<td><blockquote>
<p>Giải pháp cung cấp 03 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Tự động tạo thống kê, báo cáo về các bản vá đã được cập
nhật.</p></li>
<li><p>Tự động áp dụng các bản vá lên nhiều máy chủ một lúc.</p></li>
</ol>
<blockquote>
<p>Khôi phục các bản vá đã cập nhật.</p>
</blockquote></td>
</tr>
<tr>
<td>6</td>
<td>Tích hợp giao diện cổng thông tin quản trị</td>
<td><blockquote>
<p>Giải pháp cung cấp 02 tính năng sau:</p>
</blockquote>
<ol>
<li><p>Tích hợp giao diện cổng thông tin quản trị có tính tự hành cho
người dùng đầu cuối (để người dùng tự quản lý tài nguyên được cấp) và
giao diện cổng thông tin quản trị cho quản trị viên.</p></li>
<li><p>Hỗ trợ giao diện cổng thông tin quản trị tương thích ít nhất 02
loại trình duyệt web là Firefox và Chrome</p></li>
</ol></td>
</tr>
<tr>
<td>7</td>
<td>Tùy biến giao diện cổng thông tin quản trị</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng tùy biến giao diện
cổng thông tin quản trị về hiển thị các thông số, tiêu chí như trạng
thái, hiệu năng, tính sẵn sàng của tập hợp các máy chủ, dịch vụ.</p>
</blockquote></td>
</tr>
<tr>
<td>8</td>
<td>Quản lý, giám sát nền tảng hạ tầng dịch vụ điện toán đám mây</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng cho phép người dùng quản lý, giám sát cơ
sở hạ tầng vật lý và ảo mà phải thỏa mãn 05 điều kiện sau:</p>
</blockquote>
<ol>
<li><p>Hiển thị theo thời gian thực các thông số giám sát về CPU (idle,
used, iowait, stealth), RAM, thiết bị lưu trữ, mạng.</p></li>
<li><p>Cho phép người dùng cấu hình tùy theo ý muốn về cảnh báo hoặc báo
cáo khi có sự cố xảy ra.</p></li>
<li><p>Cho phép người dùng cấu hình khoảng thời gian lấy mẫu các thông
số giám sát.</p></li>
<li><p>Hiển thị các giá trị về thời gian ít nhất với các mức là giây,
phút, giờ, ngày.</p></li>
<li><p>Giám sát được các thành phần của cơ sở hạ tầng vật lý bao gồm bộ
chuyển mạch, bộ định tuyến, tủ chứa máy chủ và các thiết bị lưu
trữ.</p></li>
</ol></td>
</tr>
<tr>
<td>9</td>
<td>Cảnh báo khi có sự kiện / sự cố về cơ sở hạ tầng xảy ra</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng gửi cảnh báo cho người dùng khi có sự
kiện / sự cố về cơ sở hạ tầng xảy ra mà phải thỏa mãn 05 điều kiện
sau:</p>
</blockquote>
<ol>
<li><p>Gửi cảnh báo khi giá trị ngưỡng về giám sát hiệu năng được kích
hoạt.</p></li>
<li><p>Tạo cảnh báo trong vòng một phút kể từ khi một giá trị ngưỡng
được kích hoạt.</p></li>
<li><p>Cho phép người dùng định nghĩa ít nhất 03 giá trị ngưỡng khác
nhau dành cho việc cảnh báo.</p></li>
<li><p>Giải pháp cho phép người dùng thiết lập các giá trị ngưỡng đối
với từng thành phần một.</p></li>
<li><p>Giải pháp cho phép gửi cảnh báo qua email, SMS.</p></li>
</ol></td>
</tr>
<tr>
<td>10</td>
<td>Thu thập và lưu trữ log hệ thống</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng thu thập, lưu trữ và xoay vòng định kỳ
log hệ thống về các tác vụ tạo, đọc, cập nhật, xóa - CRUD (Create, Read,
Update, Delete – tạo, đọc, cập nhật, xóa), tài nguyên được sử dụng,…</p>
</blockquote></td>
</tr>
<tr>
<td>11</td>
<td>Tích hợp API giám sát dữ liệu</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng tích hợp API dành cho giám sát dữ liệu
để cho phép bên thứ 3 thực hiện giám sát, phân tích dữ liệu qua API.</p>
</blockquote></td>
</tr>
<tr>
<td>12</td>
<td>Ghi log về các sự kiện liên quan đến tài khoản</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng ghi log về các sự kiện liên quan đến tài
khoản mà phải thỏa mãn 03 điều kiện sau:</p>
</blockquote>
<ol>
<li><p>Ghi log về các thao tác đăng nhập tài khoản, quản lý tài khoản
bao gồm tạo / xoá / lập nhóm / gắn thẻ cho tài khoản người dùng và các
thao tác khác (ví dụ: gán quyền, thiết lập số lượng tài khoản người
dùng, thay đổi mật khẩu của tài khoản người dùng,…).</p></li>
<li><p>Cho phép người dùng xem các bản ghi log thông qua giao diện có
tính tự hành và khả năng xuất các bản ghi log để lưu giữ lâu
hơn.</p></li>
</ol></td>
</tr>
<tr>
<td colspan="3"><strong>6. Tích hợp</strong></td>
</tr>
<tr>
<td>1</td>
<td><blockquote>
<p>Tích hợp giao diện tương tác với thành phần quản lý</p>
</blockquote>
<p>chức năng mạng ảo (Virtual Network Function – VNF)</p></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng tích hợp giao diện tương tác với thành
phần VNF từ các hãng khác nhau, tuân theo kiến trúc ETSI MANO để hỗ trợ
quản lý vòng đời VNF cũng như khả năng mở rộng.</p>
</blockquote></td>
</tr>
<tr>
<td>2</td>
<td><blockquote>
<p>Hỗ trợ thư viện phục vụ cho lập trình, phát triển</p>
<p>phần mềm tương tác với hệ thống</p>
</blockquote></td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng hỗ trợ các thư viện (mã nguồn mở hoặc tự
nhà cung cấp dịch vụ điện toán đám mây tạo) phục vụ cho lập trình, phát
triển phần mềm tương tác với hệ thống mà phải thỏa mãn 03 điều kiện
sau:</p>
</blockquote>
<ol>
<li><p>Tương thích với ít nhất 03 trong số ngôn ngữ lập trình phổ biến
bao gồm Java, .NET, Perl, Node.js, PHP, Python, Ruby và
PowerShell.</p></li>
<li><p>Bao gồm các dịch vụ cốt lõi là vận hành, tính toán, lưu trữ và
kết nối mạng.</p></li>
<li><p>Có tài liệu kỹ thuật và ví dụ về mã nguồn.</p></li>
</ol></td>
</tr>
<tr>
<td colspan="3"><strong>7. Các yêu cầu khác</strong></td>
</tr>
<tr>
<td>1</td>
<td>Hỗ trợ máy chủ có kiến trúc CPU x86_64</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng hỗ trợ cài đặt, triển khai, vận hành hệ
thống trên máy chủ có kiến trúc CPU x86-based (bao gồm bộ xử lý Intel và
AMD) và những loại máy chủ có 2 hoặc 4 nhân của các hãng Dell, HP, IBM,
Cisco.</p>
</blockquote></td>
</tr>
<tr>
<td>2</td>
<td>Đồng bộ thời gian</td>
<td><blockquote>
<p>Giải pháp cung cấp tính năng đồng bộ thời gian cho tất cả các thành
phần trong hệ thống.</p>
</blockquote></td>
</tr>
</tbody>
</table>