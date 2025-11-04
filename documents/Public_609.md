# Public_609

# YÊU CẦU ĐẶT RA

\- Đáp ứng việc quản lý máychủ và các ứng dụng một cách có hiệu quả, kinhtế hơn, cải thiệntính bảo mật và tính tuân thủ, mang lại sự linh hoạt và nhanh gọn cần thiết để thúc đẩy hiệu năng công việc. - Đơn giản hóa và hợp lý hóa việc quản lý các trang thiết bị phần cứng để giúp kiểm soát chip hí, tăng cường bảo mật và cải thiện khả năng linh hoạt của hệ thống với giải pháp tối ưu hóa hạ tầng CNTT.

\- Quản lý hiệu quả các máychủ ảo và máy chủ vật lý, làm giảm đi sự phức tạp của hệ thống, cải thiện hiệu quả hoạt động, giúp quản lý chi phí, và tăng khả năng thích nghi của hệ thống đối với các yêu cầu công việc luôn thay đổi.

# GIẢI PHÁP VÀ MÔ HÌNH ỨNG DỤNG

##  Giải pháp đề xuất

Xây dựng một hệ thống mạng ảo hóa máy chủ và trung tâm dữ liệu (Datacenter –Server Virtualization) với công nghệ ảo hóa của Vmware, bao gồm:

  * Hợp nhất các máy chủ: tổng hợp nhiều máy chủ thành một nguồn tài nguyên hợp nhất và duy nhất.

  * Hợp nhất hệ thống lưu trữ: Toàn bộ hệ thống lưu trữ của công ty có thể bao gồm nhiều thiết bị vật lý khác nhau, được ảo hóa thành một nguồn lưu trữ chung duy nhất từ góc nhìn của các máy chủ, ứng dụng trong hệ thống. Việc chia sẻ và phân chia nguồn lưu trữ này được quản lý tập trung.

  * Ảo hóa kết nối mạng: ảo hóa các đường kết nối mạng, tạo ra một nguồn chung gồm các kết nối mạng có thể được gán một cách linh hoạt cho các máy tính, máy chủ và các thiết bị trong mạng mà không cần phải thay đổi các kết nối vật lý


## Mục tiêu Ảo hóa toàn bộ hệ thống máy chủ và ứng dụng để loại trừ: 

\- Thời gian trì trệ đầu tư thiết bị máy chủ mới khi triển khai một ứng dụng mới.

\- Thời gian chết (downtime) khi bảo trì hay nâng cấp phần cứng cho hệ thống máy chủ.

\- Tiết giảm không gian của phòng máy chủ, độ phức tạp của hệ thống cáp kết nối và chi phí hàng ngày cho hệ thống điện và làm mát.

\- Khai thác triệt để hiệu năng cũng như công năng của công nghệ và sức mạnh phần cứng máy chủ hiện nay.

\- Quản lý tập trung tại một điểm duy nhất và giảm thiểu các thao tác quản trị.

\- Dễ dàng và linh động triển khai các yêu cầu kinh doanh mới ngay lập tức và sao lưu dự phòng toàn bộ hệ thống.

## Mô hình cơ sở hạ tầng mạng ban đầu 

Giả sử công ty đang có cơ sở hạ tầng mạng ban đầu chưa áp dụng công nghệ ảo hóa như hình 6

|<image_1>|

Theo Hình 6, các server là các server vật lý và để tránh tình trạng xung đột giữa các dịch vụ, mỗi dịch vụ sẽ chạy trên một server vật lý riêng biệt (không tận dụng hết tài nguyên máy vật lý). Khi có sự cố xảy ra máy chủ vật lý sẽ ngưng hoạt động. Giải pháp khắc phục vấn đề này là cấp thêm server dự phòng cho mỗi dịch vụ, và như thế sẽ tạo ra sự phức tạp trong quản lý và chi phí đầu tư tốn kém.

## Mô hình cơ sở hạ tầng mạng ứng dụng công nghệ ảo hóa

|<image_2>|

