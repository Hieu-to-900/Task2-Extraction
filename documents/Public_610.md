# Public_610

#  Bảo trì bảo dưỡng thiết bị

## Lên lịch rà soát, bảo dưỡng thiết bị mạng

  * Bảo dưỡng thiết bị theo tháng


  * Tần suất: 1 lần/tháng.

  * Nội dung thực hiện: Rà soát và xóa các cảnh báo lỗi tồn, khai báo rác.

  * Backup dữ liệu hệ thống (database/ file cấu hình) ra server ngoài và ra đĩa quang hoặc USB nếu có.

  * Với thiết bị tại tổng trạm khu vực/ quốc gia: vệ sinh tại nơi đặt thiết bị và quanh khu vực đặt thiết bị, trên sàn và dưới sàn phòng máy tổng trạm khu vực/quốc gia.


  * Bảo dưỡng thiết bị theo quý.


  * Tần suất: 1 lần/quý/3 tháng

  * Rà soát và xóa các logfile, file database cũ, các file rác trên thiết bị lưu trữ.

  * Cập nhật thời gian hệ thống, trạng thái đồng bộ (nếu có sai khác).

  * Với thiết bị tại tổng trạm khu vực/quốc gia: kiểm tra và siết lại các cáp kết nối (nguồn/ tín hiệu/ nối đất/...), bulong, ốc-vít bị hỏng,... đảm bảo chắc chắn; bó buộc các loại cáp (nguồn, tín hiệu) nếu đang không gọn gàng.


  * Bảo dưỡng thiết bị theo 06 tháng


  * Tần suất: 6 tháng/lần

  * Audit các hệ thống thuộc lớp mạng lõi, hội tụ và cập nhật tham số theo bộ tham số chuẩn (nếu có sai khác)

  * Switchover các cặp thiết bị có dự phòng active/standby:


\+ Các cặp card/module điều khiển, chuyển mạch active/standby thuộc các thiết bị chuyển mạch, định tuyến trung tâm của mạng (các thiết bị lớp Core và Distribute)

\+ Trong trường hợp 6 tháng đã có tác động dẫn đến switchover cho thiết bị active/standby thì coi như đã thực hiện switchover đinh kỳ, và tính chu kỳ mới bắt đầu từ thời điểm switchover thiết bị lần trước đó.

  * Bảo dưỡng thiết bị theo năm


  * Tần suất: 1 lần/năm.

  * Switchover các phần tử kết nối có dự phòng active/standby standby:


\+ Thiết bị mạng: switchover các cặp node active/standby trên mạng.

\+ Trường hợp trong 1 năm đã có tác động dẫn đến switchover cho các node active/standby thì coi như đã thực hiện switchover định kỳ, và tính chu kỳ mới bắt đầu từ thời điểm switchover node.

