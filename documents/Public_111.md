# Public_111

Trong các phần trước ta đã làm quen với vấn đề suy diễn xác suất, trong đó cho trước một số bằng chứngE1, …,E n_, cần tính xác suất điều kiệnP(Q|E1, …,E n_) để kết luận về câu truy vấnQ_.

Xác suất điều kiện trên có thể tính được nếu biết toàn bộ xác suất đồng thời của các biến ngẫu nhiên. Tuy nhiên, trên thực tế, các bài toán thường có số lượng biến ngẫu nhiên lớn, dẫn tới số lượng xác suất đồng thời tăng theo hàm mũ. Do vậy, liệt kê và sử dụng bảng xác suất đồng thời đầy đủ để suy diễn là không thực tế.

Để khắc phục khó khăn trên, trong phần này ta sẽ xem xét cách sử dụng mạng Bayes như một mô hình biểu diễn xác suất rút gọn và cách thực hiện suy diễn xác suất trên mạng Bayes.

# Khái niệm mạng Bayes

Để tiện cho việc trình bày khái niệm mạng Bayes, xét một ví dụ sau3.

_Một người đi làm về và muốn dự đoán xem ở nhà có người không thông qua một số dấu hiệu có thể quan sát được. Cho biết một số dữ kiện sau:_

\-Nếu cả nhà đi vắng thì thường bật đèn ngoài sân. Tuy nhiên, đèn ngoài sân có thể được cả trong một số trường hợp có người ở nhà, ví dụ khi có khách đến chơi.\-Nếu cả nhà đi vắng thì thường buộc chó ở sân sau._

\-Tuy nhiên chó có thể được buộc ở sân sau cả khi có người ở nhà nếu như chó bị đau bụng._

\-Nếu chó buộc ở ngoài thì có thể nghe tiếng sủa, tuy nhiên có thể nghe tiếng sủa (của chó hàng xóm) cả khi chó không buộc ở ngoài._

Để thực hiện suy diễn xác suất cho bài toán trên, trước tiên cần xây dựng mô hình xác suất. Ta sẽ sử dụng năm biến ngẫu nhiên sau để thể hiện các dữ kiện liên quan tới bài toán.

O: không ai ở nhà

L: đèn sáng
D: chó ở ngoài
B: chó bị ốm.
H: nghe thấy tiếng sủa.

Việc phân tích bài toán cho thấy:

\- Nếu biết D thì H không phụ thuộc vào O, L, B.
\- Nếu biết B thì D độc lập với O.
\- O và B độc lập với nhau

Tiếp theo, ta xây dựng một đồ thị, trong đó mỗi biến ngẫu nhiên ở trên được biểu diễn bởi một nút như trên hình vẽ dưới đây (hình 4.1). Các nút được nối với nhau bằng những cung có hướng sao cho hai hai nút có quan hệ phụ thuộc được nối bởi một cung và hướng của cung thể hiện chiều tác động của nút gốc tới nút đích. Với đồ thị có hướng, ta có thể xác định quan hệ giữa các nút như sau: nếu tồn tại cung có hướng từ nút A tới nút B thì nút A được gọi là nút cha (mẹ) và nút B là nút con.

|<image_1>|

Hình 4.1: Một ví dụ mạng Bayes

Sau khi có đồ thị, ta thêm vàobảng xác suất điều kiện_. Bảng xác suất điều kiện thể hiện xác suất của biến khi biết giá trị cụ thể của các biến ở các nút cha mẹ. Trong trường hợp nút không có cha mẹ, xác suất trở thành xác suất tiền nghiệm. Để thuận tiện, bảng xác suất điều kiện được thể hiện ngay trên hình vẽ cùng với đồ thị.

Đồ thị vừa xây dựng cùng với các bảng xác suất điều kiện tạo thành mạng Bayes cho bài toán trong ví dụ trên.

_Định nghĩa:Mạng Bayes là một mô hình xác suất bao gồm 2 phần