Theo Hình 7, công ty xây dựng lại cơ sở hạ tầng CNTT bằng cách ứng dụng công nghệ ảo hóa, sử dụng phần mềm ảo hóa VmwareVsphere. Trong mô hình này có nhiều server ảo, thu hẹp số lượng server vật lý đáng kể, giảm chi phí đầu tư thiết bị kết nối mạng, giảm chi phí bảo trì bảo dưỡng, năng lượng, làm mát và các nguồn. tài nguyên khác có liên quan. Khi server vật lý này gặp sự cố, server ảo sẽ tự động được chuyển sang server vật lý khác mà không xuất hiện thời gian chết, tránh làm gián đoạn hệ thống, giúp doanh nghiệp tiết kiệm được chi phí, công tác quản lý đồng thời việc sao lưu dự phòng đơn giản và nhanh chóng hơn.

## Phần mềm và thiết bị cần thiết cho triển khai hệ thống 

Phần mềm: Sau đây liệt kê một số phần mềm

_Bảng 1: Phần mềm cần thiết cho triển khai hệ thống_
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>STT</strong></th>
<th><strong>Tên phần mềm</strong></th>
<th><strong>Bản quyền</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>OpenFiler OS</td>
<td>Miễn phí</td>
</tr>
<tr>
<td>2</td>
<td>Vmware Hypervisor ESXi</td>
<td rowspan="4">Có</td>
</tr>
<tr>
<td>3</td>
<td>Vmware vSphere Server</td>
</tr>
<tr>
<td>4</td>
<td>Vsphere Client</td>
</tr>
<tr>
<td>5</td>
<td>Windows Server 2008 r2</td>
</tr>
</tbody>
</table> 

Thiết bị:

\- Cần 2 máy chủ làm host ESXi Server, cấu hình tối thiểu của máy chủ như sau:

CPU

_Bảng 2: Cấu hình tối thiểu máy chủ Host ESXi_
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Thành phần</th>
<th>Mô tả kỹ thuật</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CPU</td>
<td>CPU 64bit x86, hỗ trợ công nghệ ảo hóa Intel VT-x hoặc AMD RVI</td>
</tr>
<tr>
<td>2</td>
<td>RAM</td>
<td>2 GB</td>
</tr>
<tr>
<td>3</td>
<td>HDD</td>
<td>120 GB</td>
</tr>
<tr>
<td rowspan="3">4</td>
<td>RAID Controller</td>
<td rowspan="3">Có</td>
</tr>
<tr>
<td>SCSI</td>
</tr>
<tr>
<td>SATA</td>
</tr>
<tr>
<td>5</td>
<td>Network Interface</td>
<td>Tối thiểu 1</td>
</tr>
</tbody>
</table> 

\- Cần 1 máy chủ vCenter Server, cấu hình tối thiểu như sau:

_Bảng 3: Cấu hình tối thiểu máy vCenter Server_
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Thành phần</th>
<th>Mô tả kỹ thuật</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CPU</td>
<td>CPU 64 bit</td>
</tr>
<tr>
<td>2</td>
<td>RAM</td>
<td>2 GB</td>
</tr>
<tr>
<td>3</td>
<td>HDD</td>
<td>120 GB</td>
</tr>
<tr>
<td>5</td>
<td>Network Interface</td>
<td>Tối thiểu a</td>
</tr>
</tbody>
</table> 

\- Cần 1 máy giả lập SAN cho hệ thống ảo hóa, cấu hình tối thiểu như sau:

_Bảng 4: Cấu hình tối thiểu máy chủ SAN_
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>STT</th>
<th>Thành phần</th>
<th>Mô tả kỹ thuật</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CPU</td>
<td>CPU 32/64 bit</td>
</tr>
<tr>
<td>2</td>
<td>RAM</td>
<td>2 GB</td>
</tr>
<tr>
<td>3</td>
<td>HDD</td>
<td>80 GB</td>
</tr>
<tr>
<td>5</td>
<td>Network Interface</td>
<td>Tối thiểu 1</td>
</tr>
</tbody>
</table> 

