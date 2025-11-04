# Public_276

# Nội dung nâng cấp
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>STT</strong></th>
<th><strong>Nội dung công việc</strong></th>
<th><strong>Chi tiết</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Hạn mức công nợ</td>
<td>Tất cả chức năng liên quan hạn mức công nợ không thay đổi</td>
</tr>
<tr>
<td>2</td>
<td>Đề xuất hạn mức sản lượng trên App/web</td>
<td><p>Cho phép người đề xuất nhập tỷ lệ đề xuất check tỷ lệ theo cấu
hình để lấy luồng ký</p>
<p>Tự động tính ra sản lượng đề xuất theo mức tỷ lệ nhập</p></td>
</tr>
</tbody>
</table> 

# Nâng cấp chức năng trên web

## Màn hình Danh sách Hạn mức bưu cục

### Giao diện màn hình Tổng hạn mức bưu cục

_Mô tả chi tiết màn hình_

  * Màn hình danh sách hạn mức được theo dõi hạn mức công nợ/Hạn mức sản lượng theo Bưu cục.

  * Điều kiện lọc:

* Chi nhánh

* Bưu cục

* Nhân viên

  * Phân quyền: 

* Phân quyền chức năng cho GĐ chi nhánh, Phụ trách bưu cục.

* User được phân quyền vào chi nhánh/bưu cục nào thì hiển thị thông tin chi nhánh/bưu cục đó.

  * Thông tin hiển thị: 

* Chi nhánh: Hiển thị thông tin chi nhánh

* Bưu cục: Hiên thị bưu cục theo chi nhánh

* Hạn mức sản lượng: Tổng hạn mức sản lượng áp dụng của tất cả các tuyến thuộc bưu cục

* Hạn mức công nợ (1): Hạn mức công nợ tổng của bưu cục = Giá trị cố định được cấp + Giá trị đề xuất thêm

* Hạn mức đã phân bổ (2): Hạn mức công nợ đã được phân bổ cho nhân viên trong bưu cục

* Hạn mức còn lại = (1)-(2)

  * Thao tác: Xem chi tiết→ Gọi đến màn hình 3.2

  * Chức năng import: button Import 


|<image_1>| 

  * Import hạn mức cố định của nhân viên trong bưu cục: Hạn mức sản lượng và Hạn mức công nợ

  * Phân quyền: phân quyền cho TTVH

  * Chọn loại hạn mức: Cho phép người dùng chọn loại hạn mức để import

  * Nguyên tắc import hạn mức công nợ: 

* Username phải tồn tại trên hệ thống và đang active

* Nếu tổng hạn mức cố định import <>= Hạn mức cố định hiện tại của Bưu cục ==> cho phép import

* Nếu tổng hạn mức cố định import < Hạn mức cố định hiện tại của bưu cục ==> gửi cảnh báo Noti vtman cho TBC "TTVH đã cập nhật giảm hạn mức cố định của bưu cục, TBC đôn đốc tuyến hoàn thành công nợ để tiếp tục phân công"

* Dữ liệu import mới được cập nhật lại vào dữ liệu hạn mức cố định hiện tại của bưu tá → cập nhật lại hạn mức của bưu cục → cập nhật lại hạn mức phân bổ = hạn mức cố định của bưu tá → lưu log cập nhật 

* User có role chi nhánh chỉ được upload dữ liệu chi nhánh user đó quản lý, User có role TCT được upload dữ liệu cho toàn TCT. Nếu upload không đúng dữ liệu chi nhánh quản lý → trả ra lỗi tại các bưu cục chi nhánh không thuộc user đó quản lý.

  * Nguyên tắc import hạn mức sản lượng: 

* Username phải tồn tại trên hệ thống và đang active

* Dữ liệu import mới được cập nhật lại vào dữ liệu hạn mức cố định hiện tại của bưu tá → Cập nhật hạn mức áp dụng = hạn mức cố định của bưu tá + mức đề xuất thêm → lưu log cập nhật 

* Chỉ user có Role TTVH mới thực hiện import.

  * Template import: |<image_2>|

  * Cho phép xuất excel danh sách hạn mức bưu tá: Template như sau:

  * |<image_3>|

  * Cho phép xuất excel danh sách hạn mức bưu cục: Template như sau: Hạn-mức-chi-nhanh


|<image_4>|

### Màn hình Chi tiết hạn mức sản lượng của bưu cục

Mô tả màn hình: 
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
<th>STT</th>
<th>Field Name</th>
<th>Control Type</th>
<th>Editable/ Readonly</th>
<th>Description/Note</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>STT</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị STT</td>
</tr>
<tr>
<td>2</td>
<td>Chi nhánh</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên chi nhánh</td>
</tr>
<tr>
<td>3</td>
<td>Tên bưu cục</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên bưu cục</td>
</tr>
<tr>
<td>4</td>
<td>User</td>
<td>Text</td>
<td>Readonly</td>
<td>HIển thị User </td>
</tr>
<tr>
<td>5</td>
<td>Tên nhân viên</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên nhân viên </td>
</tr>
<tr>
<td>6</td>
<td>Trạng thái hoạt động</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị trạng thái hoạt động</td>
</tr>
<tr>
<td>7</td>
<td>Hạn mức cố định</td>
<td>Text</td>
<td>Readonly</td>
<td>HIển thị Hạn mức cố định được cấu hình tự động hoặc TTVH cấu hình
cho đơn  vị </td>
</tr>
<tr>
<td>8</td>
<td>Hạn mức áp dụng</td>
<td>Text</td>
<td>Readonly</td>
<td><p>Hiển thị hạn mức được áp dụng với tuyến bưu tá → là hạn mức bưu
tá được sử dụng</p>
<p>Hạn mức áp dụng = Hạn mức cố định + Mức phân bổ thêm hoặc Mức đề xuất
thêm</p></td>
</tr>
<tr>
<td>9</td>
<td>Sửa hạn mức</td>
<td>Button</td>
<td>Editable</td>
<td>Click Sửa hạn mức để Chuyển sang màn hình phân bổ hạn mức</td>
</tr>
<tr>
<td>10</td>
<td>Đóng</td>
<td>Button</td>
<td>Editable</td>
<td>Click Đóng để tắt popup</td>
</tr>
</tbody>
</table> 

