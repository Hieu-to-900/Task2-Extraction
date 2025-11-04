# Public_516

# Trình tự lắp ráp

## Lập kế hoạch làm việc

Thứ tự tạo các chi tiết và các cụm lắp phụ thuộc vào việc ta trả lời các câu hỏi sau ra

sao:

  * Ta chỉnh sửa một lắp ráp có sẵn hay bắt đầu một lắp ráp mới?

  * Ta có thể đập vỡ một lắp ráp lớn thành các cụm lắp con được không?

  * Ta có thể dùng các chi tiết có sẵn và các phần tử thiết kế không?

  * Ràng buộc nào sẽ ảnh hưởng đến chức năng của thiết kế?


## Tạo hoặc chèn thành phần lắp ráp đầu tiên

Chọn một chi tiết hoặc một cụm lắp cơ sở (ví dụ như một khung hoặc tấm kim loại) làm thành phần lắp ráp đầu tiên của lắp ráp. Ta có thể chèn một thành phần lắp ráp có sẵn hoặc tạo mới một thành phần lắp ráp mới trong lắp ráp. Thành phần lắp ráp đầu tiên này cần được gán cố định (tất cả các bậc tự do đều bị hạn chế). Gốc tọa độ và các trục tọa độ của nó được căn theo gốc và các trục tọa độ của lắp ráp.

  * Tạo một thành phần lắp ráp: Chọn Assemble Create. Trong hộp thoại Create In-Place Component ta nhập tên file mới và kiểu file. Khi đó sẽ tạo ra thành phần lắp ráp đầu tiên.


|<image_1>|Hình 2.16. Hộp thoại Create In-Place Component_

  * Chèn một thành phần lắp ráp có sẵn: Chọn Assemble Place. Duyệt qua các file cần mở trong hộp thoại Open. Kích chuột vào cửa sổ đồ họa để chèn thành phần lắp ráp, có thể chèn nhiều bản một lúc, kết thúc kích chuột phải và chọn Ok. Các bản chèn không có các ràng buộc lắp ráp.


## Định vị các thành phần lắp ráp

Có nhiều cách để di chuyển các thành phần lắp ráp. Nếu một thành phần lắp ráp không phải là cố định hoặc không bị ràng buộc hoàn toàn, ta có thể di chuyển nó trong vùng lắp ráp. Các ràng buộc sẽ xóa một vài bậc tự do của thành phần lắp ráp này. Có thể dịch chuyển một thành phần lắp ráp theo các bậc tự do còn lại.

Khi một chi tiết hoặc một cụm lắp ráp được cố định nó sẽ được cố định trong hệ tọa độ lắp ráp. Chi tiết cố định này sẽ được mô tả bằng một biểu tượng riêng trên cửa sổ duyệt. Bất kỳ thành phần lắp ráp nào trong một lắp ráp cũng có thể được cố định. Thành phần lắp ráp đầu tiên của lắp ráp được tự động cố định tuy nhiên ta có thể hủy bỏ trạng thái cố định của nó.

Một thành phần lắp ráp cố định thì không giống như các thành phần lắp ráp ràng buộc khác. Một thành phần lắp ráp cố định được cố định vào hệ trục tọa độ lắp ráp. Một thành phần lắp ráp ràng buộc thì có quan hệ với các thành phần lắp ráp khác mà định nghĩa vị trí của nó. Đây là sự tác động lẫn nhau giữa các thành phần lắp ráp. Ví dụ: Nếu ta dùng công cụ Move hoặc Rotate để tạm thời định vị lại một thành phần lắp ráp được ràng buộc khi Update, thành phần lắp ráp này sẽ trở lại vị trí ràng buộc của nó.

Khi dịch chuyển một thành phần lắp ráp cố định bằng công cụ Move hoặc Rotate, bất kỳ thành phần lắp ráp nào mà có ràng buộc tới nó sẽ cùng dịch chuyển tới vị trí mới của thành phần lắp ráp cố định.

|<image_2>|

