# Public_618

# GIỚI THIỆU CHUNG

Vina Virtual Private Cloud (vVPC) là dịch vụ đám mây riêng ảo trên nền tảng Điện toán đám mây công cộng (Public Cloud) của Vina IDC. Vina Virtual Private Cloud cung cấp trọn gói phân vùng tài nguyên tính toán, lưu trữ riêng trong dải mạng ảo được tách biệt logic với các khách hàng khác, sử dụng công nghệ mạng định nghĩa bằng phần mềm (Software Defined Networking).

Khách hàng toàn quyền kiểm soát môi trường mạng ảo, bao gồm chủ động khởi tạo máy chủ ảo; và thiết lập và cấu hình hệ thống công nghệ thông tin như 1 trung tâm dữ liệu ảo (Virtual Data Center).

|<image_1>|

# TÍNH NĂNG CHÍNH

## Thiết lập trung tâm dữ liệu ảo bảo mật

Dịch vụ được cung cấp dưới dạng vùng tài nguyên (Resource Pool) đầy đủ 3 thành phần:

  * Hệ thống mạng (Network): các thiết bị ảo hóa mạng cơ bản.


  * Virtual private network: mạng ảo được cung cấp dưới hình thức 1 dải CIDR IP Private.

  * Subnet: các mạng con được tạo trong Virtual Private network để phân vùng máy chủ ảo.

  * Router: thiết bị ảo định tuyến các subnet.

  * Elastic IP: IPv4 Public để gán vào máy chủ ảo giúp truy cập ra Internet trực tiếp.

  * Security Group: Tập quy tắc kiểm soát truy cập vào/ra cho máy chủ ảo.


  * Lớp xử lý tính toán (Compute): CPU/RAM được cung cấp dưới dạng tài nguyên sẵn sàng để khởi tạo máy chủ ảo.

  * Dung lượng lưu trữ (Storage): Lưu trữ SSD được cung cấp thông qua Block Storage Volume đảm bảo IOPS ổn định, độ trễ thấp.


Các tính năng giúp khách hàng cấu hình khả năng kết nối bảo mật mà ứng dụng yêu cầu

## Mở rộng trung tâm dữ liệu ảo linh hoạt

  * Mở rộng vùng tài nguyên (Resource Pool) nhanh chóng, không giới hạn, theo block (vCPU, GB, Storage).

  * Hỗ trợ tính năng tăng nóng (hot-add) CPU, RAM và mở rộng nóng (hot-extend) ổ đĩa cho máy chủ ảo, không gây gián đoạn dịch vụ trên máy ảo.

  * Tự động thêm / xóa máy chủ ảo dựa trên kịch bản cấu hình có sẵn thông qua tính năng Autoscale, đảm bảo mức độ sẵn sàng của ứng dụng khi lưu lượng truy cập tăng đột biến.

  * Nâng cấp hiệu suất, tăng cường bảo mật hệ thống bằng việc bổ sung subnet, vLoad Balancer, Firewall Layer 4.


  * Cân bằng tải (Load Balancing): Cân bằng tải Lớp 4-Lớp 7 hỗ trợ cơ chế SSL offload, pass-through và health checks.

  * Tường lửa (Firewall): tường lửa dạng stateful phân phối trên toàn bộ môi trường với chính sách và quản lý tập trung, cho phép kiểm soát lưu lượng theo mô hình mạng North-South.

  * Mạng riêng ảo (VPN): hỗ trợ IPSec VPN (site to site) và SSL VPN (client to site).


## Khả năng khởi tạo dịch vụ nhanh chóng

  * Tùy chọn khởi tạo trên 2 vùng địa lý, hạ tầng dịch vụ đặt tại Trung tâm dữ liệu Vina được thiết kế đảm bảo cam kết Uptime 99,99%.

  * Khách hàng chủ động tùy chỉnh số lượng tài nguyên (CPU, RAM, Storage và Network) theo định cỡ cần thiết của hệ thống ứng dụng

  * Lựa chọn Hệ điều hành theo mẫu cấu hình sẵn (OS image) phổ biến, được cập nhật version mới nhất.

  * Đăng ký dịch vụ dưới hình thức cam kết theo tháng hoặc dùng trước trả sau tính theo tài nguyên sử dụng (Pay as you Go).


