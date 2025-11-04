# Public_606

Bảng dưới đây mô tả tính năng và tiêu chí, chỉ tiêu kỹ thuật đối với từng tính năng cụ thể. Đối với tính năng có một tiêu chí, chỉ tiêu kỹ thuật thì việc đánh giá là đạt khi giải pháp cung cấp được tính năng đó, không đạt nếu giải pháp không cung cấp được tính năng đó.

Đối với tính năng có nhiều tiêu chí, chỉ tiêu kỹ thuật khác nhau thì tính năng đó đạt khi tất cả các tiêu chí, chỉ tiêu kỹ thuật đều đạt, không đạt khi một trong các tiêu chí, chỉ tiêu kỹ thuật không đạt.

# YÊU CẦU CƠ BẢN VỀ TÍNH NĂNG AN TOÀN THÔNG TIN
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Tên tính năng</strong></th>
<th><strong>Tiêu chí, chỉ tiêu kỹ thuật</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Bảo vệ thông tin cá nhân của người dùng</td>
<td>Giải pháp cung cấp tính năng phòng chống việc mất mát, rò rỉ, giả
mạo, thay đổi, lợi dụng thông tin cá nhân của người dùng trong cả quá
trình truyền tin và lưu trữ.</td>
</tr>
<tr>
<td>Tích hợp dịch vụ xác thực người dùng</td>
<td>Giải pháp cung cấp tính năng xác thực người dùng thông qua các dịch
vụ bên thứ ba có thể được tích hợp vào (dựa trên, LDAP hoặc OpenID /
SAM) trước khi người dùng truy cập vào các giao diện gồm cổng thông tin
quản trị, danh mục dịch vụ và quản trị.</td>
</tr>
<tr>
<td>Tích hợp điều khiển truy cập dựa trên vai trò - RBAC (Role- Based
Access Control)</td>
<td><p>Giải pháp cung cấp 03 tính năng sau:</p>
<p>Tích hợp sẵn các quyền truy cập đã được định nghĩa trước bao gồm ít
nhất 02 quyền mức quản trị dành cho nhà cung cấp dịch vụ điện toán đám
mây (bên cung cấp) và người sử dụng sử dụng dịch vụ điện toán đám mây
(bên sử dụng).</p>
<p>Cho phép nhà cung cấp dịch vụ điện toán đám mây định nghĩa các quyền
truy cập đối với các thao tác mà nhà cung cấp thực hiện trên tất cả các
thành phần của nền tảng nhằm phục vụ mục đích quản trị.</p>
<p>Cho phép nhà cung cấp dịch vụ điện toán đám mây định nghĩa các quyền
truy cập đối với các thao tác mà người sử dụng sử dụng dịch vụ điện toán
đám mây thực hiện trên những thành phần của nền tảng mà người sử dụng
muốn sử dụng và tuân theo thỏa thuận giữa hai bên.</p></td>
</tr>
<tr>
<td>Giao tiếp giữa các thành phần qua kênh TLS</td>
<td>Giải pháp cung cấp tính năng cho phép các thành phần giao tiếp qua
kênh TLS.</td>
</tr>
<tr>
<td>Hỗ trợ TLS tự kí (Self-signed TLS)</td>
<td><p>Giải pháp cung cấp 02 tính năng sau:</p>
<p>Cho phép quản trị viên tạo các chứng thư điện tử tự kí (Self-signed)
TLS để đẩy nhanh quá trình triển khai.</p>
<p>Cho phép các chứng thư điện tử được tạo bởi một đơn vị cấp chứng thư
(CA) tin cậy (trusted certificate authority).</p></td>
</tr>
<tr>
<td>Tích hợp giao diện cổng thông tin quản trị hỗ trợ sử dụng kênh
TLS</td>
<td>Giải pháp cung cấp tính năng tích hợp giao diện cổng thông tin quản
trị hỗ trợ sử dụng kênh TLS dành cho người dùng đầu cuối và quản trị
viên khi muốn kết nối qua kênh TLS.</td>
</tr>
<tr>
<td>Chuyển hướng kết nối qua sử dụng TLS</td>
<td>Giải pháp cung cấp tính năng cho phép quản trị viên cấu hình để áp
dụng chính sách phải sử dụng kênh TLS đối với mọi kết nối truy cập vào
giao diện cổng thông tin trên và dùng các phiên HTTP không mã hóa giống
như là một lựa chọn dự phòng</td>
</tr>
<tr>
<td>Ghi log hoạt động của các hành động</td>
<td><p>Giải pháp cung cấp 03 tính năng sau:</p>
<p>Ghi log hoạt động của các hành động thực hiện trên tất cả các thành
phần.</p>
<p>Cho phép quản trị viên xem xét, kiểm tra log thu được thông qua thành
phần báo cáo.</p>
<p>Chuyển log thu thập được cho bên thứ ba cung cấp giải pháp bảo mật để
xem xét, kiểm tra kỹ hơn.</p></td>
</tr>
<tr>
<td>Tách biệt máy ảo với phần mềm giám sát máy ảo</td>
<td>Giải pháp cung cấp tính năng đảm bảo máy ảo được giám sát bởi một
phần mềm giám sát máy ảo không gây ảnh hưởng đến phần mềm giám sát
đó.</td>
</tr>
<tr>
<td>Phân quyền cho máy ảo truy cập đến tài nguyên</td>
<td>Giải pháp cung cấp tính năng đảm bảo phần mềm giám sát máy ảo phân
quyền cho máy ảo mà nó giám sát truy cập đến tài nguyên đúng theo chính
sách quản trị nền tảng.</td>
</tr>
<tr>
<td>Cấu hình cho phần mềm giám sát máy ảo</td>
<td>Giải pháp cung cấp tính năng cho phép quản trị viên cấu hình cho
phần mềm giám sát máy ảo và kiểm tra được tính hợp lệ của cấu hình phần
mềm giám sát máy ảo.</td>
</tr>
<tr>
<td>Bảo vệ dữ liệu</td>
<td>Giải pháp cung cấp tính năng phòng chống việc mất mát, rò rỉ, thay
đổi dữ liệu trong cả quá trình lưu trữ trên các bộ nhớ dùng chung và
truyền tin qua các mạng chia sẻ.</td>
</tr>
<tr>
<td>Tách biệt các máy ảo với nhau</td>
<td>Giải pháp cung cấp tính năng tách biệt hoàn toàn các máy ảo với nhau
về logic.</td>
</tr>
<tr>
<td>Đảm bảo các API của hệ thống có ít nhất 02 mức quyền truy cập đã
định nghĩa sẵn cho các API của client</td>
<td><p>Giải pháp cung cấp 02 tính năng sau:</p>
<p>Đảm bảo các chức năng quản trị và vận hành của hệ thống định nghĩa
sẵn ít nhất 02 mức quyền truy cập cho các API của client (ví dụ: quyền
root và quyền user, trong đó quyền root cao hơn quyền user).</p>
<p>Đảm bảo các chức năng quản trị và vận hành của hệ thống xác thực được
client dựa trên các tiêu chí được định nghĩa trước bởi quản trị
viên.</p></td>
</tr>
</tbody>
</table> 