## Hướng dẫn switchover thiết bị mạng
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
<th>Loại thiết bị</th>
<th>Hãng</th>
<th>Lớp thiết bị</th>
<th>Các bước thực hiện</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">1</td>
<td rowspan="4">N9K</td>
<td rowspan="4">Cisco</td>
<td rowspan="4">Core</td>
<td><ol>
<li><p>Backup cấu hình thiết bị trước khi thực hiện</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Log vào thiết bị kiểm tra trang thái hoat động của card SUP
(SUPERVISOR), xem card SUP nào đang là active, card SUP nào đang là
standby show mô-đun</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Thực hiện lấy thông tin route, trạng thái các phiên BGP và OSPF
để so sánh sau khi thực hiện switchover</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Đứng trên thiết bị đang có card SUP ở trạng thái active, thực
hiện switchover sang card SUP standy làm active</p></li>
</ol>
<ul>
<li><p>Ngắt nguồn card SUP active để switchover sang card SUP standby để
card standby chuyển sang trạng thái Sactive.</p></li>
</ul>
<p>#poweroff module "số lượng module đang hoạt động"</p>
<ul>
<li><p>Card SUP standby chuyển lên làm active, thực hiện show module để
kiểm tra lại.</p></li>
<li><p>Cấp nguồn lại cho card Standby vừa ngắt để làm dự phòng.</p></li>
</ul></td>
</tr>
<tr>
<td rowspan="4">2</td>
<td rowspan="4">NCS560</td>
<td rowspan="4">Cisco</td>
<td rowspan="4">Core</td>
<td><ol>
<li><p>1. Backup cấu hình thiết bị trước khi thực hiên</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Login vào thiết bị kiểm tra trạng thái hoạt động và xem card RP
(route processor) nào đang là active, RP nào đang là standby. Hiển thị
ngay khi login vào thiết bị #show platform</p></li>
</ol>
<p>#show redundancy</p>
<p>Để lấy thông tin RP active-standby chi tiết trên cặp thiết bị
switchover</p></td>
</tr>
<tr>
<td><ol>
<li><p>Thực hiện lấy thông tin route, trạng thái các phiên BGP và OSPF
để so sánh sau khi thực hiện switchover</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Xác định được RP nào đang là active, RP nào đang là
standby</p></li>
</ol>
<ul>
<li><p>Đứng trên thiết bị, chuyển card active sang standby và kiểm
tra</p></li>
</ul>
<p>#redundancy switchover #show platform</p>
<ul>
<li><p>Card RP standby chuyển lên làm active #show platform #show
redundancy để kiểm tra lại trạng thái active-standby trên card
RP</p></li>
</ul></td>
</tr>
<tr>
<td rowspan="4">3</td>
<td rowspan="4">ASR9K</td>
<td rowspan="4">Cisco</td>
<td rowspan="4">Core</td>
<td><ol>
<li><p>1. Backup cấu hình thiết bị trước khi thực hiện.</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Login vào thiết bị kiểm tra trạng thái hoạt động của thiết bị và
xem card RSP (route switch processors) nào đang là active, RSP nào đang
là standby. Hiên thị ngay khi login vào thiết bị #show platform #show
redundancy</p></li>
</ol>
<p>Để lấy thông tin RSP active-standby chi tiết trên cặp thiết bị
switchover</p></td>
</tr>
<tr>
<td><ol>
<li><p>Thực hiện lấy thông tin route, trạng thái các phiên BGP và OSPF
để so sánh sau khi thực hiện switchover</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Xác định được RSP nào đang là active, RSP nào đang là
standby</p></li>
</ol>
<ul>
<li><p>Đứng trên thiết bị, chuyển card active sang standby và kiểm tra #
edundancy switchover</p></li>
</ul>
<ol>
<li><p>Card RSP standby chuyển lên làm active, thực hiện #show platform
#show redundancy để kiểm tra lại trạng thái active-standby trên card
RSP</p></li>
</ol></td>
</tr>
<tr>
<td rowspan="4">4</td>
<td rowspan="4">Các dòng thiết bị Juniper hỗ trợ RE (Routing
Engine)</td>
<td rowspan="4">Juniper</td>
<td rowspan="4">Core</td>
<td><p>1. Login vào thiêt bị kiêm tra trạng thái hoạt động của thiết bị
và trạng thái của RE.</p>
<p>#show chassis hardware</p>
<p>#show system switchover</p>
<p>#request chassis routing-engine master switch check</p></td>
</tr>
<tr>
<td>2. Thực hiện lấy thông tin route, trạng thái các phiên BGP và OSPF
để so sánh sau khi thực hiện switchover</td>
</tr>
<tr>
<td><p>3. Tiến hành rút nguồn chassis RE primary, thiết bị switchover
sang RE backup hoặc thực hiện câu lệnh #system switchover</p>
<p>Sau khi switchover, thiết bị Backup trước đó chuyển lên làm
Primary.</p></td>
</tr>
<tr>
<td>4. Kiểm tra trạng thái các kết nối qua thiết bị</td>
</tr>
<tr>
<td rowspan="2">5</td>
<td rowspan="2">Các switch dòng Cisco hỗ trợ giao thức VRRP, HRRP</td>
<td rowspan="2">Cisco</td>
<td rowspan="2">Distritube</td>
<td><ol>
<li><p>Đối với các cặp switch DS chạy các giao thức dự phòng VRRP,
HSRP,...</p></li>
</ol>
<p>Với trường hợp sử dụng giao thức VRRP.</p>
<ol>
<li><p>Thực hiện lật mặt trạng thái VRRP từ thiết bị Master sang Backup,
xác định thiết bị nào đang là master</p></li>
<li><p>Thực hiện shutdown các uplink từ iết bị Master lên CR để
switchover các vlan chạy trên thiết bị Master sang thiết bị Backup. Kiểm
tra trạng thái các vlan chạy trên thiết bị Backup. Lúc này thiết bị
Backup sẽ thành Master.</p></li>
</ol>
<blockquote>
<p>#show vrrp brief</p>
</blockquote>
<ol>
<li><p>Mở lại các port vừa shutdown trên thiết bị Master cũ để trạng
thái vrrp về Backup</p></li>
</ol></td>
</tr>
<tr>
<td><ol>
<li><p>Với trường hợp sử dụng giao thức HSRP</p></li>
</ol>
<p>2.1. Thực hiện lật mặt trạng thái HSRP từ thiết bị Active sang thiết
bị Standby, xác định thiết bị nào đang chạy là thiết bị Active
trước.</p>
<p>2.2. Thực hiên shutdown các uplink của thiết bị Active, hoặc rút
nguồn thiết bị Active traffic đổ qua thiết bị Standby, lúc này các route
ảo sẽ được chuyến sang thiết bị Standby để chuyển tiếp dữ liệu.</p>
<p>2.3. Kiểm tra trạng thái thiết bị Standby</p>
<p>#show stanby</p>
<p>2.4. Mở lại các port vừa shutdown hoặc cấp nguồn lại cho thiết bị.
Lúc này thiết nào có priority lớn hơn thì thiết bị đó sẽ là thiết bị
Active và ngược lại.</p></td>
</tr>
</tbody>
</table> 