## Giao diện Web portal quản trị thân thiện

  * Giao diện hỗ trợ đa hình thức thanh toán (chuyển khoản hoặc online); gia hạn, mua bổ sung tài nguyên cho dịch vụ.

  * Cung cấp giao diện Console hỗ trợ truy cập từ xa vào các máy ảo.

  * Chủ động thiết lập, cấu hình sơ đồ mạng ảo của hệ thống: Phân chia zone (DMZ, APP, DB..), IP/Subnet…

  * Quản lý các chức năng thiết bị mạng ảo (Virtual Firewall, Virtual Load Balancer).

  * Khởi tạo, quản lý các bản cấu hình Auto scale group để tự động điều chỉnh số lượng VM theo hiệu suất sử dụng CPU/RAM của nhóm máy chủ ảo chạy service.

  * Khách hàng tự thực hiện các tính năng như bật/ tắt/ khởi động lại máy chủ ảo trực tiếp.

  * Cung cấp giao diện giám sát hiệu suất sử dụng tài nguyên: RAM/CPU/IOPS/Bandwidth của từng máy chủ ảo.

  * Hỗ trợ quản lý và phân quyền truy cập cho các người dùng khác quản trị dịch vụ (IAM).


## Giải pháp SDN mạnh mẽ

  * Chuyển mạch (Switching): Cho phép triển khai các mạng logical Layer 2 và khả năng kết nối mở rộng lên thiết bị định tuyến (vRouter, vFirewall) để kết nối liên vùng, liên Trung tâm dữ liệu.

  * Định tuyến (Routing): hỗ trợ định tuyến tĩnh và các giao thực định tuyến động (OSPF, BGP) bao gồm cả IPv6.


## Dịch vụ Giá trị gia tăng

  * Dịch vụ Sao lưu và phục hồi dữ liệu (Backup & Restore): tạo các bản backup thủ công hoặc theo lịch có sẵn.

  * Vina Hybrid Connect L2: Dịch vụ kết nối liên mạng thông qua các kết nối WAN, MPLS, Dark Fibre… đến hạ tầng on-premise hoặc các đám mây của nhà cung cấp khác.

  * Vina File Storage: Lưu trữ File Storage không giới hạn dung lượng, hỗ trợ các giao thức NFS v3.0/4.0 và SMB/CIFS 2.0

  * Các dịch vụ bảo mật, an toàn thông tin nâng cao:


  * Vina Cloud Firewall: Tường lửa thế hệ mới (Next Generation Firewal) của các hang hàng đầu (Palo Alto Networks, Fortinet…) kiểm soát sâu gói tin ở mức ứng dụng với các tính năng phân tích, signature matching, IPS/IDS, antivirus…

  * WAF: Tường lửa ứng dụng web với khả năng ngăn chặn các cuộc tấn công lớp 7: Cross-site Scripting (XSS), SQL Injection… Giám sát và phát hiện các cuộc tấn công trong trong thời gian thực.

  * AntiDDoS L4: ngăn chặn các cuộc tấn công lớp 4 dạng volume based băng thông lớn: UDP & TCP Flood, SYN Flood, Volume-based, regardless of protocols…


  * Vina Database Service: cung cấp dịch vụ cơ sở dữ liệu trên nền tảng cloud, giúp tự động hóa các tác vụ quản trị tốn nhiều thời gian như cung cấp phần cứng, thiết lập cơ sở dữ liệu, vá lỗi và sao lưu.


  * Vina Open Kubernetes Service: cung cấp dịch vụ lớp nền tảng (Platform as a Service), giúp khách hàng triển khai ứng dụng phần mềm theo kiến trúc Microservice, triển khai CI/CD trên nền tảng Kubernetes


