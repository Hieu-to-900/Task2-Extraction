# Public_583

# MỞ ĐẦU

“Big Data” được biết như là một giải pháp lý tưởng để xử lý một tập dữ liệu lớn có cấu trúc, bán cấu trúc hoặc là phi cấu trúc như dữ liệu từ các weblogs, mạng xã hội, e-mail, cảm biến và các bức ảnh mà có thể được khai thác nhằm tìm ra những thông tin hữu ích. Big Data trên thực tế đang được ứng dụng vào rất nhiều lĩnh vực của xã hội, tạo những chuyển biến ấn tượng, giúp tăng hiệu quả và năng suất của doanh nghiệp. Trong lĩnh vực ngân hàng, Big Data được sử dụng bởi các kỹ thuật phân cụm dữ liệu giúp đưa ra những quyết định quan trọng. Trong lĩnh vực thương mại Big Data cùng với các kỹ thuật phân tích dữ liệu để nhanh chóng xác định những địa điểm, chi nhánh nơi tập trung nhiều nhu cầu của khách hàng tiềm năng và đề xuất thành lập chi nhánh mới. Đối với lĩnh vực tài chính, Big Data có thể kết hợp với nhiều quy tắc được áp dụng trong lĩnh vực ngân hàng để dự đoán lượng tiền mặt cần thiết sẵn sàng cung ứng ở một chi nhánh tại thời điểm cụ thể hàng năm. Trong lĩnh vực y tế, Big Data không chỉ được ứng dụng để xác định phương hướng điều trị mà giúp cải thiện và hỗ trợ quá trình chăm sóc sức khỏe của bệnh nhân.

Năm 2014, công ty phân tích dữ liệu Gartner [3] đưa ra khái niệm mới có thể chấp nhận được về mô hình “5Vs” của Big Data. Đó là, 5 đặc trưng của Big Data: tăng về lượng (volume), tăng về vận tốc (velocity) , tăng về chủng loại (variety), tăng về độ chính xác (veracity) và tăng về giá trị thông tin (value). Hiểu một cách đơn giản, đó chính là sự phát triển không ngừng của khối lượng dữ liệu cần lưu trữ, cách thức để xử lý dữ liệu với tốc độ cao, tính đa dạng dữ liệu (variety): Theo IBM [1], chỉ có 20% dữ liệu thu được là có cấu trúc nhưng thực tế là 80% dữ liệu trên thế giới đều là dạng phi cấu trúc hoặc bán cấu trúc. Ngoài ra còn phải quản lý được các dữ liệu mới được tạo ra và các dữ liệu được cập nhật, độ chính xác của xử lý và giá trị thông tin được lưu trữ.

Tất cả các quan điểm trên đều hướng tới việc trả lời cho câu hỏi: Big Data là vấn đề gì và tại sao chúng ta cần phải nghiên cứu và tìm hiểu nó. Vấn đề này được các nhà cung cấp dịch vụ, các trung tâm tích hợp dữ liệu nghiên cứu, tìm hiểu phương pháp tốt nhất để lưu trữ loại dữ liệu với 5 yếu tố trên. Nhìn chung, có bốn lợi ích chính mà Big Data có thể mang lại đó là: cắt giảm chi phí, giảm thời gian tìm kiếm thông tin, tăng thời gian phát triển và tối ưu hóa sản phẩm, đồng thời hỗ trợ con người đưa ra những quyết định đúng đắn và hợp lý. Trong phạm vi bài báo này chúng tôi đề xuất giải pháp xử lý của Big Data trong lĩnh vực y tế, nơi sản sinh một tập dữ liệu khổng lồ từ các xét nghiệm, điều trị SARS-CoV-2 trong hơn 2 năm qua.

# BIG DATA VÀ CÔNG CỤ XỬ LÝ 

