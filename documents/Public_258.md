# Public_258

# MỤC TIÊU CHUNG

Tiến hành nghiên cứu toàn diện về nhóm Salt Typhoon, tập trung vào chiến thuật, kỹ thuật và thủ tục của họ. Sử dụng khung MITRE ATT&CK để vạch ra các hoạt động của nhóm và cung cấp những hiểu biết có thể hành động.

Phát hiện của bản báo cáo này đóng một vai trò quan trọng trong việc củng cố khả năng phòng thủ chống lại kẻ thù này.

# Salt Typhoon

Salt Typhoon là một nhóm do Nhà nước Cộng hòa Nhân dân Trung Hoa (PRC) hậu thuẫn, đã hoạt động ít nhất từ năm 2019 và chịu trách nhiệm cho nhiều vụ xâm nhập vào hạ tầng mạng của các nhà cung cấp dịch vụ internet (ISP) lớn tại Hoa Kỳ. [[1_](https://attack.mitre.org/groups/G1045/)]

JumbledPath

Nhóm này custom nhiều loại mã độc khác nhau, một trong số đó là JumbledPath với ID S1206. [[2_](https://attack.mitre.org/software/S1206/)]

JumbledPath là một tiện ích (utility) được xây dựng tùy chỉnh bằng ngôn ngữ GO , đã được Salt Typhoon sử dụng ít nhất từ năm 2024 để thực hiện packet capture trên các thiết bị Cisco từ xa. JumbledPath được biên dịch dưới dạng ELF binary sử dụng kiến trúc x86-64, điều này khiến nó có khả năng được sử dụng trên các hệ điều hành Linux và các thiết bị mạng từ nhiều nhà cung cấp khác nhau.[[3_](https://blog.talosintelligence.com/salt-typhoon-analysis/)]

Một trong các kỹ thuật mà JumbledPath thực hiện đó là hành vi xóa log tại ID T1070.002. [[4_](https://attack.mitre.org/techniques/T1070/002/)]

JumbledPath Techniques Used
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Domain</strong></td>
<td><strong>ID</strong></td>
<td><strong>Name</strong></td>
<td><strong>Use</strong></td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1560</td>
<td>Archive Collected Data</td>
<td>JumbledPath can compress and encrypt exfiltrated packet captures
from targeted devices.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1665</a></td>
<td>Hide Infrastructure</td>
<td>JumbledPath can use a chain of jump hosts to communicate with
compromised devices to obscure actor infrastructure.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1562</a></td>
<td>Impair Defenses</td>
<td>JumbledPath can impair logging on all devices used along its
connection path to compromised hosts.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1070</a></td>
<td>Indicator Removal: Clear Linux or Mac System Logs</td>
<td>JumbledPath can clear logs on all devices used along its connection
path to compromised network infrastructure.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1104</a></td>
<td>Multi-Stage Channels</td>
<td>JumbledPath can communicate over a unique series of connections to
send and retrieve data from exploited devices.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td><a>T1040</a></td>
<td>Network Sniffing</td>
<td>JumbledPath has the ability to perform packet capture on remote
devices via actor-defined jump-hosts.</td>
</tr>
</tbody>
</table> 

GHOSTSPIDER

GHOSTSPIDER được xem như là một backdoor đa mô hình tinh vi được thiết kế với nhiều lớp để load các mô-đun khác nhau dựa trên các mục đích cụ thể. Backdoor này giao tiếp với C2 của mình bằng giao thức tùy chỉnh được bảo vệ bởi bảo mật lớp vận chuyển (TLS), đảm bảo giao tiếp an toàn. [[5_](https://www.trendmicro.com/en_vn/research/24/k/earth-estries.html)]

Dưới đây là list domain mà GHOSTSPIDER kết nối về C2, có thể nói đa phần đều gửi về .com, đặc biệt tròn đó có 1 doamin đuôi .dev

|<image_1>|

GHOSTSPIDER Techniques Used

Mặc dù đã có mã định danh là FGS5008 trên MITRE nhưng chưa có nội dung chi tiết công khai [[6_](https://fight.mitre.org/software/FGS5008/)]

# Salt Typhoon Techniques Used
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
<td>T1098</td>
<td>.<a>004</a></td>
<td>Account Manipulation: SSH Authorized Keys</td>
<td>Salt Typhoon has added SSH authorized_keys under root or other users
at the Linux level on compromised network devices.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1110</td>
<td>.002</td>
<td>Brute Force: Password Cracking</td>
<td>Salt Typhoon has cracked passwords for accounts with weak encryption
obtained from the configuration files of compromised network
devices.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1136</td>
<td>Create Account</td>
<td>Salt Typhoon has created Linux-level users on compromised network
devices through modification of /etc/shadow and /etc/passwd.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1602</td>
<td>.002</td>
<td>Data from Configuration Repository: Network Device Configuration
Dump</td>
<td>Salt Typhoon has attempted to acquire credentials by dumping network
device configurations.[</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1587</td>
<td>.001</td>
<td>Develop Capabilities: Malware</td>
<td>Salt Typhoon has used custom tooling including JumbledPath.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1048</td>
<td>.003</td>
<td>Exfiltration Over Alternative Protocol: Exfiltration Over
Unencrypted Non-C2 Protocol</td>
<td>Salt Typhoon has exfiltrated configuration files from exploited
network devices over FTP and TFTP.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1190</td>
<td>Exploit Public-Facing Application</td>
<td>Salt Typhoon has exploited CVE-2018-0171 in the Smart Install
feature of Cisco IOS and Cisco IOS XE software for initial access.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1590</td>
<td>.004</td>
<td>Gather Victim Network Information: Network Topology</td>
<td>Salt Typhoon has used configuration files from exploited network
devices to help discover upstream and downstream network segments.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1562</td>
<td>.004</td>
<td>Impair Defenses: Disable or Modify System Firewall</td>
<td>Salt Typhoon has made changes to the Access Control List (ACL) and
loopback interface address on compromised devices.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1070</td>
<td>.002</td>
<td>Indicator Removal: Clear Linux or Mac System Logs</td>
<td>Salt Typhoon has cleared logs including .bash_history, auth.log,
lastlog, wtmp, and btmp.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1040</td>
<td>Network Sniffing</td>
<td>Salt Typhoon has used a variety of tools and techniques to capture
packet data between network interfaces.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1588</td>
<td>.002</td>
<td>Obtain Capabilities: Tool</td>
<td>Salt Typhoon has used publicly available tooling to exploit
vulnerabilities.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td colspan="2">T1572</td>
<td>Protocol Tunneling</td>
<td>Salt Typhoon has modified device configurations to create and use
Generic Routing Encapsulation (GRE) tunnels.</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>T1021</td>
<td>.004</td>
<td>Remote Services: SSH</td>
<td>Salt Typhoon has modified the loopback address on compromised
switches and used them as the source of SSH connections to additional
devices within the target environment, allowing them to bypass access
control lists (ACLs).</td>
</tr>
</tbody>
</table> 

# 4\. References

[1] Salt Typhoon.[https://attack.mitre.org/groups/G1045/_](https://attack.mitre.org/groups/G1045/)

[2] JumbledPath.[https://attack.mitre.org/software/S1206/_](https://attack.mitre.org/software/S1206/)

[3] Weathering the storm: In the midst of a Typhoon.[https://blog.talosintelligence.com/salt-typhoon-analysis/_](https://blog.talosintelligence.com/salt-typhoon-analysis/)

[4] Indicator Removal: Clear Linux or Mac System Logs.[https://attack.mitre.org/techniques/T1070/002/_](https://attack.mitre.org/techniques/T1070/002/)

[5] Game of Emperor: Unveiling Long Term Earth Estries Cyber Intrusions.[https://www.trendmicro.com/en_vn/research/24/k/earth-estries.html_](https://www.trendmicro.com/en_vn/research/24/k/earth-estries.html)

[6] Ghost Spider.[https://fight.mitre.org/software/FGS5008/_](https://fight.mitre.org/software/FGS5008/)