_Hình 2.17. Biểu tượng chi tiết định vị trên cửa sổ duyệt_

|<image_3>|

_Hình 2.18. Chế độ Degrees of Freedom OnS_

Hiển thị các bậc tự do có sẵn: Kích chuột phải vào chi tiết trong cửa sổ duyệt hoặc cửa sổ đồ họa sau đó chọn Properties. Trong hộp hội thoại Properties chọn nút Occurrence, đánh dấu vào hộp kiểm Degrees of Freedom sau đó kích chuột OK. Để tắt chế độ hiển thị bậc tự do ta bỏ đánh dấu trong hộp kiểm trên. Ta cũng có thể sử dụng tùy chọn Degrees of Freedom trong menu View.

|<image_4>|
_Hình 2.19. Thay đổi trạng thái cố định của một thành phần lắp ráp_

Di chuyển hoặc quay thành phần lắp ráp cố định: Kích chuột vào công cụ Move Component hoặc Rotate Component trên thanh công cụ Assembly. Sau đó, kéo rê thành phần lắp ráp cố định tới vị trí mới. Khi kích chuột vào Update bất kỳ các thành phần lắp ráp ràng buộc nào sẽ được định vị lại tới vị trí mới.

  * Di chuyển một thành phần lắp ráp với một khoảng cách xác định: Kích chuột phải vào thành phần lắp ráp cần di chuyển sau đó chọn Properties Occurrence. Ta có thể nhập số cho các giá trị dịch chuyển theo các trục tọa độ X, Y, Z. Ta cũng có thể bật tắt trạng thái cố định của thành phần lắp ráp cố định.


|<image_5>|Hình 2.20. Di chuyển một thành phần lắp ráp với khoảng cách xác định_

  * Di chuyển hoặc quay tạm thời các thành phần lắp ráp ràng buộc: Kích chuột vào công cụ Move Component hoặc Rotate Component trên thanh công cụ Assembly. Dùng các công cụ này để di chuyển hoặc quay tạm thời các thành phần lắp ráp mà không xóa mất ràng buộc. Thành phần lắp ráp ràng buộc sẽ trở thành vị trí ban đầu của nó khi ta kích chuột vào Update.


## Bổ sung thành phần lắp ráp

Trong môi trường lắp ráp ta có thể tạo một cụm lắp, một chi tiết mới hoặc chèn một chi tiết hay một cụm lắp có sẵn. Khi tạo một Component In-Place mới ta có thể gán mặt phác thảo trong mặt quan sát hiện hành hay ràng buộc nó tới một mặt của thành phần lắp ráp có sẵn. Ta có thể chèn nó vào vùng lắp ráp sau đó bổ sung các ràng buộc.

Khi một thành phần lắp ráp được kích hoạt thì các thành phần lắp ráp còn lại sẽ bị mờ đi trong cửa sổ duyệt. Chỉ có một thành phần lắp ráp có thể được kích hoạt tại một thời điểm. Bộ phận lắp ráp tự nó phải được kích hoạt khi tạo hoặc chèn một thành phần lắp ráp.

  * Kích hoạt chi tiết: Kích đúp vào tên chi tiết trong cửa sổ duyệt. Các chi tiết còn lại sẽ bị mờ đi.

  * Kích hoạt một cụm lắp: Kích đúp vào tên của của cụm lắp ráp trong cửa sổ duyệt hoặc kích chuột phải trong cửa sổ đồ họa và chọn Finish Edit.


Chú ý: Finish Edit sẽ bị ẩn trên menu ngữ cảnh trong khi đối tượng hình học được chọn trong cửa sổ đồ họa.

  * Tạo một Component In-Place: Kích chuột vào công cụ Create Component. Nếu cần tạo ràng buộc giữa mặt phác thảo và một mặt của chi tiết có sẵn thì chọn Constrain Sketch Plance to Selected Face trong hộp thoại Create In-Place Component.