Kỹ thuật xử lý dữ liệu trong Big Data chủ yếu là NoSQL (cơ sở dữ liệu theo cột, cặp khóa-giá trị) [4], do mô hình dữ liệu quan hệ không thể đáp ứng được các loại dữ liệu bán cấu trúc và không cấu trúc. Trong thực tế nhiều công ty lớn cũng đã đưa ra các công cụ khác nhau để xử lý Big Data.

## Giải pháp Hadoop/MapReduce

Năm 2004, Google công bố kiến trúc của hệ thống file phân tán GFS (Google File System) và công cụ MapReduce. Từ đó Hadoop, một Framework, cùng với GFS và MapReduce được ra đời bởi Dough Cutting để xử lý các Big Data.

### Hadoop

Apache Hadoop [5] là một framework dùng để chạy những ứng dụng trên một cluster lớn được xây dựng trên những phần cứng thông thường. Thư viện phần mềm Hadoop là một khuôn mẫu cho phép xử lý phân tán các bộ dữ liệu lớn trên các nhóm máy tính sử dụng các mô hình lập trình đơn giản. Nó được thiết kế để mở rộng từ một máy chủ duy nhất sang hàng ngàn máy khác, mỗi máy cung cấp tính toán và lưu trữ cục bộ. Hadoop thực hiện mô hình MapReduce, đây là mô hình phân tán song song, ứng dụng sẽ được chia nhỏ ra thành nhiều phân đoạn dữ liệu khác nhau (phân tán), và các phần này sẽ được thực hiện trên đồng thời trên nhiều node khác nhau (song song). Bên cạnh đó, Hadoop cung cấp một hệ thống file phân tán (HDFS) cho phép lưu trữ dữ liệu lên trên nhiều node. Cả Map/Reduce và HDFS đều được thiết kế sao cho framework sẽ tự động quản lý được các lỗi, các hư hỏng về phần cứng của các node.

### MapReduce

Có thể hiểu một cách đơn giản, MapReduce phân chia các công việc xử lý thành nhiều khối công việc nhỏ, phân tán khắp các nút tính toán (giai đoạn Map), rồi thu hồi các kết quả (giai đoạn Reduce). MapReduce có thể chạy trên các phần cứng thông thường, không đòi hỏi các server chạy MapReduce phải là các máy tính có cấu hình cao với khả năng tính toán, lưu trữ và truy xuất mạnh mẽ. Do đó, chi phí triển khai MapReduce sẽ rẻ hơn. MapReduce làm đơn giản hoá các giải thuật tính toán phân tán bằng cách chỉ cần cung cấp hai hàm Map và Reduce cùng với một số thành phần xử lý dữ liệu đầu vào.

Hàm Map: Người dùng đưa một cặp dữ liệu (key, value) làm input cho hàm Map, và tùy vào mục đích của người dùng mà hàm Map sẽ trả ra danh sách các cặp dữ liệu (intermediate key, value).

Hàm Reduce: Hệ thống sẽ gom nhóm tất cả value theo intermediate key từ các output của hàm map, để tạo thành tập các cặp dự liệu với cấu trúc là (key, tập các value cùng key). Dữ liệu input của hàm Reduce là từng cặp dữ liệu được gom nhóm ở trên và sau khi thực hiện xử lý nó sẽ trả ra cặp dữ liệu (key, value) output cuối cùng cho người dùng. Cho đến nay, Hadoop đã trở thành giải pháp nguồn mở hàng đầu hỗ trợ mô hình MapReduce. Hadoop được viết bằng Java, tuy nhiên hỗ trợ phát triển MapReduce trên nhiều ngôn ngữ khác ngoài Java như C++, Pearl, Python, …

## Kiến trúc Hadoop File System (HDFS)

|<image_1>|Giống như các hệ thống file khác, HDFS duy trì một cấu trúc cây phân cấp các file [6], thư mục mà các file sẽ đóng vai trò là các node lá. Trong HDFS, mỗi file sẽ được chia ra làm một hay nhiều block và mỗi block này sẽ có một block ID để nhận diện. Mỗi block của file sẽ được lưu trữ thành ra nhiều bản sao khác nhau vì mục đích an toàn dữ liệu.

