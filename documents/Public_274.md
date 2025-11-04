# Public_274

# MỤC TIÊU CHUNG

Tiến hành nghiên cứu toàn diện về nhóm Sandworm, tập trung vào chiến thuật, kỹ thuật và thủ tục của họ. Sử dụng khung MITRE ATT&CK để vạch ra các hoạt động của nhóm và cung cấp những hiểu biết có thể hành động.

Phát hiện của bản báo cáo này đóng một vai trò quan trọng trong việc củng cố khả năng phòng thủ chống lại kẻ thù này.

# Sandworm Team

Sandworm là một nhóm APT có liên hệ rộng rãi với các chiến dịch phá hoại nhắm vào hạ tầng trọng yếu (điện lực, viễn thông, chính phủ). Theo Mitre, nhóm bắt đầu hoạt động từ năm 2009. Sandworm Team thể hiện năng lực tấn công có hệ thống, từ xâm nhập – duy trì – điều khiển – phá hoại trên cả IT và OT

Một fun fact thú vị là tên gọi “ Sandworm ” không phải do họ tự đặt mà xuất phát từ các nhà nghiên cứu phương Tây, lấy cảm hứng từ loài sinh vật khổng lồ trong tiểu thuyết Dune – sống ẩn mình dưới cát rồi bất ngờ tấn công dữ dội.

## Nguồn gốc và tổ chức

Sandworm là một nhóm do nhà nước bảo trợ được liên kết với Nga. Nhiều tổ chức an ninh mạng và cơ quan chính phủ quốc tế đã gán nhóm này cho Cơ quan Tình báo Quân đội Nga (GRU) , cụ thể là một đơn vị tác chiến mạng thuộc Main Centre for Special Technologies (được ghi nhận là Unit 74455).

Sandworm được mô tả không phải là một nhóm “tội phạm mạng” độc lập mà là một đơn vị quân sự/tác chiến mạng có mục tiêu chiến lược, do đó hoạt động theo chỉ đạo, mục tiêu và năng lực của cơ quan nhà nước ( GRU ). Sự vận hành theo mô hình đơn vị quân đội giải thích việc nhóm sử dụng các chiến lược nhắm mục tiêu lớn (critical infrastructure), sự phối hợp giữa nhiều chiến dịch, và khả năng triển khai mã độc có tầm phá hoại cao.

## Các vụ tấn công nổi bật

Một số sự kiện tiêu biểu do Sandworm thực hiện:

  * 2009–2014: Hình thành, trinh sát và cắm chốt trong mạng mục tiêu (persistence đa lớp).

  * 2015–2016: Chiến dịch tại Ukraine: lạm dụng công cụ quản trị, thu thập thông tin xác thực, dùng script ufn.vbs, quan sát điều khiển SCADA gây mất điện.

  * 2017: Phát tán NotPetya với khả năng lây lan kiểu worm, khai thác MS17‑010, sử dụng chứng thực nội bộ để di chuyển ngang.

  * 2022: Chuỗi tấn công nhắm vào SCADA/ICS, duy trì hiện diện thông qua web‑shell bằng Neo‑REGEORG; thực thi tác vụ qua scilc.exe; phá hoại bằng CaddyWiper với khả năng Native API (T1106). Tấn công vào modem bằng AcidRain.


## Ukraine Power Grid

### Mục tiêu & Tác động

Nhóm này nhắm vào doanh nghiệp điện lực và hệ thống SCADA/DMS/EMS phụ trợ vận hành lưới. Gây ra gián đoạn cấp điện cục bộ, thao túng vận hành từ xa; gây mất dịch vụ và ảnh hưởng xã hội.

### Kỹ thuật & Công cụ đã ghi nhận

  * Credential Access

  * LSASS Memory (T1003.001) – trích xuất hash/creds từ tiến trình LSASS để leo thang đặc quyền nội bộ.

  * Brute Force (T1110) – thử mật khẩu/khớp tài khoản trên nhiều host để mở rộng kiểm soát.

  * Execution/Automation: Sử dụng script VBS ufn.vbs trong chuỗi tự động hoá hành động (kiểm soát, duy trì, hoặc dàn lệnh).

  * Lateral Movement: Khai thác thông tin xác thực thu được để di chuyển ngang qua mạng OT/IT; lạm dụng công cụ quản trị hợp lệ.


Khái quát lại:

Phishing/khai thác điểm yếu -> Cắm chốt + thu thập creds (T1003.001, T1110) -> Tự động hoá điều khiển (VBS ufn.vbs) -> Di chuyển vào tầng OT -> Thao túng SCADA -> Che giấu & rút lui.

## NotPetya 

### Mục tiêu & Tác động

Về bản chất NotPetya có hành vi ransomware nhưng thực chất phá hoại (wiper‑like) với khả năng tự lan truyền kiểu worm. Thông qua khai thác lỗ hổng SMBv1 MS17‑010, đồng thời lạm dụng chứng thực nội bộ (công cụ hợp lệ như PsExec/WMIC) để di chuyển ngang tốc độ cao.