Màn hình TBC phân bổ hạn mức thêm cho tuyến
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
<th><strong>STT</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Control Type</strong></th>
<th><strong>Editable/ Readonly</strong></th>
<th><strong>Description/Note</strong></th>
</tr>
<tr>
<th colspan="5"><strong>Thông tin tổng hợp</strong></th>
</tr>
<tr>
<th>1</th>
<th>Bưu cục</th>
<th>Text</th>
<th>Readonly</th>
<th>Hiển thị tên bưu cục</th>
</tr>
<tr>
<th>2</th>
<th>Tổng hạn mức cố định</th>
<th>Text</th>
<th>Readonly</th>
<th>Hiển thị tổng hạn mức cố định của bưu cục =  Tổng hạn mức cố định
của tất cả các tuyến thuộc bưu cục</th>
</tr>
<tr>
<th>3</th>
<th>Tổng hạn mức áp dụng</th>
<th>Text</th>
<th>Readonly</th>
<th>Hiển thị tổng hạn mức áp dụng của tuyến</th>
</tr>
<tr>
<th>4</th>
<th>Tổng hạn mức đã phân bổ/đề xuất thêm</th>
<th>Text</th>
<th>Readonly</th>
<th>Hiển thị Tổng hạn mức đã phân bổ = Tổng hạn mức áp dụng – Tổng hạn
mức cố định</th>
</tr>
<tr>
<th colspan="5"><strong>Thông tin chi tiết</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>STT</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị STT</td>
</tr>
<tr>
<td>2</td>
<td>Chi nhánh</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên chi nhánh</td>
</tr>
<tr>
<td>3</td>
<td>Tên bưu cục</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên bưu cục</td>
</tr>
<tr>
<td>4</td>
<td>User</td>
<td>Text</td>
<td>Readonly</td>
<td>HIển thị User </td>
</tr>
<tr>
<td>5</td>
<td>Tên nhân viên</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên nhân viên </td>
</tr>
<tr>
<td>6</td>
<td>Trạng thái hoạt động</td>
<td>Button</td>
<td>Editable</td>
<td>Cho phép người dùng on/off trạng thái của bưu tá </td>
</tr>
<tr>
<td>7</td>
<td>Hạn mức cố định</td>
<td>Text</td>
<td>Readonly</td>
<td>HIển thị Hạn mức cố định được cấu hình tự động hoặc TTVH cấu hình
cho đơn  vị </td>
</tr>
<tr>
<td>8</td>
<td>Hạn mức áp dụng</td>
<td>Text</td>
<td>Readonly</td>
<td><p>Hiển thị hạn mức áp dụng của từng tuyến bưu tá.</p>
<p>Hạn mức áp dụng được tính theo nguyên tắc sau:</p>
<p>Hạn mức áp dụng = Hạn mức cố định của tuyến + Hạn mức phân bổ thêm
hoặc hạn mức đề xuất thêm</p>
<p>Lưu ý:</p>
<p>- Hạn mức áp dụng không cộng đồng thời với hạn mức phân bổ và Hạn mức
đề xuất thêm</p>
<p>- Nếu có hạn mức đề xuất thêm thì hạn mức phân bổ = 0</p>
<p>- Nếu không có hạn mức đề xuất thêm Hạn mức phân bổ = Hạn mức mà TBC
phân bổ thêm</p></td>
</tr>
<tr>
<td>9</td>
<td>Hạn mức phân bổ</td>
<td>Textbox</td>
<td>Editable</td>
<td><p>Cho phép TBC phân bổ hạn mức cho các tuyến.</p>
<p>Giá trị phân bổ không được lớn hơn 25% so với hạn mức cố định của
tuyến đó, Nếu lớn hơn hiện thị cảnh báo lỗi "Hạn mức thay đổi không được
quá 25% so với Hạn mức cố định của bưu tá"</p>
<p>Lưu ý:</p>
<p>- Disable textbox với các tuyến có Hạn mức áp dụng – Hạn mức cố định
lớn hơn hoặc bằng 25%</p>
<p>- Disable textbox với các tuyến off</p></td>
</tr>
<tr>
<td>10</td>
<td>Cập nhật</td>
<td>Button</td>
<td>Editable</td>
<td>Click Cập nhật để lưu trạng thái hoạt động và Hạn mức áp dụng của
từng tuyến.</td>
</tr>
<tr>
<td>11</td>
<td>Đóng</td>
<td>Button</td>
<td>Editable</td>
<td>Click Đóng để tắt popup</td>
</tr>
</tbody>
</table> 

## Màn hình Báo cáo tổng hợp hạn mức

### Mô tả chi tiết màn hình

_* Hạn mức sản lượng:_

  * Hạn mức áp dụng: là hạn mức được áp dụng trong ngày của tuyến bưu tá đó

  * Đã sử dụng: là tổng sản lượng đơn đã phân công vào tuyến (đã loại trừ các loại vận đơn không tính hạn mức) + đơn đã PTC trong ngày

  * Còn lại = Hạn mức áp dụng - Đã sử dụng


  * Loại trừ các loại bưu gửi sau không trừ hạn mức sản lượng bưu tá: Bill chuyển hoàn (mã dịch vụ - GCH), Bill giao hàng 1 phần (Mã DV – G1P), Bill Báo phát (Mã DV – GBP), Bill đổi hàng (mã DV – GBH)


Chi tiết Bưu tá: Cho phép xem chi tiết danh sách hạn mức đơn đã phân công và Công nợ của từng tuyến bưu tá

  * Chi tiết phân công:


Hiển thị danh sách đơn đã phân công nhưng chưa gạch phát 

  * Chi tiết công nợ:


Hiển thị danh sách chi tiết công nợ của tuyến bưu tá, bao gồm: Nợ quá hạn, Nợ sắp quá hạn và Nợ trong hạn.

## [WEB] TRÌNH KÝ ĐỀ XUẤT

### Mô tả chức năng

Chức năng cho phép người dùng trình ký lên VOFFICE các đề xuất có trạng thái Chờ trình ký.

Chức năng phân quyền cho đối tượng có role tương ứng với vài trò trình ký theo cấu hình ở chức năngFICO Quản trị hệ thống à Công nợ nội bộ - Khai báo danh mục.User có vai trò trình ký, thao tác với dữ liệu tại đơn vị mà user được phân quyền.

Ngoài ra chức năng được phân quyền cho role TCT để xem dữ liệu và hỗ trợ khi có khiếu nại. User role TCT chỉ được phép xem dữ liệu, không có quyền tác động (trình ký).

### Màn hình