## Xử lý Big Data với Hornworks Sanbox

### Giới thiệu Hortonworks Data Platform

Hortonworks Data Platform (HDP) là một nền tảng phát triển và xây dựng hoàn toàn mở, HDP được thiết kế để đáp ứng nhu cầu xử lý dữ liệu lớn của doanh nghiệp. HDP là linh hoạt, cung cấp khả năng mở rộng tuyến tính, mở rộng lưu trữ và tính toán trên một loạt các phương pháp truy cập, batch và real-time, search và streaming. Nó bao gồm một tập hợp toàn diện các khả năng xử lý dữ liệu cho doanh nghiệp như: governance, integration, security và operation. HDP cho phép triển khai Hadoop bất cứ nơi nào, từ cloud cho đến hệ thống tại chỗ, trên cả Linux và Windows.

Sự xuất hiện và bùng nổ của các loại dữ liệu mới trong những năm gần đây đã gây áp lực không nhỏ về kiến trúc dữ liệu cho các tổ chức. Để đối phó, nhiều người đã chuyển sang Apache Hadoop để quản lý sự bùng nổ của dữ liệu.

Apache Hadoop có nguồn gốc là để quản lý và truy cập dữ liệu, và chỉ bao gồm 2 thành phần là: Hadoop Distributed File System (HDFS) và MapReduce, một khuôn khổ xử lý cho dữ liệu lưu trữ trong HDFS. Theo thời gian, nền tảng Hadoop mở rộng kết hợp với một loạt các dự án khác để thành một nền tảng hoàn chỉnh. Nền tảng này chia thành 5 loại sau: data access, data management, security, operations và governance.

|<image_2>|

_Hình 2.Cấu trúc của HDP

### Các thành phần của Hortonworks Data Platform

  * Data Management: Quản lý lưu trữ và xử lý tất cả các dữ liệu, bao gồm các thành phần nền tảng của HDP là Apache Hadoop YARN và Hadoop Distributed File System (HDFS).

  * Data Access: HDP cho phép nhiều công cụ xử lý dữ liệu bằng ngôn ngữ truy vấn có cấu trúc như SQL hoặc truy cập dữ liệu với độ trễ thấp như NoSQL. Truyền phát thời gian thực đến khoa học dữ liệu và xử lý hàng loạt để sử dụng dữ liệu được lưu trữ trong một nền tảng duy nhất.

  * Governance and Integration: HDP mở rộng data access và management với các công cụ mạnh mẽ để quản lý và tích hợp

  * Security: HDP cung cấp một cách tiếp cận tập trung để quản lý, cho phép triển khai chính sách bảo mật một cách nhất quán trong suốt nền tảng dữ liệu với các yêu cầu để xác thực, cấp phép, kiểm tra và bảo vệ dữ liệu.


### Cài đặt Hortonworks Sandbox (HWS)

  * Cài đặt HWS, phiên bản 2.6.5 trên hệ điều hành Windows 10.

  * Cấu hình máy tính: CPU: 64 bit (x64-based processor); Hệ điều hành: Windows 64 bit; Bộ nhớ chính Ram: > 8 GB;


Tải các phần mềm:

  * Oracle VM VirtualBox mới nhất dành cho Windows tại link: <https://www.virtualbox.org/wiki/Downloads>

  * Hortonworks Data Platform (HDP) on Hortonworks Sandbox, tại link:  
<https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html>


# ỨNG DỤNG BIGDATA BÀI TOÁN TRONG LĨNH VỰC Y TẾ 

## Giới thiệu

Big Data trong y tế được sử dụng để mô tả và thống kê khối lượng thông tin khổng lồ được tạo ra từ việc áp dụng công nghệ kỹ thuật số để thu thập hồ sơ của bệnh nhân và giúp quản lý hoạt động của bệnh viện hoặc phục vụ cho việc nghiên cứu về một sự kiện y tế. Công việc này là quá lớn và phức tạp đối với các công nghệ truyền thống.

