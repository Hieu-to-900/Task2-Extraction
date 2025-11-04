# Public_272

# Các nhóm kiểm soát

Trong an toàn thông tin, các biện pháp kiểm soát ( controls ) được chia thành ba nhóm chính:

  * Kiểm soát hành chính/Quản lý (Administrative/Managerial controls)

  * Kiểm soát kỹ thuật (Technical controls)

  * Kiểm soát vật lý/Vận hành (Physical/Operational controls)


## Kiểm soát hành chính/Quản lý

Nhóm này xử lý yếu tố con người trong an toàn thông tin. Bao gồm chính sách và quy trình quy định cách tổ chức quản lý dữ liệu, cũng như trách nhiệm của nhân viên trong việc bảo vệ tổ chức.  
Mặc dù chủ yếu dựa trên chính sách, nhưng việc thực thi có thể cần sử dụng thêm kiểm soát kỹ thuật hoặc vật lý.

## Kiểm soát kỹ thuật

Bao gồm các giải pháp như firewall, intrusion detection systems (IDS), intrusion prevention systems (IPS), antivirus (AV), encryption... Các kiểm soát này giúp tổ chức đạt được mục tiêu bảo mật.

## Kiểm soát vật lý/Vận hành

Bao gồm khóa cửa, khóa tủ, camera giám sát, thiết bị quẹt thẻ,... nhằm hạn chế quyền truy cập vật lý vào tài sản khỏi những người không có thẩm quyền.

# Các loại kiểm soát

Các loại kiểm soát bao gồm (nhưng không giới hạn):

  * Ngăn chặn (Preventative)

  * Khắc phục (Corrective)

  * Phát hiện (Detective)

  * Răn đe (Deterrent)


Các kiểm soát này kết hợp với nhau tạo thành defense in depth để bảo vệ tài sản.

  * Preventative : ngăn chặn sự cố xảy ra ngay từ đầu.

  * Corrective : khôi phục sau sự cố.

  * Detective : phát hiện sự cố đang xảy ra hoặc đã xảy ra.

  * Deterrent : răn đe, làm nản lòng kẻ tấn công.


## Administrative/Managerial Controls
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Control Name</strong></td>
<td><strong>Control Type</strong></td>
<td><strong>Control Purpose</strong></td>
</tr>
<tr>
<td>Least Privilege</td>
<td>Ngăn chặn</td>
<td>Giảm rủi ro và tác động từ insider hoặc tài khoản bị chiếm đoạt</td>
</tr>
<tr>
<td>Disaster recovery plans</td>
<td>Khắc phục</td>
<td>Đảm bảo tính liên tục trong kinh doanh</td>
</tr>
<tr>
<td>Password policies</td>
<td>Ngăn chặn</td>
<td>Giảm khả năng bị brute force hoặc dictionary attack</td>
</tr>
<tr>
<td>Access control policies</td>
<td>Ngăn chặn</td>
<td>Tăng cường tính bảo mật bằng cách quy định nhóm được truy cập/chỉnh
sửa dữ liệu</td>
</tr>
<tr>
<td>Account management policies</td>
<td>Ngăn chặn</td>
<td>Quản lý vòng đời tài khoản, giảm bề mặt tấn công, hạn chế nguy cơ từ
nhân viên cũ hoặc tài khoản mặc định</td>
</tr>
<tr>
<td>Separation of duties</td>
<td>Preventative</td>
<td>Giảm rủi ro và tác động từ insider hoặc tài khoản bị chiếm đoạt</td>
</tr>
</tbody>
</table> 

## Kiểm soát kỹ thuật
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Tên kiểm soát</strong></td>
<td>Loại kiểm soát</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Mục đích</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Firewall</td>
<td>Ngăn chăn</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Lọc bỏ traffic độc hại hoặc không mong muốn</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>IDS/IPS</td>
<td>Phát hiện</td>
<td>Phát hiện và ngăn chặn traffic bất thường khớp với
signature/rule</td>
</tr>
<tr>
<td>Encryption</td>
<td>Răn đe</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Bảo mật thông tin nhạy cảm</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Backups</td>
<td>Khắc phụctive</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Khôi phục dữ liệu sau sự cố</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Password management</td>
<td>Ngăn chặn</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Giảm tình trạng mệt mỏi mật khẩu</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Antivirus (AV) software</td>
<td>Ngăn chặn</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Quét, phát hiện và cách ly mối đe dọa đã biết</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Manual monitoring, maintenance, and intervention</td>
<td>Ngăn chặn</td>
<td>Quản lý mối đe dọa, rủi ro từ hệ thống lỗi thời</td>
</tr>
</tbody>
</table> 

## Kiểm soát vật lý/Vận hành
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Tên kiểm soát</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Loại kiểm soát</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Mục đích</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Time-controlled safe</td>
<td>Răn đe</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Giảm nguy cơ từ đe dọa vật lý</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Adequate lighting</td>
<td>Răn đe</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Hạn chế nơi ẩn nấp, giảm nguy cơ tấn công</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Closed-circuit television (CCTV)</td>
<td>Ngăn chặn/phát hiện</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Ngăn ngừa sự cố và hỗ trợ điều tra sau khi sự cố xảy ra</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Locking cabinets (for network gear)</td>
<td>Ngăn chặn</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Ngăn truy cập trái phép vào thiết bị mạng</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Signage indicating alarm service provider</td>
<td>Răn đe</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Giảm khả năng tấn công thành công</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Locks</td>
<td>Răn đe/ngăn chặn</td>
<td><table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Ngăn truy cập trái phép vào tài sản</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
</tbody>
</table></td>
</tr>
<tr>
<td>Fire detection and prevention (fire alarm, sprinkler system,
etc.)</td>
<td>Phát hiện/ Ngăn chặn</td>
<td>Phát hiện cháy và giảm thiệt hại tài sản</td>
</tr>
</tbody>
</table>