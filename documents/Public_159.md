# Public_159

# CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG

## Khái quát về mã hóa khóa bất đối xứng

Mã hóa khóa bất đối xứng, đôi khi được gọi là mã hóa khóa công khai sử dụng một cặp khóa cho quá trình mã hóa và giải mã. Trong cặp khóa, khóa công khai được sử dụng cho mã hóa và khóa riêng được sử dụng cho giải mã. Chỉ khóa riêng cần giữ bí mật, còn khóa công khai có thể phổ biến rộng rãi, nhưng phải đảm bảo tính toàn vẹn và xác thực chủ thể của khóa.

Hình 3.27 minh họa quá trình mã hóa (Encrypt) và giải mã (Decrypt) sử dụng mã hóa khóa bất đối xứng. Theo đó, người gửi (Sender) sử dụng khóa công khai (Public key) của người nhận (Recipient) để mã hóa bản rõ (Plaintext) thành bản mã (Ciphertext) và gửi nó cho người nhận. Người nhận nhận được bản mã sử dụng khóa riêng (Private key) của mình để giải mã khôi phục bản rõ.

Đặc điểm nổi bật của các hệ mã hóa khóa bất đối xứng là kích thước khóa lớn, lên đến hàng ngàn bit. Do vậy, các hệ mã hóa dạng này thường có tốc độ thực thi chậm hơn nhiều lần so với các hệ mã hóa khóa đối xứng với độ an toàn tương đương. Mặc dù vậy, các hệ mã hóa khóa bất đối xứng có khả năng đạt độ an toàn cao và ưu điểm nổi bật nhất là việc quản lý và phân phối khóa đơn giản hơn do khóa công khai có thể phân phối rộng rãi.

|<image_1>|

_Hình 3.27. Mã hóa và giải mã trong hệ mã hóa bất đối xứng_

Các giải thuật mã hóa khóa bất đối xứng điển hình bao gồm: RSA, Rabin, ElGamal, McEliece và Knapsack. Trong mục tiếp theo chúng ta tìm hiểu về giải thuật mã hóa RSA – một trong các giải thuật mã hóa khóa đối xứng được sử dụng rộng rãi nhất trên thực tế.

## Giải thuật mã hóa RSA

### Giới thiệu

Giải thuật mã hóa RSA được 3 nhà khoa học người Mỹ là Ronald Rivest, Adi Shamir và Leonard Adleman phát minh năm 1977, và tên giải thuật RSA lấy theo chữ cái đầu của tên 3 đồng tác giả. Độ an toàn của RSA dựa trên tính khó của việc phân tích số nguyên rất lớn, với độ lớn cỡ hàng trăm chữ số thập phân. Giải thuật RSA sử dụng một cặp khóa, trong đó khóa công khai dùng để mã hóa và khóa riêng dùng để giải mã. Chỉ khóa riêng RSA cần giữ bí mật. Khóa công khai có thể công bố rộng rãi. Hiện nay, các khóa RSA có kích thước nhỏ hơn 1024 bit được coi là không an toàn do tốc độ các hệ thống máy tính tăng nhanh. Để đảm bảo an toàn, khuyến nghị sử dụng khóa 2048 bit trong giai đoạn 2010-2020. Trong tương lai, cần sử dụng khóa RSA có kích thước lớn hơn, chẳng hạn 3072 bit.

### Sinh khóa

RSA cung cấp một thủ tục sinh cặp khóa (khóa công khai và khóa riêng) tương đối đơn giản. Cụ thể, thủ tục sinh khóa gồm các bước như sau:

  * Tạo 2 số nguyên tốpvàq;

  * Tính modulon=p×q_


\- Tính Φ(n) = (p-1) × (q-1)

  * Chọn sốesao cho 0 <e< Φ(n) và gcd(e, Φ(n)) = 1, trong đó hàm gcd() tính ước số chung lớn nhất của 2 số nguyên. Nếu gcd(e, Φ(n)) = 1 thìevà Φ(n) là 2 số nguyên tố cùng nhau.

  * Chọn sốdsao chod≡e-1 mod Φ(n),


hoặc (d×e) mod Φ(n) = 1

haydlà modulo nghịch đảo củae_.

  * Ta có (n,e) là khóa công khai, (n,d) là khóa riêng vàncòn được gọi là modulo.


### Mã hóa và giải mã

  * Mã hóa


\+ Thông điệp bản rõmđã được chuyển thành số, vớim<n_. Nếu thông điệp bản rõmcó kích thước lớn thì được chia thành các khốim i_, vớim i<n_.

\+ Bản mãc=m emodn_

  * Giải mã


\+ Bản mãc, vớic<n_

\+ Bản rõm=c dmodn_

### Ví dụ

  * Sinh khóa:


\+ Chọn 2 số nguyên tốp= 3 vàq= 11

\+ Tínhn=p× q = 3 × 11 = 33

\+ Tính Φ(n) = (p-1) × (q-1) = 2 × 10 = 20

\+ Chọn sốesao cho 0 <e< 20, vàevà Φ(n) là số nguyên tố cùng nhau (Φ(n) không chia hết choe). Chọne= 7

\+ Tính (dx e) mod Φ(n)  (d× 7) mod 20 = 1

_d= (20 ×k+1)/7 d= 3 (k=1)

\+ Ta có: khóa công khai là (33, 7) và khóa riêng là (33, 3)

  * Mã hóa:


\+ Với bản rõm= 6,

\+c=m emodn= 67 mod 33 = 279936 mod 33 = 30

\+ Vậy bản mãc= 30

  * Giải mã:


\+ Với bản mãc= 30

\+m=c dmodn= 303 mod 33 = 27000 mod 33 = 6

\+ Vậy bản rõm= 6.

### Một số yêu cầu với quá trình sinh khóa

Dưới đây liệt kê các yêu cầu đặt ra với các tham số sinh khóa và khóa để đảm bảo sự an toàn cho cặp khóa RSA. Các yêu cầu cụ thể gồm:

  * Yêu cầu với các tham số sinh khóapvàq:


\+ Các số nguyên tốpvàqphải được chọn sao cho việc phân tíchn(n=p×q) là không khả thi về mặt tính toán.pvàqnên có cùng độ lớn (tính bằng bit) và phải là các số đủ lớn. Nếuncó kích thước 2048 bit thìpvàqnên có kích thước khoảng 1024 bit.

\+ Hiệu sốp – qkhông nên quá nhỏ, do nếup – qquá nhỏ, tứcp≈qvàp≈ √𝑛_. Như vậy, có thể chọn các số nguyên tố ở gần √𝑛 và thử. Khi có đượcp, có thể tínhqvà tìm radlà khóa bí mật từ khóa công khaievà Φ(n) = (p\- 1)(q\- 1). Nếupvàqđược chọn ngẫu nhiên vàp–qđủ lớn, khả năng hai số này bị phân tích từngiảm đi.

  * Vấn đề sử dụng số mũ mã hóa (e) nhỏ: Khi sử dụng số mũ mã hóa (e) nhỏ, chẳng hạn


_e= 3 có thể tăng tốc độ mã hóa. Kẻ tấn công có thể nghe lén và lấy được bản mã, từ đó phân tích bản mã để khôi phục bản rõ. Do số mũ mã hóa nhỏ nên chi phí cho phân tích, hoặc vét cạn không quá lớn. Do vậy, nên sử dụng số mũ mã hóaeđủ lớn và thêm chuỗi ngẫu nhiên vào khối rõ trước khi mã hóa để giảm khả năng bị vét cạn hoặc phân tích bản mã.

  * Vấn đề sử dụng số mũ giải mã (d) nhỏ: Khi sử dụng số mũ giải mã (d) nhỏ, có thể tăng tốc độ giải mã. Nếudnhỏ và gcd(p-1,q-1) cũng nhỏ thìdcó thể tính được tương đối dễ dàng từ khóa công khai (n,e). Do vậy, để đảm bảo an toàn, nên sử dụng số mũ giải mãdđủ lớn.


# Các hàm băm

## Khái quát về hàm băm

### Giới thiệu

Hàm băm (hash function) là một hàm toán họchcó tối thiểu 2 thuộc tính:

  * Nén (Compression):hlà một ánh xạ từ chuỗi đầu vàoxcó chiều dài bất kỳ sang một chuỗi đầu rah(x) có chiều dài cố địnhnbit;

  * Dễ tính toán (Ease of computation): cho trước hàmhvà đầu vàox, việc tính toán


_h(x) là dễ dàng.

|<image_2>|

_Hình 3.28. Mô hình nén thông tin của hàm băm_

Hình 3.28 minh họa mô hình nén thông tin của hàm băm, theo đó thông điệp (Message) đầu vào với chiều dài tùy ý đi qua nhiều vòng xử lý của hàm băm để tạo chuỗi rút gọn, hay chuỗi đại diện (Digest) có kích thước cố định ở đầu ra.

### Phân loại