Việc áp dụng phân tích dữ liệu lớn trong y tế mang lại rất nhiều kết quả tích cực và cũng là cứu sống con người. Về bản chất, Big Data đề cập đến lượng thông tin khổng lồ được tạo ra bởi quá trình số hóa mọi thứ, được tổng hợp và phân tích bằng các công nghệ cụ thể. Được áp dụng cho y tế, nó sẽ sử dụng dữ liệu sức khỏe cụ thể của một dân số (hoặc của một cá nhân cụ thể) và có khả năng giúp ngăn ngừa dịch bệnh, chữa bệnh, cắt giảm chi phí, ...

Trong nhiều năm qua, việc thu thập một lượng lớn dữ liệu cho mục đích y tế rất tốn kém và mất thời gian. Với công nghệ luôn cải tiến ngày nay, việc thu thập dữ liệu đó trở nên dễ dàng hơn, tạo báo cáo chăm sóc sức khỏe toàn diện và chuyển đổi chúng thành những thông tin chi tiết quan trọng có liên quan, sau đó có thể sử dụng để cung cấp dịch vụ chăm sóc tốt hơn.

## Mô tả bài toán 

### Dữ liệu COVID-19

COVID-19 là một bệnh truyền nhiễm do vi-rút SARS-CoV-2 gây ra. Hầu hết người mắc bệnh COVID-19 sẽ gặp các triệu chứng từ nhẹ đến trung bình và hồi phục mà không cần phải điều trị đặc biệt. Tuy nhiên, một số người sẽ chuyển bệnh nghiêm trọng và cần được hỗ trợ y tế. Vi-rút này có thể lây từ miệng hoặc mũi của người bị nhiễm bệnh dưới dạng các giọt nhỏ khi họ ho, hắt hơi, nói chuyện, hát hoặc thở. Chúng ta có thể bị nhiễm bệnh khi hít phải vi-rút nếu đang ở gần người nhiễm COVID-19 hoặc chạm vào bề mặt có vi-rút rồi lại chạm tay vào mắt, mũi hoặc miệng. Vi-rút dễ lây lan hơn trong nhà và ở những nơi đông đúc.

  * Các triệu chứng thường gặp nhất: sốt, ho, mệt mỏi, mất vị giác hoặc khứu giác,

  * Các triệu chứng ít gặp hơn: đau họng, đau đầu, đau nhức, tiêu chảy, da nổi mẩn hay ngón tay hoặc ngón chân bị tấy đỏ hoặc tím tái, mắt đỏ hoặc ngứa.


Dữ liệu COVID-19 của mỗi cá nhân về quá trình tiêm chủng và điều trị rất khó tìm kiếm và sử dụng hợp pháp vì liên quan đến bảo mật dữ liệu cá nhân. Chúng tôi đã sử dụng dữ liệu công khai của Jonhn Hoppkin University và dữ liệu tiêm chủng của các nước ở châu Âu trong giai đoạn 2020-2022 để lưu trữ và xử lý trên môi trường HDP. Dữ liệu này có thể được download và lưu trữ dưới dạng file XLSx, CSV, JSON, XML.

Chúng ta sẽ thử nghiệm HWS với tập tin dữ liệu chuẩn “Data”, kích thước 4,3 MB, gồm 160.782 mẫu tin với 14 fields, chứa tất cả dữ liệu Covid trong 2 năm 2020, 2021 của châu Âu. Tập tin này được download từ link: <https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea>