# YÊU CẦU THIẾT LẬP CẤU HÌNH BẢO MẬT CHO HẠ TẦNG ĐIỆN TOÁN ĐÁM MÂY

Bảng dưới đây mô tả yêu cầu đối với việc thiết lập cấu hình bảo mật cho hạ tầng điện toán đám mây. Việc thiết lập cấu hình như dưới đây là yêu cầu áp dụng.

Các yêu cầu được đánh giá là “Đạt” khi việc thiết lập cấu hình như được mô tả (nội dung Mô tả tiêu chí) hoặc được thiết lập ở mức bảo mật cao hơn. Đánh giá là “Không đạt” việc thiết lập cấu hình ở mức thấp hơn tiêu chí được mô tả.

Nội dung mô tả tiêu chí ở bảng dưới đây trên cơ sở tham khảo thiết lập cấu hình bảo mật trên nền tảng OpenStack, cơ quan, tổ chức khi thực hiện đánh giá với nền tảng khác thì thực hiện tương tự như với nền tảng OpenStack.
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Tính năng</strong></th>
<th><strong>Tiêu chí, chỉ tiêu kỹ thuật</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Dịch vụ xác thực</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ xác
thực</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/keystone/keystone.conf được gán quyền sở hữu cho tài
khoản là keystone và nhóm tài khoản là keystone.</p>
<p>Tệp tin /etc/keystone/keystone-paste.ini được gán quyền sở hữu cho
tài khoản là keystone và nhóm tài khoản là keystone.</p>
<p>Tệp tin /etc/keystone/policy.json được gán quyền sở hữu cho tài khoản
là keystone và nhóm tài khoản là keystone.</p>
<p>Tệp tin /etc/keystone/logging.conf được gán quyền sở hữu cho tài
khoản là keystone và nhóm tài khoản là keystone.</p>
<p>Tệp tin /etc/keystone/tls/certs/signing_cert.pem được gán quyền sở
hữu cho tài khoản là keystone và nhóm tài khoản là keystone.</p>
<p>Tệp tin /etc/keystone/tls/private/signing_key.pem được gán quyền sở
hữu cho tài khoản là keystone và nhóm tài khoản là keystone.</p>
<p>Tệp tin /etc/keystone/tls/certs/ca.pem được gán quyền sở hữu cho tài
khoản là keystone và nhóm tài khoản là keystone.</p>
<p>Thư mục /etc/keystone/ được gán quyền sở hữu cho tài khoản là
keystone và nhóm tài khoản là keystone</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ xác
thực</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/keystone/keystone.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/keystone/keystone-paste.ini được gán quyền truy cập tối
thiểu là 640.</p>
<p>Tệp tin /etc/keystone/policy.json được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/keystone/logging.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin//etc/keystone/tls/certs/signing_cert.pem được gán quyền truy
cập tối thiểu là 640.</p>
<p>Tệp tin /etc/keystone/tls/private/signing_key.pem được gán quyền truy
cập tối thiểu là 640.</p>
<p>Tệp tin /etc/keystone/tls/certs/ca.pem được gán quyền truy cập tối
thiểu là 640.</p>
<p>Thư mục /etc/keystone/ được gán quyền truy cập tối thiểu là
750.</p></td>
</tr>
<tr>
<td>Kích hoạt kênh TLS trên máy chủ cung cấp dịch vụ xác thực</td>
<td>Cho phép người quản trị kết nối, quản trị với nền tảng điện toán đám
mây thông qua kết nối bảo mật TLS</td>
</tr>
<tr>
<td>Sử dụng hàm băm mạnh cho các token tạo bởi hạ tầng khóa công khai
PKI (Public Key Infrastructure) của dịch vụ xác thực</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số hash_algorithm ở phần [token] trong tệp tin</p>
<p>/etc/keystone/keystone.conf được gán giá trị là SHA256.</p></td>
</tr>
<tr>
<td>Phòng chống tấn công DoS (Denial- of-Service)</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số max_request_body_size trong tệp tin /etc/
keystone/keystone.conf được gán giá trị là 114688 (theo mặc định) hoặc
được gán một giá trị hợp lý và phù hợp với môi trường triển khai thực
tế.</p></td>
</tr>
<tr>
<td>Phòng chống lợi dụng token admin để chiếm quyền quản trị</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số admin_token ở phần [DEFAULT] trong tệp tin
/etc/keystone/keystone.conf được vô hiệu hóa (được gán giá trị
rỗng).</p>
<p>Tham số AdminTokenAuthMiddleware ở phần [filter:admin_token_auth]
trong tệp tin /etc/keystone/keystone-paste.ini được xóa đi.</p></td>
</tr>
<tr>
<td>Ẩn những thông tin nhạy cảm trong quá trình xác thực</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số insecure_debug ở phần [DEFAULT] trong tệp tin
/etc/keystone/keystone.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế đảm bảo an toàn cho quá trình sinh token</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số provider ở phần [token] trong tệp tin /etc/
keystone/keystone.conf được gán giá trị là fernet.</p></td>
</tr>
<tr>
<td colspan="2">Dịch vụ quản trị giao diện dashboard</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ
dashboard</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tệp tin /etc/openstack-dashboard/local_settings.py được gán quyền
sở hữu cho tài khoản là root và nhóm tài khoản là horizon.</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ
dashboard</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tệp tin /etc/openstack-dashboard/local_settings.py được gán quyền
truy cập tối thiểu là 640.</p></td>
</tr>
<tr>
<td>Phòng chống tấn công XFS (Cross- Frame Scripting)</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số DISALLOW_IFRAME_EMBED trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán giá trị là
True.</p></td>
</tr>
<tr>
<td>Phòng chống tấn công CSRF (Cross- Site Request Forgery)</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số CSRF_COOKIE_SECURE trong tệp tin</p>
<p>/etc/openstack-dashboard/local_settings.py được gán giá trị là
True.</p></td>
</tr>
<tr>
<td>Phòng chống lấy cắp session ID thông qua tấn công MitM (Man-in-the-
Middle)</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số SESSION_COOKIE_SECURE trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán giá trị là
True.</p></td>
</tr>
<tr>
<td>Phòng chống lấy cắp session ID thông qua tấn công XSS (Cross-Site
Scripting)</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số SESSION_COOKIE_HTTPONLY trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán giá trị là
True.</p></td>
</tr>
<tr>
<td>Vô hiệu hóa tính năng tự động điền mật khẩu</td>
<td><p>Tham số thiết lập cho tệp tin cấu hình với nền tảng OpenStack
(thực hiện tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số PASSWORD_AUTOCOMPLETE trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán giá trị là
False.</p></td>
</tr>
<tr>
<td>Vô hiệu hóa tính năng hiển thị bản rõ của mật khẩu</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số DISABLE_PASSWORD_REVEAL trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán giá trị là
True.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế chỉ cho phép quản trị viên thay đổi mật khẩu</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số ENFORCE_PASSWORD_CHECK trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán giá trị là
True.</p></td>
</tr>
<tr>
<td>Định nghĩa biểu thức chính quy kiểm tra mật khẩu</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số PASSWORD_VALIDATOR trong tệp tin</p>
<p>/etc/openstack-dashboard/local_settings.py được gán giá trị khác với
giá trị mặc định là "regex": '.*'.</p></td>
</tr>
<tr>
<td><p>Định nghĩa giá trị cho header X- Forwarded-Proto đối với các kết
nối đến dịch vụ</p>
<p>dashboard qua proxy và kênh TLS</p></td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số SECURE_PROXY_TLS_HEADER trong tệp tin
/etc/openstack-dashboard/local_settings.py được gán hai giá trị là
'HTTP_X_FORWARDEDPROTO', 'https'.</p></td>
</tr>
<tr>
<td colspan="2">Dịch vụ tính toán</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ tính
toán</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/nova/nova.conf được gán quyền sở hữu cho tài khoản là
root và nhóm tài khoản là nova.</p>
<p>Tệp tin /etc/nova/api-paste.ini được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là nova.</p>
<p>Tệp tin /etc/nova/policy.json được gán quyền sở hữu cho tài khoản là
root và nhóm tài khoản là nova.</p>
<p>Tệp tin /etc/nova/rootwrap.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là nova.</p>
<p>Thư mục /etc/nova/ được gán quyền sở hữu cho tài khoản là root và
nhóm tài khoản là nova.</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ tính
toán</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/nova/nova.conf được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/nova/api-paste.ini được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/nova/policy.json được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/nova/rootwrap.conf được gán quyền truy cập tối thiểu là
640.</p>
<p>Thư mục /etc/nova/ được gán quyền truy cập tối thiểu là 750.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực bằng dịch vụ xác thực đối với những kết
nối đến dịch vụ tính toán</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số auth_strategy trong tệp tin /etc/nova/nova. conf được gán
giá trị là keystone.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực qua kênh TLS đối với những kết nối đến
dịch vụ tính toán</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số www_authenticate_uri ở phần [keystoneauthtoken] trong tệp
tin /etc/nova/nova.conf được gán giá trị là đường dẫn API đầu cuối đến
máy chủ cung cấp dịch vụ keystone bắt đầu với xâu https://.</p>
<p>Tham số insecure ở phần [keystone_authtoken] trong tệp tin
/etc/nova/nova.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ tính toán và
dịch vụ quản lý máy chủ ảo</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số api_máy chủ ở phần [glance] trong tệp tin</p>
<p>/etc/nova/nova.conf được gán giá trị là đường dẫn API đầu cuối đến
máy chủ cung cấp dịch vụ glance bắt đầu với xâu https://.</p>
<p>Tham số api_insecure ở phần [glance] trong tệp tin</p>
<p>/etc/nova/nova.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td colspan="2">Dịch vụ lưu trữ</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ lưu
trữ</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/cinder/cinder.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là cinder.</p>
<p>Tệp tin /etc/cinder/api-paste.ini được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là cinder.</p>
<p>Tệp tin /etc/cinder/policy.json được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là cinder.</p>
<p>Tệp tin /etc/cinder/rootwrap.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là cinder.</p>
<p>Thư mục /etc/cinder/ được gán quyền sở hữu cho tài khoản là root và
nhóm tài khoản là cinder.</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ lưu
trữ</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/cinder/cinder.conf được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/cinder/api-paste.ini được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/cinder/policy.json được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/cinder/rootwrap.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Thư mục /etc/cinder/ được gán quyền truy cập tối thiểu là
750.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực bằng dịch vụ xác thực đối với những kết
nối đến dịch vụ lưu trữ</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số auth_strategy trong tệp tin /etc/cinder/ cinder.conf được
gán giá trị là keystone.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực qua kênh TLS đối với những kết nối đến
dịch vụ lưu trữ</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số www_authenticate_uri ở phần [keystoneauthtoken] trong tệp
tin /etc/ cinder/cinder.conf được gán giá trị là đường dẫn API đầu cuối
đến máy chủ cung cấp dịch vụ keystone bắt đầu với xâu https://.</p>
<p>Tham số insecure ở phần [keystone_authtoken] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ lưu trữ và dịch
vụ tính toán</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số nova_api_insecure ở phần [DEFAULT] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ lưu trữ và dịch
vụ quản lý máy chủ ảo</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số glance_api_máy chủ ở phần [glance] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị là đường dẫn API đầu cuối đến
máy chủ cung cấp dịch vụ glance bắt đầu với xâu https://.</p>
<p>Tham số glance_api_insecure ở phần [glance] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế đảm bảo an toàn vận hành các thiết bị NAS (Network
- Attached Storage)</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số nas_secure_file_permissions ở phần [DEFAULT] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị là auto.</p>
<p>Tham số nas_secure_file_operations ở phần [DEFAULT] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị là auto.</p></td>
</tr>
<tr>
<td>Phòng chống tấn công DoS (Denial- of-Service)</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số max_request_body_size ở phần [oslomiddleware] trong tệp
tin /etc/cinder/cinder.conf được gán giá trị là 114688.</p></td>
</tr>
<tr>
<td>Kích hoạt tính năng mã hóa volume</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số backend ở phần [key_manager] trong tệp tin
/etc/cinder/cinder.conf được gán giá trị.</p>
<p>Tham số backend ở phần [key_manager] trong tệp tin
/etc/nova/nova.conf được gán giá trị.</p></td>
</tr>
<tr>
<td colspan="2">Dịch vụ quản lý máy chủ ảo</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ quản lý
máy chủ ảo</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>1. Tệp tin /etc/glance/glance-api-paste.ini được gán quyền truy cập
tối thiểu là 640.</p>
<p>Tệp tin /etc/glance/glance-api.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/glance/glance-cache.conf được gán quyền truy cập tối
thiểu là 640.</p>
<p>Tệp tin /etc/glance/glance-manage.conf được gán quyền truy cập tối
thiểu là 640.</p>
<p>Tệp tin /etc/glance/glance-registry-paste.ini được gán quyền truy cập
tối thiểu là 640.</p>
<p>Tệp tin /etc/glance/glance-registry.conf được gán quyền truy cập tối
thiểu là 640.</p>
<p>Tệp tin /etc/glance/glance-scrubber.conf được gán quyền truy cập tối
thiểu là 640.</p>
<p>Tệp tin /etc/glance/glance-swift-store.conf được gán quyền truy cập
tối thiểu là 640.</p>
<p>Tệp tin /etc/glance/policy.json được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/glance/schema-image.json được gán quyền truy cập tối
thiểu là 640.</p>
<p>Tệp tin /etc/glance/schema.json được gán quyền truy cập tối thiểu là
640.</p>
<p>12. Thư mục /etc/glance/ được gán quyền truy cập tối thiểu là
750.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực bằng dịch vụ xác thực đối với những kết
nối đến dịch vụ quản lý máy chủ ảo</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số auth_strategy ở phần [DEFAULT] trong tệp tin
/etc/glance/glance-api.conf được gán giá trị là keystone.</p>
<p>Tham số auth_strategy ở phần [DEFAULT] trong tệp tin
/etc/glance/glance-registry.conf được gán giá trị là keystone.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực qua kênh TLS đối với những kết nối đến
dịch vụ quản lý máy chủ ảo</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số www_authenticate_uri ở phần [keystoneauthtoken] trong tệp
tin /etc/glance/glanceregistry. conf được gán giá trị là đường dẫn API
đầu cuối đến máy chủ cung cấp dịch vụ keystone bắt đầu với xâu
https://.</p>
<p>Tham số insecure ở phần [keystone_authtoken] trong tệp tin
/etc/glance/glance-registry.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Phòng chống tấn công quét thăm dò port</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số copy_from trong tệp tin /etc/glance/policy. json được gán
giá trị (ví dụ: role:admin).</p></td>
</tr>
<tr>
<td colspan="2">Dịch vụ chia sẻ lưu trữ</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ chia sẻ
lưu trữ</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/manila/manila.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là manila.</p>
<p>Tệp tin /etc/manila/api-paste.ini được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là manila.</p>
<p>Tệp tin /etc/manila/policy.json được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là manila.</p>
<p>Tệp tin /etc/manila/rootwrap.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là manila.</p>
<p>Thư mục /etc/manila/ được gán quyền sở hữu cho tài khoản là root và
nhóm tài khoản là manila.</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ chia sẻ
lưu trữ</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/manila/manila.conf được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/manila/api-paste.ini được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/manila/policy.json được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/manila/rootwrap.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Thư mục /etc/manila/ được gán quyền truy cập tối thiểu là
750.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực bằng dịch vụ xác thực đối với những kết
nối đến dịch vụ chia sẻ lưu trữ</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số auth_strategy ở phần [DEFAULT] trong tệp tin
/etc/manila/manila.conf được gán giá trị là keystone.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực qua kênh TLS đối với những kết nối đến
dịch vụ chia sẻ lưu trữ</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số identity_uri ở phần [keystone_authtoken] trong tệp tin
/etc/manila/manila.conf được gán giá trị là đường dẫn API đầu cuối đến
máy chủ cung cấp dịch vụ keystone bắt đầu với xâu https://.</p>
<p>Tham số insecure ở phần [keystone_authtoken] trong tệp tin
/etc/manila/manila.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ chia sẻ lưu trữ
và dịch vụ tính toán</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số nova_api_insecure ở phần [DEFAULT] trong tệp tin
/etc/manila/manila.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ chia sẻ lưu trữ
và dịch vụ quản lý mạng</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số neutron_api_insecure ở phần [DEFAULT] trong tệp tin
/etc/manila/manila.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ chia sẻ lưu trữ
và dịch vụ lưu trữ</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số cinder_api_insecure ở phần [DEFAULT] trong tệp tin
/etc/manila/manila.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Phòng chống tấn công DoS (Denial- of-Service)</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>- Tham số max_request_body_size ở phần [oslomiddleware] trong tệp
tin /etc/manila/manila.conf được gán giá trị là 114688.</p></td>
</tr>
<tr>
<td colspan="2">Dich vụ quản lý mạng (networking)</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ quản lý
mạng</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/neutron/neutron.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là neutron.</p>
<p>Tệp tin /etc/neutron/api-paste.ini được gán quyền sở hữu cho tài
khoản là root và nhóm tài khoản là neutron.</p>
<p>Tệp tin /etc/neutron/policy.json được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là neutron.</p>
<p>Tệp tin /etc/neutron/rootwrap.conf được gán quyền sở hữu cho tài
khoản là root và nhóm tài khoản là neutron.</p>
<p>Thư mục /etc/neutron/ được gán quyền sở hữu cho tài khoản là root và
nhóm tài khoản là neutron.</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ quản lý
mạng</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>Tệp tin /etc/neutron/neutron.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/neutron/api-paste.ini được gán quyền truy cập tối thiểu
là 640.</p>
<p>Tệp tin /etc/neutron/policy.json được gán quyền truy cập tối thiểu là
640.</p>
<p>Tệp tin /etc/neutron/rootwrap.conf được gán quyền truy cập tối thiểu
là 640.</p>
<p>Thư mục /etc/neutron/ được gán quyền truy cập tối thiểu là
750.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực bằng dịch vụ xác thực đối với những kết
nối đến dịch vụ quản lý mạng</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số auth_strategy ở phần [DEFAULT] trong tệp tin
/etc/neutron/neutron.conf được gán giá trị là keystone.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực qua kênh TLS đối với những kết nối đến
dịch vụ quản lý mạng</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số www_authenticate_uri ở phần [keystoneauthtoken] trong tệp
tin /etc/neutron/neutron.conf được gán giá trị là đường dẫn API đầu cuối
đến máy chủ cung cấp dịch vụ keystone bắt đầu với xâu https://.</p>
<p>Tham số insecure ở phần [keystone_authtoken] trong tệp tin
/etc/neutron/neutron.conf được gán giá trị là False.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế giao tiếp qua kênh TLS giữa dịch vụ quản lý mạng và
các đối tượng khác</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số use_tls ở phần [DEFAULT] trong tệp tin</p>
<p>/etc/neutron/neutron.conf được gán giá trị là True.</p></td>
</tr>
<tr>
<td colspan="2">Dịch vụ quản lý thông tin mật</td>
</tr>
<tr>
<td>Cấp quyền sở hữu phù hợp cho các tệp tin cấu hình dịch vụ quản lý
thông tin mật</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>File /etc/barbican/barbican.conf được gán quyền sở hữu cho tài khoản
là root và nhóm tài khoản là barbican.</p>
<p>File /etc/barbican/barbican-api-paste.ini được gán quyền sở hữu cho
tài khoản là root và nhóm tài khoản là barbican.</p>
<p>File /etc/barbican/policy.json được gán quyền sở hữu cho tài khoản là
root và nhóm tài khoản là barbican.</p>
<p>Directory /etc/barbican/ được gán quyền sở hữu cho tài khoản là root
và nhóm tài khoản là barbican.</p></td>
</tr>
<tr>
<td>Cấp quyền truy cập phù hợp cho các tệp tin cấu hình dịch vụ quản lý
thông tin mật</td>
<td><p>Các tệp tin cấu hình với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) bao gồm:</p>
<p>File /etc/barbican/barbican.conf được gán quyền truy cập tối thiểu là
640.</p>
<p>File /etc/barbican/barbican-api-paste.ini được gán quyền truy cập tối
thiểu là 640.</p>
<p>File /etc/barbican/policy.json được gán quyền truy cập tối thiểu là
640.</p>
<p>Directory /etc/barbican/ được gán quyền truy cập tối thiểu là
750.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực bằng dịch vụ xác thực đối với những kết
nối đến dịch vụ quản lý thông tin mật</td>
<td><p>Tham số được thiết lập với nền tảng OpenStack (thực hiện tương tự
đối với các nền tảng khác) như sau:</p>
<p>- Tham số auth_strategy được liệt kê ở phần
[pipeline:barbican-api-keystone] trong file /etc/
barbican/barbican-api-paste.ini.</p></td>
</tr>
<tr>
<td>Thiết lập cơ chế xác thực qua kênh TLS đối với những kết nối đến
dịch vụ quản lý thông tin mật</td>
<td><p>Các tham số được thiết lập với nền tảng OpenStack (thực hiện
tương tự đối với các nền tảng khác) như sau:</p>
<p>Tham số identity_uri ở phần [keystone_authtoken] trong file
/etc/barbican/barbican.conf được gán giá trị là đường dẫn API đầu cuối
đến máy chủ cung cấp dịch vụ keystone bắt đầu với xâu https://.</p>
<p>Tham số insecure ở phần [keystone_authtoken] trong file
/etc/barbican/barbican.conf được gán giá trị là False.</p></td>
</tr>
</tbody>
</table>