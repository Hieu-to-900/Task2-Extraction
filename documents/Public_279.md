# Public_279

# Tổng quan

## Quy trình

|<image_1>|

|<image_2>|

## Mô tả

Tại bước 4 và 7, Fico check những điều kiện sau:
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Điều kiện check</th>
<th>Mô tả</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Kiểm tra trùng lặp</td>
<td>Đơn hàng đã được xử lý/phát hàng trước đó hay chưa?</td>
</tr>
<tr>
<td>2</td>
<td>Check tổng chi tiết mặt hàng của đơn = Tổng số lượng mặt hàng của
đơn hàng</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Check thông tin đơn hàng và chi tiết (tạm thời chưa che4ck)</td>
<td><p>Tổng SL mặt hàng trên đơn = Tổng dl chi tiết</p>
<p>Tổng tiền trước thuế trên đơn = Tổng tiền trước thuế chi tiết (loại
1+3+4+5+6)</p>
<p>Tổng thuế trên đơn = Tổng thuế chi tiết ((loại 1+3+4+5+6)</p>
<p>Tổng tiền sau thuế = Tổng tiền sau thuế chi tiết
((1+3+4+5+6))</p></td>
</tr>
<tr>
<td>4</td>
<td>Check tiên trên chi tiết mặt hàng (tạm thời chưa check)</td>
<td><p>Các bước check</p>
<p>1 – Tính từng loại tiền theo công thức dưới đây</p>
<p>2 – Làm tròn số tiền sau khi tính được theo cấu hình Vinvoice</p>
<p>3 – So sánh số tiền đã làm tròn với số hệ thống nguồn gửi sang</p>
<p>Tổng tiền trước thuế = Đơn giá * SL</p>
<p>Tiền thuế = Tiền trước thuế *% thuế</p>
<p>Tiền sau thế = Tiền trước thuế + Tiền thuế</p></td>
</tr>
<tr>
<td>5</td>
<td>Check tiền chiết khấu</td>
<td>Chiết khấu truyền sang như 1 mặt hàng, tính tiền như 1 mặt hàng</td>
</tr>
<tr>
<td>6</td>
<td>Check các trường bắt buộc theo API</td>
<td><p>Tiền hàng hóa: max 500</p>
<p>Mã hàng hóa: max 50</p>
<p>Tên đơn vị tính: max 300</p>
<p>Số lượng: sau dấu phẩy max 4 số, không nhận số âm</p></td>
</tr>
<tr>
<td>7</td>
<td>Check dữ liệu các đường truyền sang đúng số thập phân chưa?</td>
<td>Theo cấu hình Vinvoice yêu cầu</td>
</tr>
</tbody>
</table> 

## Danh sách tính năng

Danh sách tính năng và API

  * Danh sách API


\+ API tra cứu hóa đơn

\+ API gửi thông tin đơn hàng

\+ API Callback trả kết quả hóa đơn

\+ API đồng bộ thông tin khách hàng

  * Quản lý danh sách đơn hàng


# Sơ đồ trạng thái

|<image_3>|

Bảng mapping trạng thái
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
<th>TT FMCG Show cho user</th>
<th>Sub TT FMCG</th>
<th>Action</th>
<th>Fico</th>
<th>Action</th>
<th>Bảng kê hóa đơn</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chưa xuất HĐ</td>
<td>Chưa yc xuất HĐ</td>
<td>Sửa TT xuất HĐ/Đẩy lại</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chưa xuất HĐ</td>
<td>Lỗi TT xuất HĐ</td>
<td>Sửa TT xuất HĐ/Đẩy lại</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="4">Đang phát hành</td>
<td rowspan="4">Đang xuất HĐ</td>
<td rowspan="4">Tra cứu TT của HĐ</td>
<td rowspan="4">Đã gom bảng kê</td>
<td rowspan="4">Không</td>
<td>Tạo mới</td>
<td></td>
</tr>
<tr>
<td>Chốt bảng kê</td>
<td></td>
</tr>
<tr>
<td>Chờ phát hành</td>
<td></td>
</tr>
<tr>
<td>Đã phát hành</td>
<td></td>
</tr>
<tr>
<td>Đã xuất HĐ</td>
<td>Đã xuất HĐ</td>
<td>Gửi lại HĐ cho khách</td>
<td>Đã xuất HĐ</td>
<td></td>
<td>Đã phát hành</td>
<td></td>
</tr>
<tr>
<td>Xuất HĐ thất bại</td>
<td>Xuất HĐ thất bại</td>
<td>Sửa lại TT xuất HĐ/Đẩy lại</td>
<td>Xuất HĐ thất bại</td>
<td></td>
<td>Lỗi xuất HĐ</td>
<td>Gỡ bill bảng kê, sửa thông tin</td>
</tr>
</tbody>
</table>