#### Trình ký đề xuất

|<image_5>|

#### Chi tiết đề xuất

|<image_6>|

Chi tiết gia hạn theo bảng kê

|<image_7>|

Chi tiết gia hạn thời hạn nộp tiền

### Mô tả màn hình

#### Trình ký đề xuất
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
<th><strong>STT</strong></th>
<th><strong>Thông tin</strong></th>
<th><strong>Kiểu DL</strong></th>
<th><strong>Bắt buộc</strong></th>
<th><strong>Mặc định</strong></th>
<th><strong>Mô tả</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>Chọn bưu cục</td>
<td>Combobox</td>
<td>Không</td>
<td>Tất cả</td>
<td><p>Cho phép chọn bưu cục mà user được phép truy cập, thuộc chi nhánh
của bưu cục đang đăng nhập, bao gồm:</p>
<p>-        Tất cả: Lấy dữ liệu thuộc tất cả bưu cục mà user đc phép
truy cập, theo chi nhánh đang đăng nhập</p>
<p>-        Danh sách bưu cục mà user được phép truy cập thuộc chi nhánh
đang đăng nhập. Định dạng: [Tên bưu cục] – [Mã bưu cục]</p>
<p>Cho phép nhập text tìm kiếm theo tên/mã bưu cục</p></td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>Chọn loại đề xuất</td>
<td>Combobox</td>
<td>Có</td>
<td>Không</td>
<td><p>Cho phép chọn loại đề xuất, bao gồm:</p>
<p>-        Tất cả: Lấy dữ liệu tất cả các loại đề xuất</p>
<p>-        Đề xuất tăng hạn mức (công nợ/sản lượng)</p>
<p>-        Đề xuất thay đổi thời hạn nộp tiền</p>
<p>-        Đề xuất gia hạn theo đơn-bảng kê</p>
<p>Chỉ chọn 1 trong 4 lựa chọn.</p></td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Chọn cấp trình ký</td>
<td>Combobox</td>
<td>Không</td>
<td>Không</td>
<td><p>Chọn cấp trình ký, bao gồm:</p>
<p>-        Tất cả</p>
<p>-        Danh sách cấp trình ký: Xác định theo danh mục đối tượng
được cấu hình tại chức năng <em>Công nợ nội bộ - Khai báo danh mục</em>.
VD: V_GDCN</p></td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Chọn trạng thái</td>
<td>Combobox</td>
<td>Không</td>
<td>Không</td>
<td><p>Cho phép chọn trạng thái trình ký:</p>
<p>-        Chờ trình ký: Là các đề xuất chờ trình ký</p>
<p>-        Chờ ký duyệt: Là các đề xuất đã trình ký Vof, chờ các cấp ký
duyệt</p>
<p>-        Đã duyệt: đề xuất được các cấp ký duyệt nhưng chưa đến thời
gian hiệu lực</p>
<p>-        Đang sử dụng: đề xuất được các cấp ký duyệt và đang trong
thời gian hiệu lực</p>
<p>-        Hết hạn: đề xuất được các cấp ký duyệt và đã qua thời gian
hiệu lực</p>
<p>-        Từ chối: đề xuất bị từ chối ký duyệt</p></td>
</tr>
<tr>
<td><strong>5</strong></td>
<td>Tìm kiếm</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép tìm kiếm đề xuất theo các mục đã chọn</td>
</tr>
<tr>
<td><strong>6</strong></td>
<td>Trình ký</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td><p>Cho phép gom trình ký lên Voffice các đề xuất có cùng cấp trình
ký.</p>
<p>Chỉ enable button khi NSD chọn ít nhất 1 đề xuất và các đề xuất có
cùng cấp trình ký</p>
<p>Click button à Hiển thị màn hình cho phép nhập các thông tin trính ký
(mục 19-22)</p></td>
</tr>
<tr>
<td><strong>7</strong></td>
<td>Checkbox</td>
<td>Checkbox</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép chọn 1 hoặc nhiều đề xuất</td>
</tr>
<tr>
<td><strong>8</strong></td>
<td>STT</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị số thứ tự</td>
</tr>
<tr>
<td><strong>9</strong></td>
<td>Chi nhánh</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị tên chi nhánh</td>
</tr>
<tr>
<td><strong>10</strong></td>
<td>Bưu cục</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td><p>Hiển thị thông tin bưu cục:</p>
<p>Bưu cục [tên bưu cục] – [Mã bưu cục]</p></td>
</tr>
<tr>
<td><strong>11</strong></td>
<td>Loại đề xuất</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị loại đề xuất</td>
</tr>
<tr>
<td><strong>12</strong></td>
<td>User</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị user</td>
</tr>
<tr>
<td><strong>13</strong></td>
<td>Tên nhân viên</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị tên user</td>
</tr>
<tr>
<td><strong>14</strong></td>
<td>Lý do đề xuất</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị lý do đề xuất đã chọn</td>
</tr>
<tr>
<td><strong>15</strong></td>
<td>Ghi chú</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị nội dung Ghi chú đã nhập (nếu có)</td>
</tr>
<tr>
<td><strong>16</strong></td>
<td>Đối tượng phê duyệt</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị đối tượng phê duyệt cấp tiếp theo mà đối tượng phê duyệt
trước đó đã chọn</td>
</tr>
<tr>
<td><strong>17</strong></td>
<td>Thời gian đề xuất</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td><p>Hiển thị thời gian đề xuất</p>
<p>Dd/mm/yyyy</p>
<p>Hh:mm:ss</p></td>
</tr>
<tr>
<td><strong>18</strong></td>
<td>Thời gian cập nhật</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị thời gian cập nhật: thời gian cập nhật vào danh sách chờ
tổng hợp trình ký.</td>
</tr>
<tr>
<td><strong>19</strong></td>
<td>Thao tác</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td><p>Cho phép xem chi tiết đề xuất</p>
<p>Màn hình: <em><strong>3.4.3.2</strong></em> <em><strong>Chi tiết đề
xuất</strong></em></p></td>
</tr>
<tr>
<td colspan="6"><strong>Trình ký đề xuất</strong></td>
</tr>
<tr>
<td><strong>20</strong></td>
<td>Nhập nội dung thực trạng</td>
<td>TextInput</td>
<td>Không</td>
<td>Không</td>
<td><p>Cho phép nhập nội dung thực trạng, nội dung này sẽ hiển thị trong
file mẫu trình ký</p>
<p>Maxlength: 1000</p></td>
</tr>
<tr>
<td><strong>21</strong></td>
<td>Chọn người phê duyệt</td>
<td>Combobox</td>
<td>Không</td>
<td>Không</td>
<td><p>Cho phép chọn đối tượng phê duyệt theo luồng phê duyệt đã cấu
hình.</p>
<p>Hiển thị danh sách đối tượng theo luồng phê duyệt.</p>
<p>Riêng chân ký TCT-Kế toán trưởng hệ thống sẽ tự động hiển thị đối
tượng và không cho phép chọn lại. Đối tượng được lấy theo role TCT – Kế
toán trưởng (trường hợp trên hệ thống có nhiều hơn 1 đối tượng có role
này, hiển thị ngẫu nhiên 1 đối tượng).</p>
<p>Trường hợp không có đối tượng phê duyệt à hiển thị thông báo Message
lỗi: "Không xác định được đối tượng [tên role] tại đơn vị, yêu cầu kiểm
tra lại ", không cho tạo Trình ký.</p></td>
</tr>
<tr>
<td><strong>22</strong></td>
<td>Hiển thị chân ký</td>
<td>Radio button</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép người dùng lựa chọn hiển thị (click button) hoặc không hiển
thị (không click button) chữ ký trong file trình ký.</td>
</tr>
<tr>
<td><strong>23</strong></td>
<td>Hủy</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép hủy trình ký</td>
</tr>
<tr>
<td><strong>24</strong></td>
<td>Xác nhận</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép xác nhận các thông tin trình ký vừa chọn</td>
</tr>
<tr>
<td colspan="6"><strong>Mẫu trình ký</strong></td>
</tr>
<tr>
<td><strong>25</strong></td>
<td>File trình ký</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị file trình ký mẫu</td>
</tr>
<tr>
<td><strong>26</strong></td>
<td>Phụ lục</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td><p>Hiển thị file đính kèm của các đề xuất</p>
<p>Chỉ hiển thị các file định dạng PDF</p></td>
</tr>
<tr>
<td><strong>27</strong></td>
<td>Tên chi nhánh</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td><p>Hiển thị tên chi nhánh trình ký</p>
<p>Với các chi nhánh đặc biệt, hiển thị tên theo file phụ lục PTC cung
cấp</p></td>
</tr>
<tr>
<td><strong>28</strong></td>
<td>Mã chi nhánh</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị mã chi nhánh trình ký</td>
</tr>
<tr>
<td><strong>29</strong></td>
<td>Tỉnh/TP</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td><p>Hiển thị tên tỉnh, thành phố = tên chi nhánh</p>
<p>Với các chi nhánh đặc biệt, hiển thị tên theo file phụ lục</p></td>
</tr>
<tr>
<td><strong>30</strong></td>
<td>Ngày/tháng/năm</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị thông tin ngày trính ký</td>
</tr>
<tr>
<td><strong>31</strong></td>
<td>Kính gửi</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Tên role của cấp phê duyệt cao nhất</td>
</tr>
<tr>
<td><strong>32</strong></td>
<td>Đề nghị</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Tên role của cấp phê duyệt cao nhất</td>
</tr>
<tr>
<td><strong>33</strong></td>
<td>Thực trạng</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị nội dung thực trạng đã nhập</td>
</tr>
<tr>
<td><strong>34</strong></td>
<td>Chi tiết đề xuất</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Hiển thị nội dung chi tiết đề xuất</td>
</tr>
<tr>
<td><strong>35</strong></td>
<td>Kính đề nghị</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td>Tên role của cấp phê duyệt cao nhất</td>
</tr>
<tr>
<td><strong>36</strong></td>
<td>Chân ký</td>
<td>Text</td>
<td>Không</td>
<td>Không</td>
<td><p>Gắn chân ký theo luồng trình ký.</p>
<p>Chân ký Người đề xuất: Hiển thị họ tên người yêu cầu đề xuất (ko gắn
chữ ký VOF)</p>
<p>Chân ký Trưởng bưu cục: comment số 1, gắn chân ký theo mã nhân viên
của người trình ký – cố định hiển thị.</p>
<p>Các chân ký sau sẽ phụ thuộc vào luồng ký và cấu hình trình ký có
hiển thị chân ký hay ko. Người phê duyệt có hiển thị chữ ký tương ứng
với các comment (gắn chân ký): 2, 3, 4.</p>
<p>Chân ký GĐCN : Comment số 2</p>
<p>Chân ký Trưởng nhóm đối soát: Comment số 3</p>
<p>Chân ký P.Tài chính: Comment số 4</p>
<p>Chân ký nào ko đc gắn chân ký à ko hiển thị trên file trình ký</p>
<p>VD: Luồng ký bao gồm:</p>
<p>1.     Phó GĐCN: Chọn ko hiển thị chữ ký</p>
<p>2.     GĐCN: Chọn hiển thị chữ ký</p>
<p>3.     TCT – Kế toán đối soát: Chọn ko hiển thị chữ ký</p>
<p>4.     TCT – Kế toán trưởng: Chọn hiển thị chữ ký</p>
<p>è Comment 1: Gắn tại chân ký Trưởng bưu cục, Hiển thị chữ ký của
người trình ký</p>
<p>è Comment 2: Gắn tại chân ký Giám đốc chi nhánh, hiển thị chữ ký của
role GĐCN</p>
<p>è Comment 3: Gắn tại chân ký Trưởng nhóm đối soát, hiển thị chữ ký
của role Kế toán trưởng.</p>
<p>è Comment 4: Ko đc khai báo nên ko hiển thị chân ký P.TC trong file
trình ký</p></td>
</tr>
<tr>
<td><strong>37</strong></td>
<td>Hủy</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép hủy thao tác trình ký</td>
</tr>
<tr>
<td><strong>38</strong></td>
<td>Trình ký</td>
<td>Button</td>
<td>Không</td>
<td>Không</td>
<td>Cho phép trình ký theo cài đặt đã chọn. Click button hệ thống gọi
đến màn hình đăng nhập VOF, yêu cầu NSD nhập thông tin user, pass để
đăng nhập trình ký VOF</td>
</tr>
</tbody>
</table> 