\- Phần thứ nhất là một đồ thị có hướng không chứa chu trình, trong đó mỗi nút tương ứng với một biến ngẫu nhiên, các cung thể hiện mối quan hệ phụ thuộc giữa các biến.

\- Phần thứ hai là các bảng xác suất điều kiện: mỗi nút có một bảng xác suất điều kiện cho biết xác suất các giá trị của biến khi biết giá trị các nút cha mẹ.

Cấu trúc của đồ thị trong mạng Bayes thể hiện mối quan hệ phụ thuộc hoặc độc lập giữa các biến ngẫu nhiên của bài toán. Hai nút được nối với nhau bởi một cung khi giữa hai nút có quan hệ trực tiếp với nhau, trong đó giá trị nút gốc ảnh hưởng tới giá trị nút đích.

Lưu ý rằng trong cấu trúc của mạng Bayes không cho phép có chu trình. Hạn chế này ảnh hưởng tới khả năng mô hình hóa của mạng Bayes trong một số trường hợp tuy nhiên cho phép đơn giản hóa việc xây dựng và suy diễn trên mạng Bayes.

Bảng xác suất điều kiện xác định cụ thể ảnh hưởng của các nút cha mẹ tới giá trị nút con. Ở đây ta chỉ xét trường hợp biến ngẫu nhiên có thể nhận giá trị rời rạc và bảng xác suất điều kiện được cho theo tổ hợp giá trị của các nút cha mẹ. Mỗi d ng trong bảng tương ứng với một điều kiện cụ thể, thực chất là một tổ hợp giá trị các nút cha. Ví dụ, trong mạng Bayes của ví dụ trên, d ng thứ nhất trong bảng xác suất của nút D ứng với điều kiện trong đó O = True và B = True. Nếu nút không có cha mẹ thì bảng xác suất chỉ gồm một d ng duy nhất như trường hợp với nút O và nút B.

# Tính độc lập xác suất trong mạng Bayes

Mạng Bayes thể hiện hai thông tin chính.

_Thứ nhất, đây là biểu diễn rút gọn của toàn bộ xác suất đồng thời. Trong ví dụ trên ta chỉ cần 10 xác suất thay vì 25-1 xác suất đồng thời. Tùy theo kích thước và đặc điểm cụ thể của bài toán, hiệu quả của việc rút gọn số lượng xác suất có thể lớn hơn rất nhiều. Chẳng hạn, với mạng gồm 30 nút nhị phân, mỗi nút có 5 nút cha, ta cần tất cả 960 xác suất điều kiện cho mạng Bayes, trong khi bảng xác suất đồng thời cho 30 biến như vậy phải có 230-1, tức là hơn một tỷ dòng.

_Thứ hai, mạng Bayes cho thấy sự phụ thuộc hoặc độc lập xác suất có điều kiện giữa các biến. Về thực chất, chính việc độc lập về xác suất dẫn tới khả năng biểu diễn rút gọn các xác suất đồng thời.

Tính độc lập xác suất trong mạng Bayes thể hiện qua tính chất sau.

_Tính chất:_

\- Mỗi nút trên mạng Bayes độc lập có điều kiện với tất cả các nút không phải là hậu duệ của nút đó nếu biết giá trị các nút cha.

\- Mỗi nút độc lập có điều kiện với tất cả các nút khác trên mạng nếu biết giá trị tất cả nút cha, nút con và nút cha của các nút con.

Ví dụ: Theo mạng Bayes trong ví dụ trên H độc lập với O, L, B nếu biết giá trị của D.

Tính các xác suất đồng thời

Sử dụng tính độc lập xác suất vừa phát biểu ở trên, có thể tính xác suất đồng thời của tất cả các biến. Xét ví dụ sau

_Ví dụ:cần tínhP(H, D, L, ¬O, B)_

Theo công thức chuỗi:

_P(H, D, L,¬ O, B) = P(H| D, L, ¬O, B) * P(D| L,¬ O, B) * P(L|¬ O, B) * P(¬O|B) * P(B)Do tính độc lập xác suất (có điều kiện):

_P (H| B, D, ¬O, L) = P(H|D)_

