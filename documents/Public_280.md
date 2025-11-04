# Public_280

# Tổng quan

## Mục đích tài liệu

Tài liệu này được xây dựng nhằm mục đích mô tả thiết kế của các chức năng đáp ứng yêu cầu nghiệp vụ theo quy trình tài liệu.

## Thuật ngữ và chữ viết tắt
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>Thuật ngữ/ Từ viết tắt</p>
</blockquote></th>
<th>Định nghĩa</th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>LOG</p>
</blockquote></td>
<td><blockquote>
<p>Công ty TNHH MTV Logistics DHL</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>TCT</p>
</blockquote></td>
<td><blockquote>
<p>Tổng công ty</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>TTVH</p>
</blockquote></td>
<td><blockquote>
<p>Trung tâm Vận hành chuyển phát</p>
</blockquote></td>
</tr>
</tbody>
</table> 

# Nội dung

## Báo cáo KPI Công nợ COD

### Mô tả chức năng
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>Mục đích</p>
</blockquote></th>
<th><blockquote>
<p>Cho phép người dùng theo dõi chỉ số KPI công nợ COD.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>Hệ thống thực hiện</p>
</blockquote></td>
<td><blockquote>
<p>NOC: noc.dhl.vn</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Đối tượng sử dụng</p>
</blockquote></td>
<td><blockquote>
<p>Cấp quyền truy cập cho các user thuộc các role sau:</p>
</blockquote>
<ul>
<li><p>Lãnh đạo TCT; Phòng tài chính: Xem toàn bộ dữ liệu của báo cáo
theo tất cả các cấp.</p></li>
<li><p>Cấp Chi nhánh: Lãnh đạo chi nhánh; Chuyên quản chi nhánh; Nhân
viên điều hành chất lượng: Xem dữ liệu của chi nhánh quản lý và các bưu
cục trực thuộc.</p></li>
<li><p>Cấp Bưu cục: Lãnh đạo bưu cục: Xem dữ liệu của bưu cục quản
lý.</p></li>
</ul></td>
</tr>
<tr>
<td><blockquote>
<p>Điều kiện đầu vào</p>
</blockquote></td>
<td><blockquote>
<p>Người dùng đăng nhập hệ thống thành công, truy cập mục Báo cáo tài
chính.</p>
<p><strong>Đăng nhập</strong>  <strong>Báo cáo tài chính</strong> 
<strong>Báo cáo KPI công nợ COD</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Điều kiện đầu ra</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị chỉ số KPI công nợ COD.</p>
</blockquote></td>
</tr>
</tbody>
</table> 