### Yêu cầu nghiệp vụ chi tiết

Chức năng cho phép người dùng – đối tượng được cấu hình vai trò trình ký trong luồng phê duyệt liên quan đến thời hạn nộp tiền hoặc hạn mức (cấu hình vai trò tại chức năng (FICOàQuản trị hệ thốngàCông nợ nội bộ - Khai báo danh mụcàKhai báo danh mục thời hạn nộp tiềnvàCấu hình luồng phê duyệt)

Sau khi khai báo, hệ thống sẽ xác định luồng phê duyệt, đối tượng có vai trò trình ký tương ứng với thông tin đề xuất (so sánh với thông tin cấu hình luồng phê duyệt). Khi đến chân phê duyệt của đối tượng có vai trò trình ký, đề xuất sẽ được cập nhật trạng thái Chờ trình ký, hiển thị tại màn hình đề xuất trình ký của đối tượng.

Chỉ thực hiện trình ký được với các đề xuất trạng thái Chờ trình ký, có thể chọn nhiều đề xuất, nhưng phải cùng loại đề xuất (thời hạn nộp tiền/hạn mức/gia hạn đơn-bảng kê) thì mới cho trình ký trong cùng 1 lượt (do luồng ký của các loại đề xuất có thể khác nhau).

Các bước trình ký:

Bước 1 : Người dùng chọn các đề xuất cùng loại, trạng thái Chờ trình ký để thực hiện trình ký. Hệ thống hiển thị màn hình trính ký, hiển thị role trong luồng phê duyệt (theo cấu hình) lần lượt từ trên xuống, cho phép chọn đối tượng ký duyệt, chỉ hiển thị danh sách đối tượng có role tương ứng với luồng phê duyệt đã cấu hình. Đồng thời chọn xem đối tượng có hiển thị chữ ký trong luồng phê duyệt hay không. Khi chọn đối tượng, hệ thống kiểm tra đối tượng có thông tin trên VOF hay không, thông qua mã nhân viên của đối tượng được chọn, nếu không có thông tin trên VOF, hệ thống hiển thị cảnh báo: ”Người dùng không có thông tin ký Voffice. Vui lòng kiểm tra lại mã nhân viên”, và không cho tạo trình ký.

Bước 2: Sau khi xác nhận thông tin cấu hình trình ký (xác định đối tượng, có hiển thị chữ ký hay ko). Hệ thống lần lượt xác định hiển thị chữ ký tại các chân ký (comment). Chân ký (comment) sẽ tương ứng với số lượng đối tượng phê duyệt

  * Comment 1: Tương ứng chân ký của Người trình ký – tên chân ký Trưởng bưu cục (theo quy định hiện tại)

  * Comment 2: Tương ứng chân ký của đối tượng phê duyệt thứ 2 trong luồng ký - Tên chân ký lấy theo Chức danh phê duyệt trong cấu hình

  * Comment 3: Tương ứng chân ký của đối tượng phê duyệt thứ 3 trong luồng ký - Tên chân ký lấy theo Chức danh phê duyệt trong cấu hình

  * Comment n: Tương ứng chân ký của đối tượng phê duyệt thứ n trong luồng ký - Tên chân ký lấy theo Chức danh phê duyệt trong cấu hình


Căn cứ vào cấu hình hiển thị chữ ký, hệ thống sẽ gán tương ứng từ comment số 2, 3, 4 với các đối tượng được cấu hình hiển thị chữ ký từ trên xuống dưới. Comment nào ko có đối tượng hiển thị chữ ký sẽ được ẩn khỏi file trình ký.

_VD1: Cấu hình luồng ký bao gồm:

  1. Role Phó GĐCN: Chọn ko hiển thị chữ ký

  2. Role GĐCN: Chọn hiển thị chữ ký

  3. Role TCT – Kế toán đối soát: Chọn ko hiển thị chữ ký

  4. Role TCT – Kế toán trưởng: Chọn hiển thị chữ ký


  * Comment 1: Gắn tại chân ký Trưởng bưu cục, Hiển thị chữ ký của người trình ký

  * Comment 2: Gắn tại chân ký Giám đốc chi nhánh, hiển thị chữ ký của role GĐCN

  * Comment 3: Gắn tại chân ký Trưởng nhóm đối soát, hiển thị chữ ký của role Kế toán trưởng.

  * Comment 4: Ko đc khai báo nên ko hiển thị chân ký P.TC trong file trình ký


_VD2: Cấu hình luồng ký bao gồm:

  1. Role Phó GĐCN: Chọn ko hiển thị chữ ký

  2. Role GĐCN: Chọn hiển thị chữ ký


  * Comment 1: Gắn tại chân ký Trưởng bưu cục, Hiển thị chữ ký của người trình ký

  * Comment 2: Gắn tại chân ký Giám đốc chi nhánh, hiển thị chữ ký của role GĐCN

  * Comment 3, 4: Ko đc khai báo chữ ký nên ko hiển thị chân ký Trưởng nhóm đối soát và Kế toán trưởng trong tờ trình.


Bước 3: Sau khi xác nhận nội dung trong file trình ký, người dùng chọn Trình ký, hệ thống hiển thị màn hình cho phép nhập thông tin user, pass tài khoản Voffice để đăng nhập trình ký.

Đăng nhập thành công, hiển thị màn hình các thông tin trình ký:

  * Trích yếu nội dung: Đề xuất nâng hạn mức/tăng thời hạn nộp tiền/gia hạn thời gian nộp tiền - Chi nhánh:[Tên chi nhánh thực hiện trình ký] -Bưu cục: [Tên bưu cục thực hiện trình ký]

  * Nội dung: Đề xuất nâng hạn mức/tăng thời hạn nộp tiền/gia hạn thời gian nộp tiền - Chi nhánh:[Tên chi nhánh thực hiện trình ký] -Bưu cục: [Tên bưu cục thực hiện trình ký]

  * Hình thức văn bản: Đề xuất

  * Độ khẩn: Khẩn

  * Danh sách người ký: Hiển thị danh sách người ký đã chọn và cấu hình tại màn hình Trình ký đề xuất dựa theo mã nhân viên của đối tượng được chọn để xác định người ký tương ứng trên hệ thống VOF.

  * Văn bản trình ký: là file mẫu trình ký

  * Văn bản đính kèm: Hiển thị các file đính kèm (dạng PDF) của các đề xuất có trong lượt trình ký. (Các file đính kèm khác định dạng PDF không thể hiển thị lên lượt trình ký)


Trình ký thành công, hệ thống cập nhật trạng thái đề xuất thành Chờ ký duyệt. Tờ trình đc các cấp phê duyệt, hệ thống trạng thái đề xuất Đã duyệt/Đang sử dụng/Hết hạn phụ thuộc vào thời gian áp dụng. Tờ trình bị từ chối, hệ thống cập nhật trạng thái đề xuất thành Từ chối. Với các đề xuất trạng thái từ chối, người đề xuất phải đề xuất lại từ đầu. 

_Vận hành: Để đảm bảo thông tin trình ký, có đối tượng để chọn phê duyệt theo luồng cấu hình, P.TC yêu cầu đơn vị khai báo đủ các role theo luồng ký tại tất cả các đơn vị.

_Chức năng ảnh hưởng_ :

  * Thêm trường thông tin Vai trò phê duyệt cho các đối tượng tại chức năng:FICOàQuản trị hệ thốngàCông nợ nội bộ - Khai báo danh mụcàKhai báo danh mục thời hạn nộp tiềnvàCấu hình luồng phê duyệt_


Cho phép chọn các Vai trò:

  * Phê duyệt: Đối tượng thực hiện phê duyệt trên app Vtman/web Fico

  * Trình ký: Đối tượng thực hiện phê duyệt trên app Vtman/web Fico, sau đó tổng hợp trình ký các đề xuất lên Voffice để các cấp tiếp theo ký duyệt trên Vofice

  * Ký duyệt: Đối tượng thực hiện phê duyệt (ký duyệt) trên Voffice.

  * Bổ sung trạng thái đề xuất: 2 trạng thái Chờ trình ký, Chờ ký duyệt. Áp dụng cho tất cả các loại đề xuất.

  * Chờ trình ký: đề xuất đã qua 1 hoặc nhiều cấp phê duyệt trên app VTMan/web fico, đang chờ được tổng hợp trình ký lên Voffice. Đối tượng tổng hợp trình ký sẽ được P.TC khai báo vai trò tại chức năngFICOàQuản trị hệ thốngàCông nợ nội bộ - Khai báo danh mụcàKhai báo danh mục thời hạn nộp tiềnvàCấu hình luồng phê duyệt_

  * Chờ ký duyệt: đề xuất đã được trình ký lên Voffice, đang chờ các cấp ký duyệt.


## [WEB] Danh sách đề xuất Hạn mức bưu cục

### Màn hình danh sách đề xuất 

Mô tả Màn hình danh sách đề xuất 
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
<th><strong>STT</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Control Type</strong></th>
<th><strong>Editable/ Readonly</strong></th>
<th><strong>Description/Note</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5"><strong>Tra cứu</strong></td>
</tr>
<tr>
<td>1</td>
<td>Thời gian đề xuất</td>
<td>Calendar</td>
<td>Editable</td>
<td><p>Cho phép người dùng chọn khoảng thời gian đề xuất.</p>
<p>Giới hạn chọn tới ngày hiện tại</p></td>
</tr>
<tr>
<td>2</td>
<td>Chi nhánh</td>
<td>Dropdown list</td>
<td>Editable</td>
<td><p>Hiển thị danh sách chi nhánh cho người dùng chọn</p>
<p>Mặc định theo phân quyền</p>
<p>Nếu role TCT → hiển thị tất cả chi nhánh cho người dùng chọn</p>
<p>Nếu role chi nhánh → mặc định chi nhánh  mà user quản lý - không cho
phép chọn</p>
<p>Nếu role Bưu cục → Hiện thị mặc định chi nhánh quản lý bưu cục -
không cho phép chọn</p></td>
</tr>
<tr>
<td>3</td>
<td>Bưu cục</td>
<td>Dropdown list</td>
<td>Editable</td>
<td><p>Hiển thị danh sách bưu cục cho người dùng chọn</p>
<p>Mặc định theo phân quyền</p>
<p>Nếu role TCT → hiển thị tất cả bưu cục thuộc chi nhánh đã chọn cho
người dùng chọn</p>
<p>Nếu role chi nhánh → hiển thị danh sách bưu cục mà user quản lý </p>
<p>Nếu role Bưu cục → Hiện thị mặc định bưu cục- không cho phép
chọn</p></td>
</tr>
<tr>
<td>4</td>
<td>Nhân viên</td>
<td>Dropdown list</td>
<td>Editable</td>
<td><p>Hiển thị danh sách mã nhân viên thuộc bưu cục quản lý khi chọn
Buu cục.</p>
<p>Nếu không chọn bưu cục → không cho phép chọn  Nhân viên</p></td>
</tr>
<tr>
<td>5</td>
<td>Trạng thái</td>
<td>Dropdown list</td>
<td>Editable</td>
<td><p>Hiển thị danh sách trạng thái của đề xuất</p>
<ul>
<li><p>Chờ trình ký → TBC tạo đề xuất thành công và chờ trình ký
Voff</p></li>
<li><p>Chờ ký duyệt → đã trình ký voff và đang chờ kết quả trình
ký</p></li>
<li><p>Hủy → TBC đã hủy đề xuất</p></li>
<li><p>Từ chối → đề xuất đã bị từ chối Voff </p></li>
<li><p>Đã duyệt → Đề xuất đã được phê duyệt voff nhưng chưa đến thời
gian áp dụng</p></li>
<li><p>Đang sử dụng → Đề xuất đã được phê duyệt và đến thời gian áp
dụng</p></li>
<li><p>Hết hạn → là đề xuất đã hết hạn áp dụng</p></li>
</ul></td>
</tr>
<tr>
<td>6</td>
<td>Tìm kiếm</td>
<td>Button</td>
<td>Editable</td>
<td>Click Tìm kiếm đề lọc dữ liệu theo điều kiện tìm kiếm</td>
</tr>
<tr>
<td colspan="5"><strong>Dữ liệu chi tiết</strong></td>
</tr>
<tr>
<td>1</td>
<td>STT</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị STT → click vào dòng STT hiển thị danh sách đề xuất thuộc
bưu cục hiển thị</td>
</tr>
<tr>
<td>2</td>
<td>Chi nhánh</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị chi nhánh</td>
</tr>
<tr>
<td>3</td>
<td>Bưu cục</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tên bưu cục</td>
</tr>
<tr>
<td>4</td>
<td>Tài khoản đề xuất</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị tài khoản đề xuất (username)</td>
</tr>
<tr>
<td>5</td>
<td>Nhân viên đề xuất</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị  tên nhân viên  đề xuất</td>
</tr>
<tr>
<td>6</td>
<td>Loại đề xuất</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị  tên loại đề xuất</td>
</tr>
<tr>
<td>7</td>
<td>Hạn mức bưu cục cũ</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị hạn mức hiện tại của bưu cục</td>
</tr>
<tr>
<td>8</td>
<td>Hạn mức đề xuất bổ sung thêm</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị hạn mức bổ sung thêm</td>
</tr>
<tr>
<td>9</td>
<td>Áp dụng từ ngày</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị thời gian bắt đầu áp dụng </td>
</tr>
<tr>
<td>10</td>
<td>Áp dụng đến ngày</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị thời gian hết hạn</td>
</tr>
<tr>
<td>11</td>
<td>Lý do đề xuất</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị lý do đề xuất</td>
</tr>
<tr>
<td>12</td>
<td>Ghi chú</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị ghi chú theo lý do đề xuất</td>
</tr>
<tr>
<td>13</td>
<td>File đính kèm</td>
<td>Hyperlink</td>
<td>Editable</td>
<td>Hiển thị file đính kèm</td>
</tr>
<tr>
<td>14</td>
<td>Đối tượng phê duyệt</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị đối tượng phê duyệt cuối cùng theo luồng ký</td>
</tr>
<tr>
<td>15</td>
<td>Trạng thái</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị trạng thái của đề xuất </td>
</tr>
<tr>
<td>16</td>
<td>Lý do từ chối</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị lý do từ chối  trên Voff (Nếu lấy được)</td>
</tr>
<tr>
<td>17</td>
<td>File tờ trình</td>
<td>Hyperlink</td>
<td>Editable</td>
<td><p>Hiển thị tên file tờ trình đã ký trên voff. Hiển thì khi luồng ký
được phê duyệt ban hành.</p>
<p>Click Tên file cho phép tải về file</p></td>
</tr>
<tr>
<td>18</td>
<td>Thời gian đề xuất</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị thời gian tạo đề xuất thành công</td>
</tr>
<tr>
<td>19</td>
<td>Thời gian cập nhật</td>
<td>Text</td>
<td>Readonly</td>
<td>Hiển thị thời gian đề xuất được phê duyệt thành công. Ký duyệt ban
hành.</td>
</tr>
<tr>
<td>20</td>
<td>Thao tác</td>
<td>Text</td>
<td>Editable</td>
<td><p>Cho phép người dùng thao tác với các trạng thái.</p>
<ul>
<li><p>Sửa: cho phép sửa lại đề xuất với trạng thái chờ trình ký của
loại đề xuất Hạn mức công nợ, ko cho phép sửa với loại Hạn mức sản
lượng</p></li>
<li><p>Xóa: cho phép xóa đề xuất có các trạng thái Chờ trình ký, Đang sử
dụng → Cập nhật về trạng thái Hủy. TH với trạng thái Đang sử dụng khi
hủy sẽ trừ hạn  mức đã đề xuất.</p></li>
</ul></td>
</tr>
<tr>
<td>21</td>
<td>Đề xuất</td>
<td>Button</td>
<td>Editable</td>
<td>Click button đề xuất → Chuyển màn hình 3.8.2</td>
</tr>
</tbody>
</table> 

Nghiệp vụ chi tiết:

* Loại đề xuất Hạn mức công nợ:

  * User được phép trình ký nhiều đề xuất cùng loại và cùng luồng ký 

  * Sau khi ký duyệt thành công → Cộng hạn mức vào tổng hạn mức của bưu cục

  * TH đề xuất hết hạn → Cấp nhật về trạng thái Hết hạn → Cập nhật hạn mức phân bổ của tuyến = Hạn mức cố định của tuyến đó

  * TH hủy đề xuất Đang sử dụng → Cập nhật về trạng thái Hủy → Cập nhật hạn mức phân bổ của tuyến = Hạn mức cố định của tuyến đó


* Loại đề xuất Hạn mức Sản lượng:

  * User được phép trình ký nhiều đề xuất cùng loại và cùng luồng ký 

  * Sau khi ký duyệt thành công → Cộng hạn mức vào hạn mức của tuyến đề xuất

  * TH đề xuất hết hạn → Cấp nhật về trạng thái Hết hạn → Cập nhật hạn mức cố định của tuyến về hạn mức cố định ban đầu → cập nhật lại Hạn mức áp dụng cho các tuyến

  * TH hủy đề xuất Đang sử dụng → Cập nhật về trạng thái Hủy → Cập nhật hạn mức cố định của tuyến về hạn mức cố định ban đầu → cập nhật lại Hạn mức áp dụng cho các tuyến


### Màn hình thêm mới đề xuất 

|<image_8>|

Màn hình nếu chọn Hạn mức sản lượng

|<image_9>|

Mô tả Màn hình thêm mới đề xuất:
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
<th><strong>STT</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Control Type</strong></th>
<th><strong>Editable/ Readonly</strong></th>
<th><strong>Description/Note</strong></th>
</tr>
<tr>
<th>1</th>
<th>Loại đề xuất</th>
<th>Dropdown list</th>
<th>Editable</th>
<th><p>Hiển thị danh sách loại đề xuất cho người dùng chọn </p>
<ul>
<li><p>Loại đề xuất: Hiển thị theo phân quyền.</p></li>
</ul>
<blockquote>
<p>Giá trị hiển thị:</p>
<p>Hạn mức sản lượng: Hiển thị với tất cả các role kể cả TBC</p>
<p>Hạn mức công nợ: Chỉ hiển thị nếu là role TBC</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>Hạn mức đề xuất</td>
<td>Textbox</td>
<td>Editable</td>
<td><p>Cho phép người dùng nhập giá trị. Giá trị nhập là số nguyên dương
và lớn hơn mức cấu hình nhỏ nhất</p>
<p>Hower chuột vào icon |<image_10>| hiển thị tooltip: “Nhập mức tỷ
lệ lớn hơn 25%”</p>
<p>Sau khi nhập tỷ lệ Click Enter hoặc nhấp chuột Hệ thống tính giá trị
đề xuất thêm theo công thức:</p>
<p>Hạn mức đề xuất thêm = Hạn mức cố định * tỷ lệ đã nhập.</p></td>
</tr>
<tr>
<td>3</td>
<td>Lý do đề xuất </td>
<td>Dropdown list</td>
<td>Editable</td>
<td>Hiển thị danh sách lý do đề xuất (lấy theo cấu hình)</td>
</tr>
<tr>
<td>4</td>
<td>Người phê duyệt</td>
<td>Dropdown list</td>
<td>Editable</td>
<td><p>Hiển thị danh sách Chọn người duyệt cấp phê duyệt đầu tiên, lấy
danh sách theo cấu hình luồng ký.</p>
<p>Chỉ hiển thị nếu chọn loại đề xuất là Hạn mức sản lượng</p></td>
</tr>
<tr>
<td>5</td>
<td>Thời gian áp dụng</td>
<td>Calendar</td>
<td>Editable</td>
<td><p>Cho phép chọn thời gian áp dụng. chỉ cho phép chọn trong khoảng
thời gian 7 ngày</p>
<p>Giá trị mặc định: 7 ngày tính từ ngày hiện tại</p></td>
</tr>
<tr>
<td>6</td>
<td>File đính kèm</td>
<td>File</td>
<td>Editable</td>
<td>Cho phép import lên file đính kèm</td>
</tr>
<tr>
<td>7</td>
<td>Lưu </td>
<td>Button</td>
<td>Editable</td>
<td><p>Click Lưu để lưu cấu hình</p>
<p>Nguyên tắc lưu  cấu hình: tạo đề xuất thành công nếu đạt đủ các yêu
cầu sau:</p>
<ol>
<li><p>Bưu cục không tồn tại đề xuất có 1 trong các trạng thái trạng
thái Đang sử dụng, chờ trình ký, Đã duyệt, Chờ ký duyệt</p></li>
<li><p>Nếu tồn tại mục 1 thì check thời gian áp dụng ko trùng với khoảng
áp dụng của các đề xuất đã tồn tại với trạng thái Đang sử dụng, chờ
trình ký, Đã duyệt, Chờ ký duyệt</p></li>
</ol></td>
</tr>
<tr>
<td>8</td>
<td>Đóng</td>
<td>Button</td>
<td>Editable</td>
<td>Click Đóng để tắt popup cập nhật</td>
</tr>
</tbody>
</table> 

Nếu là đề xuất Hạn mức sản lượng→ cập nhật đề xuất trạng thái Chờ duyệt → TBC phê duyệt và trình ký

Nếu là đề xuất Hạn mức công nợ → Cập nhật đề xuất trạng thái Chờ trình ký → TBC thực hiện trình ký
<table style="width:100%;">
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
<th><strong>5.</strong></th>
<th>Thời gian cập nhật</th>
<th>Text</th>
<th>N/A</th>
<th>Readonly</th>
<th>Hiển thị thời gian cập nhật</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>6.</strong></td>
<td>Người cập nhật</td>
<td>Text</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị thông tin người cập nhật</td>
</tr>
<tr>
<td><strong>7.</strong></td>
<td>Thao tác</td>
<td>Button</td>
<td>N/A</td>
<td>Editable</td>
<td><p>Hiển thị icon cho người dùng chọn. Hiển thị tooltip tương ứng khi
hower icon:</p>
<p>- Sửa : Cho phép người dùng sửa cấu hình.</p>
<p>- Xem lịch sử: Cho phép người dùng xem lịch sử chỉnh sửa</p></td>
</tr>
<tr>
<td><strong>II.</strong></td>
<td colspan="5">Màn hình cập nhật cấu hình</td>
</tr>
<tr>
<td><strong>8</strong></td>
<td>Chọn Kỳ đánh giá</td>
<td>Texbox</td>
<td>Yes</td>
<td>Editable</td>
<td>Cho phép người dùng chọn số ngày. Giá trị nhập vào là số nguyên
dương lớn hơn hoặc = 0</td>
</tr>
<tr>
<td><strong>9</strong></td>
<td>Loại đánh giá</td>
<td>Dropdownlist</td>
<td>Yes</td>
<td>Editable</td>
<td><p>Cho phép người dùng chọn kỳ đánh giá:</p>
<p>Giá trị hiển thị:</p>
<p>- Không tính T7, CN</p>
<p>- Tính T7, CN</p>
<p>Giá trị mặc định: Không tính T7, CN</p></td>
</tr>
<tr>
<td><strong>10</strong></td>
<td>Trạng thái hoạt động</td>
<td>Button</td>
<td>N/A</td>
<td>Readonly</td>
<td><p>Cho phép người dùng on/off cấu hình. Áp dụng cho cấu hình mới
nhất.</p>
<p>Nếu cấu hình mới nhật = off tức là không có cấu hình kỳ đánh giá hạn
mức cố định = kỳ đánh giá gần nhất</p></td>
</tr>
<tr>
<td><strong>11</strong></td>
<td>Đóng</td>
<td>Button</td>
<td>N/A</td>
<td>Editable</td>
<td>Đóng yêu cầu chỉnh sửa cấu hình</td>
</tr>
<tr>
<td><strong>12</strong></td>
<td>Lưu</td>
<td>Button</td>
<td>N/A</td>
<td>Editable</td>
<td><p>Click Lưu để lưu thông tin cấu hình cảnh báo.</p>
<p>Cập nhật toàn bộ cấu hình cũ về trạng thái Không hoạt động.</p></td>
</tr>
<tr>
<td><strong>III.</strong></td>
<td colspan="5"><p>Lịch sử cập nhật cấu hình</p>
<p>Hiển thị danh sách lịch sử cấu hình</p></td>
</tr>
<tr>
<td><strong>13</strong></td>
<td>STT</td>
<td>Text</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị STT</td>
</tr>
<tr>
<td><strong>14</strong></td>
<td>Kỳ đánh giá</td>
<td>Text</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị kỳ đánh giá theo cấu hình</td>
</tr>
<tr>
<td><strong>15</strong></td>
<td>Loại đánh giá</td>
<td>Text</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị loại đánh giá theo cấu hình</td>
</tr>
<tr>
<td><strong>16</strong></td>
<td>Trạng thái hoạt động</td>
<td>Lable</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị trạng thái hoạt động của cấu hình</td>
</tr>
<tr>
<td><strong>17</strong></td>
<td>Thời gian cập nhật</td>
<td>Text</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị thời gian cập nhật</td>
</tr>
<tr>
<td><strong>18</strong></td>
<td>Người cập nhật</td>
<td>Text</td>
<td>N/A</td>
<td>Readonly</td>
<td>Hiển thị thông tin người cập nhật</td>
</tr>
</tbody>
</table>