_Bảng 2_. Diễn giải các trường của tập tin dữ liệu chuẩn
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>YearWeekISO</th>
<th>Thời gian (tuần) nhận vac xin</th>
</tr>
</thead>
<tbody>
<tr>
<td>ReportingCountry</td>
<td>Mã quốc gia theo chuẩn ISO 3166-1-alpha-2</td>
</tr>
<tr>
<td>Denominator</td>
<td>Tổng số dân số cho từng nhóm đối tượng được liệt kê trong
TargetGroup</td>
</tr>
<tr>
<td>NumberDosesReceived</td>
<td>Số liều vac xin được nhận trong thời gian (tuần) báo cáo</td>
</tr>
<tr>
<td>FirstDose</td>
<td>Số liều vắc xin đầu tiên đã tiêm cho các cá nhân trong tuần báo
cáo.</td>
</tr>
<tr>
<td>FirstDoseRefused</td>
<td>Số cá nhân từ chối tiêm</td>
</tr>
<tr>
<td>SecondDose</td>
<td>Số vắc xin liều thứ hai được tiêm cho các cá nhân trong tuần báo
cáo</td>
</tr>
<tr>
<td>UnknownDose</td>
<td>Số liều được sử dụng trong tuần báo cáo mà loại liều không được chỉ
định (tức là số lượng không biết đó là liều thứ nhất hay thứ hai).</td>
</tr>
<tr>
<td>Region</td>
<td>Region = country code</td>
</tr>
<tr>
<td>TargetGroup</td>
<td>Nhóm đối tượng tiêm phòng, bao <strong>gồm</strong>: ALL: người trên
18; &lt;18; ..., HCW: người chăm sóc y tế; LTCF: người được chăm sóc dài
hạn; ...</td>
</tr>
<tr>
<td>Vaccine</td>
<td>Tên vắc xin. Các vắc xin bổ sung sẽ được bổ sung khi được phê duyệt
hoặc theo yêu cầu.</td>
</tr>
<tr>
<td>Population</td>
<td>Dân số theo độ tuổi cụ thể cho mỗi quốc gia</td>
</tr>
</tbody>
</table> 

Xét truy vấn:

SELECT ReportingCountry, CONCAT(ROUND((sum(FirstDose) / max(Denominator) * 100),2),'%') as UptakePercentage

FROM ecdc_covid19_vaccine_tracker

WHERE ReportingCountry in ('DE','ES','DK') AND TargetGroup = 'ALL'

GROUP BY ReportingCountry

Nếu sử dụng SQL hoặc Hortonworks Sandbox (HWS) thì chúng ta có được kết quả như sau:
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>ReportingCountry</strong></th>
<th><strong>UptakePercentage</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>DE</td>
<td>75.7%</td>
</tr>
<tr>
<td>DK</td>
<td>87.99%</td>
</tr>
<tr>
<td>ES</td>
<td>86.66%</td>
</tr>
</tbody>
</table> 

Mặc dù từ một câu truy vấn cả SQL và HWS đều cho cùng một kết quả nhưng vấn đề đặt ra ở đây là chúng ta cần biết khả năng xử lý và lưu trữ của mỗi phương pháp với các ưu nhược điểm của nó như thế nào.

Thực hiện 31 lần test với tập tin dữ liệu chuẩn và các tập tin được nhân bản từ tập tin dữ liệu chuẩn chúng tôi được quả như sau:

_Bảng 2_. Số liệu thực nghiệm từ SQL và HWS
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th rowspan="2"><strong>Lần xử lý</strong></th>
<th rowspan="2"><strong>Số mẫu tin</strong></th>
<th colspan="2"><strong>SQL Server</strong></th>
<th colspan="2"><strong>Hortonworks Sandbox</strong></th>
</tr>
<tr>
<th><strong>Dung lượng lưu trữ</strong></th>
<th><strong>Thời gian cho kết quả</strong></th>
<th><strong>Dung lượng lưu trữ</strong></th>
<th><strong>Thời gian cho kết quả</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>160.782</td>
<td>47 MB</td>
<td>1s</td>
<td>27 MB</td>
<td>27s 672ms</td>
</tr>
<tr>
<td>2</td>
<td>3.067.600</td>
<td>900 MB</td>
<td>23s</td>
<td>543 MB</td>
<td>1m 48s 567ms</td>
</tr>
<tr>
<td>3</td>
<td>6.135.200</td>
<td>1.800 MB</td>
<td>43s</td>
<td>1.087 MB</td>
<td>1m 45s 923ms</td>
</tr>
<tr>
<td>4</td>
<td>9.202.800</td>
<td>2.701 MB</td>
<td>57s</td>
<td>1.631 MB</td>
<td>1m 30s 217ms</td>
</tr>
<tr>
<td>5</td>
<td>12.270.400</td>
<td>3.601 MB</td>
<td>40s</td>
<td>2.175 MB</td>
<td>1m 32s 716ms</td>
</tr>
<tr>
<td>6</td>
<td>15.338.000</td>
<td>4.502 MB</td>
<td>1m 45s</td>
<td>2.719 MB</td>
<td>2m 19s 243ms</td>
</tr>
<tr>
<td>7</td>
<td>18.405.600</td>
<td>5.402 MB</td>
<td>2m 21s</td>
<td>3.263 MB</td>
<td>2m 26s 7ms</td>
</tr>
<tr>
<td>8</td>
<td>21.473.200</td>
<td>6.303 MB</td>
<td>2m 33s</td>
<td>3.807 MB</td>
<td>2m 23s 479ms</td>
</tr>
<tr>
<td>9</td>
<td>24.540.800</td>
<td>7.203 MB</td>
<td>3m 51s</td>
<td>4.351 MB</td>
<td>3m 2s 899ms</td>
</tr>
<tr>
<td>10</td>
<td>27.608.400</td>
<td>8.103 MB</td>
<td>4m 25s</td>
<td>4.895 MB</td>
<td>2m 52s 676ms</td>
</tr>
<tr>
<td>11</td>
<td>30.676.000</td>
<td>9.004 MB</td>
<td>4m 32s</td>
<td>5.439 MB</td>
<td>2m 59s 401ms</td>
</tr>
<tr>
<td>12</td>
<td>33.743.600</td>
<td>9.904 MB</td>
<td>5m 31s</td>
<td>5.983 MB</td>
<td>3m 7s 723ms</td>
</tr>
<tr>
<td>13</td>
<td>36.811.200</td>
<td>10.805 MB</td>
<td>5m 45s</td>
<td>6.527 MB</td>
<td>3m 25s 444ms</td>
</tr>
<tr>
<td>14</td>
<td>39.878.800</td>
<td>11.705 MB</td>
<td>6m 37s</td>
<td>7.071 MB</td>
<td>3m 49s 642ms</td>
</tr>
<tr>
<td>15</td>
<td>42.946.400</td>
<td>12.606 MB</td>
<td>6m 50s</td>
<td>7.615 MB</td>
<td>4m 11s 205ms</td>
</tr>
<tr>
<td>16</td>
<td>46.014.000</td>
<td>13.506 MB</td>
<td>7m 53s</td>
<td>8.159 MB</td>
<td>4m 17s 28ms</td>
</tr>
<tr>
<td>17</td>
<td>49.081.600</td>
<td>14.407 MB</td>
<td>8m 00s</td>
<td>8.703 MB</td>
<td>4m 18s 868ms</td>
</tr>
<tr>
<td>18</td>
<td>52.149.200</td>
<td>15.307 MB</td>
<td>8m 14s</td>
<td>9.247 MB</td>
<td>3m 55s 830ms</td>
</tr>
<tr>
<td>19</td>
<td>55.216.800</td>
<td>16.207 MB</td>
<td>9m 11s</td>
<td>9.791 MB</td>
<td>3m 53s 1ms</td>
</tr>
<tr>
<td>20</td>
<td>58.284.400</td>
<td>17.108 MB</td>
<td>10m 22s</td>
<td>10.334 MB</td>
<td>4m 37s 736ms</td>
</tr>
<tr>
<td>21</td>
<td>61.352.000</td>
<td>18.008 MB</td>
<td>11m 30s</td>
<td>10.878 MB</td>
<td>5m 1s 430ms</td>
</tr>
<tr>
<td>22</td>
<td>64.419.600</td>
<td>18.909 MB</td>
<td>11m 58s</td>
<td>11.422 MB</td>
<td>5m 21s 614ms</td>
</tr>
<tr>
<td>23</td>
<td>67.487.200</td>
<td>19.809 MB</td>
<td>12m 43s</td>
<td>11.966 MB</td>
<td>4m 53s 553ms</td>
</tr>
<tr>
<td>24</td>
<td>70.554.800</td>
<td>20.710 MB</td>
<td>13m 44s</td>
<td>12.510 MB</td>
<td>5m 31s 161ms</td>
</tr>
<tr>
<td>25</td>
<td>73.622.400</td>
<td>21.610 MB</td>
<td>15m 03s</td>
<td>13.054 MB</td>
<td>5m 50s 815ms</td>
</tr>
<tr>
<td>26</td>
<td>76.690.000</td>
<td>22.510 MB</td>
<td>15m 41s</td>
<td>13.598 MB</td>
<td>6m 577ms</td>
</tr>
<tr>
<td>27</td>
<td>79.757.600</td>
<td>23.411 MB</td>
<td>16m 13s</td>
<td>14.142 MB</td>
<td>6m 575ms</td>
</tr>
<tr>
<td>28</td>
<td>82.825.200</td>
<td>24.311 MB</td>
<td>17m 19s</td>
<td>14.686 MB</td>
<td>5m 43s 969ms</td>
</tr>
<tr>
<td>29</td>
<td>85.892.800</td>
<td>25.212 MB</td>
<td>17m 48s</td>
<td>15.230 MB</td>
<td>5m 46s 741ms</td>
</tr>
<tr>
<td>30</td>
<td>88.960.400</td>
<td>26.112 MB</td>
<td>18m 50s</td>
<td>15.774 MB</td>
<td>6m 25s 625ms</td>
</tr>
<tr>
<td>31</td>
<td>92.028.000</td>
<td>27.013 MB</td>
<td>Báo lỗi</td>
<td>16.318 MB</td>
<td>5m 51s 52ms</td>
</tr>
</tbody>
</table> 