Cách khác có thể kích chuột vào một vị trí trong cửa sổ đồ họa để xác định mặt phác thảo.

  * Tạo một chi tiết hoặc một cụm lắp dẫn xuất: Duyệt và mở file Part (.ipt) đối với Feature cơ sở. Trong thanh công cụ Feature kích chuột vào nút Derived Component. Xác định hệ số tỷ lệ, mặt đối xứng và kích OK. Nếu ta chỉnh sửa Feature của chi tiết dẫn xuất kích chuột phải và chọn Update Derived Feature. Để phá hủy liên kết và không cập nhật sự thay đổi của chi tiết gốc, kích chuột phải vào Feature dẫn xuất trong cửa sổ duyệt và kích chuột vào Break link.

  * Chèn một chi tiết hoặc một cụm lắp: Kích chuột vào công cụ Place Component sau đó chỉ rõ file cần chèn. Kích chuột vào cửa sổ đồ họa để định vị thành phần lắp ráp khi chèn. Mỗi lần kích chuột vào cửa sổ đồ họa sẽ chèn một bản của chi tiết hoặc cụm chi lắp cần chèn. Không có ràng buộc nào được gán khi dùng công cụ Place Component.


## Tạo mảng các thành phần lắp ráp

Bạn có thể tạo mảng chi tiết, nhóm chi tiết, cụm lắp. Các thành phần lắp ráp được tạo mảng có thể bao gồm các ràng buộc và là các đối tượng lắp ráp duy nhất với các đặc tính không có trong các thành phần lắp ráp chèn thông thường. Ta có thể tạo các thành phần lắp ráp được tạo mảng và có liên kết tới mảng các Feature chi tiết. Ví dụ: Một mảng các lỗ có thể tồn tại cùng các bulong mà có mối liên hệ với mảng các lỗ. Nếu số lỗ thay đổi thì số bulong cũng thay đổi theo.

Để tạo mảng các thành phần lắp ráp: Kích chuột vào công cụ Pattern Component sau đó chọn nút Rectangular hoặc Circular. Ta có thể chọn các thành phần lắp ráp cần tạo mảng trong cửa sổ duyệt hoặc trong cửa sổ đồ họa. Sau đó, chọn các cạnh của thành phần lắp ráp, các trục làm việc hoặc các trục tọa độ để xác định hướng của các hàng và các cột hoặc trục quay. Nhập số phần tử và khoảng cách giữa các phần tử.

Chú ý: Mỗi lần chèn một thành phần lắp ráp hoặc tạo một mảng từ một thành phần lắp ráp, Autodesk Inventor liên kết nó tới tất cả các cá thể khác của thành phần lắp ráp đó. Thay đổi một mô hình đơn sẽ làm thay đổi tất cả các cá thể khác. Để tạo một thành phần lắp ráp mới dựa trên thành phần lắp ráp khác, ghi phiên bản với tên chi tiết và chèn phiên bản vào trong lắp ráp.

|<image_6>|Hình 2.22. Hộp thoại Pattern Component_

## Thay đổi các thành phần lắp ráp

Việc các nhà thiết kế thay đổi một chi tiết trong lắp ráp là việc thường xuyên diễn ra. Autodesk Inventor chèn chi tiết mới với các trục tọa độ của nó được căn theo các trục tọa độ của chi tiết có sẵn. Ta phải gán bất kỳ ràng buộc nào cho nó.

Để thay đổi một thành phần lắp ráp: Kích chuột vào công cụ Replace Component trên thanh công cụ Assembly sau đó chọn thành phần lắp ráp cần thay đổi sau đó tìm đến thành phần lắp ráp mới. Tất cả các ràng buộc trên thành phần lắp ráp có sẵn sẽ bị mất trong khi thay đổi.

## Bổ sung các ràng buộc tới các thành phần lắp ráp