### Mô tả màn hình
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
<th><blockquote>
<p><strong>STT</strong></p>
</blockquote></th>
<th><strong>Trường dữ liệu</strong></th>
<th colspan="2"><strong>Kiểu dữ liệu</strong></th>
<th><blockquote>
<p><strong>Mô tả</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><blockquote>
<p><strong>Bộ lọc</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bộ lọc thời gian</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Datepicker</p>
</blockquote></td>
<td><blockquote>
<p>Cho phép lọc theo thời gian, chỉ cho phép chọn từ ngày N-1 về trước.
Bao gồm</p>
<p>+ Lũy kế ngày: cho phép lọc dữ liệu theo ngày. Mặc định: ngày N-1</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Bộ lọc theo vùng</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Dropdownlist</p>
</blockquote></td>
<td><blockquote>
<p>Cho phép lọc theo vùng phát (là vùng của chi nhánh phát thực tế). Bao
gồm: Theo cây tổ chức NOC.</p>
<p>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Bộ lọc theo chi nhánh</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Dropdownlist</p>
</blockquote></td>
<td><blockquote>
<p>Cho phép lọc và tìm kiếm theo chi nhánh phát thực tế. Bao gồm: Theo
cây tổ chức NOC.</p>
<p>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Bộ lọc theo vùng con</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Dropdownlist</p>
</blockquote></td>
<td><blockquote>
<p>Cho phép lọc và tìm kiếm theo vùng con của chi nhánh HNI/HCM. Bao
gồm: Theo cây tổ chức NOC.</p>
<p>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả</p>
<p>Lưu ý:</p>
<p>+ Bộ lọc vùng con chỉ hiển thị khi đã chọn Bộ lọc theo chi nhánh =
HNI/HCM.</p>
<p>+ Cho phép lọc: Chi nhánh → Vùng con → Bưu cục; Chi nhánh → Bưu
cục.</p>
</blockquote></td>
</tr>
<tr>
<td>5</td>
<td>Bộ lọc theo bưu cục</td>
<td colspan="2">Dropdownlist</td>
<td><blockquote>
<p>Cho phép lọc và tìm kiếm theo bưu cục phát thực tế, chỉ cho phép lọc
theo bưu cục sau khi đã chọn bộ lọc theo chi nhánh.</p>
<p>Bao gồm: Theo cây tổ chức NOC. Chỉ cho phép chọn 1 lựa chọn.</p>
<p>Mặc định: Tất cả.</p>
</blockquote></td>
</tr>
<tr>
<td>6</td>
<td>Bộ lọc theo đánh giá ngày</td>
<td colspan="2">Dropdownlist</td>
<td><blockquote>
<p>Cho phép lọc và tìm kiếm theo đánh giá ngày. Bao gồm:</p>
<p>+ Đạt</p>
<p>+ Không đạt</p>
<p>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả.</p>
</blockquote></td>
</tr>
<tr>
<td>7</td>
<td>Xuất excel theo màn</td>
<td colspan="2">Button</td>
<td><blockquote>
<p>Chọn → Tải xuống file excel theo báo cáo tổng hợp đang hiển thị trên
màn hình.</p>
<p>Tên file: kpicongnocodtonghop_ddmmyyyy</p>
</blockquote></td>
</tr>
<tr>
<td>8</td>
<td>Xuất excel chi tiết</td>
<td colspan="2">Button</td>
<td><blockquote>
<p>Chọn → Tải xuống file excel chi tiết bưu gửi tính kpi công nợ theo
điều kiện lọc đã chọn (xuất chi tiết bưu gửi theo ngày).</p>
<p>Tên file: kpicongnocodchitiettheongay_ddmmyyyy</p>
</blockquote></td>
</tr>
<tr>
<td colspan="5"><p><strong>Báo cáo</strong></p>
<p>Thời gian cập nhật dữ liệu:</p>
<p>+ Ngày N cập nhật số liệu ngày N-1 tại 2 mốc 10h và 17h.</p>
<p>+ Ngày 5 tháng N+1 chạy lại và chốt dữ liệu tháng N.</p></td>
</tr>
<tr>
<td colspan="5"><p>Mô tả chung: Lấy toàn bộ bưu gửi đã phát sinh trạng
thái 501 và có thời gian đến hạn thu tiền nằm trong ngày được chọn tại
bộ lọc thời gian (loại các đơn có tiền thu hộ = 0 hoặc null)</p>
<p>Lưu ý:</p>
<p>+ Nếu thời gian đến hạn thu tiền vào ngày chủ nhật, ngày Lễ, ngày Tết
được loại trừ và được tính vào ngày làm việc gần nhất (ví dụ: thời gian
đến hạn thu tiền là 09:00:00 ngày 30/08 là chủ nhật, ngày 01/09 và 02/09
là ngày lễ =&gt; thời gian đến hạn thu tiền được tính là 09:00:00 ngày
03/09)</p>
<p>+ Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung
cấp: <a>Quy
đổi chi tiết ngày 2023 2024 2025.xlsx</a></p></td>
</tr>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Vùng</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị vùng phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Chi nhánh</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị mã chi nhánh phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vùng con</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị mã vùng con phát thực tế.</p>
<p>Cột Vùng con chỉ hiển thị sau khi chọn chi nhánh HNI/HCM tại bộ lọc
chi nhánh.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Bưu cục</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị bưu cục phát thực tế.</p>
<p>Cột Bưu cục chỉ hiển thị sau khi chọn chi nhánh tại bộ lọc chi
nhánh.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Tuyến bưu tá</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị tuyến bưu tá phát thực tế. Định dạng: Họ và tên (mã nhân
viên) Nếu không có mã nhân viên  Để (--)</p>
<p>Cột Tuyến bưu tá chỉ hiển thị sau khi chọn bưu cục tại bộ lọc bưu
cục.</p>
</blockquote></td>
</tr>
<tr>
<td colspan="5"><blockquote>
<p><strong>Ngày</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Số tiền phải thu</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị tổng số tiền thu hộ. ĐVT: VNĐ</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Số tiền thu đúng hạn</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị tổng số tiền thu hộ có thời gian thu &lt;= thời gian đến hạn
thu tiền. ĐVT: VNĐ</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Tỷ lệ thu công nợ</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị tỷ lệ thu công nợ ngày. <u>Công thức:</u></p>
<p>Tỷ lệ thu công nợ ngày = (Số tiền thu đúng hạn / Số tiền phải thu) *
100 (%) <u>Định dạng:</u> %, làm tròn đến 2 chữ số thập phân.</p>
<p>Chọn |<image_1>| Cho phép lọc giá trị của cột
theo thứ tự.</p>
<p>+ Click |<image_2>|: Lọc từ thấp lên cao.</p>
<p>+ Click |<image_3>|: Lọc từ cao xuống thấp.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Đánh giá</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị đánh giá.</p>
<p>+ Hiển thị Đạt: Nếu Tỷ lệ thu công nợ &gt;= 99.9%</p>
<p>+ Hiển thị Không đạt: Nếu Tỷ lệ thu công nợ &lt; 99.9% Hover |<image_4>|  Hiển thị “KPI thu công nợ =
99.9”</p>
</blockquote></td>
</tr>
<tr>
<td colspan="5"><blockquote>
<p><strong>Lũy kế tháng</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Số ngày kế hoạch</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hiển thị số ngày tính KPI lũy kế tháng đến ngày.</p>
<p>Trong đó: Số ngày tính KPI = Số ngày lũy kế từ ngày 1 đến ngày được
chọn - Số ngày chủ nhật, ngày Lễ, ngày Tết trong khoảng thời gian
xét.</p>
<p>Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung cấp:
<a><u>Quy</u></a>
<a><u>đổi
chi tiết ngày 2023 2024 2025.xlsx</u></a></p>
</blockquote></td>
</tr>
<tr>
<td>11</td>
<td>Số ngày đạt KPI</td>
<td>Number</td>
<td colspan="2"><blockquote>
<p>Hiển thị số ngày đạt KPI trong tổng số ngày kế hoạch.</p>
<p>Trong đó: Số ngày đạt KPI là những ngày có Tỷ lệ thu công nợ ngày
&gt;= 99.9%</p>
</blockquote></td>
</tr>
<tr>
<td>12</td>
<td>Số tiền phải thu</td>
<td>Number</td>
<td colspan="2"><blockquote>
<p>Hiển thị tổng số tiền thu hộ lũy kế tháng. ĐVT: VNĐ</p>
</blockquote></td>
</tr>
<tr>
<td>13</td>
<td>Số tiền thu đúng hạn</td>
<td>Number</td>
<td colspan="2"><blockquote>
<p>Hiển thị tổng số tiền thu hộ có thời gian thu &lt;= thời gian đến hạn
thu tiền lũy kế tháng.</p>
<p>ĐVT: VNĐ</p>
</blockquote></td>
</tr>
<tr>
<td>14</td>
<td>Tỷ lệ thu công nợ bình quân</td>
<td>Number</td>
<td colspan="2"><blockquote>
<p>Hiển thị tỷ lệ thu công nợ bình quân tháng từ ngày 1 đến ngày được
chọn. Công thức:</p>
<p>Tỷ lệ thu công nợ bình quân tháng = (Tổng tỷ lệ thu công nợ các ngày
tính KPI</p>
<p>/ Số ngày tính KPI) * 100 (%)</p>
<p>Lưu ý: Số ngày tính KPI = Số ngày lũy kế từ ngày 1 đến ngày được chọn
- Số ngày chủ nhật, ngày Lễ, ngày Tết trong khoảng thời gian xét.</p>
<p>Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung cấp:
<a>Quy</a>
<a>đổi
chi tiết ngày 2023 2024 2025.xlsx</a></p>
<p>Định dạng: %, làm tròn đến 2 chữ số thập phân. Chọn |<image_5>| Cho phép lọc giá trị của cột
theo thứ tự.</p>
<p>+ Click |<image_6>|: Lọc từ thấp lên cao.</p>
<p>+ Click |<image_7>|: Lọc từ cao xuống thấp.</p>
</blockquote></td>
</tr>
<tr>
<td>15</td>
<td>Đánh giá</td>
<td>Text</td>
<td colspan="2"><blockquote>
<p>Hiển thị đánh giá.</p>
<p>+ Hiển thị Đạt: Nếu Tỷ lệ thu công nợ bình quân &gt;= 99.9%</p>
<p>+ Hiển thị Không đạt: Nếu Tỷ lệ thu công nợ bình quân &lt; 99.9%</p>
<p>Hover |<image_8>| Hiển thị “KPI thu công nợ =
99.9”</p>
</blockquote></td>
</tr>
</tbody>
</table> 