Biểu đồ dưới đây so sánh thời gian xử lý của HWS và SQL với 31 lần test:

|<image_3>|

_Hình 3.So sánh thời gian xử lý của HWS và SQL

Từ thực nghiệm chúng tôi rút ra được một số kết quả sau:

  1. Cùng một tập tin với số mẫu tin xác định nhưng dung lượng lưu trữ của nó trong HWS luôn luôn có kich cỡ nhỏ hơn dung lượng lưu trữ trong SQL.

  2. Thời gian xử lý của SQL tốt hơn HWS đối với những tập tin có kích thước nhỏ nhưng với tập tin có kích thước lớn thì HWS lại có thời gian xử lý nhanh hơn.

  3. HWS có khả năng xử lý dữ liệu bán cấu trúc như dữ liệu XML hoặc dữ liệu không có cấu trúc như dữ liệu từ các mạng xã hội, weblog, hình ảnh giao thông, ...

  4. SQL chỉ xử lý dữ liệu có cấu trúc, không có khả năng xử lý các tập tin có kích cỡ khá lớn (thường là báo lỗi hoặc thời gian xử lý rất lâu)


# KẾT LUẬN 

Mục đích bài báo này là giới thiệu về Big Data, giải pháp xử lý và lưu trữ đối với các loại dữ liệu có kích thước lớn, cụ thể ở đây là dữ liệu Covid được sinh trong quá trình tiêm chủng và điều trị Covid trong thời gian qua. Bài báo cũng bàn về cơ chế xử lý cho Big Data trong môi trường Hadoop, đó là HDFS và MapReduce, để người đọc hiểu được nguyên tắc xử lý các Big Data trên nền tảng phân tán Hadoop. Việc tìm hiểu các công cụ này sẽ mang lại nhiều lựa chọn giải pháp xử lý và lưu trữ và cho việc phát triển ứng dụng phân tán với nhiều mục đích khác nhau.