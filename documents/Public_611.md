# Public_611

# GIẢI THÍCH THUẬT NGỮ, ĐỊNH NGHĨA, KHÁI NIỆM

  * Sự kiện an toàn thông tin (Information security event): Là sự việc xác định liên quan đến trạng thái của một hệ thống, dịch vụ hoặc trạng thái mạng nằm ngoài việc vận hành thông thường, cho thấy có khả năng vi phạm chính sách ATTT hay lỗi kiểm soát ATTT, hoặc một tình huống không lường trước liên quan đến ATTT. Không phải tất cả các sự kiện ATTT đều là sự cố ATTT.

  * Sự cố an toàn thông tin (Information security incidient): Là một hoặc một loạt các sự kiện ATTT không mong muốn hoặc không dự tính có khả năng ảnh hưởng đáng kể đến các hoạt động nghiệp vụ và đe dọa ATTT.

  * SOC (Security Operation Center): được giao nhiệm vụ giám sát, điều phối, ứng cứu, xử lý sự cố ATTT và đảm bảo ATTT cho Công ty.

  * Tier 1: bộ phận thuộc Phòng Vận hành dịch vụ số của Trung tâm Dịch vụ hạ tầng số/TT VHKT làm đầu mối chịu trách nhiệm thực hiện giám sát hệ thống. an

  * Tier 2: bộ phận trực SOC thuộc BU MSSP- Trung tâm Hợp tác kinh doanh làm đầu mối chịu trách nhiệm thực hiện tiếp nhận các ticket từ Tier 1, tiến hành xác minh, phối hợp với SO xử lý ticket.

  * Tier 3: bộ phận SOC thuộc BU MSSP- Trung tâm Hợp tác kinh doanh làm đầu mối thực hiện xử lý, trong trường hợp Tier 2 không thể xử lý được hoặc đã xử lý nhưng không thành công. Trường hợp Tier 3- Viettel IDC không thể xử lý thì chuyển lên SOC manager để tiếp tục xử lý.

  * SLA: thời gian xử lý cảnh báo

  * Ticket: Ticket sự cố ATTT được tạo và đưa lên hệ thống SOAR để điều phối luồng xử lý sự cố ATTT.

  * SOAR (Security Orchestration, Automation and Response): là giải pháp điều phối, tự động hóa phản ứng an ninh thông tin tập trung giúp xác định, ưu tiên và tiêu chuẩn hóa cho các chức năng ứng phó sự cố, lỗ hồng, vấn đề ATTT.

  * SOC manager: làm nhiệm vụ điều hành xử lý sự cố, phê duyệt yêu cầu về thời gian xử lý sự cố của SO (nếu có); phê duyệt yêu cầu hỗ trợ xử lý ticket của SO (nếu có) và đóng ticket.

  * Ban lãnh đạo: Ban lãnh đạo quản lý sự cố ATTT chịu trách nhiệm xác nhận hoặc phê duyệt kế hoạch ứng cứu sự cố ATTT ATTT và chủ trì xử lý sự cố ATTT nghiêm trọng.