## Các bước triển khai hệ thống

Tiến hành cài đặt hệ thống theo trình tự các bước sau:

Bước 1: Cài đặt Vmware ESXi lần lượt cho2 server ESXi. Đây là 2 host server chạy song songvới nhau, vận hành các máy ảo và khi host này ngưng hoạt động thì host kia sẽ tự động thay thế.

Bước 2: Cài đặt vCenter Server. Đây là máy chủ trung tâm quản lý toàn bộ hệ thống ảo hóa. Các dịch vụ chạy trên máy vCenter Server gồm có: Vsphere Web Client, vCenter Server, vCenter Update Manager.

Bước 3: Cài đặt SAN Server. Đây là máy chủ giả lập hệ thống lưu trữ SANs được dung để hỗ trợ cho các chức năng nâng cao của hệ thống ảo hóa. SAN server chạy hệ điều hành OpenFiler (có thể dùng các ứng dụng khác để giả lập SAN Server).

Bước 4: Cài đặt máy vSphere Client. Đây là một máy client bình thường sử dụng phần mềm vSphere Client dùng kết kết nối vào vCenter Server hoặc host để quản lý.

Bước 5: Dùng vSphere Client kết nối vào vCenter Server sau đó thực hiện cấuhình. Tiến trình cấu hình hệ thống bao gồm các thao tác sau:

\- Liên kết máy ESXi vào vCenter Server(Add host)

\- Tạo Cluster

\- Đưa host vào trong Cluster

\- Kết nối SAN vào hệ thống –

Tạo máy ảo trên máy chủ ESXi

\- Thực hiện kỹ thuật di chuyển máy ảo giữa các host và Datastore

\- Cấu hình Vmware DRS

\- Cấu hình Vmware HA

\- Thực hiện kỹ thuật sử dụngSnapshot

\- Tạo và cấu hình vNetwork Distributed Switch

#  MÔ HÌNH TRIỂN KHAI HỆ THỐNG

|<image_3>|

Hình 8: Mô hình demo Vmware Vsphere

Để đơn giản quá trình cài đặt, bài báo đưa ra mô hình cài đặt đơn giản và có tính demo như Hình 8, không trình bày chi tiết quá trình cài đặt.

Các thành phần sử dụng trong Hình 8 bao gồm

: - Hệ thống máy chủ host (dùng máy ảo giả lập máy vật lý ESXi Server), số lượng: 2

\- Máy chủ vCenter (dùng máy ảo giả lập máy vật lý), số lượng: 1

\- Máy chủ SAN Storage (dùng máy ảo giả lập máy vật lý), số lượng: 1

\- Máy dùng làm Vsphere Client (dùng máy ảo giả lập máy vật lý), số lượng: 1 - Phần mềm sử dụng:

\+ Microsoft Windows Server 2008 R2.

\+ Vmware Vsphere (Vmware Hypervisor ESXi, Vmware Vsphere)

\+ Openfile OS.

# TRIỂN KHAI HỆ THỐNG 

Các bước chính trong quá trình triển khai như sau:

Bước 1: Quản lý ESXi Server với VM vSphere client

  * Liên kết máy ESXi vào vCenter Server (Add Host)

  * Tạo Cluster

  * Đưa host vào trong cluster

  * Sử dụng vSphere Client


Bước 2: Kết nối SAN vào hệ thống (Add Networking và Add Storage)

Bước 3: Tạo máy ảo trên máy chủ ESXi

Bước 4: Di chuyển máy ảo giữa các Host và Datastore

\- Di chuyển máy ảo đã tắt nguồn

\- Di chuyển máy ảo đang chạy bằng StoragevMotion

\- Di chuyển máy ảo đang chạybằngvMotion

Bước 5: Thực hiện Vmware DRS(Distributed Resource Scheduler)

Bước 6: Thực hiện Vmware HA(HighAvailability)

Bước 7: Sử dụng Snapshot

Bước 8: Tạo và sử dụng vDS(vNetworkDistributed Switch)