Có thể phân loại các hàm băm theo khóa sử dụng hoặc theo chức năng. Theo khóa sử dụng, các hàm băm gồm 2 loại: hàm băm không khóa (unkeyed) và hàm băm có khóa (keyed), như biểu diễn trên Hình 3.29. Trong khi hàm băm không khóa nhận đầu vào chỉ là thông điệp (dạngh(x), với hàm bămhvà thông điệpx), hàm băm có khóa nhận đầu vào gồm thông điệp và khóa bí mật (theo dạngh(x,K), với hàm bămhvà thông điệpxvàKlà khóa bí mật). Trong các hàm băm không khóa, các mã phát hiện sửa đổi (MDC – Modification Detection Code) được sử dụng rộng rãi nhất, bên cạnh một số hàm băm không khóa khác. Tương tự, trong các hàm băm có khóa, các mã xác thực thông điệp (MAC - Message Authentication Code) được sử dụng rộng rãi nhất, bên cạnh một số hàm băm có khóa khác.

|<image_3>|

_Hình 3.29. Phân loại các hàm băm theo khóa sử dụng_

Theo chức năng, có thể chia các hàm băm thành 2 loại chính:

  * Mã phát hiện sửa đổi (MDC - Modification Detection Code): MDC thường được sử dụng để tạo chuỗi đại diện cho thông điệp và dùng kết hợp với các kỹ thuật khác (như chữ ký số) để đảm bảo tính toàn vẹn của thông điệp. MDC thuộc loại hàm băm không khóa. MDC gồm 2 loại nhỏ:


\+ Hàm băm một chiều (OWHF - One-way hash functions): Với hàm băm một chiều, việc tính giá trị băm là dễ dàng, nhưng việc khôi phục thông điệp từ giá trị băm là rất khó khăn;

\+ Hàm băm chống đụng độ (CRHF - Collision resistant hash functions): Với hàm băm chống đụng độ, sẽ là rất khó để tìm được 2 thông điệp khác nhau nhưng có cùng giá trị băm.

  * Mã xác thực thông điệp (MAC - Message Authentication Code): MAC cũng được dùng để đảm bảo tính toàn vẹn của thông điệp mà không cần một kỹ thuật bổ sung nào khác. MAC là loại hàm băm có khóa như đã đề cập ở trên, với đầu vào là thông điệp và một khóa bí mật.


### Mô hình xử lý dữ liệu

Hình 3.30 biểu diễn mô hình tổng quát xử lý dữ liệu của các hàm băm. Theo đó, thông điệp đầu vào với độ dài tùy ý (arbitrary length input) đi qua hàm nén lặp nhiều vòng (iterated compression function) để tạo chuỗi đầu ra có kích thước cố định (fixed length output). Chuỗi này đi qua một khâu chuyển đổi định dạng tùy chọn (optional output transformation) để tạo ra chuỗi băm kết quả (output).

|<image_4>|

_Hình 3.30. Mô hình tổng quát xử lý dữ liệu của hàm băm_

Hình 3.31 mô tả chi tiết quá trình xử lý dữ liệu của các hàm băm. Theo đó, quá trình xử lý gồm 3 bước chính: (1) tiền xử lý (preprocessing), (2) xử lý lặp (iterated processing) và (3) chuyển đổi định dạng. Trong bước tiền xử lý, thông điệp đầu vàoxtrước hết được nối đuôi thêm một số bit và kích thước khối, sau đó chia thành các khối có kích thước xác định. Kết quả của bước này làtkhối dữ liệu có cùng kích thước có dạngx=x 1x2…xtlàm đầu vào cho bước 2\. Trong bước 2, từng khối dữ liệux iđược xử lý thông qua hàm nénf_

để tạo đầu ra làH i_. Kết quả của bước 2 là chuỗi đầu raH tvàH tđược chuyển đổi định dạng bởi hàmgđể tạo chuỗi giá trị băm hết quảh(x).

|<image_5>|

_Hình 3.31. Mô hình chi tiết xử lý dữ liệu của hàm băm_

## Một số hàm băm thông dụng

Các hàm băm thông dụng giới thiệu trong mục này đều là các hàm băm không khóa, gồm các họ hàm băm chính như sau:

  * Họ hàm băm MD (Message Digest) gồm các hàm băm MD2, MD4, MD5 và MD6.

  * Họ hàm băm SHA (Secure Hash Algorithm) gồm các hàm băm SHA0, SHA1, SHA2 và SHA3.

  * Một số hàm băm khác, gồm CRC (Cyclic redundancy checks), Checksums,...


Các mục con tiếp theo của mục này giới thiệu 2 hàm băm đã và đang được sử dụng rộng rãi nhất là hàm băm MD5 và SHA1.

### Hàm băm MD5

  * Giới thiệu


MD5 (Message Digest) là hàm băm không khóa được Ronald Rivest thiết kế năm 1991 để thay thế MD4. Chuỗi giá trị băm đầu ra của MD5 là 128 bit (16 byte) và thường được biểu diễn thành 32 số hexa. MD5 được sử dụng khá rộng rãi trong nhiều ứng dụng, như tạo chuỗi đảm bảo tính toàn vẹn thông điệp, tạo chuỗi kiểm tra lỗi, hoặc kiểm tra tính toàn vẹn dữ liệu (Checksum) và mã hóa mật khẩu trong các hệ điều hành và các ứng dụng. MD5 hiện nay được khuyến nghị không nên sử dụng do nó không còn đủ an toàn.