# QUY TRÌNH XỬ LÝ SỰ CỐ
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
<th>Bước</th>
<th>Hoạt động</th>
<th>Mô tả chi tiết</th>
<th>Vai trò</th>
<th>Đầu vào</th>
<th>Đầu ra</th>
<th>Thời gian thực hiện</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Tiếp nhận và xác minh thông tin cảnh báo về sự cố</td>
<td><ol>
<li><p>Tiếp nhận thông tin cảnh báo về sự cố ATTT từ:</p></li>
</ol>
<ul>
<li><p>Cảnh báo của các giải pháp ATTT: SIEM,</p></li>
<li><p>Email, điện thoại của Phòng/Ban, cá nhân phát hiện sự cố ATTT báo
cho bộ phận ATTT qua email: <a>idc.attt@123com.vn</a>;</p></li>
<li><p>Đe dọa Hungting, Pentest</p></li>
</ul>
<ol>
<li><p>Thực hiện xác minh thông tin cảnh báo:</p></li>
</ol>
<ul>
<li><p>Cảnh báo đúng: Chuyển bước 2a. Phân loại, đánh giá mức
độ</p></li>
<li><p>Cảnh báo sai: cảnh báo nhầm nghiệp vụ quản trị, nghiệp vụ đơn vị,
tác động có kế hoạch... Chuyển bước 2b. Cập nhật trạng thái cảnh báo
REJECT-False Positive, đóng case.</p></li>
</ul></td>
<td>Tier 1</td>
<td><ul>
<li><p>Dấu hiệu sự cố ATTT được nhận diện từ:</p></li>
<li><p>Cảnh báo của các giải pháp ATTT</p></li>
<li><p>Email, điện thoại của các Chi nhánh, Phòng/ban cá nhân phát hiện
sự cố ATTT</p></li>
<li><p>Săn lùng mối đe dọa, Pentest</p></li>
</ul></td>
<td>Cảnh báo về ATTT được báo cáo</td>
<td>Ngay khi phát hiện cảnh báo từ các nguồn tương ứng</td>
</tr>
<tr>
<td>2a</td>
<td>Phân loại sự cố ATTT</td>
<td><p>Phân loại, đánh giá mức độ nguy hiểm của cảnh báo gồm 2 mức độ:
nghiêm trọng và thông thường (PL 01: Hướng dẫn phân loại mức độ sự cố
ATTT).</p>
<p>Với các sự cố xử lý qua ticket trên hệ thống SOAR thì thực hiện tiếp
bước 3.</p>
<p>Với các sự cố cần thông báo cho SO xử lý luôn thì liên hệ SO hệ thống
theo Phụ lục 02. Danh sách liên lạc ứng cứu sự cố ATTT và thực hiện theo
Quy trình quản lý và xử lý sự cố</p></td>
<td rowspan="2">Tier 1</td>
<td>Cảnh báo/thông báo</td>
<td>Cảnh báo ATTT được phân loại</td>
<td></td>
</tr>
<tr>
<td>2b</td>
<td>Đóng cảnh báo về sự cô ATTT</td>
<td>Trường hợp là cảnh báo giả: Cập nhật trạng thái cảnh báo
REJECT-False Positive, đóng cảnh báo trên hệ thống SOAR</td>
<td>Cảnh báo về sự cố ATTT được đánh giá không phải là sự cố</td>
<td>Cảnh báo được đóng</td>
<td>Ngay sau khi có kết quả đánh giá cảnh báo</td>
</tr>
<tr>
<td>3</td>
<td>Tạo ra các sự cố</td>
<td><p>Tier 1 tạo case sự cố (Status = OPEN) trên SOAR Case sự sự cố
được gán cho:</p>
<p>Tier 1 đối với case đã có hướng dẫn xử lý. Chuyển bước 4b thực hiện
nhiệm vụ Case Management điều hành xử lý sự cố</p>
<p>Tier 2 đối với case sự cố chưa có hướng dẫn xử lý (Bước 4a)</p></td>
<td>Tier 1</td>
<td>Case chưa được xử lý</td>
<td>Case được gán cho Tier 1</td>
<td>Ngay sau bước 2a</td>
</tr>
<tr>
<td>4a</td>
<td>Tier 2 tiếp nhận sự cố</td>
<td><p>Tier 2 tiếp nhận case sự cố, trạng thái case là OPEN.</p>
<p>Thực hiện xác minh thông tin cảnh báo:</p>
<p>Cảnh báo sai chuyển bước 5 và cập nhật trạng thái cảnh báo REJECT -
False Positive, đóng case.</p>
<p>Cảnh báo đúng:</p>
<p>+ Cảnh báo đã biết hướng xử lý chuyển sang bước 4b thực hiện nhiệm vụ
Case Management điều hành xử lý.</p>
<p>Cảnh báo không xác minh được hướng xử lý gán sự cố cho Tier 3 (bước
6)</p></td>
<td>Tier 2</td>
<td>Case chưa được xử lý</td>
<td>Case được gán cho Tier 2</td>
<td rowspan="2">Ngay sau bước 3</td>
</tr>
<tr>
<td>4b</td>
<td>Case Management điều hành xử lý case</td>
<td><p>Case Management thực hiện điều hành xử lý case:</p>
<p>Tạo các ticket nghiệp vụ cho System Owner/IT Admin</p>
<p>A Nêu Tier 1 hoặc Tier 2 thực hiện theo hướng dẫn nhưng không xử lý
thành công hoặc xác định mức độ sự cố Nghiêm trọng, chuyển case cho Tier
3 điều hành xử lý (Bước 6)</p>
<p>Nếu xử lý thành công: Đóng case. Trạng thái Case là CLOSE.</p>
<p>Nếu cần xác minh nghiệp vụ cần tạo Ticket cho SO/IT Admin</p></td>
<td><p>Tier 1,</p>
<p>Tier 2,</p>
<p>Tier 3</p></td>
<td>Ticket chưa được xử lý</td>
<td>Ticket đã được xử lý</td>
</tr>
<tr>
<td>5</td>
<td><p>Cập nhật trạng thái</p>
<p>Reject – False positive</p></td>
<td>Cảnh báo sai chuyển bước 5 và cập nhật trạng -thái cảnh báo REJECT –
False Positive, đóng case.</td>
<td>Tier 2</td>
<td>Cảnh báo sai</td>
<td>Đóng case</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Tier 3 tiếp nhận case</td>
<td><p>OPEN. Tier 3 tiếp nhận case sự cố, trạng thái case là</p>
<p>Chuyển bước 4b thực hiện nhiệm vụ CaseManagement điều hành xử lý sự
cố.</p></td>
<td>Tier 3</td>
<td>Case sự cố</td>
<td></td>
<td></td>
</tr>
<tr>
<td>7a</td>
<td>Xác minh thông tin ticket nhận được</td>
<td><p>SO/IT admin xác minh thông tin ticket nhận được:</p>
<p>Nếu ticket gán đúng nghiệp vụ cho nhóm: Cập nhật trạng thái ticket IN
PROGRESS để bắt đầu công việc (Bước 8a);</p>
<p>Nếu ticket gán sai: Cập nhật trạng thái ticket AWAITING REASSIGNMENT
để Case Management thực hiện gán lại (Bước 8b).</p></td>
<td>SO, IT Admin</td>
<td>Ticket trên SOAR</td>
<td></td>
<td></td>
</tr>
<tr>
<td>7b</td>
<td>Đóng case</td>
<td>Đóng case khi tất cả các ticket điều hành đã được xử lý xong.</td>
<td>Case management</td>
<td>Ticket trên SOAR</td>
<td>Ticket được xử lý</td>
<td>Ngay sau bước 2b</td>
</tr>
<tr>
<td>8a</td>
<td>Bắt đầu xử lý công việc theo chức năng, nghiệp vụ của nhóm</td>
<td><p>Bắt đầu xử lý công việc theo chức năng, nghiệp vụ của nhóm A Nếu
cần hỗ trợ từ Case Management chuyển sang bước 9a;</p>
<p>thêm thời gian để xử lý hoặc cần ngoại Nếu cần lệ cho ticket.</p>
<p>Cập nhật trạng thái A WAITING PENDING (Bước b)</p>
<p>Xử lý xong ticket: Cập nhật thông tin xử lý và trạng thái CLOSE cho
ticket (Bước 9c).</p></td>
<td>SO, IT Admin</td>
<td>Ticket trên SOAR</td>
<td>Ticket được xử lý</td>
<td>Ngay sau bước 6</td>
</tr>
<tr>
<td>8b</td>
<td>Case Management tiếp nhận ticket</td>
<td>Case Management thực hiện gán lại ticket có trạng thái AWATING
REASSIGNMENT về đúng nhóm, người xử lý. Cập nhật lại trạng thái OPEN cho
ticket.</td>
<td><p>Tier 1,</p>
<p>Tier 2,</p>
<p>Tier 3</p></td>
<td>Ticket trên SOAR</td>
<td>Ticket được cập nhật trạng thái</td>
<td>Ngay sau bước 6</td>
</tr>
<tr>
<td>9a</td>
<td>Tiếp nhận hỗ trợ</td>
<td><p>Case Management xác minh yêu cầu hỗ trợ:</p>
<p>Nếu yêu cầu hỗ trợ sai (hoặc đã có hướng dẫn, Case Management không
có quyền) thì từ chối hỗ trợ;</p>
<p>- Nếu yêu cầu hỗ trợ đúng (SO chưa có hướng dẫn, không có quyền...)
thì chuyển sang bước 4b cho Case Management tiếp tục điều hành xử lý sự
cố.</p>
<p>- Thông báo lại cho SO/IT Admin sau khi hoàn thành yêu cầu hỗ
trợ.</p></td>
<td>SOC Manager</td>
<td rowspan="2">Ticket trên SOAR</td>
<td rowspan="2">Ticket được cập nhật trạng thái</td>
<td rowspan="2">Ngay sau bước 8a</td>
</tr>
<tr>
<td>9b</td>
<td><p>Tiếp nhận ticket</p>
<p>trạng thái</p>
<p>AWAITING PENDING</p></td>
<td><p>Case Management xác minh yêu cầu hỗ trợ:</p>
<p>-Nếu yêu cầu hỗ trợ sai (hoặc đã có hướng dẫn, Case Management không
có quyền) thì từ chối hỗ trợ;</p>
<p>-Nếu yêu cầu hỗ trợ đúng (SO chưa có hướng dẫn, không có quyền...)
thì chuyển sang bước 4b cho Case Management tiếp tục điều hành xử lý sự
cố.</p>
<p>- Thông báo lại cho SO/IT Admin sau khi hoàn thành yêu cầu hỗ
trợ.</p></td>
<td><p>Tier 1,</p>
<p>Tier 2,</p>
<p>Tier 3</p></td>
</tr>
<tr>
<td>9c</td>
<td>Cập nhật thông tin xử lý ticket</td>
<td><p>Cập nhật thông tin xử lý và đóng ticket khi:</p>
<p>Ticket sự vụ được xử lý thành công.</p>
<p>TicKet trùng do đã nhận được ticket tương tự trước đó và đã xử lý
thành công.</p>
<p>Thông báo kêt quả cho Case Management</p></td>
<td>SO, IT Admin</td>
<td>Ticket trên SOAR</td>
<td>Ticket được xử lý</td>
<td>Ngay sau bước 8a</td>
</tr>
<tr>
<td>10</td>
<td>Đồng ý pending</td>
<td>Đồng ý xét duyệt thêm thời gian xử lý ticket hoặc ngoại lệ cho
ticket. Trạng thái ticket PENDING.</td>
<td><p>Tier 1,</p>
<p>Tier 2,</p>
<p>Tier 3</p></td>
<td>Ticket trên SOAR</td>
<td>Ticket pending</td>
<td>Ngay sau bước 9c</td>
</tr>
</tbody>
</table>