_P(D| L, ¬O, B) = P(D|¬ O, B)_

_P(L| ¬O, B) = P(L|¬O)_

_P(¬O|B)=P(O)_

do vậy,

_P(H, D, L,¬ O, B) = P(H| D, L, ¬O, B) * P(D| L,¬ O, B) * P(L|¬ O, B) * P(¬O|B) * P(B) = P(H|¬O) * P(D|¬ O, B) * P(L|¬O) * P(¬O) * P(B)_

Một cách tổng quát, giả sử mạng có n nút tương ứng với n biến ngẫu nhiênX1, …,X ncủa bài toán đang xét. Từ thông tin của mạng, có thể tính mọi xác suất đồng thời của n biến, trong đó mỗi xác suất đồng thời có dạngP(X1 =x1 ∧X2 =x2 ∧…∧X n=x n_) hay viết gọn làP(x1, …,x n_). Xác suất đồng thời được tính theo công thức tổng quát sau:

_n_
_P(X1 =x1,...,X n=x n) = ∏P(X i=x i|cha_me(X i))
_i=1
hay viết gọn là
_n_
_P(x1,...,x n) = ∏P(x i|cha_me(X i))
_i=1
trong đócha_me(X i_) là giá trị cụ thể các nút cha mẹ của nútX i_.

Để minh họa cho công thức trên, ta sẽ tính xác suất xẩy ra tình huống ở nhà có người, chó bị ốm và được buộc ngoài sân, đồng thời đèn không sáng và nghe tiếng chó sủa. Xác suất tình huống này chính làP(B, ¬O, D, ¬L, H)và được tính như sau:

_P(B, ¬O, D, ¬L, H) = P(B) * P(¬O) * P(D|¬O, B) * P(H|D) * P(¬L|˥O)_

_=0,3 * 0,4 * 0,05 * 0,7 * 0,3

_=0,00126

Trong một phần trên ta đã thấy rằng nếu có mọi xác suất đồng thời thì có thể thực hiện suy diễn xác suất cho mọi dạng câu truy vấn. Như vậy, với mạng Bayes ta có thể suy diễn bằng cách trước tiên tính ra mọi xác suất đồng thời cần thiết. Tuy nhiên, cách này đòi hỏi tính toán nhiều và vì vậy trên thực tế thường sử dụng một số phương pháp suy diễn khác hiệu quả hơn. Vấn đề này sẽ được nhắc tới trong một phần sau.

# Cách xây dựng mạng Bayes

Để có thể sử dụng, trước tiên cần xây dựng ra mạng Bayes. Quá trình xây dựng mạng Bayes bao gồm việc xác định tất cả các biến ngẫu nhiên liên quan, xác định cấu trúc đồ thị của mạng, và cuối cùng là xác định giá trị cho các bảng xác suất điều kiện. Trong phần này, ta sẽ coi như đã có biến ngẫu nhiên, việc xây dựng mạng chỉ bao gồm xác định cấu trúc và bảng xác suất điều kiện.

Có hai cách tiếp cận chính để xây dựng mạng Bayes.

• Cách thứ nhất do con người (chuyên gia) thực hiện dựa trên hiểu biết của mình về bài toán đang xét. Việc xây dựng mạng được chia thành hai bước: xác định cấu trúc đồ thị và điền giá trị cho bảng xác suất điều kiện.

• Cách thứ hai là tự động xác định cấu trúc và xác suất điều kiện từ dữ liệu. Ở đây, dữ liệu có dạng giá trị các biến ghi nhận được trong quá khứ, ví dụ ta có thể ghi lại tổ hợp cá giá trị của năm biến trong ví dụ trên trong thời gian vài năm. Quá trình xây dựng mạng khi đó bao gồm xác định cấu trúc của đồ thị và bảng xác suất điều kiện sao cho phân bố xác suất do mạng thể hiện phù hợp nhất với tần suất xuất hiện các giá trị trong tập dữ liệu.

Phần này chỉ xem xét cách xây dựng mạng do con người thực hiện và mô tả một quy trình cụ thể cho việc xây dựng mạng.