# Báo cáo KPI công nợ COD theo tuyến bưu tá
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>STT</strong></p>
</blockquote></th>
<th><strong>Trường dữ liệu</strong></th>
<th><strong>Kiểu dữ liệu</strong></th>
<th><blockquote>
<p><strong>Mô tả</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><p><strong>Mô tả chung:</strong></p>
<ul>
<li><p>Tần suất cấp nhật dữ liệu: Sau khi chốt số tháng tại ngày 5 ngày
N+1, hiển thị báo cáo KPI công nợ COD theo tuyến bưu tá tháng N (chọn
bất kỳ ngày nào tháng N tại bộ lọc thời gian đều xuất báo cáo theo tháng
từ ngày 1 đến ngày cuối tháng N).</p></li>
<li><p>Truy cập: Đăng nhập → Truy xuất dữ liệu → Báo cáo KPI công nợ COD
theo tuyến bưu tá (lũy kế)</p></li>
<li><p>Tên file xuất: bckpicongnocodtheobuutaluyke_ddmmyyyy</p></li>
<li><p>Tên báo cáo: Báo cáo KPI công nợ COD theo tuyến bưu tá (lũy
kế)</p></li>
<li><p>Loại báo cáo: Tài chính</p></li>
<li><p>Phân quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất
toàn bộ dữ liệu.</p></li>
</ul></td>
</tr>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Vùng</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị vùng phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Chi nhánh</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị mã chi nhánh phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vùng con</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị mã vùng con phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Bưu cục</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị bưu cục phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Tuyến bưu tá</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị họ và tên tuyến bưu tá phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Mã nhân viên</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị mã nhân viên tuyến bưu tá phát thực tế. Nếu không có mã nhân
viên  Để trống</p>
</blockquote></td>
</tr>
<tr>
<td colspan="4"><blockquote>
<p><strong>Lũy kế tháng</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Số ngày kế hoạch</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị số ngày tính KPI lũy kế tháng đến ngày.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p><strong>STT</strong></p>
</blockquote></td>
<td><strong>Trường dữ liệu</strong></td>
<td><strong>Kiểu dữ liệu</strong></td>
<td><blockquote>
<p><strong>Mô tả</strong></p>
</blockquote></td>
</tr>
<tr>
<td colspan="4"><blockquote>
<p><strong>Mô tả chung:</strong></p>
</blockquote>
<ul>
<li><p>Tần suất cấp nhật dữ liệu: Sau khi chốt số tháng tại ngày 5 ngày
N+1, hiển thị báo cáo KPI công nợ COD theo tuyến bưu tá tháng N (chọn
bất kỳ ngày nào tháng N tại bộ lọc thời gian đều xuất báo cáo theo tháng
từ ngày 1 đến ngày cuối tháng N).</p></li>
<li><p>Truy cập: Đăng nhập → Truy xuất dữ liệu → Báo cáo KPI công nợ COD
theo tuyến bưu tá (lũy kế)</p></li>
<li><p>Tên file xuất: bckpicongnocodtheobuutaluyke_ddmmyyyy</p></li>
<li><p>Tên báo cáo: Báo cáo KPI công nợ COD theo tuyến bưu tá (lũy
kế)</p></li>
<li><p>Loại báo cáo: Tài chính</p></li>
<li><p>Phân quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất
toàn bộ dữ liệu.</p></li>
</ul></td>
</tr>
<tr>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Vùng</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị vùng phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Chi nhánh</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị mã chi nhánh phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Vùng con</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị mã vùng con phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Bưu cục</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị bưu cục phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Tuyến bưu tá</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị họ và tên tuyến bưu tá phát thực tế.</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Mã nhân viên</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị mã nhân viên tuyến bưu tá phát thực tế. Nếu không có mã nhân
viên  Để trống</p>
</blockquote></td>
</tr>
<tr>
<td colspan="4"><blockquote>
<p><strong>Lũy kế tháng</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Số ngày kế hoạch</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị số ngày tính KPI lũy kế tháng đến ngày.</p>
<p>Trong đó: Số ngày tính KPI = Số ngày lũy kế từ ngày 1 đến ngày được
chọn - Số ngày chủ nhật, ngày Lễ, ngày Tết trong khoảng thời gian
xét.</p>
<p>Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung cấp:
<a><u>Quy</u></a>
<a><u>đổi
chi tiết ngày 2023 2024 2025.xlsx</u></a></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Số ngày đạt KPI</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị số ngày đạt KPI trong tổng số ngày kế hoạch.</p>
<p>Trong đó: Số ngày đạt KPI là những ngày có Tỷ lệ thu công nợ ngày
&gt;= 99.9%</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Số tiền phải thu</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị tổng số tiền thu hộ lũy kế tháng. ĐVT: VNĐ</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Số tiền thu đúng hạn</p>
</blockquote></td>
<td><blockquote>
<p>Number</p>
</blockquote></td>
<td><blockquote>
<p>Hiển thị tổng số tiền thu hộ có thời gian thu &lt;= thời gian đến hạn
thu tiền lũy kế tháng.</p>
<p>ĐVT: VNĐ</p>
</blockquote></td>
</tr>
<tr>
<td>11</td>
<td>Tỷ lệ thu công nợ bình quân</td>
<td>Number</td>
<td><blockquote>
<p>Hiển thị tỷ lệ thu công nợ bình quân tháng từ ngày 1 đến ngày được
chọn. <u>Công thức:</u></p>
<p>Tỷ lệ thu công nợ bình quân tháng = (Tổng tỷ lệ thu công nợ các ngày
tính KPI / Số ngày tính KPI) * 100 (%)</p>
<p><u>Lưu ý:</u> Số ngày tính KPI = Số ngày lũy kế từ ngày 1 đến ngày
được chọn - Số ngày chủ nhật, ngày Lễ, ngày Tết trong khoảng thời gian
xét.</p>
<p>Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung cấp:
<a><u>Quy</u></a>
<a><u>đổi
chi tiết ngày 2023 2024 2025.xlsx</u></a></p>
<p><u>Định dạng:</u> %, làm tròn đến 2 chữ số thập phân.</p>
</blockquote></td>
</tr>
<tr>
<td>12</td>
<td>Đánh giá</td>
<td>Number</td>
<td><blockquote>
<p>Hiển thị đánh giá.</p>
<p>+ Hiển thị Đạt: Nếu Tỷ lệ thu công nợ bình quân &gt;= 99.9%</p>
</blockquote>
<p>+ Hiển thị Không đạt: Nếu Tỷ lệ thu công nợ bình quân &lt;
99.9%</p></td>
</tr>
</tbody>
</table>