## Kiểm tra và vệ sinh hệ thống làm mát

  * Kiểm tra quạt tản nhiệt: Kiểm tra xem tất cả các quạt trên CPU, GPU, nguồn, và vỏ thiết bị có hoạt động bình thường không. Nghe kỹ xem có mạnh có thể chỉ ra quạt tiếng ồn bất thường không (tiếng gầm hoặc rung 4 bị hỏng hoặc mất cân bằng).

  * Nếu phát hiện quạt hoạt động kém hiệu quả, quá ồn hoặc không hoạt động, hãy thay thế chúng ngay lập tức.


## Kiểm tra và vệ sinh lỗ thông gió và bộ lọc khí

  * Kiểm tra các lỗ thông gió của thiêtt bị, đảm bảo không có bụi bẩn hoặc các Kiểm tra các lỗ thông gió của thiết bị, đảm bảo vật thể lạ gây cản trở luồng không khí.


  * Nếu thiết bị sử dụng bộ lọc không khí, vệ sinh hoặc thay thế bộ lọc thường xuyên. Bộ lọc không khí có thể bị tắc nghẽn bụi bẩn, khiến quạt phải làm việc với cường độ cao hơn, từ từ đó làm tăng nhiệt độ của thiết bị.


## Lên kế hoạch bảo trì định kỳ hệ thống làm mát

\- Kiểm tra hàng tháng: Thực hiện kiểm tra hàng tháng các quạt và hệ thống làm mát của thiết bị. Đảm bảo không có dấu hiệu bất thường nào xảy ra và nhiệt độ của các thành phần luôn ổn định.

  * Bảo dưỡng hàng quý: Thực hiện vệ sinh định kỳ hệ thống làm mát hàng quý, bao gồm làm sạch quạt, lỗ thông gió,...

  * Bảo trì hệ thống điều hòa không khí hàng năm: Định kỳ bảo trì hệ thống điều hòa không khí, đảm bảo chúng hoạt động hiệu quả để hỗ trợ làm mát cho toàn bộ hệ thống.


# Vệ sinh và bảo trì vật lý

## Vệ sinh bên ngoài thiết bị

Làm sạch vỏ ngoài của thiết bị: Sử dụng khăn mềm hoặc các chất liệu không dẫn điện để lau sạch vỏ ngoài, tránh làm hư hỏng hoặc trầy xước. Bụi bẩn có thể tích tụ trên bề mặt và dẫn đến các vấn đề về tản nhiệt hoặc ảnh hưởng đến hiệu suất.