Các bước xây dựng mạng được thực hiện như trên hình 4.2. Sau khi đã có cấu trúc mạng, chuyên gia sẽ xác định giá trị cho các bảng xác suất điều kiện. Thông thường, việc xác định giá trị xác suất điều kiện khó hơn nhiều so với việc xác định cấu trúc mạng, tức là xác định quan hệ giữa các nút.

|<image_2>|

Hình 3.1 : Phương pháp xây dựng mạng Bayes

Để minh họa, xét ví dụ sau. Một người vừa lắp hệ thống báo động chống trộm ở nhà. Hệ thống sẽ phát tiếng động khi có trộm. Tuy nhiên, hệ thống có thể báo động (sai) nếu có chấn động do động đất. Trong trường hợp nghe thấy hệ thống báo động, hai người hàng xóm tên làm Nam và Việt sẽ gọi điện cho chủ nhà. Do nhiều nguyên nhân khác nhau, Nam và Việt có thể thông báo sai, chẳng hạn do ồn nên không nghe thấy chuông báo động hoặc ngược lại, nhầm âm thanh khác là tiếng chuông.

Theo phương pháp trên, các bước xây dựng mạng được thực hiện như sau.

  * B1: lựa chọn biến: sử dụng 5 biến sau


T (có trộm), Đ (động đất), B (chuông báo động), N (Nam gọi điện), V (Việt gọi điện)

  * B2: các biến được sắp xếp theo thứ tự T, Đ, B, N, V

  * B3: thực hiện như các bước ở hình vẽ, ta xây dựng được mạng thể hiện trên hình sau (để đơn giản, trên hình vẽ chỉ thể hiện cấu trúc và không có bảng xác suất điều kiện).


|<image_3>|

Hình 3.2.: Kết quả xây dựng mạng Bayes cho ví dụ chuông báo trộm

Ảnh hướng của việc sắp xếp các nút tới kết quả xây dựng mạng.

Trên thực tế, việc xây dựng mạng Bayes không đơn giản, đặc biệt trong việc chọn thứ tự các nút đúng để từ đây chọn được tập nút cha có kích thước nhỏ. Để làm rõ điểm này, ta giả sử trong ví dụ trên, các biến được xếp theo thứ tự khác: N, V, C, T, Đ.

Các bước thêm nút sẽ thực hiện như sau:

\- Thêm nút N: không có nút cha

\- Thêm nút V: nếu Nam gọi điện, xác suất Việt gọi điện sẽ tăng lên do sự kiện Nam gọi điện nhiều khả năng do có báo động và do vậy xác suất Việt nghe thấy chuông và gọi điện tăng theo. Do vậy N có ảnh hướng tới V và được thêm vào tập cha của V.

\- Thêm C: Nếu Nam và Việt cùng gọi thì khả năng có chuông cao hơn, do vậy cần thêm cả N và V vào tập cha của C.

\- Thêm T: Nếu đã biết trạng thái của chuông thì không cần quan tâm tới Nam và Việt nữa, do vậy chỉ có C là cha của T.

\- Thêm Đ: nếu có chuông, khả năng động đất tăng lên. Tuy nhiên, nếu đồng thời ta biết có trộm thì việc có trộm giải thích phần nào nguyên nhân chuông kêu. Như vậy, cả chuông và có trộm ảnh hướng tới xác suất động đất, tức là C và T đều là cha của Đ.

Kết quả của mạng Bayes xây dựng theo thứ tự mới được thể hiện trên hình dưới. So sánh với kết quả ở trên, mạng Bayes mới phức tạp hơn, theo nghĩa có nhiều cung hơn hay trung bình các nút có nhiều nút cha hơn. Ngoài ra, ý nghĩa một số quan hệ trên mạng rất không trực quan và khó giải thích, chẳng hạn việc xác suất động đất phục thuộc vào chuông báo động và có trộm. Như vậy, mặc dù cả hai mạng Bayes xây dựng ở trên đều đúng theo nghĩa đảm bảo các ràng buộc về xác suất và đều cho phép tính ra các xác suất đồng thời, việc lựa chọn không đúng thứ tự nút sẽ làm mạng khó hiểu và phức tạp hơn.