Ta có thể bổ sung 4 kiểu ràng buộc tới các thành phần lắp ráp: mate, angle, tangent và insert. Mỗi kiểu của ràng buộc có nhiều phương án. Các phương án được định nghĩa bởi hướng của các vector vuông góc với thành phần lắp ráp. Ta có thể Mate các thành phần lắp ráp bằng cách nhấn phím Alt và kéo rê chi tiết vào vị trí Mate. Phương pháp này thì nhanh bởi vì không cần nhập lệnh tạo ràng buộc. Một số bậc tự do sẽ bị mất khi ta thêm các ràng buộc. Các bậc tự do có thể vẫn có sẵn nhưng bị hạn chế. Ví dụ: Nếu ta gán một ràng buộc Tangent tới 2 quả cầu thì tất cả sáu bậc tự do vẫn còn nhưng ta không thể dịch chuyển một quả cầu dù chỉ là theo một hướng. Thử dựng một vài chi tiết để xem các ràng buộc hạn chế chuyển động của chúng như thế nào.

|<image_7>|

_Hình 2.23. Gán ràng buộc cho các chi tiết lắp ráp_

  * Tạo ràng buộc 2 mặt, cạnh, điểm hoặc các Work Feature với nhau: Trong hộp thoại Place Constraint kích chuột vào Mate. Ta có hai phương án trong lệnh Mate là Mate và Flush như minh họa hình 2.24. Nếu ta muốn các mũi tên vuông góc hướng vào nhau thì ta chọn Mate. Nếu ta muốn các đối tượng hình học đặt cạnh nhau và các mũi tên theo cùng một hướng ta chọn Flush. Nếu muốn tạo khe hở nhập giá trị hở vào hộp offset.


|<image_8>|

_Hình 2.24. Ràng buộc Mate trong hộp thoại Place Constraint_

  * Tạo ràng buộc hai mặt hoặc hai cạnh hợp với nhau một góc nhất định: Trong hộp thoại Place Constraint kích chuột vào Angle. Ta có thể chọn các vector vuông góc với các mặt hoặc các cạnh riêng. Có 4 giải pháp cho mỗi cặp lắp ráp. Các mặt được lựa chọn của chi tiết sẽ được ràng buộc theo góc.


|<image_9>|

_Hình 2.25. Ràng buộc Angle trong hộp thoại Place Constraint_

  * Tạo ràng buộc của một mặt cong với một mặt phẳng hoặc một mặt cong khác:


Trong hộp thoại Place Constraint kích chuột vào Tangent. Trong trường hợp này ta có hai phương án là tiếp xúc trong và tiếp xúc ngoài như hình dưới đây:

|<image_10>|
_Hình 2.26. Ràng buộc Tangent trong hộp thoại Place Constraint_

  * Tạo ràng buộc ngang bằng giữa lỗ và mặt trụ: Trong hộp thoại Place Constraint kích chuột vào Insert. Lệnh này sẽ gán đồng tâm của các cung trong hoặc đường tròn được chọn để tạo ràng buộc. Để gán ràng buộc ta chọn đường tròn trên hình trụ và trên lỗ mà ta muốn ràng buộc.


Chú ý: Các ràng buộc Insert được hạn chế bởi các bề mặt phẳng mà vuông góc với đường trục của hình trụ và của lỗ.

|<image_11>|

_Hình 2.27. Ràng buộc Insert trong hộp thoại Place Constraint_

## Bổ sung ràng buộc cho các chi tiết thích nghi

Có thể tạo các chi tiết đặt dưới sự ràng buộc mà được thích nghi theo ràng buộc đó trong lắp ráp. Bằng cách này, chức năng thiết kế sẽ điều khiển hình dạng của các thành

phần lắp ráp. Ví dụ, ta có thể tạo một miếng đệm và gán ràng buộc sao cho nó sẽ kéo dãn hoặc thu nhỏ để điền đầy khe hở giữa hai chi tiết.