Nhiều điểm yếu của MD5 đã bị khai thác, như điển hình MD5 bị khai thác bởi mã độc Flame vào năm 2012.

  * Quá trình xử lý thông điệp


Quá trình xử lý thông điệp của MD5 gồm 2 khâu làtiền xử lývàcác vòng lặp xử lý_.

Cụ thể, chi tiết về các khâu này như sau:

  * Tiền xử lý: Thông điệp được chia thành các khối 512 bit (16 từ 32 bit). Nếu kích thước thông điệp không là bội số của 512 thì nối thêm số bit còn thiếu.

  * Các vòng lặp xử lý: Phần xử lý chính của MD5 làm việc trênstate128 bit, chia thành 4 từ 32 bit (A, B, C, D):


\+ Các từ A, B, C, D được khởi trị bằng một hằng cố định;

\+ Từng phần 32 bit của khối đầu vào 512 bit được đưa dần vào để thay đổistate;

\+ Quá trình xử lý gồm 4 vòng, mỗi vòng gồm 16 thao tác tương tự nhau.

\+ Mỗi thao tác gồm: Xử lý bởi hàm F (4 dạng hàm khác nhau cho mỗi vòng), Cộng modulo và Quay trái. Hình 3.32 biểu diễn lưu đồ xử lý của một thao tác của MD5, trong đó A, B, C, D là các từ 32 bit củastate, Mi: khối 32 bit thông điệp đầu vào, Ki là 32 bit hằng khác nhau cho mỗi thao tác, <<<s là thao tác dịch tráisbit, |<image_6>| biểu diễn phép cộng modulo 32 bit và F là hàm phi tuyến tính.

|<image_7>|

_Hình 3.32. Lưu đồ xử lý một thao tác của MD5_

Hàm F gồm 4 dạng được dùng cho 4 vòng lặp. Cụ thể, F có các dạng như sau: F(B, C, D) = (B ∧ C) ∨ (¬B ∧ D)

G(B, C, D) = (B ∧ D) ∨ (C ∧ ¬D) H(B, C, D) = B ⊕ C ⊕ D

I(B, C, D) = C ⊕ (B ∨ ¬D)

trong đó, các ký hiệu ⊕, ∧, ∨, ¬ biểu diễn các phép toán lô gíc XOR, AND, OR và NOT tương ứng.

### Hàm băm SHA1

  * Giới thiệu


SHA1 (Secure Hash Function) được Cơ quan mật vụ Mỹ thiết kế năm 1995 để thay thế cho hàm băm SHA0. Chuỗi giá trị băm đầu ra của SHA1 có kích thước 160 bit và thường được biểu diễn thành 40 số hexa. Tương tự MD5, SHA1 được sử dụng rộng rãi để đảm bảo tính xác thực và toàn vẹn thông điệp.

  * Quá trình xử lý thông điệp


SHA1 sử dụng thủ tục xử lý thông điệp tương tự MD5, cũng gồm 2 khâu làtiền xử lý_

vàcác vòng lặp xử lý_. Cụ thể, chi tiết về các khâu này như sau:

  * Tiền xử lý: Thông điệp được chia thành các khối 512 bit (16 từ 32 bit). Nếu kích thước thông điệp không là bội số của 512 thì nối thêm số bit còn thiếu.

  * Các vòng lặp xử lý: Phần xử lý chính của SHA1 làm việc trênstate160 bit, chia thành 5 từ 32 bit (A, B, C, D, E):


\+ Các từ A, B, C, D, E được khởi trị bằng một hằng cố định;

\+ Từng phần 32 bit của khối đầu vào 512 bit được đưa dần vào để thay đổistate;

\+ Quá trình xử lý gồm 80 vòng, mỗi vòng gồm các thao tác: add, and, or, xor, rotate, mod.

\+ Mỗi vòng xử lý gồm: Xử lý bởi hàm phi tuyến tính F (có nhiều dạng hàm khác nhau), Cộng modulo và Quay trái. Hình 3.33 biểu diễn lưu đồ một vòng xử lý của SHA1, trong đó A, B, C, D, E là các từ 32 bit củastate, Wt: khối 32 bit thông điệp đầu vào, Kt là 32 bit hằng khác nhau cho mỗi vòng, <<<n là thao tác dịch tráinbit, |<image_8>| biểu diễn phép cộng modulo 32 bit và F là hàm phi tuyến tính.

|<image_9>|

_Hình 3.33. Lưu đồ một vòng xử lý của SHA1_