Kiểm tra cổng kết nối và khe cắm: Các cổng kết nối như USB, Ethernet, và các khe cắm mở rộng có thể bị oxy hóa hoặc hư hỏng sau thời gian dài sử dụng. Kiểm tra xem các cổng này có bị rỉ sét hoặc hư hại không, đồng thời làm sạch bằng dung dịch chuyên dụng nếu cần.

## Kiểm tra và vệ sinh các cổng kết nối vật lý

Kiểm tra tình trạng cáp: Các cáp kết nối nguồn và dữ liệu cần được kiểm tra định kỳ. Đảm bảo chúng không bị gấp khúc, đứt hoặc quá căng, điều này có thể gây ra sự cố cho hệ thống.

Kiểm tra các cổng kết nối: Đảm bảo các cổng kết nối giữa thiết bị và các thiết bị ngoại vi không bị lỏng lẻo. Nếu phát hiện cổng bị mòn, cần thay thế hoặc sửa chữa kịp thời để tránh mất kết nối.

# Bảo trì hệ thống cáp và kết nối mạng

## Kiểm tra hệ thống cáp mạng

Kiểm tra cáp mạng Ethernet: Cáp Ethernet là xương sống của hệ thống mạng. Bạn cần kiểm tra các dây cáp xem có dấu hiệu bị mòn, đứt hoặc gấp khúc không. Nếu cáp bị hỏng, hãy thay thế bằng cáp mới đạt tiêu chuẩn Cat5e, Cat6 hoặc cao hơn tùy nhu cầu sử dụng.

Kiểm tra cáp quang (fiber optic): Nếu sử dụng kết nối quang, cần kiểm tra định kỳ các dây cáp quang để đảm bảo không có hiện tượng đứt gãy hoặc suy giảm tín hiệu. Các kết nối quang cần được giữ sạch sẽ để tránh ảnh hưởng đến chất lượng truyền tải.

Đảm bảo quản lý cáp tốt: Cáp mạng cần cần được quản lý một cách gọn gàng và khoa học, tránh việc gấp khúc hoặc kéo căng quá mức. Điều này giúp duy trì trì hiệu suất của mạng và giảm thiểu rủi ro hỏng hóc.

## Kiểm tra tình trạng hoạt động của cổng mạng:

Bị hư hại sau thời gian dài sử dụng. Hãy đảm bảo rằng các cổng mạng hoạt động ổn định và không có sự cố như mất kết nối hay giảm băng thông.

# Kiểm tra và bảo trì hệ thống giá đỡ và bố trí thiết bị

## Kiểm tra và quản lý hệ thống giá đỡ (rack)

  * Đảm bảo sự chắc chắn của thiết bị trong giá đỡ: Các thiết bị cần được gắn chắc chắn vào hệ thống giá đỡ để tránh rung lắc hoặc di chuyển không mong muốn, có thể gây ảnh hưởng đến các kết nối và hoạt động của thiết bị. Sử dụng ốc vít hoặc kẹp chặt để đảm bảo sự ổn định.

  * Quản lý cáp trong giá đỡ: Cáp nguồn và cáp mạng cần được bố trí gọn gàng trong giá đỡ để tránh cản trở hoặc gây khó khăn khi bảo trì. Bạn nên sử dụng các phụ kiện quản lý cáp như dây rút, khay cáp hoặc tấm chắn cáp để giữ cáp gọn gàng và dễ quản lý.


## Kiểm tra bố trí các thiết bị

  * Bố trí thiết bị khoa học: Các thiết bị trong giá đỡ cần được bố trí sao cho đảm bảo luồng không khí tản nhiệt hiệu quả. Tránh đặt các thiết bị quá sát nhau hoặc chặn luồng khí giữa các thiết bị.

  * Dễ dàng tiếp cận các thiết bị: Khí bố trí các thiết bị trong phòng server, bạn cần đảm bảo rằng tất cả các thiết bị có thể dễ dàng tiếp cận để thực hiện kiểm tra và bảo trì. Điều này giúp giảm thời gian bảo trì và đảm bảo rằng hệ thống luôn hoạt hoạt động liên tục.