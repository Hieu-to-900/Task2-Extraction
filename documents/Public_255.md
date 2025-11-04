# Public_255

# Tổng quan

Credential Dumping là kỹ thuật mà kẻ tấn công sử dụng để trích xuất thông tin chứng thực (mật khẩu, hash, token) từ hệ thống bị xâm. Các nguồn dữ liệu điển hình bao gồm SAM, NTDS, /etc/shadow, hoặc trực tiếp từ bộ nhớ (process memory). Kỹ thuật này thường nhằm mục tiêu mở rộng truy cập trong mạng nội bộ và hỗ trợ lateral movement.

Mục tiêu báo cáo: mô tả kỹ thuật, các biến thể, phương pháp phát hiện, mitigation, và cung cấp một bảng sự kiện mẫu lớn phục vụ cho bài lab / phân tích forensics.

# Chi tiết kỹ thuật

Các phương thức credential dumping phổ biến:  
\- Đọc trực tiếp tệp lưu trữ chứng thực: ví dụ /etc/shadow trên Linux, SAM/NTDS trên Windows.  
\- Dump từ bộ nhớ: đọc process memory của tiến trình lưu giữ thông tin chứng thực (ví dụ LSASS trên Windows).  
\- Sử dụng công cụ/tiện ích: mimikatz, gsecdump, pwdump, creddump, secretos.  
\- Lấy thông tin từ file cấu hình, script hoặc backup không được mã hóa.

Lưu ý về môi trường: hệ thống Windows thường lưu nhiều thông tin nhạy cảm trong memory của tiến trình LSASS hoặc trong AD database (NTDS.dit). Trên Linux, file /etc/shadow và các file cấu hình ứng dụng là mục tiêu.

# Kịch bản tấn công 

Mô tả kịch bản: Kẻ tấn công xâm nhập một host công cộng (ví dụ quản trị từ xa), cài payload để thu thập hash từ LSASS, crack hoặc reuse hash để SSH sang host khác, từ đó truy cập database chứa dữ liệu nhạy cảm.

Chi tiết bước:  
1) Recon - tìm host quản trị và các tài khoản có quyền cao.  
2) Initial Access - khai thác vuln hoặc sử dụng credential phishing để có foothold.  
3) Dump - sử dụng công cụ để dump memory/credential stores.  
4) Abuse - sử dụng credential để di chuyển ngang hoặc nâng quyền.  
5) Persistence & Exfil - cài backdoor và exfil dữ liệu.

# Phát hiện và biện pháp giảm thiểu

Phát hiện:  
\- Giám sát hoạt động tiến trình bất thường (lsass.exe memory read, procdump usage).  
\- Tìm kiếm hành vi dump file, outbound connections sau khi dump.  
\- Sử dụng YARA/Suricata để phát hiện chuỗi đặc trưng.

Giảm thiểu:  
\- Bật LAPS / Credential Guard trên Windows, áp dụng EDR.  
\- Hạn chế quyền: least privilege, segment network.  
\- Bảo vệ tệp nhạy cảm (chặn truy cập /etc/shadow), áp dụng mật khẩu mạnh và 2FA.

# Hướng dẫn triển khai Lab

Phần này mô tả cách sử dụng bảng sự kiện mẫu trong quá trình lab: cách dựng môi trường, tạo activity mô phỏng, và cách dùng bảng sự kiện để thực hành phân tích.

Mẹo: Sử dụng docker-compose để dựng mạng lab, seed file logs và script simulate_swipe.sh / simulate_lsass_dump.sh để tạo các sự kiện tương ứng.

Bảng sự kiện chi tiết (dùng cho phân tích forensic)

Bảng dưới đây liệt kê nhiều sự kiện liên quan đến credential dumping và hoạt động tấn công liên quan. Bảng có nhiều hàng để đảm bảo trải dài qua nhiều trang, thuận tiện cho bài tập phân tích log.