Một số yêu cầu để thích nghi:

  * Phác thảo phải được ràng buộc đúng cả về hình học và kích thước. Nếu phác thảo đã bị gán toàn bộ các kích thước thì Autodesk Inventor sẽ không thể thay đổi kích thước. Nếu có nhiều kích thước còn thiếu thì Autodesk Inventor có thể thay đổi sai đối tượng hình học;

  * Chi tiết phải được gán thích nghi trong lắp ráp. Kích chuột phải vào chi tiết trong cửa sổ duyệt của lắp ráp sau đó chọn Adaptive;

  * Feature phải được đặt thích nghi trong file chi tiết. Kích hoạt chi tiết sau đó kích chuột phải vào Feature trong cửa sổ duyệt và chọn Adaptive;

  * Chỉ có một cá thể của chi tiết có thể được thích nghi. Nếu một chi tiết đã được thích nghi thì tùy chọn Adaptivity sẽ bị mờ đi trên menu ngữ cảnh.


Các ràng buộc thích nghi được gán sau khi thành phần lắp ráp đã được ràng buộc về vị trí. Trước tiên Autodesk Inventor định vị lại chi tiết để đảm bảo theo ràng buộc. Nếu thành phần lắp ráp không thể dịch chuyển, hệ thống sẽ thích nghi chi tiết đó để điều chỉnh khoảng trống. Nếu thành phần lắp ráp đã bị ràng buộc hoàn toàn, dòng nhắc nhắc ta đang tạo các ràng buộc thừa trên chi tiết.

# Các công cụ lắp ráp

Khi tạo hoặc chỉnh sửa một chi tiết trong lắp ráp, thanh công cụ lắp ráp không được kích họa trong khi thanh công cụ Part Model được kích hoạt.
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Loại</strong></th>
<th><blockquote>
<p><strong>Nút lệnh</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Công cụ</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Chức năng</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6">Component</td>
<td><blockquote>
<p>|<image_12>|</p>
</blockquote></td>
<td><blockquote>
<p>Place Component</p>
</blockquote></td>
<td>Chèn một chi tiết hoặc một cụm lắp có sẵn</td>
</tr>
<tr>
<td><blockquote>
<p>|<image_13>|</p>
</blockquote></td>
<td><blockquote>
<p>Create Component</p>
</blockquote></td>
<td><blockquote>
<p>Tạo một cụm lắp hoặc một chi tiết mới trong môi trường lắp ráp</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_14>|</p>
</blockquote></td>
<td><blockquote>
<p>Move Component</p>
</blockquote></td>
<td><blockquote>
<p>Cho phép dịch chuyển tạm thời một thành phần lắp ráp đã được ràng
buộc. Thành phần lắp ráp sẽ trở lại vị trí cũ khi ta Update</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_15>|</p>
</blockquote></td>
<td><blockquote>
<p>Rotate Component</p>
</blockquote></td>
<td><blockquote>
<p>Cho phép quay tạm thời một thành phần lắp ráp đã được ràng buộc.
Thành phần lắp ráp sẽ trở lại vị trí cũ khi ta Update</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_16>|</p>
</blockquote></td>
<td><blockquote>
<p>Replace Component</p>
</blockquote></td>
<td><blockquote>
<p>Thay một chi tiết trong một lắp ráp bằng một chi tiết khác</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_17>|</p>
</blockquote></td>
<td><blockquote>
<p>Pattern Component</p>
</blockquote></td>
<td><blockquote>
<p>Tạo mảng các chi tiết lắp ráp</p>
</blockquote></td>
</tr>
<tr>
<td>Constraint</td>
<td><blockquote>
<p>|<image_18>|</p>
</blockquote></td>
<td><blockquote>
<p>Place Constraint</p>
</blockquote></td>
<td><blockquote>
<p>Gán ràng buộc giữa các mặt, các cạnh hoặc các Work Feature. Các ràng
buộc có thể được thích nghi</p>
</blockquote></td>
</tr>
<tr>
<td>All</td>
<td><blockquote>
<p>|<image_19>|</p>
</blockquote></td>
<td><blockquote>
<p>Replace All</p>
</blockquote></td>
<td><blockquote>
<p>Thay nhiều chi tiết trong lắp ráp bằng một chi tiết khác</p>
</blockquote></td>
</tr>
</tbody>
</table>