|<image_4>|

Hình 3.3: Kết quả xây dựng mạng Bayes khi sử dụng thứ tự các nút khác

Từ ví dụ trên ta có thể đưa ra một số nhận xét về kết quả xây dựng mạng Bayes.

__Nhận xét:__

\- Cùng một tập hợp biến có thể xây dựng nhiều mạng Bayes khác nhau.
\- Thứ tự sắp xếp có ảnh hưởng tới mạng Bayes. Nên sắp xếp sao cho các nút đóng vai tr nguyên nhân đứng trước nút hệ quả.
\- Tất cả các mạng được xây dựng như trên đều hợp lệ, theo nghĩa không vi phạm các ràng buộc về xác suất và đều cho phép thực hiện suy diễn.

# Tính độc lập xác suất tổng quát: khái niệmd-phân cách

Trong phần trước, ta đã xem xét khả năng biểu diễn tính độc lập xác suất của mạng Bayes, ví dụ, mỗixnút độc lập với các nút không phải hậu duệ nếu biết giá trị tất cả nút cha củax_. Tuy nhiên, đây mới là các trường hợp riêng, trong trường hợp tổng quát cần có khả năng xác định liệu một tập hợp các nútXcó độc lập với tập hợp các nútYkhi biết các nútEkhông. Các tính chất độc lập xác suất đã trình bầy trong phần trước không cho phép trả lời tất cả các câu hỏi tổng quát dạng này. Chẳng hạn, trong ví dụ mạng Bayes trên hình 4.1 dưới đây, nếu không biết giá trị của nút C thì theo tính chất của mạng Bayes, N và V độc lập (không điều kiện) với nhau do V không phải hậu duệ của N và N không có cha. Tuy nhiên, nếu đã biết giá trị của C thì N và V còn độc lập với nhau không? Hai tính chất trình bày trong phần trước không cho phép trả lời câu hỏi này.

|<image_5>|

Hình 4.1. Ví dụ mạng Bayes

Trong phần này, ta sẽ xem xét cách trả lời câu hỏi về tính độc lập của tập các nút X với tập nút Y khi biết tập nút E trên một mạng Bayes bằng cách sử dụng khái niệmd-phân cách(d-separation).

Nguyên lý chung củad-phân cách là gắn khái niệm phụ thuộc xác suất với tính kết nối (tức là có đường đi giữa các nút), và khái niệm độc lập xác suất với tính không kết nối, hay chia cắt, trên đồ thị có hướng khi ta biết giá trị một số nútE_. Chữ “d” ở đây là viết tắt của từ “directional” tức là “có hướng”. Theo đó, các nútXvà các nútYlàd-kết nối với nhau nếu chúng không bịd-phân cách.Nếu các nút X và các nút Y bị d-phân cách bởi các nút E thì X và Y là độc lập xác suất với nhau khi biết E_.

Để xác định tínhd-phân cách của tập X và Y, trước tiên ta cần xác định tínhd-phân cách giữa hai nút đơnxthuộcXvàythuộcY_. Từ đây, hai tập nút sẽ độc lập với nhau nếu mỗi nút trong tập này độc lập với tất cả các nút trong tập kia. Sau đây là các quy tắc cho phép xác định tínhd-phân cách hay tính độc lập xác suất của hai biếnxvày_.

Quy tắc 1 : nútxvàyđược gọi làd-kết nối nếu tồn tại đường đi không bị phong tỏa giữa hai nút. Ngược lại, nếu không tồn tại đường đi như vậy thìxvàylàd-phân cách.

Trong quy tắc này, đường đi là một chuỗi các cung nằm liền nhau, không tính tới hướng của các cung đó. Đường đi không bị phong tỏa là đường đi mà trên đó không có hai cung liền kề hướng vào nhau. Trong trường hợp tồn tại hai cung như vậy thì thông tin sẽ không thể đi qua được và do vậy các nút không thể kết nối với nhau. Nút có hai cung hướng vào như vậy gọi lànút xung đột_.