# SO SÁNH TÍNH NĂNG CÁC DÒNG SẢN PHẨM CLOUD COMPUTE
<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>IaaS</strong></p>
<p><strong>Tiêu chí</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Vina Cloud Server</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Vina Virtual Private Cloud</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p><strong>Khu vực</strong></p>
</blockquote></td>
<td><blockquote>
<p>Pháp Vân / Bình Dương</p>
</blockquote></td>
<td><blockquote>
<p>Pháp Vân / Bình Dương</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Mô hình triển</strong></p>
<p><strong>khai</strong></p>
</blockquote></td>
<td><blockquote>
<p>Public Cloud</p>
</blockquote></td>
<td><blockquote>
<p>Public Cloud</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Hình thức cung cấp</strong></p>
</blockquote></td>
<td><blockquote>
<p>Máy chủ ảo (VM)</p>
</blockquote></td>
<td><blockquote>
<p>Cụm tài nguyên (Resource pool)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Kịch bản sử dụng</strong></p>
</blockquote></td>
<td><blockquote>
<p>Website tĩnh, Blog, môi trường Dev/Test, trang giới thiệu dịch
vụ…</p>
</blockquote></td>
<td><blockquote>
<p>Complex Website, Database Cluster, phần mềm doanh nghiệp, hệ thống
ERP, CRM…, Hybrid Cloud</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p><strong>Uptime</strong></p>
</blockquote></td>
<td><blockquote>
<p>99,99%</p>
</blockquote></td>
<td><blockquote>
<p>~95%</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="16"><blockquote>
<p><strong>Tính năng mặc định</strong></p>
</blockquote></td>
<td><blockquote>
<p>Giao diện quản trị Website</p>
</blockquote></td>
<td><blockquote>
<p>Giao diện quản trị Website</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Start/stop/restart VM</p>
</blockquote></td>
<td><blockquote>
<p>Tự khởi tạo VM</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Giám sát hiệu năng VM (biểu đồ)</p>
</blockquote></td>
<td><blockquote>
<p>Không giới hạn số lượng VM khởi tạo</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Operation System Image</p>
</blockquote></td>
<td><blockquote>
<p>Tăng / giảm cấu hình VM</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Xác thực &amp; Phân quyền (IAM)</p>
</blockquote></td>
<td><blockquote>
<p>Start/stop/restart VM</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>IP Public</p>
</blockquote></td>
<td><blockquote>
<p>Quản trị Card mạng VM (network Interface)</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>Pay as you Go</p>
</blockquote></td>
<td><blockquote>
<p>Giám sát hiệu năng VM (biểu đồ)</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Operation System Image</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Xác thực &amp; Phân quyền (IAM)</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Elastic IP</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Quản trị Volume Block Storage</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Khởi tạo / sửa / xóa mạng riêng ảo (Subnet)</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Kiểm soát lưu lượng truy cập VM (Security Group)</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>NAT Gateway</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Auto Scale</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Pay as you Go</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="6"><blockquote>
<p><strong>Tính năng trả</strong></p>
<p><strong>phí</strong></p>
</blockquote></td>
<td><blockquote>
<p>Subnet</p>
</blockquote></td>
<td><blockquote>
<p>vLoad Balancer</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>vLoad Balancer</p>
</blockquote></td>
<td><blockquote>
<p>vFirewall</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>vFirewall</p>
</blockquote></td>
<td><blockquote>
<p>VPN Site to Site</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>VPN Site to Site</p>
</blockquote></td>
<td><blockquote>
<p>VPN Client to Site</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>VPN Client to Site</p>
</blockquote></td>
<td><blockquote>
<p>VPC Peering</p>
</blockquote></td>
</tr>
<tr>
<td></td>
<td><blockquote>
<p>Infrastructure as code</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="10"><blockquote>
<p><strong>Dịch vụ kết nối</strong></p>
</blockquote></td>
<td colspan="2">Vina Cloud Backup</td>
</tr>
<tr>
<td colspan="2">Vina Cloud Firewall</td>
</tr>
<tr>
<td colspan="2">Vina Cloud Disaster Recovery</td>
</tr>
<tr>
<td colspan="2">Vina Database Service</td>
</tr>
<tr>
<td colspan="2">Vina Hybrid Connect</td>
</tr>
<tr>
<td colspan="2">Vina Cloud File Storage</td>
</tr>
<tr>
<td colspan="2">Vina Cloud Object Storage</td>
</tr>
<tr>
<td colspan="2">Vina Open Kubernetes Service</td>
</tr>
<tr>
<td colspan="2">Vina Container Registry</td>
</tr>
<tr>
<td colspan="2">Vina Cloudrity (WAF, AntiDDoS)</td>
</tr>
</tbody>
</table>