Bảng dữ liệu credential dump
<table style="width:100%;">
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Timestamp</strong></td>
<td><strong>Host</strong></td>
<td><strong>Event</strong></td>
<td><strong>Source IP</strong></td>
<td><strong>File/Hash</strong></td>
<td><strong>Action</strong></td>
</tr>
<tr>
<td>2013-11-29 00:00:00</td>
<td>ADMIN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.190</td>
<td>lsass.dmp / SHA256: b9c402da05821277</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 00:05:00</td>
<td>STAGE-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.8.122</td>
<td>proc: unknown_exec / SHA256: 1f82ddeb7dc7c714</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 00:10:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.7.96</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 00:15:00</td>
<td>WEB-01</td>
<td>Config File Read</td>
<td>10.0.10.42</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 00:20:00</td>
<td>POS-01</td>
<td>SSH Login</td>
<td>10.0.1.219</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 00:25:00</td>
<td>DB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.106</td>
<td>lsass.dmp / SHA256: d19684345abce819</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 00:30:00</td>
<td>POS-02</td>
<td>Process Memory Read</td>
<td>10.0.10.12</td>
<td>blackpos-lab.bin / SHA256: 99129601fa0661f2</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 00:35:00</td>
<td>WORKSTATION-12</td>
<td>SSH Login</td>
<td>10.0.8.60</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 00:40:00</td>
<td>POS-01</td>
<td>Service Installed</td>
<td>10.0.9.119</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 00:45:00</td>
<td>POS-02</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.114</td>
<td>cards-20131129_part5.csv / SHA256: d0fef2e4262d8d25</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 00:50:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.205</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 00:55:00</td>
<td>WEB-01</td>
<td>SSH Login</td>
<td>10.0.7.58</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 01:00:00</td>
<td rowspan="2">ADMIN-01</td>
<td>SQL Dump</td>
<td rowspan="2">10.0.2.96</td>
<td rowspan="2">db-dump-20131129.sql / SHA256: e84fbab96c874f7f</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 01:05:00</td>
<td>Config File Read</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 01:10:00</td>
<td>WEB-01</td>
<td>Process Memory Read</td>
<td>10.0.2.228</td>
<td>blackpos-lab.bin / SHA256: 29bd38d37a50e15b</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 01:15:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.9.223</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 01:20:00</td>
<td>VPN-01</td>
<td>SSH Login</td>
<td>10.0.10.140</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 01:25:00</td>
<td>PROXY-01</td>
<td>SQL Dump</td>
<td>10.0.10.80</td>
<td>db-dump-20131129.sql / SHA256: 0a377e6ab46b1848</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 01:30:00</td>
<td>LSASS-BOX</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.93</td>
<td>cards-20131129_part3.csv / SHA256: 9655ff022efeeab0</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 01:35:00</td>
<td>PROXY-01</td>
<td>SSH Login</td>
<td>10.0.8.13</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 01:40:00</td>
<td>STAGE-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.4.118</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 01:45:00</td>
<td>WORKSTATION-12</td>
<td>Config File Read</td>
<td>10.0.8.188</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 01:50:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.6.134</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 01:55:00</td>
<td>POS-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.7.53</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 02:00:00</td>
<td>LSASS-BOX</td>
<td>Scheduled Task Creation</td>
<td>10.0.8.36</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 02:05:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.4.220</td>
<td>lsass.dmp / SHA256: 8bd952f21211d778</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 02:10:00</td>
<td>LSASS-BOX</td>
<td>Scheduled Task Creation</td>
<td>10.0.8.104</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 02:15:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.188</td>
<td>cards-20131129_part5.csv / SHA256: beddff63db8a35f1</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 02:20:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.8.142</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 02:25:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.9.234</td>
<td>db-dump-20131129.sql / SHA256: 1949c9ffcd5ea198</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 02:30:00</td>
<td>WORKSTATION-12</td>
<td>LSASS Dump Detected</td>
<td>10.0.8.150</td>
<td>lsass.dmp / SHA256: 31acd7e7fbd13b07</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 02:35:00</td>
<td>DB-01</td>
<td>Large POST to external</td>
<td>10.0.6.134</td>
<td>cards-20131129_part8.csv / SHA256: 1acef8425062d864</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 02:40:00</td>
<td>WORKSTATION-12</td>
<td>FTP Upload Attempt</td>
<td>10.0.5.113</td>
<td>cards-20131129_part2.csv / SHA256: 3f95ad26ab122140</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 02:45:00</td>
<td>WEB-01</td>
<td>SSH Login</td>
<td>10.0.2.60</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 02:50:00</td>
<td>WEB-01</td>
<td>SSH Login</td>
<td>10.0.6.170</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 02:55:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.5.171</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 03:00:00</td>
<td>POS-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.7.195</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 03:05:00</td>
<td>POS-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.41</td>
<td>cards-20131129_part8.csv / SHA256: 7d992b1dcda137f9</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 03:10:00</td>
<td>PROXY-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.207</td>
<td>lsass.dmp / SHA256: fbcecbaf2dd1066f</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 03:15:00</td>
<td>WORKSTATION-12</td>
<td>Large POST to external</td>
<td>10.0.4.14</td>
<td>cards-20131129_part6.csv / SHA256: 2bdcb8927f505792</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 03:20:00</td>
<td>VPN-01</td>
<td>SQL Dump</td>
<td>10.0.5.181</td>
<td>db-dump-20131129.sql / SHA256: b26468dfed17825f</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 03:25:00</td>
<td>LSASS-BOX</td>
<td>SQL Dump</td>
<td>10.0.10.177</td>
<td>db-dump-20131129.sql / SHA256: 70e075d63ddda7ac</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 03:30:00</td>
<td>VPN-01</td>
<td>Process Memory Read</td>
<td>10.0.2.74</td>
<td>blackpos-lab.bin / SHA256: 8d6f97856397c9f1</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 03:35:00</td>
<td>ADMIN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.2.222</td>
<td>lsass.dmp / SHA256: 43607084bb5a3223</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 03:40:00</td>
<td>STAGE-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.163</td>
<td>lsass.dmp / SHA256: 8d6b20250bad1d86</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 03:45:00</td>
<td>STAGE-01</td>
<td>SSH Login</td>
<td>10.0.6.52</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 03:50:00</td>
<td>STAGE-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.7.252</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 03:55:00</td>
<td>DB-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.7.173</td>
<td>cards-20131129_part5.csv / SHA256: 1d08a515d606cefa</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 04:00:00</td>
<td>VPN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.2.238</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 04:05:00</td>
<td>PROXY-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.9.67</td>
<td>lsass.dmp / SHA256: 387249bd316e85a7</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 04:10:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.5.180</td>
<td>cards-20131129_part2.csv / SHA256: 846147560642fc8a</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 04:15:00</td>
<td>LSASS-BOX</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.77</td>
<td>cards-20131129_part4.csv / SHA256: 2146c12be4da2470</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 04:20:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.1.192</td>
<td>lsass.dmp / SHA256: a3a847cbfb46feec</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 04:25:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.4.4</td>
<td>proc: unknown_exec / SHA256: ca09f69ea5c9933e</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 04:30:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.6.112</td>
<td>cards-20131129_part10.csv / SHA256: b026418045dc86e3</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 04:35:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.125</td>
<td>lsass.dmp / SHA256: 573e245a5953a2c1</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 04:40:00</td>
<td>DB-01</td>
<td>SSH Login</td>
<td>10.0.5.13</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 04:45:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.5.53</td>
<td>cards-20131129_part2.csv / SHA256: 990afed33020d1a8</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 04:50:00</td>
<td>PROXY-01</td>
<td>Service Installed</td>
<td>10.0.3.209</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 04:55:00</td>
<td>POS-01</td>
<td>Large POST to external</td>
<td>10.0.8.123</td>
<td>cards-20131129_part7.csv / SHA256: 8235dca3a59763b6</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 05:00:00</td>
<td>DB-01</td>
<td>Process Memory Read</td>
<td>10.0.2.129</td>
<td>blackpos-lab.bin / SHA256: 3b6263199a08826e</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 05:05:00</td>
<td>VPN-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.5.239</td>
<td>proc: unknown_exec / SHA256: 27eed54ace18372e</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 05:10:00</td>
<td>POS-02</td>
<td>SSH Login</td>
<td>10.0.6.158</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 05:15:00</td>
<td>LSASS-BOX</td>
<td>SSH Login</td>
<td>10.0.10.147</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 05:20:00</td>
<td>DB-01</td>
<td>Process Memory Read</td>
<td>10.0.1.148</td>
<td>blackpos-lab.bin / SHA256: 96f82f754c9129fa</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 05:25:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.9.180</td>
<td>proc: unknown_exec / SHA256: c91dc4d99869a506</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 05:30:00</td>
<td>LSASS-BOX</td>
<td>Service Installed</td>
<td>10.0.1.153</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 05:35:00</td>
<td>LSASS-BOX</td>
<td>FTP Upload Attempt</td>
<td>10.0.6.17</td>
<td>cards-20131129_part7.csv / SHA256: 1d4ed652ec76f995</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 05:40:00</td>
<td>LSASS-BOX</td>
<td>FTP Upload Attempt</td>
<td>10.0.2.180</td>
<td>cards-20131129_part6.csv / SHA256: 91b946a3f54dc62e</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 05:45:00</td>
<td>POS-02</td>
<td>Suspicious Process Spawn</td>
<td>10.0.5.146</td>
<td>proc: unknown_exec / SHA256: 373b6d8d4b25f9cd</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 05:50:00</td>
<td>PROXY-01</td>
<td>Process Memory Read</td>
<td>10.0.3.39</td>
<td>blackpos-lab.bin / SHA256: 58f28fcd4ee3bc09</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 05:55:00</td>
<td>PROXY-01</td>
<td>SSH Login</td>
<td>10.0.3.47</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 06:00:00</td>
<td>WEB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.2.235</td>
<td>lsass.dmp / SHA256: 667671af8708a70f</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 06:05:00</td>
<td>VPN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.10.6</td>
<td>cards-20131129_part4.csv / SHA256: 6591105b19efe558</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:10:00</td>
<td>WORKSTATION-12</td>
<td>Config File Read</td>
<td>10.0.7.212</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 06:15:00</td>
<td>VPN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.90</td>
<td>cards-20131129_part7.csv / SHA256: 585f7d0ff19289d5</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:20:00</td>
<td>DB-01</td>
<td>Config File Read</td>
<td>10.0.9.131</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 06:25:00</td>
<td>DB-01</td>
<td>Large POST to external</td>
<td>10.0.6.209</td>
<td>cards-20131129_part4.csv / SHA256: 12b770e02fcfde95</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:30:00</td>
<td>POS-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.5.156</td>
<td>cards-20131129_part7.csv / SHA256: 45ddcac5ba881906</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:35:00</td>
<td>WORKSTATION-12</td>
<td>Large POST to external</td>
<td>10.0.6.76</td>
<td>cards-20131129_part9.csv / SHA256: d1eabd81c82a9bd0</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:40:00</td>
<td>LSASS-BOX</td>
<td>Suspicious Process Spawn</td>
<td>10.0.5.163</td>
<td>proc: unknown_exec / SHA256: 25ebe27973dec46f</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 06:45:00</td>
<td>VPN-01</td>
<td>Large POST to external</td>
<td>10.0.9.2</td>
<td>cards-20131129_part8.csv / SHA256: 4c4eec07c64c6b94</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:50:00</td>
<td>DB-01</td>
<td>Large POST to external</td>
<td>10.0.2.135</td>
<td>cards-20131129_part5.csv / SHA256: cfe73d1ffe063ee5</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 06:55:00</td>
<td>LSASS-BOX</td>
<td>SQL Dump</td>
<td>10.0.10.199</td>
<td>db-dump-20131129.sql / SHA256: 2744b59f8584afeb</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 07:00:00</td>
<td>POS-02</td>
<td>Suspicious Process Spawn</td>
<td>10.0.8.112</td>
<td>proc: unknown_exec / SHA256: c7ad6e872c0a4c9b</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 07:05:00</td>
<td>WEB-01</td>
<td>Large POST to external</td>
<td>10.0.10.94</td>
<td>cards-20131129_part9.csv / SHA256: 7d9314a396f20570</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 07:10:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.6.90</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 07:15:00</td>
<td>ADMIN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.243</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 07:20:00</td>
<td>STAGE-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.8.12</td>
<td>lsass.dmp / SHA256: 84193ae1a6dcfbcd</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 07:25:00</td>
<td>POS-01</td>
<td>Service Installed</td>
<td>10.0.9.56</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 07:30:00</td>
<td>DB-01</td>
<td>SSH Login</td>
<td>10.0.8.207</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 07:35:00</td>
<td>LSASS-BOX</td>
<td>Config File Read</td>
<td>10.0.3.86</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 07:40:00</td>
<td>DB-01</td>
<td>SSH Login</td>
<td>10.0.6.19</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 07:45:00</td>
<td>POS-01</td>
<td>SQL Dump</td>
<td>10.0.5.239</td>
<td>db-dump-20131129.sql / SHA256: a8b8817bf3d761f7</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 07:50:00</td>
<td>ADMIN-01</td>
<td>Service Installed</td>
<td>10.0.2.50</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 07:55:00</td>
<td>WORKSTATION-12</td>
<td>Suspicious Process Spawn</td>
<td>10.0.2.83</td>
<td>proc: unknown_exec / SHA256: 51402279fa6e9e2a</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 08:00:00</td>
<td>STAGE-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.9.127</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 08:05:00</td>
<td>WORKSTATION-12</td>
<td>FTP Upload Attempt</td>
<td>10.0.5.146</td>
<td>cards-20131129_part8.csv / SHA256: 58364e3a8790adc5</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 08:10:00</td>
<td>POS-02</td>
<td>SQL Dump</td>
<td>10.0.6.219</td>
<td>db-dump-20131129.sql / SHA256: 950481b02b5e06f3</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 08:15:00</td>
<td>POS-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.213</td>
<td>cards-20131129_part3.csv / SHA256: 597ba5041e013ab6</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 08:20:00</td>
<td>DB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.148</td>
<td>lsass.dmp / SHA256: d7154c4a60625256</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 08:25:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.4.141</td>
<td>cards-20131129_part2.csv / SHA256: 10003b7a20751ea1</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 08:30:00</td>
<td>STAGE-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.198</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 08:35:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.2.107</td>
<td>db-dump-20131129.sql / SHA256: 6818c26f1fbd7ed7</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 08:40:00</td>
<td>VPN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.5.135</td>
<td>cards-20131129_part1.csv / SHA256: 966b0e15f7e1ca14</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 08:45:00</td>
<td>VPN-01</td>
<td>Process Memory Read</td>
<td>10.0.8.103</td>
<td>blackpos-lab.bin / SHA256: 3d7430fe33854c22</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 08:50:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.136</td>
<td>cards-20131129_part4.csv / SHA256: 908deb054564c783</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 08:55:00</td>
<td>PROXY-01</td>
<td>SQL Dump</td>
<td>10.0.2.17</td>
<td>db-dump-20131129.sql / SHA256: c7b145ea7431a2d5</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 09:00:00</td>
<td>LSASS-BOX</td>
<td>Large POST to external</td>
<td>10.0.3.221</td>
<td>cards-20131129_part7.csv / SHA256: 7500829e888145d0</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 09:05:00</td>
<td>ADMIN-01</td>
<td>SSH Login</td>
<td>10.0.7.233</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 09:10:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.10.107</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 09:15:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.9.249</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 09:20:00</td>
<td>WORKSTATION-12</td>
<td>Service Installed</td>
<td>10.0.4.19</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 09:25:00</td>
<td>LSASS-BOX</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.7</td>
<td>cards-20131129_part6.csv / SHA256: 45b0cda00ff43595</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 09:30:00</td>
<td>STAGE-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.7.31</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 09:35:00</td>
<td>ADMIN-01</td>
<td>Service Installed</td>
<td>10.0.8.20</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 09:40:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.8.162</td>
<td>proc: unknown_exec / SHA256: dc79ec9313294407</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 09:45:00</td>
<td>PROXY-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.122</td>
<td>cards-20131129_part10.csv / SHA256: 15262acad16be89d</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 09:50:00</td>
<td>WORKSTATION-12</td>
<td>SQL Dump</td>
<td>10.0.9.203</td>
<td>db-dump-20131129.sql / SHA256: ca3aaf4cde2695d7</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 09:55:00</td>
<td>STAGE-01</td>
<td>Config File Read</td>
<td>10.0.10.79</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 10:00:00</td>
<td>WEB-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.1.174</td>
<td>proc: unknown_exec / SHA256: 2a5243398731c6d6</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 10:05:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.1.81</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 10:10:00</td>
<td>STAGE-01</td>
<td>SQL Dump</td>
<td>10.0.3.72</td>
<td>db-dump-20131129.sql / SHA256: 84acea8d005cb2c4</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 10:15:00</td>
<td>VPN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.10.207</td>
<td>cards-20131129_part2.csv / SHA256: e9532cd3e5928eae</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 10:20:00</td>
<td>WEB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.2.189</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 10:25:00</td>
<td>PROXY-01</td>
<td>Config File Read</td>
<td>10.0.5.71</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 10:30:00</td>
<td>STAGE-01</td>
<td>SSH Login</td>
<td>10.0.5.88</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 10:35:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.10.5</td>
<td>lsass.dmp / SHA256: b0290303a758bb13</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 10:40:00</td>
<td>WEB-01</td>
<td>SSH Login</td>
<td>10.0.7.237</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 10:45:00</td>
<td>DB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.146</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 10:50:00</td>
<td>PROXY-01</td>
<td>Service Installed</td>
<td>10.0.8.239</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 10:55:00</td>
<td>WEB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.146</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 11:00:00</td>
<td>VPN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.128</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 11:05:00</td>
<td>DB-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.4.201</td>
<td>proc: unknown_exec / SHA256: 106068704ee01ddf</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 11:10:00</td>
<td>WEB-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.2.240</td>
<td>proc: unknown_exec / SHA256: 7a64edd274697a16</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 11:15:00</td>
<td>DB-01</td>
<td>Process Memory Read</td>
<td>10.0.7.68</td>
<td>blackpos-lab.bin / SHA256: e2bbaa394a53f999</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 11:20:00</td>
<td>WEB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.160</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 11:25:00</td>
<td>WEB-01</td>
<td>Config File Read</td>
<td>10.0.6.208</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 11:30:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.8.130</td>
<td>lsass.dmp / SHA256: 6028a6f0e67a98d7</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 11:35:00</td>
<td>DB-01</td>
<td>Config File Read</td>
<td>10.0.10.19</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 11:40:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.9.116</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 11:45:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.198</td>
<td>lsass.dmp / SHA256: b2c011a3fb316592</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 11:50:00</td>
<td>ADMIN-01</td>
<td>Large POST to external</td>
<td>10.0.4.229</td>
<td>cards-20131129_part5.csv / SHA256: 57502ba5380a9320</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 11:55:00</td>
<td>STAGE-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.8.202</td>
<td>lsass.dmp / SHA256: c9bc765f12bf3e4c</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 12:00:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.36</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 12:05:00</td>
<td>VPN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.160</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 12:10:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.201</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 12:15:00</td>
<td>STAGE-01</td>
<td>Process Memory Read</td>
<td>10.0.10.3</td>
<td>blackpos-lab.bin / SHA256: b6c8cdc8def6cbc8</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 12:20:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.4.115</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 12:25:00</td>
<td>POS-02</td>
<td>Service Installed</td>
<td>10.0.6.89</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 12:30:00</td>
<td>POS-01</td>
<td>SQL Dump</td>
<td>10.0.5.229</td>
<td>db-dump-20131129.sql / SHA256: 84e1da2ce2801e21</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 12:35:00</td>
<td>DB-01</td>
<td>SSH Login</td>
<td>10.0.10.38</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 12:40:00</td>
<td>WEB-01</td>
<td>Large POST to external</td>
<td>10.0.6.43</td>
<td>cards-20131129_part8.csv / SHA256: 4fe7dd1b54e63941</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 12:45:00</td>
<td>POS-02</td>
<td>Config File Read</td>
<td>10.0.8.1</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 12:50:00</td>
<td>POS-01</td>
<td>Config File Read</td>
<td>10.0.2.134</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 12:55:00</td>
<td>PROXY-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.10.173</td>
<td>proc: unknown_exec / SHA256: 26001ad2132cc667</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 13:00:00</td>
<td>WEB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.219</td>
<td>lsass.dmp / SHA256: 8ec4b6adfd72ecd9</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 13:05:00</td>
<td>VPN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.8.71</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 13:10:00</td>
<td>ADMIN-01</td>
<td>SQL Dump</td>
<td>10.0.3.155</td>
<td>db-dump-20131129.sql / SHA256: c4dcbc4456165b7c</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 13:15:00</td>
<td>ADMIN-01</td>
<td>Process Memory Read</td>
<td>10.0.8.79</td>
<td>blackpos-lab.bin / SHA256: 529c19335be45215</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 13:20:00</td>
<td>DB-01</td>
<td>Config File Read</td>
<td>10.0.3.106</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 13:25:00</td>
<td>PROXY-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.1.149</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 13:30:00</td>
<td>WEB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.1.64</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 13:35:00</td>
<td>POS-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.248</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 13:40:00</td>
<td>STAGE-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.4.167</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 13:45:00</td>
<td>PROXY-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.4.245</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 13:50:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.10.145</td>
<td>proc: unknown_exec / SHA256: 26219d625a3e2750</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 13:55:00</td>
<td>STAGE-01</td>
<td>SQL Dump</td>
<td>10.0.3.210</td>
<td>db-dump-20131129.sql / SHA256: 453b1ebbce374666</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 14:00:00</td>
<td>LSASS-BOX</td>
<td>Service Installed</td>
<td>10.0.6.241</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 14:05:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.1.99</td>
<td>db-dump-20131129.sql / SHA256: 826caffdc1af946b</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 14:10:00</td>
<td>PROXY-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.68</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 14:15:00</td>
<td>WORKSTATION-12</td>
<td>SQL Dump</td>
<td>10.0.4.204</td>
<td>db-dump-20131129.sql / SHA256: c64dfe06934c4dde</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 14:20:00</td>
<td>STAGE-01</td>
<td>Process Memory Read</td>
<td>10.0.10.198</td>
<td>blackpos-lab.bin / SHA256: 35444b0e72b7569e</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 14:25:00</td>
<td>WEB-01</td>
<td>Process Memory Read</td>
<td>10.0.3.166</td>
<td>blackpos-lab.bin / SHA256: c163460646b55e90</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 14:30:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.1.199</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 14:35:00</td>
<td>POS-02</td>
<td>Large POST to external</td>
<td>10.0.1.251</td>
<td>cards-20131129_part4.csv / SHA256: 702046f0a5860505</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 14:40:00</td>
<td>WEB-01</td>
<td>SSH Login</td>
<td>10.0.2.135</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 14:45:00</td>
<td>VPN-01</td>
<td>Large POST to external</td>
<td>10.0.7.136</td>
<td>cards-20131129_part10.csv / SHA256: e95768a19f1ceef0</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 14:50:00</td>
<td>ADMIN-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.9.101</td>
<td>proc: unknown_exec / SHA256: 6130b47147e15ec2</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 14:55:00</td>
<td>WORKSTATION-12</td>
<td>SQL Dump</td>
<td>10.0.7.133</td>
<td>db-dump-20131129.sql / SHA256: 526252effea0ab56</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 15:00:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.8.70</td>
<td>db-dump-20131129.sql / SHA256: b8283af3567af33b</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 15:05:00</td>
<td>POS-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.72</td>
<td>lsass.dmp / SHA256: f8e1a86a0450ace2</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 15:10:00</td>
<td>POS-01</td>
<td>SSH Login</td>
<td>10.0.4.252</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 15:15:00</td>
<td>VPN-01</td>
<td>Service Installed</td>
<td>10.0.4.196</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 15:20:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.3.239</td>
<td>proc: unknown_exec / SHA256: 4b7e9d4b497ab147</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 15:25:00</td>
<td>POS-02</td>
<td>Suspicious Process Spawn</td>
<td>10.0.4.213</td>
<td>proc: unknown_exec / SHA256: 0451dd1f5ffb6706</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 15:30:00</td>
<td>WEB-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.2.18</td>
<td>cards-20131129_part9.csv / SHA256: 11788df4eecba9ad</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 15:35:00</td>
<td>PROXY-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.8.76</td>
<td>proc: unknown_exec / SHA256: 869c918ff18a36a9</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 15:40:00</td>
<td>STAGE-01</td>
<td>Config File Read</td>
<td>10.0.2.89</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 15:45:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.10.224</td>
<td>cards-20131129_part8.csv / SHA256: 17faa7a766be7382</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 15:50:00</td>
<td>POS-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.3.167</td>
<td>cards-20131129_part6.csv / SHA256: ef9167aa8bd0d1fc</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 15:55:00</td>
<td>POS-01</td>
<td>SSH Login</td>
<td>10.0.6.41</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 16:00:00</td>
<td>LSASS-BOX</td>
<td>Process Memory Read</td>
<td>10.0.9.215</td>
<td>blackpos-lab.bin / SHA256: 928e13cd34af7245</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 16:05:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.2.124</td>
<td>lsass.dmp / SHA256: 111134e298d34d3e</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 16:10:00</td>
<td>WORKSTATION-12</td>
<td>Large POST to external</td>
<td>10.0.2.161</td>
<td>cards-20131129_part1.csv / SHA256: 110484162d8f2a8c</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 16:15:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.10.169</td>
<td>cards-20131129_part1.csv / SHA256: 2f8c4bfca67590ad</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 16:20:00</td>
<td>ADMIN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.165</td>
<td>cards-20131129_part3.csv / SHA256: 842334f65f9079b5</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 16:25:00</td>
<td>DB-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.10.217</td>
<td>proc: unknown_exec / SHA256: 65ee7734a85a03b7</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 16:30:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.179</td>
<td>cards-20131129_part2.csv / SHA256: 6b6973dcf8cd4b02</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 16:35:00</td>
<td>POS-01</td>
<td>SQL Dump</td>
<td>10.0.2.21</td>
<td>db-dump-20131129.sql / SHA256: 1a05d69b723c4c93</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 16:40:00</td>
<td>POS-01</td>
<td>Process Memory Read</td>
<td>10.0.4.186</td>
<td>blackpos-lab.bin / SHA256: 632528ddc08195bb</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 16:45:00</td>
<td>WEB-01</td>
<td>Service Installed</td>
<td>10.0.10.100</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 16:50:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.7.86</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 16:55:00</td>
<td>WORKSTATION-12</td>
<td>SQL Dump</td>
<td>10.0.6.27</td>
<td>db-dump-20131129.sql / SHA256: d870d52a4a1afe62</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 17:00:00</td>
<td>DB-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.3.11</td>
<td>proc: unknown_exec / SHA256: 3ad51277bc207f81</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 17:05:00</td>
<td>LSASS-BOX</td>
<td>SSH Login</td>
<td>10.0.5.225</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 17:10:00</td>
<td>STAGE-01</td>
<td>Config File Read</td>
<td>10.0.6.115</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 17:15:00</td>
<td>STAGE-01</td>
<td>Config File Read</td>
<td>10.0.2.211</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 17:20:00</td>
<td>ADMIN-01</td>
<td>Process Memory Read</td>
<td>10.0.4.108</td>
<td>blackpos-lab.bin / SHA256: ca25ef44c184bb56</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 17:25:00</td>
<td>POS-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.139</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 17:30:00</td>
<td>DB-01</td>
<td>Config File Read</td>
<td>10.0.9.60</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 17:35:00</td>
<td>DB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.2.55</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 17:40:00</td>
<td>STAGE-01</td>
<td>SQL Dump</td>
<td>10.0.1.138</td>
<td>db-dump-20131129.sql / SHA256: 81363fd4e9606ad8</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 17:45:00</td>
<td>VPN-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.7.13</td>
<td>proc: unknown_exec / SHA256: ce14fb490fc3d9ed</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 17:50:00</td>
<td>ADMIN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.6.43</td>
<td>lsass.dmp / SHA256: 6569453d4aa21d34</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 17:55:00</td>
<td>VPN-01</td>
<td>Process Memory Read</td>
<td>10.0.8.163</td>
<td>blackpos-lab.bin / SHA256: b1ab4dafd469b15d</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 18:00:00</td>
<td>PROXY-01</td>
<td>Large POST to external</td>
<td>10.0.6.47</td>
<td>cards-20131129_part5.csv / SHA256: c4196950302f44e0</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 18:05:00</td>
<td>WORKSTATION-12</td>
<td>Service Installed</td>
<td>10.0.2.30</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 18:10:00</td>
<td>VPN-01</td>
<td>Large POST to external</td>
<td>10.0.2.165</td>
<td>cards-20131129_part1.csv / SHA256: cc0873a374d47a46</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 18:15:00</td>
<td>POS-01</td>
<td>Config File Read</td>
<td>10.0.9.99</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 18:20:00</td>
<td>ADMIN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.4.200</td>
<td>lsass.dmp / SHA256: 3e54fd25802542db</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 18:25:00</td>
<td>POS-02</td>
<td>Process Memory Read</td>
<td>10.0.5.215</td>
<td>blackpos-lab.bin / SHA256: 4d245ca39b8d46fc</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 18:30:00</td>
<td>LSASS-BOX</td>
<td>Scheduled Task Creation</td>
<td>10.0.9.250</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 18:35:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.225</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 18:40:00</td>
<td>POS-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.5.77</td>
<td>lsass.dmp / SHA256: 8145218b75e3e85a</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 18:45:00</td>
<td>ADMIN-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.5.107</td>
<td>proc: unknown_exec / SHA256: 40e5ba94438b7e4a</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 18:50:00</td>
<td>STAGE-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.7.38</td>
<td>proc: unknown_exec / SHA256: d6eb1d9665cb9108</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 18:55:00</td>
<td>STAGE-01</td>
<td>Process Memory Read</td>
<td>10.0.9.187</td>
<td>blackpos-lab.bin / SHA256: 4f606210092eec6f</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 19:00:00</td>
<td>WORKSTATION-12</td>
<td>SQL Dump</td>
<td>10.0.6.116</td>
<td>db-dump-20131129.sql / SHA256: f0989cb9998b198d</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 19:05:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.7.213</td>
<td>cards-20131129_part2.csv / SHA256: 7160c1f013e2994a</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 19:10:00</td>
<td>DB-01</td>
<td>SSH Login</td>
<td>10.0.5.33</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 19:15:00</td>
<td>STAGE-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.4.70</td>
<td>proc: unknown_exec / SHA256: 2079ecc29900d121</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 19:20:00</td>
<td>ADMIN-01</td>
<td>Large POST to external</td>
<td>10.0.10.89</td>
<td>cards-20131129_part2.csv / SHA256: 9b953ffd5bf3bc16</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 19:25:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.4.220</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 19:30:00</td>
<td>POS-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.10.110</td>
<td>lsass.dmp / SHA256: f305109b0d0e1513</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 19:35:00</td>
<td>PROXY-01</td>
<td>Large POST to external</td>
<td>10.0.4.252</td>
<td>cards-20131129_part6.csv / SHA256: bf6e8c3e5357c30f</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 19:40:00</td>
<td>WORKSTATION-12</td>
<td>Suspicious Process Spawn</td>
<td>10.0.9.112</td>
<td>proc: unknown_exec / SHA256: ef7fbc5ac20c4b47</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 19:45:00</td>
<td>LSASS-BOX</td>
<td>LSASS Dump Detected</td>
<td>10.0.10.73</td>
<td>lsass.dmp / SHA256: 2de904cf75fd589a</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 19:50:00</td>
<td>PROXY-01</td>
<td>Process Memory Read</td>
<td>10.0.8.83</td>
<td>blackpos-lab.bin / SHA256: 30848b2006bf8183</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 19:55:00</td>
<td>POS-02</td>
<td>FTP Upload Attempt</td>
<td>10.0.6.108</td>
<td>cards-20131129_part6.csv / SHA256: 5f707ce3c67177d6</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 20:00:00</td>
<td>STAGE-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.6.31</td>
<td>lsass.dmp / SHA256: 5a50e6ea7f586738</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 20:05:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.4.117</td>
<td>cards-20131129_part1.csv / SHA256: d25c9c748a29c06c</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 20:10:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.179</td>
<td>lsass.dmp / SHA256: de68c9046c1372b4</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 20:15:00</td>
<td>VPN-01</td>
<td>SQL Dump</td>
<td>10.0.6.215</td>
<td>db-dump-20131129.sql / SHA256: bbce0fd8fae81289</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 20:20:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.3.170</td>
<td>cards-20131129_part9.csv / SHA256: 01df0fb935363796</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 20:25:00</td>
<td>PROXY-01</td>
<td>SQL Dump</td>
<td>10.0.8.89</td>
<td>db-dump-20131129.sql / SHA256: a2f34fbdc5aed325</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 20:30:00</td>
<td>ADMIN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.2.135</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 20:35:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.82</td>
<td>lsass.dmp / SHA256: 7e66d3dd7f3b9f20</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 20:40:00</td>
<td>POS-01</td>
<td>Process Memory Read</td>
<td>10.0.8.249</td>
<td>blackpos-lab.bin / SHA256: 1cc9fa732a42c014</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 20:45:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.4.94</td>
<td>proc: unknown_exec / SHA256: 20cb34e7883a79dc</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 20:50:00</td>
<td>LSASS-BOX</td>
<td>Service Installed</td>
<td>10.0.1.27</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 20:55:00</td>
<td>POS-01</td>
<td>SQL Dump</td>
<td>10.0.5.23</td>
<td>db-dump-20131129.sql / SHA256: a6b8d8fc4ab89bab</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 21:00:00</td>
<td>DB-01</td>
<td>Service Installed</td>
<td>10.0.7.35</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 21:05:00</td>
<td>STAGE-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.8.82</td>
<td>cards-20131129_part5.csv / SHA256: a46d359a7adcdb61</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 21:10:00</td>
<td>PROXY-01</td>
<td>Service Installed</td>
<td>10.0.7.123</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 21:15:00</td>
<td>DB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.20</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 21:20:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.2.50</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 21:25:00</td>
<td>WORKSTATION-12</td>
<td>Suspicious Process Spawn</td>
<td>10.0.4.107</td>
<td>proc: unknown_exec / SHA256: 2c997e95134de801</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 21:30:00</td>
<td>LSASS-BOX</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.36</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 21:35:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.7.166</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 21:40:00</td>
<td>LSASS-BOX</td>
<td>Process Memory Read</td>
<td>10.0.4.138</td>
<td>blackpos-lab.bin / SHA256: 35601431cedc4a3a</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 21:45:00</td>
<td>LSASS-BOX</td>
<td>SQL Dump</td>
<td>10.0.7.38</td>
<td>db-dump-20131129.sql / SHA256: 0d6b2f9d90cb0b38</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 21:50:00</td>
<td>VPN-01</td>
<td>Process Memory Read</td>
<td>10.0.5.245</td>
<td>blackpos-lab.bin / SHA256: 3f3e4dafb4993e67</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-29 21:55:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.3.150</td>
<td>db-dump-20131129.sql / SHA256: e451c6f9d9488bae</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 22:00:00</td>
<td>LSASS-BOX</td>
<td>Scheduled Task Creation</td>
<td>10.0.8.139</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 22:05:00</td>
<td>POS-01</td>
<td>SSH Login</td>
<td>10.0.9.240</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 22:10:00</td>
<td>DB-01</td>
<td>Config File Read</td>
<td>10.0.5.109</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 22:15:00</td>
<td>POS-01</td>
<td>Config File Read</td>
<td>10.0.10.204</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 22:20:00</td>
<td>STAGE-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.10.17</td>
<td>proc: unknown_exec / SHA256: 59f82b34988e94dd</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 22:25:00</td>
<td>POS-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.7.135</td>
<td>proc: unknown_exec / SHA256: 8fa8a4f7533d2377</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-29 22:30:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.9.195</td>
<td>lsass.dmp / SHA256: 292eef2d19b786b9</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 22:35:00</td>
<td>VPN-01</td>
<td>Service Installed</td>
<td>10.0.4.58</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 22:40:00</td>
<td>POS-01</td>
<td>Config File Read</td>
<td>10.0.7.99</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 22:45:00</td>
<td>WORKSTATION-12</td>
<td>FTP Upload Attempt</td>
<td>10.0.2.191</td>
<td>cards-20131129_part9.csv / SHA256: dac3b27bd0cecda2</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 22:50:00</td>
<td>DB-01</td>
<td>Config File Read</td>
<td>10.0.9.215</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-29 22:55:00</td>
<td>WEB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.10.184</td>
<td>lsass.dmp / SHA256: 761cfe9de6c1f2b2</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 23:00:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.7.49</td>
<td>db-dump-20131129.sql / SHA256: d9c4371d04ea3696</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 23:05:00</td>
<td>ADMIN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.253</td>
<td>cards-20131129_part6.csv / SHA256: b7b91e61bdf1c67e</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 23:10:00</td>
<td>POS-02</td>
<td>FTP Upload Attempt</td>
<td>10.0.6.50</td>
<td>cards-20131129_part4.csv / SHA256: c5847f3ab670ae6f</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 23:15:00</td>
<td>WORKSTATION-12</td>
<td>Service Installed</td>
<td>10.0.5.27</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-29 23:20:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.7.85</td>
<td>lsass.dmp / SHA256: 64f63ce53690375e</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-29 23:25:00</td>
<td>PROXY-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.1.222</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 23:30:00</td>
<td>VPN-01</td>
<td>SSH Login</td>
<td>10.0.6.198</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-29 23:35:00</td>
<td>VPN-01</td>
<td>SQL Dump</td>
<td>10.0.1.37</td>
<td>db-dump-20131129.sql / SHA256: bab203e457e26192</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-29 23:40:00</td>
<td>POS-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.7.254</td>
<td>cards-20131129_part3.csv / SHA256: 62583c52cbffb0f6</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 23:45:00</td>
<td>PROXY-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.2.230</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-29 23:50:00</td>
<td>WORKSTATION-12</td>
<td>Large POST to external</td>
<td>10.0.9.78</td>
<td>cards-20131129_part10.csv / SHA256: 858109f8d8c4ebf7</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-29 23:55:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.4.32</td>
<td>db-dump-20131129.sql / SHA256: 58a332dd1c6493e3</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 00:00:00</td>
<td>PROXY-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.7.217</td>
<td>cards-20131129_part6.csv / SHA256: 521ffb2bd0e9b31b</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 00:05:00</td>
<td>POS-01</td>
<td>Config File Read</td>
<td>10.0.5.97</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-30 00:10:00</td>
<td>POS-02</td>
<td>SSH Login</td>
<td>10.0.4.76</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 00:15:00</td>
<td>POS-01</td>
<td>Config File Read</td>
<td>10.0.3.156</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-30 00:20:00</td>
<td>WEB-01</td>
<td>Large POST to external</td>
<td>10.0.7.115</td>
<td>cards-20131129_part5.csv / SHA256: df97d92dd82d7160</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 00:25:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.215</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 00:30:00</td>
<td>LSASS-BOX</td>
<td>Suspicious Process Spawn</td>
<td>10.0.8.254</td>
<td>proc: unknown_exec / SHA256: 9c3e6af6f6180c64</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 00:35:00</td>
<td>WORKSTATION-12</td>
<td>LSASS Dump Detected</td>
<td>10.0.8.90</td>
<td>lsass.dmp / SHA256: b70bd341ed530b35</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 00:40:00</td>
<td>DB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.2.245</td>
<td>lsass.dmp / SHA256: be0cb2bc67eb9b43</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 00:45:00</td>
<td>ADMIN-01</td>
<td>Large POST to external</td>
<td>10.0.9.170</td>
<td>cards-20131129_part1.csv / SHA256: 75e2a66da079b932</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 00:50:00</td>
<td>LSASS-BOX</td>
<td>Large POST to external</td>
<td>10.0.7.56</td>
<td>cards-20131129_part8.csv / SHA256: d41b8af1da968ca2</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 00:55:00</td>
<td>VPN-01</td>
<td>Service Installed</td>
<td>10.0.1.177</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 01:00:00</td>
<td>DB-01</td>
<td>Process Memory Read</td>
<td>10.0.10.229</td>
<td>blackpos-lab.bin / SHA256: f74636c9a6dec5bf</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 01:05:00</td>
<td>LSASS-BOX</td>
<td>Service Installed</td>
<td>10.0.2.173</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 01:10:00</td>
<td>WEB-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.4.1</td>
<td>cards-20131129_part1.csv / SHA256: 3dd47b1e739c1d1d</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 01:15:00</td>
<td>WEB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.8.92</td>
<td>lsass.dmp / SHA256: 276dca0ba7eb16a0</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 01:20:00</td>
<td>STAGE-01</td>
<td>SSH Login</td>
<td>10.0.4.195</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 01:25:00</td>
<td>ADMIN-01</td>
<td>Service Installed</td>
<td>10.0.6.141</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 01:30:00</td>
<td>WEB-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.8.101</td>
<td>proc: unknown_exec / SHA256: 9e4d12485cb51e1b</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 01:35:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.9.193</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 01:40:00</td>
<td>POS-01</td>
<td>SSH Login</td>
<td>10.0.2.132</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 01:45:00</td>
<td>WORKSTATION-12</td>
<td>SSH Login</td>
<td>10.0.4.231</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 01:50:00</td>
<td>POS-02</td>
<td>SQL Dump</td>
<td>10.0.7.2</td>
<td>db-dump-20131129.sql / SHA256: 438b187127484d78</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 01:55:00</td>
<td>WORKSTATION-12</td>
<td>Service Installed</td>
<td>10.0.3.3</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 02:00:00</td>
<td>PROXY-01</td>
<td>Service Installed</td>
<td>10.0.2.109</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 02:05:00</td>
<td>DB-01</td>
<td>Large POST to external</td>
<td>10.0.6.213</td>
<td>cards-20131129_part10.csv / SHA256: 5001178f87560503</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 02:10:00</td>
<td>DB-01</td>
<td>Process Memory Read</td>
<td>10.0.2.191</td>
<td>blackpos-lab.bin / SHA256: 24f6a192035f864d</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 02:15:00</td>
<td>VPN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.8.17</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 02:20:00</td>
<td>ADMIN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.6.237</td>
<td>cards-20131129_part4.csv / SHA256: ce01ff4245df4466</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 02:25:00</td>
<td>PROXY-01</td>
<td>SQL Dump</td>
<td>10.0.6.180</td>
<td>db-dump-20131129.sql / SHA256: e813f6085dc2b9db</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 02:30:00</td>
<td>WORKSTATION-12</td>
<td>Service Installed</td>
<td>10.0.3.37</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 02:35:00</td>
<td>VPN-01</td>
<td>Large POST to external</td>
<td>10.0.10.117</td>
<td>cards-20131129_part10.csv / SHA256: 400fb171f4347ee9</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 02:40:00</td>
<td>WEB-01</td>
<td>Process Memory Read</td>
<td>10.0.7.133</td>
<td>blackpos-lab.bin / SHA256: e2bda3e62f3dec53</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 02:45:00</td>
<td>LSASS-BOX</td>
<td>SQL Dump</td>
<td>10.0.3.105</td>
<td>db-dump-20131129.sql / SHA256: f9cb407a44838a45</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 02:50:00</td>
<td>POS-02</td>
<td>Suspicious Process Spawn</td>
<td>10.0.5.2</td>
<td>proc: unknown_exec / SHA256: be05a3d196aef8c8</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 02:55:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.6.4</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 03:00:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.244</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 03:05:00</td>
<td>LSASS-BOX</td>
<td>SSH Login</td>
<td>10.0.5.151</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 03:10:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.4.248</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-30 03:15:00</td>
<td>STAGE-01</td>
<td>Large POST to external</td>
<td>10.0.6.63</td>
<td>cards-20131129_part8.csv / SHA256: c0e80997db50435b</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 03:20:00</td>
<td>STAGE-01</td>
<td>SSH Login</td>
<td>10.0.10.242</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 03:25:00</td>
<td>STAGE-01</td>
<td>Process Memory Read</td>
<td>10.0.8.108</td>
<td>blackpos-lab.bin / SHA256: e869cc6ac1fc629c</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 03:30:00</td>
<td>ADMIN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.4.160</td>
<td>lsass.dmp / SHA256: d81942dbed9c3a28</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 03:35:00</td>
<td>VPN-01</td>
<td>Service Installed</td>
<td>10.0.2.58</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 03:40:00</td>
<td>VPN-01</td>
<td>Large POST to external</td>
<td>10.0.9.72</td>
<td>cards-20131129_part1.csv / SHA256: 2f25ef8892a937eb</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 03:45:00</td>
<td>PROXY-01</td>
<td>SSH Login</td>
<td>10.0.5.114</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 03:50:00</td>
<td>VPN-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.6.240</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 03:55:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.4.142</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 04:00:00</td>
<td>WEB-01</td>
<td>Large POST to external</td>
<td>10.0.5.249</td>
<td>cards-20131129_part1.csv / SHA256: 2adf79bd5922498a</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 04:05:00</td>
<td>WORKSTATION-12</td>
<td>SQL Dump</td>
<td>10.0.4.55</td>
<td>db-dump-20131129.sql / SHA256: 4f1dff19803cf845</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 04:10:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.2.76</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 04:15:00</td>
<td>POS-01</td>
<td>Process Memory Read</td>
<td>10.0.1.78</td>
<td>blackpos-lab.bin / SHA256: 236fa33cdfa4a93e</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 04:20:00</td>
<td>PROXY-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.1.62</td>
<td>proc: unknown_exec / SHA256: 60aae3a070e6c506</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 04:25:00</td>
<td>POS-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.199</td>
<td>cards-20131129_part8.csv / SHA256: 2b7760c699c0703f</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 04:30:00</td>
<td>STAGE-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.10.11</td>
<td>lsass.dmp / SHA256: c7da6e58e2bf9bd0</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 04:35:00</td>
<td>POS-02</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.138</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 04:40:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.5.60</td>
<td>lsass.dmp / SHA256: dc6ecb759e708ca8</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 04:45:00</td>
<td>WORKSTATION-12</td>
<td>Process Memory Read</td>
<td>10.0.8.99</td>
<td>blackpos-lab.bin / SHA256: 71bc5cec3daf47f5</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 04:50:00</td>
<td>WORKSTATION-12</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.147</td>
<td>cards-20131129_part1.csv / SHA256: e3977a9f3dc426ee</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 04:55:00</td>
<td>POS-02</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.181</td>
<td>cards-20131129_part2.csv / SHA256: 899dd387a124486e</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 05:00:00</td>
<td>POS-01</td>
<td>SQL Dump</td>
<td>10.0.1.153</td>
<td>db-dump-20131129.sql / SHA256: c6bc506c73aa0f76</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 05:05:00</td>
<td>POS-02</td>
<td>Process Memory Read</td>
<td>10.0.4.94</td>
<td>blackpos-lab.bin / SHA256: 0e4c9632e0e4784c</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 05:10:00</td>
<td>PROXY-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.9.101</td>
<td>proc: unknown_exec / SHA256: 99458975f221c769</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 05:15:00</td>
<td>WEB-01</td>
<td>Service Installed</td>
<td>10.0.6.66</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 05:20:00</td>
<td>WORKSTATION-12</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.206</td>
<td>cards-20131129_part1.csv / SHA256: 84c714c3ea65f486</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 05:25:00</td>
<td>WORKSTATION-12</td>
<td>Process Memory Read</td>
<td>10.0.9.117</td>
<td>blackpos-lab.bin / SHA256: 7d8ba738839f906c</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 05:30:00</td>
<td>STAGE-01</td>
<td>Process Memory Read</td>
<td>10.0.9.27</td>
<td>blackpos-lab.bin / SHA256: cfe7e5b9a80458a9</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 05:35:00</td>
<td>PROXY-01</td>
<td>Config File Read</td>
<td>10.0.6.89</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-30 05:40:00</td>
<td>VPN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.8.10</td>
<td>cards-20131129_part8.csv / SHA256: e249ea2439fb1bb1</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 05:45:00</td>
<td>LSASS-BOX</td>
<td>Large POST to external</td>
<td>10.0.4.160</td>
<td>cards-20131129_part4.csv / SHA256: bfaf5cdef585a56e</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 05:50:00</td>
<td>DB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.10.155</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 05:55:00</td>
<td>WORKSTATION-12</td>
<td>SSH Login</td>
<td>10.0.10.19</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 06:00:00</td>
<td>WEB-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.195</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 06:05:00</td>
<td>POS-02</td>
<td>SSH Login</td>
<td>10.0.9.154</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 06:10:00</td>
<td>STAGE-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.7.122</td>
<td>proc: unknown_exec / SHA256: f88f46ab20ae03b5</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 06:15:00</td>
<td>VPN-01</td>
<td>Suspicious Process Spawn</td>
<td>10.0.6.124</td>
<td>proc: unknown_exec / SHA256: c62af96724fac63b</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 06:20:00</td>
<td>DB-01</td>
<td>Service Installed</td>
<td>10.0.5.148</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 06:25:00</td>
<td>POS-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.4.163</td>
<td>lsass.dmp / SHA256: 42048aa974840765</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 06:30:00</td>
<td>PROXY-01</td>
<td>Process Memory Read</td>
<td>10.0.9.212</td>
<td>blackpos-lab.bin / SHA256: 5c2f395426b296ec</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 06:35:00</td>
<td>PROXY-01</td>
<td>Large POST to external</td>
<td>10.0.8.73</td>
<td>cards-20131129_part4.csv / SHA256: b844a46ef0393616</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 06:40:00</td>
<td>LSASS-BOX</td>
<td>Process Memory Read</td>
<td>10.0.7.134</td>
<td>blackpos-lab.bin / SHA256: 19cb008c900a8122</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 06:45:00</td>
<td>STAGE-01</td>
<td>SQL Dump</td>
<td>10.0.5.90</td>
<td>db-dump-20131129.sql / SHA256: a5d4c8e7c9a0eb7f</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 06:50:00</td>
<td>WORKSTATION-12</td>
<td>Scheduled Task Creation</td>
<td>10.0.3.201</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 06:55:00</td>
<td>ADMIN-01</td>
<td>Process Memory Read</td>
<td>10.0.3.136</td>
<td>blackpos-lab.bin / SHA256: c0652ae67d0ef924</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 07:00:00</td>
<td>STAGE-01</td>
<td>Service Installed</td>
<td>10.0.4.94</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 07:05:00</td>
<td>DB-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.91</td>
<td>cards-20131129_part1.csv / SHA256: 06cf0b882ef6dffa</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 07:10:00</td>
<td>DB-01</td>
<td>SQL Dump</td>
<td>10.0.7.241</td>
<td>db-dump-20131129.sql / SHA256: b5b5d2863976af7a</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 07:15:00</td>
<td>POS-01</td>
<td>Service Installed</td>
<td>10.0.4.81</td>
<td>service: backdoor_svc</td>
<td>Service started at boot</td>
</tr>
<tr>
<td>2013-11-30 07:20:00</td>
<td>WEB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.6.127</td>
<td>lsass.dmp / SHA256: e86ff55df7e8d24d</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 07:25:00</td>
<td>VPN-01</td>
<td>SSH Login</td>
<td>10.0.5.22</td>
<td>n/a</td>
<td>Login successful (possible credential reuse)</td>
</tr>
<tr>
<td>2013-11-30 07:30:00</td>
<td>WEB-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.10.216</td>
<td>cards-20131129_part7.csv / SHA256: 92c2315b8e64ebfb</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 07:35:00</td>
<td>POS-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.122</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 07:40:00</td>
<td>DB-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.173</td>
<td>lsass.dmp / SHA256: 1c00cb07f6cdc304</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 07:45:00</td>
<td>WEB-01</td>
<td>Process Memory Read</td>
<td>10.0.5.116</td>
<td>blackpos-lab.bin / SHA256: 0e3fd56f5d59fe5c</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 07:50:00</td>
<td>WORKSTATION-12</td>
<td>Suspicious Process Spawn</td>
<td>10.0.2.253</td>
<td>proc: unknown_exec / SHA256: a284aa86f4c2da34</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 07:55:00</td>
<td>ADMIN-01</td>
<td>Config File Read</td>
<td>10.0.6.117</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-30 08:00:00</td>
<td>WEB-01</td>
<td>SQL Dump</td>
<td>10.0.6.253</td>
<td>db-dump-20131129.sql / SHA256: ae3a5a8ab3bf8448</td>
<td>Sensitive data exported</td>
</tr>
<tr>
<td>2013-11-30 08:05:00</td>
<td>PROXY-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.1.17</td>
<td>cards-20131129_part2.csv / SHA256: b43c3900be5f5f50</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 08:10:00</td>
<td>VPN-01</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.251</td>
<td>lsass.dmp / SHA256: b68e9e59e0240edc</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 08:15:00</td>
<td>PROXY-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.8.239</td>
<td>cards-20131129_part5.csv / SHA256: 338d2f32d1d3a071</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 08:20:00</td>
<td>STAGE-01</td>
<td>Process Memory Read</td>
<td>10.0.1.170</td>
<td>blackpos-lab.bin / SHA256: 722efe12b0b810a8</td>
<td>Credential pattern found</td>
</tr>
<tr>
<td>2013-11-30 08:25:00</td>
<td>PROXY-01</td>
<td>Large POST to external</td>
<td>10.0.1.107</td>
<td>cards-20131129_part1.csv / SHA256: 97bcacd1078ebe26</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 08:30:00</td>
<td>POS-02</td>
<td>Suspicious Process Spawn</td>
<td>10.0.1.17</td>
<td>proc: unknown_exec / SHA256: 490f82df73a8eead</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 08:35:00</td>
<td>POS-02</td>
<td>LSASS Dump Detected</td>
<td>10.0.3.58</td>
<td>lsass.dmp / SHA256: a10d1426dcbb25b2</td>
<td>Possible credential exfil from memory</td>
</tr>
<tr>
<td>2013-11-30 08:40:00</td>
<td>LSASS-BOX</td>
<td>Large POST to external</td>
<td>10.0.7.201</td>
<td>cards-20131129_part9.csv / SHA256: 865b2dd49c9253b2</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 08:45:00</td>
<td>LSASS-BOX</td>
<td>Large POST to external</td>
<td>10.0.1.138</td>
<td>cards-20131129_part2.csv / SHA256: e7149c9aea07d4f8</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 08:50:00</td>
<td>PROXY-01</td>
<td>Config File Read</td>
<td>10.0.8.209</td>
<td>config.ini</td>
<td>Credentials found in config</td>
</tr>
<tr>
<td>2013-11-30 08:55:00</td>
<td>POS-01</td>
<td>Scheduled Task Creation</td>
<td>10.0.5.198</td>
<td>task: persist_worker</td>
<td>Persistence scheduled</td>
</tr>
<tr>
<td>2013-11-30 09:00:00</td>
<td>VPN-01</td>
<td>FTP Upload Attempt</td>
<td>10.0.7.14</td>
<td>cards-20131129_part5.csv / SHA256: b13ccbd23b0894a3</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 09:05:00</td>
<td>WORKSTATION-12</td>
<td>Suspicious Process Spawn</td>
<td>10.0.5.168</td>
<td>proc: unknown_exec / SHA256: 9a73dff0d8ef5fa0</td>
<td>Spawned by user 'svc_hvac'</td>
</tr>
<tr>
<td>2013-11-30 09:10:00</td>
<td>POS-02</td>
<td>Large POST to external</td>
<td>10.0.8.116</td>
<td>cards-20131129_part4.csv / SHA256: ce02838f65efe817</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
<tr>
<td>2013-11-30 09:15:00</td>
<td>POS-02</td>
<td>FTP Upload Attempt</td>
<td>10.0.9.104</td>
<td>cards-20131129_part9.csv / SHA256: a24e1365964acdce</td>
<td>Outbound to ftp-exfil-targetlab.example</td>
</tr>
</tbody>
</table> 

Lưu ý:  
\- Các dữ liệu, hash và domain trong tài liệu này đều đã được giả hóa cho mục đích đào tạo.  
\- Không bao gồm mã độc thật; chỉ mô phỏng hành vi để phục vụ lab và phân tích.

Tài liệu tham khảo (gợi ý):  
\- Báo cáo điều tra vụ Target Breach (2013)  
\- Bài viết phân tích BlackPOS / memory-scraper  
\- MITRE ATT&CK: T1003 Credential Dumping