Ví dụ, trong trường hợp sau:
|<image_6>|

giữaxvàytồn tại đường đix\-r\-s\-t\-u\-v\-y, tuy nhiêntlà nút xung đột do hai cungstvàuthướng vào nhau. Đường đix\-r\-s\-tvàt\-u\-v\-ylà các đường đi không bị phong tỏa, do vậyxvàtlà d-kết nối,tvàycũng vậy. Tuy vậy,xvàykhông phải làd-kết nối do không tồn tại đường đi nào không qua nút xung độtt_. Như vậy,xvàylàd-phân cách trên mạng này và do vậy độc lập xác suất (không điều kiện) với nhau.

Tính kết nối và phân cách xác định theo quy tắc 1 là không điều kiện và do vậy tính độc lập xác suất được xác định theo quy tắc 1 làđộc lập không điều kiện_.

Quy tắc 2 : nútxvàylàd-kết nối có điều kiện khi biết tập nútEnếu tồn tại đường đi không bị phong tỏa (không chứa nút xung đột) và không đi qua bất cứ nút nào thuộcE_. Ngược lại, nếu không tồn tại đường đi như vậy thì ta nói rằngxvàylàd-phân cách bởiE_. Nói cách khác, mọi đường đi giữaxvày(nếu có) đều bịEphong tỏa.

Quy tắc 2 là cần thiết do khi ta biết giá trị một số nút (tập nútE), tính chất độc lập hay phụ thuộc giữa các nút c n lại có thể thay đổi: một số nút độc lập trở nên phụ thuộc, và ngược lại, một ss nút phụ thuộc trở thành độc lập. Tính độc lập hay phụ thuộc trong trường hợp này được gọi làd-phân cách có điều kiện theo tập biếnE_.

Ví dụ: trên hình sau, giả sử tậpEgồm hai nútrvàvđược khoanh tr n. Theo quy tắc 2, không tồn tại đường đi không bị phong tỏa nào giữaxvàymà không đi quaE, do đóxvàylàd-phân cách khi biếtE_. Tương tự như vậy:xvàs,uvày,svàulàd-phân cách khi biếtEdo đường đis–r–tđi qua nútrthuộcE, đường điy–v–sđi qua nútvthuộcE, c n đường đis–t–ulà đường đi bị phong tỏa tại nút xung độtttheo quy tắc 1. Chỉ có các cặp nútsvàt,tvàulà không bị phong tỏa bởiE_.

|<image_7>|

Quy tắc 3 : nếu một nút xung đột là thành viên của tậpE, hoặc có hậu duệ thuộc tậpE, thì nút đó không c n phong tỏa các đường đi qua nó nữa.

Quy tắc này được sử dụng cho trường hợp ta biết một sự kiện được gây ra bởi hai hay nhiều nguyên nhân. Khi ta đã biết một nguyên nhân là đúng thì xác suất những nguyên nhân c n lại giảm đi, và ngược lại nếu ta biết một nguyên nhân là sai thì xác suất những nguyên nhân c n lại tăng lên. Chẳng hạn, xẩy ra tai nạn máy bay với hai nguyên nhân là trục trặc kỹ thuật hoặc lỗi của con người. Nếu ta đã xác định được xẩy ra trục trặc kỹ thuật thì xác suất lỗi con người sẽ bị giảm đi (mặc dù không loại trừ hoàn toàn).

_Ví dụ: trên ví dụ ở hình sau, giả sử tập E gồm các nút r và p được đánh dấu bằng cách khoanh tr n. Theo quy tắc 3, nút s và y là d-kết nối do nút xung đột t có hậu duệ là nút p thuộc E, do vậy đã giải tỏa đường đi s – t – u – v – y. Trong khi đó x và u vẫn là d-phân cách do mặc dù t đã được giải tỏa nhưng nút r vẫn bị phong tỏa theo quy tắc 2.

|<image_8>|