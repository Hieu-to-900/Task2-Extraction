# Public_266

# MỤC TIÊU CHUNG

Tiến hành nghiên cứu toàn diện về nhóm Lazarus Group, tập trung vào chiến thuật, kỹ thuật và thủ tục của họ. Sử dụng khung MITRE ATT&CK để vạch ra các hoạt động của nhóm và cung cấp những hiểu biết có thể hành động. [[1_](https://attack.mitre.org/groups/G0032/)]

Phát hiện của bản báo cáo này đóng một vai trò quan trọng trong việc củng cố khả năng phòng thủ chống lại kẻ thù này.

# Lazarus Group

Lazarus Group là một trong những nhóm tin tặc nguy hiểm và nổi tiếng nhất hiện nay. Nhóm này được cho là có liên hệ chặt chẽ với chính phủ Bắc Triều Tiên, hoạt động ít nhất từ năm 2009 đến nay. Lazarus thường xuyên tiến hành các cuộc tấn công mạng quy mô lớn nhằm vào nhiều mục tiêu khác nhau, bao gồm cả lĩnh vực chính trị, quân sự và tài chính.[1]

## Nguồn gốc và tổ chức

Theo các báo cáo tình báo và phân tích an ninh mạng, Lazarus Group được điều hành bởi Reconnaissance General Bureau (RGB) – cơ quan tình báo quân sự của Triều Tiên. Bên trong Lazarus tồn tại nhiều nhánh phụ chuyên trách: [[1_](https://attack.mitre.org/groups/G0032/)]

  * BlueNorOff / APT38 : Tập trung vào các cuộc tấn công tài chính, nhắm vào hệ thống ngân hàng và tiền mã hóa.[1]

  * AndAriel : Thực hiện các chiến dịch gián điệp mạng và tấn công vào hạ tầng quan trọng, đặc biệt tại Hàn Quốc.[1]

  * Hidden Cobra, Guardians of Peace, ZINC, v.v., được dùng để che giấu dấu vết và tạo sự nhầm lẫn cho cơ quan điều tra .[[1_](https://attack.mitre.org/groups/G0032/)]


## Các vụ tấn công nổi bật

Một số sự kiện tiêu biểu do Lazarus Group thực hiện:

  * 2014 – Sony Pictures : Tấn công, đánh cắp dữ liệu và làm rò rỉ thông tin mật, được cho là trả đũa bộ phim The Interview. [[2_](https://www.nccgroup.com/the-lazarus-group-north-korean-scourge-for-plus10-years)]

  * 2016 – Ngân hàng Trung ương Bangladesh : Lazarus đánh cắp 81 triệu USD qua hệ thống SWIFT. [[3_](https://eurepoc.eu/wp-content/uploads/2024/02/Advanced-Persistent-Threat-Profile-Lazarus-February-2024.pdf)]

  * 2017 – WannaCry Ransomware : Mã độc tống tiền toàn cầu, gây ảnh hưởng đến hơn 150 quốc gia.

  * 2022 – Ronin Network / Axie Infinity : Đánh cắp hơn 620 triệu USD tiền mã hóa.

  * 2023 – Stake[.]com và Atomic Wallet : Tổng cộng Lazarus đã lấy hơn 300 triệu USD từ các nền tảng crypto [[4_](https://hacken.io/discover/lazarus-group/)]


Điểm đáng chú ý là Lazarus không chỉ triển khai Dream Job như một chiến dịch đơn lẻ. Nó còn liên kết với các hoạt động khác như Operation North Star và Operation Interception , thể hiện chiến lược lâu dài nhằm vào cá nhân trong lĩnh vực kỹ thuật và an ninh quốc phòng. [[5_](https://attack.mitre.org/campaigns/C0022/)]

## Operation Dream Job

Bài báo cáo này sẽ tập trung vào chiến dịch Operation Dream Job.

Operation Dream Job là một trong những chiến dịch tấn công mạng phức tạp nhất do Lazarus Group tiến hành. Chiến dịch này lợi dụng các cơ hội nghề nghiệp giả mạo từ những công ty công nghệ và quốc phòng lớn để dụ dỗ nạn nhân tải về các tài liệu hoặc phần mềm chứa mã độc. Lần đầu tiên chiến dịch này được phát hiện là vào tháng 9 năm 2019 theo dữ liệu từ MITRE ATT&CK. [[5_](https://attack.mitre.org/campaigns/C0022/)]

###  Phương thức tấn công

#### Kỹ thuật lợi dụng hệ thống hợp pháp

Trong chiến dịch này, Lazarus đã khai thác các binary hợp pháp của Windows như Regsvr32 và Rundll32 để thực hiện proxy execution. Đây là kỹ thuật "Living off the Land" (LOLBin) thường thấy, giúp kẻ tấn công ngụy trang hoạt động của mình dưới lớp vỏ hợp pháp, khó bị phát hiện bởi các hệ thống phòng thủ truyền thống. [[5_](https://attack.mitre.org/campaigns/C0022/)]

#### Kỹ thuật di chuyển ngang

Sau khi xâm nhập ban đầu, Lazarus sử dụng kỹ thuật Internal Spearphishing để mở rộng phạm vi kiểm soát trong cùng một tổ chức. Kỹ thuật này được MITRE định danh là T1534. Điều này cho phép kẻ tấn công mở rộng quyền truy cập mà không cần phải khai thác thêm nhiều lỗ hổng. [[5_](https://attack.mitre.org/campaigns/C0022/)]

#### Phần mềm độc hại

Một RAT (Remote Access Trojan) quan trọng trong chiến dịch này là DRATzarus. Đây là công cụ giúp Lazarus duy trì truy cập từ xa, thực hiện các lệnh và đánh cắp dữ liệu. DRATzarus sử dụng Native API để thực thi trực tiếp trên hệ thống, đồng thời áp dụng kỹ thuật Time-Based Evasion nhằm tránh bị sandbox phân tích trong môi trường ảo. [[6_](https://attack.mitre.org/techniques/T1106/)] [[7_](https://attack.mitre.org/techniques/T1497/003/)]

### Operation Dream Job Techniques Used [[5_](https://attack.mitre.org/campaigns/C0022/)]
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Domain</strong></td>
<td colspan="2"><strong>ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Use</strong></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1087</td>
<td>.002</td>
<td>Account Discovery: Domain Account</td>
<td>During Operation Dream Job, Lazarus Group queried compromised
victim's active directory servers to obtain the list of employees
including administrator accounts.</td>
</tr>
<tr>
<td rowspan="3"><strong>Enterprise</strong></td>
<td rowspan="3">T1583</td>
<td>.001</td>
<td>Acquire Infrastructure: Domains</td>
<td>During Operation Dream Job, Lazarus Group registered a domain name
identical to that of a compromised company as part of their BEC
effort.</td>
</tr>
<tr>
<td>.004</td>
<td>Acquire Infrastructure: Server</td>
<td>During Operation Dream Job, Lazarus Group acquired servers to host
their malicious tools.</td>
</tr>
<tr>
<td>.006</td>
<td>Acquire Infrastructure: Web Services</td>
<td>During Operation Dream Job, Lazarus Group used file hosting services
like DropBox and OneDrive.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1071</td>
<td>.001</td>
<td>Application Layer Protocol: Web Protocols</td>
<td>During Operation Dream Job, Lazarus Group uses HTTP and HTTPS to
contact actor-controlled C2 servers.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1560</td>
<td>.001</td>
<td>Archive Collected Data: Archive via Utility</td>
<td>During Operation Dream Job, Lazarus Group uses HTTP and HTTPS to
contact actor-controlled C2 servers.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1547</td>
<td>.001</td>
<td>Boot or Logon Autostart Execution: Registry Run Keys / Startup
Folder</td>
<td>During Operation Dream Job, Lazarus Group archived victim's data
into a RAR file.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1110</td>
<td>Brute Force</td>
<td>During Operation Dream Job, Lazarus Group placed LNK files into the
victims' startup folder for persistence.</td>
</tr>
<tr>
<td rowspan="3"><strong>Enterprise</strong></td>
<td rowspan="3">T1059</td>
<td>.001</td>
<td>Command and Scripting Interpreter: PowerShell</td>
<td>During Operation Dream Job, Lazarus Group used PowerShell commands
to explore the environment of compromised victims.</td>
</tr>
<tr>
<td>.003</td>
<td>Command and Scripting Interpreter: Windows Command Shell</td>
<td>During Operation Dream Job, Lazarus Group launched malicious DLL
files, created new folders, and renamed folders with the use of the
Windows command shell.</td>
</tr>
<tr>
<td>.005</td>
<td>Command and Scripting Interpreter: Visual Basic</td>
<td>During Operation Dream Job, Lazarus Group executed a VBA written
malicious macro after victims download malicious DOTM files; Lazarus
Group also used Visual Basic macro code to extract a double Base64
encoded DLL implant.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1584</td>
<td>.001</td>
<td>Compromise Infrastructure: Domains</td>
<td>For Operation Dream Job, Lazarus Group compromised domains in Italy
and other countries for their C2 infrastructure.</td>
</tr>
<tr>
<td>.004</td>
<td>Compromise Infrastructure: Server</td>
<td>For Operation Dream Job, Lazarus Group compromised servers to host
their malicious tools</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1005</td>
<td>Data from Local System</td>
<td>During Operation Dream Job, Lazarus Group used malicious Trojans and
DLL files to exfiltrate data from an infected host.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1622</td>
<td>Debugger Evasion</td>
<td>During Operation Dream Job, Lazarus Group used tools that used the
IsDebuggerPresent call to detect debuggers.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1587</td>
<td>.001</td>
<td>Develop Capabilities: Malware</td>
<td>For Operation Dream Job, Lazarus Group developed custom tools such
as Sumarta, DBLL Dropper, Torisma, and DRATzarus for their
operations.</td>
</tr>
<tr>
<td>.002</td>
<td>Develop Capabilities: Code Signing Certificates</td>
<td>During Operation Dream Job, Lazarus Group digitally signed their
malware and the dbxcli utility.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1573</td>
<td>.001</td>
<td>Encrypted Channel: Symmetric Cryptography</td>
<td>During Operation Dream Job, Lazarus Group used an AES key to
communicate with their C2 server.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1585</td>
<td>.001</td>
<td>Establish Accounts: Social Media Accounts</td>
<td>For Operation Dream Job, Lazarus Group created fake LinkedIn
accounts for their targeting efforts.</td>
</tr>
<tr>
<td>.002</td>
<td>Establish Accounts: Email Accounts</td>
<td>During Operation Dream Job, Lazarus Group created fake email
accounts to correspond with fake LinkedIn personas; Lazarus Group also
established email accounts to match those of the victim as part of their
BEC attempt.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1041</td>
<td>Exfiltration Over C2 Channel</td>
<td>During Operation Dream Job, Lazarus Group exfiltrated data from a
compromised host to actor-controlled C2 servers.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1567</td>
<td>.002</td>
<td>Exfiltration Over Web Service: Exfiltration to Cloud Storage</td>
<td>During Operation Dream Job, Lazarus Group used a custom build of
open-source command-line dbxcli to exfiltrate stolen data to
Dropbox.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1083</td>
<td>File and Directory Discovery</td>
<td>During Operation Dream Job, Lazarus Group conducted word searches
within documents on a compromised host in search of security and
financial matters.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1589</td>
<td>Gather Victim Identity Information</td>
<td>For Operation Dream Job, Lazarus Group conducted extensive
reconnaissance research on potential targets.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1591</td>
<td></td>
<td>Gather Victim Org Information</td>
<td>For Operation Dream Job, Lazarus Group gathered victim organization
information to identify specific targets.</td>
</tr>
<tr>
<td>.004</td>
<td>Identify Roles</td>
<td>During Operation Dream Job, Lazarus Group targeted specific
individuals within an organization with tailored job vacancy
announcements.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1656</td>
<td>Impersonation</td>
<td>During Operation Dream Job, Lazarus Group impersonated HR hiring
personnel through LinkedIn messages and conducted interviews with
victims in order to deceive them into downloading malware.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1070</td>
<td>.004</td>
<td>Indicator Removal: File Deletion</td>
<td>During Operation Dream Job, Lazarus Group removed all previously
delivered files from a compromised computer.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1105</td>
<td>Ingress Tool Transfer</td>
<td>During Operation Dream Job, Lazarus Group downloaded multistage
malware and tools onto a compromised host.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1534</td>
<td>Internal Spearphishing</td>
<td>During Operation Dream Job, Lazarus Group conducted internal
spearphishing from within a compromised organization.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1036</td>
<td>.008</td>
<td>Masquerading: Masquerade File Type</td>
<td>During Operation Dream Job, Lazarus Group disguised malicious
template files as JPEG files to avoid detection.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1106</td>
<td>Native API</td>
<td>During Operation Dream Job, Lazarus Group used Windows API
ObtainUserAgentString to obtain the victim's User-Agent and used the
value to connect to their C2 server.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1027</td>
<td>.002</td>
<td>Obfuscated Files or Information: Software Packing</td>
<td>During Operation Dream Job, Lazarus Group packed malicious .db files
with Themida to evade detection.</td>
</tr>
<tr>
<td>.013</td>
<td>Obfuscated Files or Information: Encrypted/Encoded File</td>
<td>During Operation Dream Job, Lazarus Group encrypted malware such as
DRATzarus with XOR and DLL files with base64.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1588</td>
<td>.002</td>
<td>Obtain Capabilities: Tool</td>
<td>For Operation Dream Job, Lazarus Group obtained tools such as
Wake-On-Lan, Responder, ChromePass, and dbxcli.</td>
</tr>
<tr>
<td>.003</td>
<td>Obtain Capabilities: Code Signing Certificates</td>
<td>During Operation Dream Job, Lazarus Group used code signing
certificates issued by Sectigo RSA for some of its malware and
tools.</td>
</tr>
<tr>
<td rowspan="3"><strong>Enterprise</strong></td>
<td rowspan="3">T1566</td>
<td>.001</td>
<td>Phishing: Spearphishing Attachment</td>
<td>During Operation Dream Job, Lazarus Group sent emails with malicious
attachments to gain unauthorized access to targets' computers.</td>
</tr>
<tr>
<td>.002</td>
<td>Phishing: Spearphishing Link</td>
<td>During Operation Dream Job, Lazarus Group sent malicious OneDrive
links with fictitious job offer advertisements via email.</td>
</tr>
<tr>
<td>.003</td>
<td>Phishing: Spearphishing via Service</td>
<td>During Operation Dream Job, Lazarus Group sent victims spearphishing
messages via LinkedIn concerning fictitious jobs.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1053</a></td>
<td>.005</td>
<td>Scheduled Task/Job: Scheduled Task</td>
<td>During Operation Dream Job, Lazarus Group created scheduled tasks to
set a periodic execution of a remote XSL script.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1593</a></td>
<td>.001</td>
<td>Search Open Websites/Domains: Social Media</td>
<td>For Operation Dream Job, Lazarus Group used LinkedIn to identify and
target employees within a chosen organization.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1505</a></td>
<td>.004</td>
<td>Server Software Component: IIS Components</td>
<td>During Operation Dream Job, Lazarus Group targeted Windows servers
running Internet Information Systems (IIS) to install C2
components.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2"><a>T1608</a></td>
<td>.001</td>
<td>Stage Capabilities: Upload Malware</td>
<td>For Operation Dream Job, Lazarus Group used compromised servers to
host malware.</td>
</tr>
<tr>
<td>.002</td>
<td>Stage Capabilities: Upload Tool</td>
<td>For Operation Dream Job, Lazarus Group used multiple servers to host
malicious tools.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1553</td>
<td>.002</td>
<td>Subvert Trust Controls: Code Signing</td>
<td>During Operation Dream Job, Lazarus Group digitally signed their own
malware to evade detection.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1218</td>
<td>.010</td>
<td>System Binary Proxy Execution: Regsvr32</td>
<td>During Operation Dream Job, Lazarus Group used regsvr32 to execute
malware.</td>
</tr>
<tr>
<td>.011</td>
<td>System Binary Proxy Execution: Rundll32</td>
<td>During Operation Dream Job, Lazarus Group executed malware with
C:\\windows\system32\rundll32.exe
"C:\ProgramData\ThumbNail\thumbnail.db", CtrlPanel
S-6-81-3811-75432205-060098-6872 0 0 905.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1614</td>
<td>.001</td>
<td>System Location Discovery: System Language Discovery</td>
<td>During Operation Dream Job, Lazarus Group deployed malware designed
not to run on computers set to Korean, Japanese, or Chinese in Windows
language preferences.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1221</td>
<td>Template Injection</td>
<td>During Operation Dream Job, Lazarus Group used DOCX files to
retrieve a malicious document template/DOTM file.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1204</td>
<td></td>
<td>User Execution: Malicious Link</td>
<td>During Operation Dream Job, Lazarus Group lured users into executing
a malicious link to disclose private account information or provide
initial access.</td>
</tr>
<tr>
<td></td>
<td>User Execution: Malicious File</td>
<td>During Operation Dream Job, Lazarus Group lured victims into
executing malicious documents that contained "dream job" descriptions
from defense, aerospace, and other sectors.</td>
</tr>
<tr>
<td rowspan="6"><strong>Enterprise</strong></td>
<td rowspan="6">T1497</td>
<td rowspan="3">.001</td>
<td rowspan="2">Virtualization/Sandbox Evasion: System Checks</td>
<td rowspan="2">During Operation Dream Job, Lazarus Group used tools
that conducted a variety of system checks to detect sandboxes or VMware
services.</td>
</tr>
<tr>
</tr>
<tr>
<td rowspan="4">Virtualization/Sandbox Evasion: Time Based Evasion</td>
<td rowspan="4">During Operation Dream Job, Lazarus Group used tools
that collected GetTickCount and GetSystemTimeAsFileTime data to detect
sandbox or VMware services.</td>
</tr>
<tr>
<td rowspan="3">.003</td>
</tr>
<tr>
</tr>
<tr>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1047</td>
<td>Windows Management Instrumentation</td>
<td>During Operation Dream Job, Lazarus Group used WMIC to executed a
remote XSL script.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1220</td>
<td>XSL Script Processing</td>
<td>During Operation Dream Job, Lazarus Group used a remote XSL script
to download a Base64-encoded DLL custom downloader.</td>
</tr>
</tbody>
</table> 

# Lazarus Group Techniques Used [[1_](https://attack.mitre.org/groups/G0032/)]
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Domain</strong></td>
<td colspan="2"><strong>ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Use</strong></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1134</td>
<td>.002</td>
<td>Access Token Manipulation: Create Process with Token</td>
<td>Lazarus Group keylogger KiloAlfa obtains user tokens from
interactive sessions to execute itself with API call
CreateProcessAsUserA under that user's context.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1087</td>
<td>.002</td>
<td><a>Account
Discovery</a>: <a>Domain
Account</a></td>
<td>During <a>Operation
Dream Job</a>, <a>Lazarus
Group</a> queried compromised victim's active directory servers to
obtain the list of employees including administrator accounts.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1098</a></td>
<td>Account Manipulation</td>
<td>Lazarus Group malware WhiskeyDelta-Two contains a function that
attempts to rename the administrator’s account.</td>
</tr>
<tr>
<td rowspan="3"><strong>Enterprise</strong></td>
<td rowspan="3"><a>T1583</a></td>
<td><a>.001</a></td>
<td>Acquire Infrastructure: Domains</td>
<td><p><a>Lazarus Group</a>
has acquired domains related to their campaigns to act as distribution
points and C2 channels.</p>
<p>During <a>Operation
Dream Job</a>, <a>Lazarus
Group</a> registered a domain name identical to that of a compromised
company as part of their BEC effort.</p></td>
</tr>
<tr>
<td><a>.004</a></td>
<td>Acquire Infrastructure: Server</td>
<td>During <a>Operation
Dream Job</a>, <a>Lazarus
Group</a> acquired servers to host their malicious tools.</td>
</tr>
<tr>
<td><a>.006</a></td>
<td>Acquire Infrastructure: Web Services</td>
<td><p>Lazarus Group has hosted malicious downloads on Github.</p>
<p>During Operation Dream Job, Lazarus Group used file hosting services
like DropBox and OneDrive.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1557</a></td>
<td><a>.001</a></td>
<td><a>Adversary-in-the-Middle</a>:
<a>LLMNR/NBT-NS
Poisoning and SMB Relay</a></td>
<td>Lazarus Group executed Responder using the command [Responder file
path] -i [IP address] -rPv on a compromised host to harvest credentials
and move laterally.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1071</td>
<td>.001</td>
<td>Application Layer Protocol: Web Protocols</td>
<td><p>Lazarus Group has conducted C2 over HTTP and HTTPS.</p>
<p>During Operation Dream Job, Lazarus Group uses HTTP and HTTPS to
contact actor-controlled C2 servers.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1010</td>
<td>Application Window Discovery</td>
<td>Lazarus Group malware IndiaIndia obtains and sends to its C2 server
the title of the window for each running process. The KilaAlfa keylogger
also reports the title of the window in the foreground.</td>
</tr>
<tr>
<td rowspan="4"><strong>Enterprise</strong></td>
<td rowspan="4">T1560</td>
<td></td>
<td>Archive Collected Data</td>
<td>Lazarus Group has compressed exfiltrated data with RAR and used
RomeoDelta malware to archive specified directories in .zip format,
encrypt the .zip file, and upload it to C2.</td>
</tr>
<tr>
<td>.001</td>
<td>Archive via Utility</td>
<td>During Operation Dream Job, Lazarus Group archived victim's data
into a RAR file.</td>
</tr>
<tr>
<td>.002</td>
<td>Archive via Library</td>
<td>Lazarus Group malware IndiaIndia saves information gathered about
the victim to a file that is compressed with Zlib, encrypted, and
uploaded to a C2 server.</td>
</tr>
<tr>
<td>.003</td>
<td>Archive via Custom Method</td>
<td>A Lazarus Group malware sample encrypts data using a simple byte
based XOR operation prior to exfiltration.</td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1547</td>
<td>.001</td>
<td>Boot or Logon Autostart Execution: Registry Run Keys / Startup
Folder</td>
<td><p>Lazarus Group has maintained persistence by loading malicious
code into a startup folder or by adding a Registry Run.</p>
<p>During Operation Dream Job, Lazarus Group placed LNK files into the
victims' startup folder for persistence.</p></td>
</tr>
<tr>
<td>.009</td>
<td>Boot or Logon Autostart Execution: Shortcut Modification</td>
<td>Lazarus Group malware has maintained persistence on a system by
creating a LNK shortcut in the user’s Startup folder.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1110</td>
<td>.003</td>
<td>Brute Force: Password Spraying</td>
<td>Lazarus Group malware attempts to connect to Windows shares for
lateral movement by using a generated list of usernames, which center
around permutations of the username Administrator, and weak
passwords.</td>
</tr>
<tr>
<td rowspan="3"><strong>Enterprise</strong></td>
<td rowspan="3">T1059</td>
<td>.001</td>
<td>Command and Scripting Interpreter: PowerShell</td>
<td><p>Lazarus Group has used PowerShell to execute commands and
malicious code.</p>
<p>During Operation Dream Job, Lazarus Group used PowerShell commands to
explore the environment of compromised victims.</p></td>
</tr>
<tr>
<td>.003</td>
<td>Command and Scripting Interpreter: Windows Command Shell</td>
<td><p>Lazarus Group malware uses cmd.exe to execute commands on a
compromised host. A Destover-like variant used by Lazarus Group uses a
batch file mechanism to delete its binaries from the system.</p>
<p>During Operation Dream Job, Lazarus Group launched malicious DLL
files, created new folders, and renamed folders with the use of the
Windows command shell.</p></td>
</tr>
<tr>
<td>.005</td>
<td>Command and Scripting Interpreter: Visual Basic</td>
<td><p>Lazarus Group has used VBA and embedded macros in Word documents
to execute malicious code.</p>
<p>During Operation Dream Job, Lazarus Group executed a VBA written
malicious macro after victims download malicious DOTM files; Lazarus
Group also used Visual Basic macro code to extract a double Base64
encoded DLL implant.</p></td>
</tr>
<tr>
<td rowspan="2"><strong>Enterprise</strong></td>
<td rowspan="2">T1584</td>
<td>.001</td>
<td>Compromise Infrastructure: Domains</td>
<td>For Operation Dream Job, Lazarus Group compromised domains in Italy
and other countries for their C2 infrastructure.</td>
</tr>
<tr>
<td>.004</td>
<td>Compromise Infrastructure: Server</td>
<td><p>Lazarus Group has compromised servers to stage malicious
tools.</p>
<p>For Operation Dream Job, Lazarus Group compromised servers to host
their malicious tools.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1543</td>
<td>.003</td>
<td>Create or Modify System Process: Windows Service</td>
<td>Several Lazarus Group malware families install themselves as new
services.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1485</td>
<td>Data Destruction</td>
<td>Lazarus Group has used a custom secure delete function to overwrite
file contents with data from heap memory.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1132</td>
<td>.001</td>
<td>Data Encoding: Standard Encoding</td>
<td>A Lazarus Group malware sample encodes data with base64.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1005</td>
<td>Data from Local System</td>
<td><p>Lazarus Group has collected data and files from compromised
networks.</p>
<p>During Operation Dream Job, Lazarus Group used malicious Trojans and
DLL files to exfiltrate data from an infected host.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1001</td>
<td>.003</td>
<td>Data Obfuscation: Protocol or Service Impersonation</td>
<td>Lazarus Group malware also uses a unique form of communication
encryption known as FakeTLS that mimics TLS but uses a different
encryption method, potentially evading SSL traffic
inspection/decryption.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1074</td>
<td>.001</td>
<td>Data Staged: Local Data Staging</td>
<td>Lazarus Group malware IndiaIndia saves information gathered about
the victim to a file that is saved in the %TEMP% directory, then
compressed, encrypted, and uploaded to a C2 server.</td>
</tr>
</tbody>
</table> 

# References

[1] Lazarus Group.[https://attack.mitre.org/groups/G0032/_](https://attack.mitre.org/groups/G0032/)

[2] Cyber Security NCC Group Resource Hub articles, The Lazarus group: North Korean scourge for +10 years.[https://www.nccgroup.com/the-lazarus-group-north-korean-scourge-for-plus10-years_](https://www.nccgroup.com/the-lazarus-group-north-korean-scourge-for-plus10-years)

[3] Lazarus Group, The APT with countless lives.[https://eurepoc.eu/wp-content/uploads/2024/02/Advanced-Persistent-Threat-Profile-Lazarus-February-2024.pdf_](https://eurepoc.eu/wp-content/uploads/2024/02/Advanced-Persistent-Threat-Profile-Lazarus-February-2024.pdf)

[4] Inside Lazarus Group: Analyzing North Korea's Most Infamous Crypto Hacks.[https://hacken.io/discover/lazarus-group/_](https://hacken.io/discover/lazarus-group/)

[5] Operation Dream Job.[https://attack.mitre.org/campaigns/C0022/_](https://attack.mitre.org/campaigns/C0022/)

[6] Native API.[https://attack.mitre.org/techniques/T1106/_](https://attack.mitre.org/techniques/T1106/)

[7] Virtualization/Sandbox Evasion: Time Based Evasion.[https://attack.mitre.org/techniques/T1497/003/_](https://attack.mitre.org/techniques/T1497/003/)