Cuộc tấn công đã lan toàn cầu, gây gián đoạn chuỗi cung ứng, thiệt hại lớn về tài chính/vận hành.

## AcidRain 

### Mục tiêu & Tác động

AcidRain nhắm vào firmware/thành phần lưu trữ của modem/thiết bị mạng, gây mất kết nối diện rộng – đặc biệt nguy hiểm với hạ tầng vệ tinh/viễn thông khi bị đồng loạt tác động.

# Sandworm Team Techniques Used 
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
<td><a>T1087</a></td>
<td><a>.002</a></td>
<td><a>Account
Discovery</a>: <a>Domain
Account</a></td>
<td><a>Sandworm Team</a>
has used a tool to query Active Directory using LDAP, discovering
information about usernames listed in AD.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.003</a></td>
<td><a>Account
Discovery</a>: <a>Email
Account</a></td>
<td><a>Sandworm Team</a>
used malware to enumerate email settings, including usernames and
passwords, from the M.E.Doc application.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1098</a></td>
<td><a>Account
Manipulation</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used the
sp_addlinkedsrvlogin command in MS-SQL to create a link between a
created account and other servers in the network.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1583</a></td>
<td><a>Acquire
Infrastructure</a></td>
<td><a>Sandworm Team</a>
used various third-party email campaign management services to deliver
phishing emails.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.001</a></td>
<td><a>Domains</a></td>
<td><a>Sandworm Team</a>
has registered domain names and created URLs that are often designed to
mimic or spoof legitimate websites, such as email login pages, online
file sharing and storage websites, and password reset pages, while also
hosting these items on legitimate, compromised network
infrastructure.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.004</a></td>
<td><a>Server</a></td>
<td><a>Sandworm Team</a>
has leased servers from resellers instead of leasing infrastructure
directly from hosting companies to enable its operations.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1595</a></td>
<td><a>.002</a></td>
<td><a>Active
Scanning</a>: <a>Vulnerability
Scanning</a></td>
<td><a>Sandworm Team</a>
has scanned network infrastructure for vulnerabilities as part of its
operational planning.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1071</a></td>
<td><a>.001</a></td>
<td><a>Application
Layer Protocol</a>: <a>Web
Protocols</a></td>
<td><p><a>Sandworm
Team</a>'s BCS-server tool connects to the designated C2 server via
HTTP.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used <a>BlackEnergy</a> to
communicate between compromised hosts and their command-and-control
servers via HTTP post requests.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1110</a></td>
<td><a>Brute
Force</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used a
script to attempt RPC authentication against a number of hosts.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1059</a></td>
<td><a>.001</a></td>
<td><a>Command and
Scripting Interpreter</a>: <a>PowerShell</a></td>
<td><p><a>Sandworm Team</a>
has used PowerShell scripts to run a credential harvesting tool in
memory to evade defenses.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
PowerShell scripts to run a credential harvesting tool in memory to
evade defenses.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> utilized
a PowerShell utility called TANKTRAP to spread and launch a wiper using
Windows Group Policy.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.003</a></td>
<td><a>Command and
Scripting Interpreter</a>: <a>Windows Command
Shell</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used the
xp_cmdshell command in MS-SQL.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.005</a></td>
<td><a>Command and
Scripting Interpreter</a>: <a>Visual
Basic</a></td>
<td><p><a>Sandworm Team</a>
has created VBScripts to run an SSH server.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> installed
a VBA script called vba_macro.exe. This macro dropped FONTCACHE.DAT, the
primary <a>BlackEnergy</a> implant;
rundll32.exe, for executing the malware; NTUSER.log, an empty file; and
desktop.ini, the default file used to determine folder displays on
Windows machines.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> created
VBScripts to run on an SSH server.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1586</a></td>
<td><a>.001</a></td>
<td><a>Compromise
Accounts</a>: <a>Social Media
Accounts</a></td>
<td><a>Sandworm Team</a>
creates credential capture webpages to compromise existing, legitimate
social media accounts.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1554</a></td>
<td><a>Compromise Host
Software Binary</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used a
trojanized version of Windows Notepad to add a layer of persistence for
<a>Industroyer</a>.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1584</a></td>
<td><a>.004</a></td>
<td><a>Compromise
Infrastructure</a>: <a>Server</a></td>
<td><a>Sandworm Team</a>
compromised legitimate Linux servers running the EXIM mail transfer
agent for use in subsequent campaigns.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.005</a></td>
<td><a>Compromise
Infrastructure</a>: <a>Botnet</a></td>
<td><a>Sandworm Team</a>
has used a large-scale botnet to target Small Office/Home Office (SOHO)
network devices.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1136</a></td>
<td><a>.002</a></td>
<td><a>Create
Account</a>: <a>Domain
Account</a></td>
<td><p>During the <a>2015 Ukraine Electric
Power Attack</a>, <a>Sandworm Team</a> created
privileged domain accounts to be used for further exploitation and
lateral movement.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> created
two new accounts, "admin" and "система" (System). The accounts were then
assigned to a domain matching local operation and were delegated new
privileges.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1543</a></td>
<td><a>.002</a></td>
<td><a>Create or Modify
System Process</a>: <a>Systemd
Service</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a>
configured Systemd to maintain persistence of GOGETTER, specifying the
WantedBy=multi-user.target configuration to run GOGETTER when the system
begins accepting user logins.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.003</a></td>
<td><a>Create or Modify
System Process</a>: <a>Windows
Service</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used an
arbitrary system service to load at system boot for persistence for <a>Industroyer</a>. They
also replaced the ImagePath registry value of a Windows service with a
new backdoor binary.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1555</a></td>
<td><a>.003</a></td>
<td><a>Credentials from
Password Stores</a>: <a>Credentials from
Web Browsers</a></td>
<td><a>Sandworm Team</a>'s
CredRaptor tool can collect saved passwords from various internet
browsers.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1485</a></td>
<td><a>Data
Destruction</a></td>
<td><p><a>Sandworm Team</a>
has used <a>CaddyWiper</a>, <a>SDelete</a>, and the <a>BlackEnergy</a> KillDisk
component to overwrite files on victim systems. Additionally, <a>Sandworm Team</a> has used
the JUNKMAIL tool to overwrite files with null bytes.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> deployed
<a>CaddyWiper</a> on the
victim’s IT environment systems to wipe files related to the OT
capabilities, along with mapped drives, and physical drive
partitions.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1132</a></td>
<td><a>.001</a></td>
<td><a>Data
Encoding</a>: <a>Standard
Encoding</a></td>
<td><a>Sandworm Team</a>'s
BCS-server tool uses base64 encoding and HTML tags for the communication
traffic between the C2 server.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1486</a></td>
<td><a>Data Encrypted
for Impact</a></td>
<td><a>Sandworm Team</a>
has used <a>Prestige</a>
ransomware to encrypt data at targeted organizations in transportation
and related logistics industries in Ukraine and Poland.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1213</a></td>
<td><a>Data from
Information Repositories</a></td>
<td><a>Sandworm Team</a>
exfiltrates data of interest from enterprise databases using
Adminer.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1005</a></td>
<td><a>Data from Local
System</a></td>
<td><a>Sandworm Team</a>
has exfiltrated internal documents, files, and other data from
compromised hosts.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1491</a></td>
<td><a>.002</a></td>
<td><a>Defacement</a>:
<a>External
Defacement</a></td>
<td><a>Sandworm Team</a>
defaced approximately 15,000 websites belonging to Georgian government,
non-government, and private sector organizations in 2019.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1140</a></td>
<td><a>Deobfuscate/Decode
Files or Information</a></td>
<td><a>Sandworm Team</a>'s
VBS backdoor can decode Base64-encoded data and save it to the %TEMP%
folder. The group also decrypted received information using the Triple
DES algorithm and decompresses it using GZip.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1587</a></td>
<td><a>.001</a></td>
<td><a>Develop
Capabilities</a>: <a>Malware</a></td>
<td><a>Sandworm Team</a>
has developed malware for its operations, including malicious mobile
applications and destructive malware such as <a>NotPetya</a> and <a>Olympic
Destroyer</a>.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1561</a></td>
<td><a>.002</a></td>
<td><a>Disk Wipe</a>:
<a>Disk Structure
Wipe</a></td>
<td><a>Sandworm Team</a>
has used the <a>BlackEnergy</a> KillDisk
component to corrupt the infected system's master boot record.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1484</a></td>
<td><a>.001</a></td>
<td><a>Domain or Tenant
Policy Modification</a>: <a>Group Policy
Modification</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> leveraged
Group Policy Objects (GPOs) to deploy and execute malware.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1499</a></td>
<td><a>Endpoint Denial
of Service</a></td>
<td><a>Sandworm Team</a>
temporarily disrupted service to Georgian government, non-government,
and private sector websites after compromising a Georgian web hosting
provider in 2019.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1585</a></td>
<td><a>.001</a></td>
<td><a>Establish
Accounts</a>: <a>Social Media
Accounts</a></td>
<td><a>Sandworm Team</a>
has established social media accounts to disseminate victim
internal-only documents and other sensitive data.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>Establish
Accounts</a>: <a>Email
Accounts</a></td>
<td><a>Sandworm Team</a>
has created email accounts that mimic legitimate organizations for its
spearphishing operations.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1041</a></td>
<td><a>Exfiltration
Over C2 Channel</a></td>
<td><a>Sandworm Team</a>
has sent system information to its C2 server using HTTP.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1190</a></td>
<td><a>Exploit
Public-Facing Application</a></td>
<td><a>Sandworm Team</a>
exploits public-facing applications for initial access and to acquire
infrastructure, such as exploitation of the EXIM mail transfer agent in
Linux systems.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1203</a></td>
<td><a>Exploitation for
Client Execution</a></td>
<td><a>Sandworm Team</a>
has exploited vulnerabilities in Microsoft PowerPoint via OLE objects
(CVE-2014-4114) and Microsoft Word via crafted TIFF images
(CVE-2013-3906).</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1133</a></td>
<td><a>External Remote
Services</a></td>
<td><p><a>Sandworm Team</a>
has used Dropbear SSH with a hardcoded backdoor password to maintain
persistence within the target network. <a>Sandworm Team</a> has also
used VPN tunnels established in legitimate software company
infrastructure to gain access to internal networks of that software
company's users.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> installed
a modified Dropbear SSH client as the backdoor to target
systems.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1083</a></td>
<td><a>File and
Directory Discovery</a></td>
<td><a>Sandworm Team</a>
has enumerated files on a compromised host.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1592</a></td>
<td><a>.002</a></td>
<td><a>Gather Victim
Host Information</a>: <a>Software</a></td>
<td><a>Sandworm Team</a>
has researched software code to enable supply-chain operations, most
notably for the 2017 <a>NotPetya</a> attack. <a>Sandworm Team</a> also
collected a list of computers using specific software as part of its
targeting efforts.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1589</a></td>
<td><a>.002</a></td>
<td><a>Gather Victim
Identity Information</a>: <a>Email
Addresses</a></td>
<td><a>Sandworm Team</a>
has obtained valid emails addresses while conducting research against
target organizations that were subsequently used in spearphishing
campaigns.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.003</a></td>
<td><a>Gather Victim
Identity Information</a>: <a>Employee
Names</a></td>
<td><a>Sandworm Team</a>'s
research of potential victim organizations included the identification
and collection of employee information.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1590</a></td>
<td><a>.001</a></td>
<td><a>Gather Victim
Network Information</a>: <a>Domain
Properties</a></td>
<td><a>Sandworm Team</a>
conducted technical reconnaissance of the Parliament of Georgia's
official internet domain prior to its 2019 attack.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1591</a></td>
<td><a>.002</a></td>
<td><a>Gather Victim
Org Information</a>: <a>Business
Relationships</a></td>
<td>In preparation for its attack against the 2018 Winter Olympics, <a>Sandworm Team</a> conducted
online research of partner organizations listed on an official
PyeongChang Olympics partnership site.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1562</a></td>
<td><a>.001</a></td>
<td><a>Impair
Defenses</a>: <a>Disable or Modify
Tools</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> modified
in-registry internet settings to lower internet security.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>Impair
Defenses</a>: <a>Disable Windows
Event Logging</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> disabled
event logging on compromised systems.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1070</a></td>
<td><a>.004</a></td>
<td><a>Indicator
Removal</a>: <a>File
Deletion</a></td>
<td><p><a>Sandworm Team</a>
has used backdoors that can delete files used in an attack from an
infected system.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, vba_macro.exe deletes itself after
FONTCACHE.DAT, rundll32.exe, and the associated .lnk file is
delivered.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1105</a></td>
<td><a>Ingress Tool
Transfer</a></td>
<td><p><a>Sandworm Team</a>
has pushed additional malicious tools onto an infected system to steal
user credentials, move laterally, and destroy data.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> pushed
additional malicious tools onto an infected system to steal user
credentials, move laterally, and destroy data.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1490</a></td>
<td><a>Inhibit System
Recovery</a></td>
<td><a>Sandworm Team</a>
uses <a>Prestige</a> to
delete the backup catalog from the target system using:
C:\Windows\System32\wbadmin.exe delete catalog -quiet and to delete
volume shadow copies using: C:\Windows\System32\vssadmin.exe delete
shadows /all /quiet.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1056</a></td>
<td><a>.001</a></td>
<td><a>Input
Capture</a>: <a>Keylogging</a></td>
<td><p><a>Sandworm Team</a>
has used a keylogger to capture keystrokes by using the SetWindowsHookEx
function.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> gathered
account credentials via a <a>BlackEnergy</a> keylogger
plugin.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1570</a></td>
<td><a>Lateral Tool
Transfer</a></td>
<td><p><a>Sandworm Team</a>
has used move to transfer files to a network share and has copied
payloads--such as <a>Prestige</a>
ransomware--to an Active Directory Domain Controller and distributed via
the Default Domain Group Policy Object. Additionally, <a>Sandworm Team</a> has
transferred an ISO file into the OT network to gain initial access.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> moved
their tools laterally within the corporate network and between the ICS
and corporate network.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used move
to transfer files to a network share.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used a
Group Policy Object (GPO) to copy <a>CaddyWiper</a>'s
executable msserver.exe from a staging server to a local hard drive
before deployment.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1036</a></td>
<td><a>Masquerading</a></td>
<td><a>Sandworm Team</a>
masqueraded malicious installers as Windows update packages to evade
defense and entice users to execute binaries.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.004</a></td>
<td><a>Masquerade
Task or Service</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> leveraged
Systemd service units to masquerade GOGETTER malware as legitimate or
seemingly legitimate services.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.005</a></td>
<td><a>Match
Legitimate Resource Name or Location</a></td>
<td><p><a>Sandworm Team</a>
has avoided detection by naming a malicious binary explorer.exe.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, DLLs and EXEs with filenames
associated with common electric power sector protocols were used to
masquerade files.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.008</a></td>
<td><a>Masquerade
File Type</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a>
masqueraded executables as .txt files.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.010</a></td>
<td><a>Masquerade
Account Name</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> created
two new accounts, "admin" and "система" (System).</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1112</a></td>
<td><a>Modify
Registry</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> modified
in-registry Internet settings to lower internet security before
launching rundll32.exe, which in-turn launches the malware and
communicates with C2 servers over the Internet. .</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1106</a></td>
<td><a>Native
API</a></td>
<td><a>Sandworm Team</a>
uses <a>Prestige</a> to
disable and restore file system redirection by using the following
functions: Wow64DisableWow64FsRedirection() and
Wow64RevertWow64FsRedirection().</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1040</a></td>
<td><a>Network
Sniffing</a></td>
<td><p><a>Sandworm Team</a>
has used intercepter-NG to sniff passwords in network traffic.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used <a>BlackEnergy</a>’s network
sniffer module to discover user credentials being sent over the network
between the local LAN and the power grid’s industrial control
systems.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1095</a></td>
<td><a>Non-Application
Layer Protocol</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> proxied
C2 communications within a TLS-based tunnel.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1571</a></td>
<td><a>Non-Standard
Port</a></td>
<td><a>Sandworm Team</a>
has used port 6789 to accept connections on the group's SSH server.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1027</a></td>
<td><a>Obfuscated Files
or Information</a></td>
<td><p><a>Sandworm Team</a>
has used Base64 encoding within malware variants.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
heavily obfuscated code with <a>Industroyer</a> in its
Windows Notepad backdoor.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>Software
Packing</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used UPX
to pack a copy of <a>Mimikatz</a>.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.010</a></td>
<td><a>Command
Obfuscation</a></td>
<td><a>Sandworm Team</a>
has used ROT13 encoding, AES encryption and compression with the zlib
library for their Python-based backdoor.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1588</a></td>
<td><a>.002</a></td>
<td><a>Obtain
Capabilities</a>: <a>Tool</a></td>
<td><a>Sandworm Team</a>
has acquired open-source tools for their operations, including <a>Invoke-PSImage</a>, which
was used to establish an encrypted channel from a compromised host to <a>Sandworm Team</a>'s C2
server in preparation for the 2018 Winter Olympics attack, as well as <a>Impacket</a> and
RemoteExec, which were used in their 2022 <a>Prestige</a> operations.
Additionally, <a>Sandworm
Team</a> has used <a>Empire</a>, <a>Cobalt Strike</a> and <a>PoshC2</a>.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.006</a></td>
<td><a>Obtain
Capabilities</a>: <a>Vulnerabilities</a></td>
<td>In 2017, <a>Sandworm
Team</a> conducted technical research related to vulnerabilities
associated with websites used by the Korean Sport and Olympic Committee,
a Korean power company, and a Korean airport.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1003</a></td>
<td><a>.001</a></td>
<td><a>OS Credential
Dumping</a>: <a>LSASS
Memory</a></td>
<td><p><a>Sandworm Team</a>
has used its plainpwd tool, a modified version of <a>Mimikatz</a>, and
comsvcs.dll to dump Windows credentials from system memory.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used <a>Mimikatz</a> to capture
and use legitimate credentials.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.003</a></td>
<td><a>OS Credential
Dumping</a>: <a>NTDS</a></td>
<td><a>Sandworm Team</a>
has used ntdsutil.exe to back up the Active Directory database, likely
for credential access.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1566</a></td>
<td><a>.001</a></td>
<td><a>Phishing</a>: <a>Spearphishing
Attachment</a></td>
<td><p><a>Sandworm Team</a>
has delivered malicious Microsoft Office and ZIP file attachments via
spearphishing emails.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> obtained
their initial foothold into many IT systems using Microsoft Office
attachments delivered through phishing emails.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>Phishing</a>: <a>Spearphishing
Link</a></td>
<td><a>Sandworm Team</a>
has crafted phishing emails containing malicious hyperlinks.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1598</a></td>
<td><a>.003</a></td>
<td><a>Phishing for
Information</a>: <a>Spearphishing
Link</a></td>
<td><a>Sandworm Team</a>
has crafted spearphishing emails with hyperlinks designed to trick
unwitting recipients into revealing their account credentials.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1055</a></td>
<td><a>Process
Injection</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> loaded <a>BlackEnergy</a> into
svchost.exe, which then launched iexplore.exe for their C2.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1572</a></td>
<td><a>Protocol
Tunneling</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> deployed
the GOGETTER tunneler software to establish a "Yamux" TLS-based C2
channel with an external server(s).</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1090</a></td>
<td><a>Proxy</a></td>
<td><a>Sandworm Team</a>'s
BCS-server tool can create an internal proxy server to redirect traffic
from the adversary-controlled C2 to internal servers which may not be
connected to the internet, but are interconnected locally.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1219</a></td>
<td><a>Remote Access
Tools</a></td>
<td><a>Sandworm Team</a>
has used remote administration tools or remote industrial control system
client software for execution and to maliciously release electricity
breakers.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1021</a></td>
<td><a>.002</a></td>
<td><a>Remote
Services</a>: <a>SMB/Windows Admin
Shares</a></td>
<td><p><a>Sandworm Team</a>
has copied payloads to the ADMIN$ share of remote systems and run net
use to connect to network shares.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> utilized
net use to connect to network shares.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1018</a></td>
<td><a>Remote System
Discovery</a></td>
<td><p><a>Sandworm Team</a>
has used a tool to query Active Directory using LDAP, discovering
information about computers listed in AD.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> remotely
discovered systems over LAN connections. OT systems were visible from
the IT network as well, giving adversaries the ability to discover
operational assets.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> checked
for connectivity to resources within the network and used LDAP to query
Active Directory, discovering information about computers listed in
AD.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1053</a></td>
<td><a>.005</a></td>
<td><a>Scheduled
Task/Job</a>: <a>Scheduled
Task</a></td>
<td><p><a>Sandworm Team</a>
leveraged SHARPIVORY, a .NET dropper that writes embedded payload to
disk and uses scheduled tasks to persist on victim machines.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> leveraged
Scheduled Tasks through a Group Policy Object (GPO) to execute <a>CaddyWiper</a> at a
predetermined time.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1593</a></td>
<td><a>Search Open
Websites/Domains</a></td>
<td><a>Sandworm Team</a>
researched Ukraine's unique legal entity identifier (called an "EDRPOU"
number), including running queries on the EDRPOU website, in preparation
for the <a>NotPetya</a>
attack. <a>Sandworm
Team</a> has also researched third-party websites to help it craft
credible spearphishing emails.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1594</a></td>
<td><a>Search
Victim-Owned Websites</a></td>
<td><a>Sandworm Team</a>
has conducted research against potential victim websites as part of its
operational planning.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1505</a></td>
<td><a>.001</a></td>
<td><a>Server Software
Component</a>: <a>SQL Stored
Procedures</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
various MS-SQL stored procedures.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.003</a></td>
<td><a>Server Software
Component</a>: <a>Web Shell</a></td>
<td><p><a>Sandworm Team</a>
has used webshells including <a>P.A.S. Webshell</a> to
maintain access to victim networks.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> deployed
the Neo-REGEORG webshell on an internet-facing server.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1489</a></td>
<td><a>Service
Stop</a></td>
<td><a>Sandworm Team</a>
attempts to stop the MSSQL Windows service to ensure successful
encryption of locked files.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1072</a></td>
<td><a>Software
Deployment Tools</a></td>
<td><a>Sandworm Team</a>
has used the commercially available tool RemoteExec for agentless remote
code execution.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1608</a></td>
<td><a>.001</a></td>
<td><a>Stage
Capabilities</a>: <a>Upload
Malware</a></td>
<td><a>Sandworm Team</a>
staged compromised versions of legitimate software installers in forums
to enable initial access to executing user.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1539</a></td>
<td><a>Steal Web
Session Cookie</a></td>
<td><a>Sandworm Team</a>
used information stealer malware to collect browser session
cookies.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1195</a></td>
<td><a>Supply Chain
Compromise</a></td>
<td><a>Sandworm Team</a>
staged compromised versions of legitimate software installers on forums
to achieve initial, untargetetd access in victim environments.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>Compromise
Software Supply Chain</a></td>
<td><a>Sandworm Team</a>
has distributed <a>NotPetya</a> by
compromising the legitimate Ukrainian accounting software M.E.Doc and
replacing a legitimate software update with a malicious one.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1218</a></td>
<td><a>.011</a></td>
<td><a>System Binary
Proxy Execution</a>: <a>Rundll32</a></td>
<td><p><a>Sandworm Team</a>
used a backdoor which could execute a supplied DLL using
rundll32.exe.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used a
backdoor which could execute a supplied DLL using rundll32.exe.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1082</a></td>
<td><a>System
Information Discovery</a></td>
<td><a>Sandworm Team</a>
used a backdoor to enumerate information about the infected system's
operating system.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1049</a></td>
<td><a>System Network
Connections Discovery</a></td>
<td><a>Sandworm Team</a>
had gathered user, IP address, and server data related to RDP sessions
on a compromised host. It has also accessed network diagram files useful
for understanding how a host's network was configured.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1033</a></td>
<td><a>System
Owner/User Discovery</a></td>
<td><a>Sandworm Team</a>
has collected the username from a compromised host.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1199</a></td>
<td><a>Trusted
Relationship</a></td>
<td><a>Sandworm Team</a>
has used dedicated network connections from one victim organization to
gain unauthorized access to a separate organization. Additionally, <a>Sandworm Team</a> has
accessed Internet service providers and telecommunication entities that
provide mobile connectivity.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1204</a></td>
<td><a>.001</a></td>
<td><a>User
Execution</a>: <a>Malicious
Link</a></td>
<td><a>Sandworm Team</a>
has tricked unwitting recipients into clicking on malicious hyperlinks
within emails crafted to resemble trustworthy senders.</td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>User
Execution</a>: <a>Malicious
File</a></td>
<td><p><a>Sandworm Team</a>
has tricked unwitting recipients into clicking on spearphishing
attachments and enabling malicious macros embedded within files.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> leveraged
Microsoft Office attachments which contained malicious macros that were
automatically executed once the user permitted them.</p></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1078</a></td>
<td><a>Valid
Accounts</a></td>
<td><p><a>Sandworm Team</a>
have used previously acquired legitimate credentials prior to
attacks.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
valid accounts on the corporate network to escalate privileges, move
laterally, and establish persistence within the corporate
network.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><a>.002</a></td>
<td><a>Domain
Accounts</a></td>
<td><a>Sandworm Team</a>
has used stolen credentials to access administrative accounts within the
domain.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1102</a></td>
<td><a>.002</a></td>
<td><a>Web Service</a>:
<a>Bidirectional
Communication</a></td>
<td><a>Sandworm Team</a>
has used the Telegram Bot API from Telegram Messenger to send and
receive commands to its Python backdoor. <a>Sandworm Team</a> also used
legitimate M.E.Doc software update check requests for sending and
receiving commands and hosted malicious payloads on putdrive.com.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2"><a>T1047</a></td>
<td><a>Windows
Management Instrumentation</a></td>
<td><p><a>Sandworm Team</a>
has used <a>Impacket</a>’s WMIexec
module for remote code execution and VBScript to run WMI queries.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, WMI in scripts were used for remote
execution and system surveys.</p></td>
</tr>
<tr>
<td><strong>Mobile</strong></td>
<td colspan="2"><a>T1660</a></td>
<td><a>Phishing</a></td>
<td><a>Sandworm Team</a>
used SMS-based phishing to target victims with malicious links.</td>
</tr>
<tr>
<td><strong>Mobile</strong></td>
<td colspan="2"><a>T1409</a></td>
<td><a>Stored
Application Data</a></td>
<td><a>Sandworm Team</a>
can collect encrypted Telegram and Signal communications.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0895</a></td>
<td><a>Autorun
Image</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
existing hypervisor access to map an ISO image named a.iso to a virtual
machine running a SCADA server. The SCADA server’s operating system was
configured to autorun CD-ROM images, and as a result, a malicious VBS
script on the ISO image was automatically executed.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0803</a></td>
<td><a>Block Command
Message</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> blocked
command messages by using malicious firmware to render
serial-to-ethernet converters inoperable.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0804</a></td>
<td><a>Block Reporting
Message</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> blocked
reporting messages by using malicious firmware to render
serial-to-ethernet converters inoperable.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0805</a></td>
<td><a>Block Serial
COM</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> overwrote
the serial-to-ethernet converter firmware, rendering the devices not
operational. This meant that communication to the downstream serial
devices was either not possible or more difficult.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0807</a></td>
<td><a>Command-Line
Interface</a></td>
<td><p><a>Sandworm Team</a>
uses the MS-SQL server xp_cmdshell command, and PowerShell to execute
commands.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> supplied
the name of the payload DLL to <a>Industroyer</a> via a
command line parameter.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> leveraged
the SCIL-API on the MicroSCADA platform to execute commands through the
scilc.exe binary.</p></td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0885</a></td>
<td><a>Commonly Used
Port</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used port
443 to communicate with their C2 servers.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0884</a></td>
<td><a>Connection
Proxy</a></td>
<td><p><a>Sandworm Team</a>
establishes an internal proxy prior to the installation of backdoors
within the network.</p>
<p>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a>
established an internal proxy prior to the installation of backdoors
within the network.</p></td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0813</a></td>
<td><a>Denial of
Control</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>KillDisk</a> rendered
devices that were necessary for remote recovery unusable, including at
least one RTU. Additionally, <a>Sandworm Team</a> overwrote
the firmware for serial-to-ethernet converters, denying operators
control of the downstream devices.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0814</a></td>
<td><a>Denial of
Service</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, power company phone line operators
were hit with a denial of service attack so that they couldn’t field
customers’ calls about outages. Operators were also denied service to
their downstream devices when their serial-to-ethernet converters had
their firmware overwritten, which bricked the devices.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0816</a></td>
<td><a>Device
Restart/Shutdown</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> scheduled
the uninterruptable power supplies (UPS) to shutdown data and telephone
servers via the UPS management interface.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0819</a></td>
<td><a>Exploit
Public-Facing Application</a></td>
<td><a>Sandworm Team</a>
actors exploited vulnerabilities in GE's Cimplicity HMI and
Advantech/Broadwin WebAccess HMI software which had been directly
exposed to the internet.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0822</a></td>
<td><a>External Remote
Services</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
Valid Accounts taken from the Windows Domain Controller to access the
control system Virtual Private Network (VPN) used by grid
operators.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0823</a></td>
<td><a>Graphical User
Interface</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> utilized
HMI GUIs in the SCADA environment to open breakers.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0867</a></td>
<td><a>Lateral Tool
Transfer</a></td>
<td><p>During the <a>2015 Ukraine Electric
Power Attack</a>, <a>Sandworm Team</a> moved
their tools laterally within the ICS network.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used a
VBS script to facilitate lateral tool transfer. The VBS script was used
to copy ICS-specific payloads with the following command: cscript
C:\Backinfo\ufn.vbs C:\Backinfo\101.dll C:\Delta\101.dll</p></td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0826</a></td>
<td><a>Loss of
Availability</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> opened
the breakers at the infected sites, shutting the power off for thousands
of businesses and households for around 6 hours.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0827</a></td>
<td><a>Loss of
Control</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, operators were shut out of their
equipment either through the denial of peripheral use or the degradation
of equipment. Operators were therefore unable to recover from the
incident through their traditional means. Much of the power was restored
manually.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0828</a></td>
<td><a>Loss of
Productivity and Revenue</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, power breakers were opened which
caused the operating companies to be unable to deliver power, and left
thousands of businesses and households without power for around 6
hours.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0831</a></td>
<td><a>Manipulation of
Control</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> opened
live breakers via remote commands to the HMI, causing blackouts.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0849</a></td>
<td><a>Masquerading</a></td>
<td>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a>
transferred executable files as .txt and then renamed them to .exe,
likely to avoid detection through extension tracking.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0886</a></td>
<td><a>Remote
Services</a></td>
<td><p>During the <a>2015 Ukraine Electric
Power Attack</a>, <a>Sandworm Team</a> used an
IT helpdesk software to move the mouse on ICS control devices to
maliciously release electricity breakers.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
MS-SQL access to a pivot machine, allowing code execution throughout the
ICS network.</p></td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0846</a></td>
<td><a>Remote System
Discovery</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> remotely
discovered operational assets once on the OT network.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0853</a></td>
<td><a>Scripting</a></td>
<td><p>During the <a>2016 Ukraine Electric
Power Attack</a>, <a>Sandworm Team</a> utilized
VBS and batch scripts for file movement and as wrappers for PowerShell
execution.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> utilizes
a Visual Basic script lun.vbs to execute n.bat which then executed the
MicroSCADA scilc.exe command.</p></td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0894</a></td>
<td><a>System Binary
Proxy Execution</a></td>
<td>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> executed
a MicroSCADA application binary scilc.exe to send a predefined list of
SCADA instructions specified in a file defined by the adversary, s1.txt.
The executed command C:\sc\prog\exec\scilc.exe -do pack\scil\s1.txt
leverages the SCADA software to send unauthorized command messages to
remote substations.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0857</a></td>
<td><a>System
Firmware</a></td>
<td>During the <a>2015
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> overwrote
the serial-to-ethernet gateways with custom firmware to make systems
either disabled, shutdown, and/or unrecoverable.</td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0855</a></td>
<td><a>Unauthorized
Command Message</a></td>
<td><p>During the <a>2015 Ukraine Electric
Power Attack</a>, <a>Sandworm Team</a> issued
unauthorized commands to substation breaks after gaining control of
operator workstations and accessing a distribution management system
(DMS) application.</p>
<p>During the <a>2022
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used the
MicroSCADA SCIL-API to specify a set of SCADA instructions, including
the sending of unauthorized commands to substation devices.</p></td>
</tr>
<tr>
<td><strong>ICS</strong></td>
<td colspan="2"><a>T0859</a></td>
<td><a>Valid
Accounts</a></td>
<td><p>During the <a>2015 Ukraine Electric
Power Attack</a>, <a>Sandworm Team</a> used
valid accounts to laterally move through VPN connections and dual-homed
systems. Sandworm Team used the credentials of valid accounts to
interact with client applications and access employee workstations
hosting HMI applications.</p>
<p>During the <a>2016
Ukraine Electric Power Attack</a>, <a>Sandworm Team</a> used
valid accounts to laterally move through VPN connections and dual-homed
systems.</p></td>
</tr>
</tbody>
</table>