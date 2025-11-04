# Public_517

Autodesk Inventor liên kết mô hình chi tiết và cụm lắp với bản vẽ. Mọi thay đổi của mô hình sẽ được cập nhật vào bản vẽ. Ngược lại, bạn có thể thay đổi mô hình chi tiết và cụm lắp bằng cách sửa kích thước mô hình ngay trong bản vẽ. Mối quan hệ 2 chiều này đảm bảo cho bản vẽ luôn luôn phản ánh các thông số thiết kế mới nhất của mô hình.

# Trình tự thực hiện

## Khởi tạo bản vẽ mới

File bản vẽ mới sẽ được khởi tạo khi bạn chọn menu File  New hoặc kích phím New trên thanh công cụ Standard, chọn Drawing template từ một trong các thẻ Default, English hoặc Metric, Default là một trang giấy trống có viền và khung tên, bạn có thể sửa đổi chúng nếu cần. Các thẻ English hoặc Metric chứa các bản vẽ mẫu theo đơn vị đo tương ứng.

## Tạo các hình chiếu

Autodesk Inventor cho phép tạo và xử lý nhiều hình chiếu. Place View có các công cụ hiệu dụng, kể cả khả năng kéo, thả để chuyển hình chiếu giữa các trang bản vẽ.

Để tạo một Design View, kích phím Base View trên thanh công cụ Place View, dùng chức năng Component trong hộp thoại Drawing View để tìm file mô hình chi tiết hoặc cụm lắp cần xuất ra bản vẽ, chọn loại hình chiếu trong danh sách View và xác định tỷ lệ (scale). Đưa con trỏ đến vị trí thích hợp trên giấy vẽ để đặt hình chiếu đầu tiên.

Để tạo một hình chiếu, kích phím Projected View, chọn một hình chiếu và di chuột. Nếu di chuột theo phương nằm ngang hay thẳng đứng thì sẽ tạo được một hình chiếu vuông góc. Nếu di theo một góc thì tạo được một hình chiếu trục đo. Mỗi khi chọn được vị trí vừa ý thì nhấn phím trái chuột để xác nhận. Sau khi đặt đủ hình chiếu cần thiết thì nhấn phím phải, chọn Create trong menu.

Để tạo một hình chiếu phụ: Vì hình chiếu phụ được tạo từ một hình chiếu chính nên trước hết phải tạo ra hình chiếu chính. Kích phím Auxiliary View trên thành công cụ Place View. Trong hộp thoại Auxiliary View, nhập tên (label), tỷ lệ cho hình chiếu nhưng chưa nhấn OK. Chọn một đường thẳng trên hình chiếu chính, di chuột theo phương song song hoặc vuông góc với đường thẳng đứng để định vị hình chiếu phụ, sau đó nhấn phím trái chuột để kết thúc lệnh.

Để tạo một hình cắt, chọn Section View, chọn một hình chiếu và vẽ trên đó một đường cắt. Khi vẽ xong, nhấp phím phải để hiện menu và chọn Continue. Nhập tên (label) và tỷ lệ trong hộp thoại Section View. Di con trỏ theo phương chiếu để chọn vị trí và nhấn phím trái chuột. Autodesk Inventor tự động ghi nhãn cho đường cắt, gạch mặt cắt và ghi nhãn cho hình cắt.

Để tạo một hình chiếu riêng phần, chọn Detail View, chọn một hình chiếu làm hình chiếu chính. Một hộp thoại xuất hiện để nhập nhãn (label), tỷ lệ (scale) và kiểu (style) vùng chiếu. Kiểu mặc định là vòng tròn. Nếu muốn kiểu chữ nhật thì kích phím phải chuột và chọn Rectangular Fence. Nhấn chuột để chọn vị trí tâm vòng tròn, xong di chuột để xác định kích thước. Chọn vị trí đặt hình chiếu. Hình chiếu và vùng chọn được tự động tạo ra và gắn nhãn.

## Quay hình chiếu

Bạn có thể quay hình chiếu theo cạnh hay theo góc. Khi quay hình chiếu, quan hệ hình học giữa các đối tượng trên đó được duy trì. Tùy theo tiêu chuẩn hiện dùng, Autodesk Inventor có thể bổ sung thông tin để ghi chú rằng hình chiếu đã được quay khỏi vị trí bình thường của nó.

Để quay hình chiếu, chọn hình chiếu cần quay, xong nhấn phím phải và chọn Rotate View trong menu vừa hiện ra. Chọn phương pháp quay theo cạnh hay theo góc, nhập các thông tin cần thiết. Nhấn OK để cập nhật hình chiếu.

## Thêm tờ giấy vẽ

Một file bản vẽ (Drawing) có thể chứa nhiều tờ giấy vẽ (Sheet). Bạn có thể thêm một hay nhiều tờ giấy vẽ vào file. Tại mỗi thời điểm chỉ có một tờ giấy vẽ hoạt động, nghĩa là có thể điều khiển được. Các tờ giấy vẽ khác không hoạt động và bị bôi xám. Thư mục Drawing Resources luôn luôn hoạt động.

Để thêm một tờ giấy vẽ, kích phím New Sheet trên thanh công cụ Place View.

Để tạo một tờ giấy vẽ với dạng đặc biệt, mở rộng Drawing Resources  Sheet Formats trong Browser. Kích phải chuột vào một trong những Sheet Format và chọn New Sheet. Dùng Drawing Resources để chèn khung viền và khung tên.

|<image_1>|

_Hình 2.30. Tạo tờ giấy vẽ với dạng đặc biệt_

Để kích hoạt một tờ giấy vẽ, kích đúp vào tên nó trong Brower. Tờ giấy vẽ đó được kích hoạt, các tờ khác bị mờ đi.

Để chuyển một hình chiếu giữa các tờ giấy vẽ, kích hoạt tờ giấy vẽ nguồn (chứa hình chiếu cần chuyển đi). Chọn tên hoặc biểu tượng hình chiếu, kéo nó sang tờ đích. Con trỏ phải hiện trên tên hoặc biểu tượng của tờ đích mới thả hình chiếu vào được.

Để copy một hình chiếu sang tờ giấy vẽ khác, kích hoạt tờ giấy vẽ nguồn (chứa hình chiếu cần chuyển đi). Kích phải tên hoặc biểu tượng hình chiếu, chọn Copy trong menu. Kích phải tên hoặc biểu tượng hình chiếu, chọn Past trong menu. Tờ giấy đích sẽ tự kích hoạt và bạn sẽ thấy hình chiếu xuất hiện trên đó.

## Sử dụng kích thước mô hình

Bạn có thể cho hiện kích thước mô hình trong bản vẽ. Chỉ kích thước nào song song với mặt phẳng chiếu mới được hiện lên. Nếu bạn cài đặt Autodesk Inventor với tùy chọn, cho phép sửa đổi mô hình từ trong bản vẽ thì bạn có thể thay đổi mô hình bằng cách sửa kích thước mô hình trong bản vẽ. Bạn có thể thay đổi kiểu kích thước mô hình như với kích thước bản vẽ.

Để hiện kích thước mô hình trong bản vẽ, kích phải một hình chiếu và chọn Get Model Dimensions trong menu vừa hiện lên. Các kích thước mô hình song song với mặt phẳng chiếu sẽ hiện lên trong hình chiếu.

Để xóa kích thước mô hình khỏi hình chiếu, kích phải lên kích thước cần xóa rồi chọn Delete trong menu vừa hiện lên.

Để chuyển kích thước mô hình sang hình chiếu khác, xóa kích thước trong hình chiếu nguồn, xong kích phải lên hình chiếu đích và chọn Get Model Dimensions trong menu vừa hiện lên.

Để sửa một kích thước mô hình, kích phải lên kích thước cần sửa, chọn Edit Model Dimension trong menu vừa hiện lên. Nhập giá trị mới vào hộp thoại Edit Dimension, xong kích vào dấu check để thực hiện.

## Tạo kích thước trong bản vẽ

Muốn ghi kích thước bản vẽ phải chuyển sang môi trường Drawing Annotation. Mọi thủ tục ghi kích thước về cơ bản giống như trong môi trường thiết kế. Khi bạn chọn một đối tượng hay các đối tượng quan hệ thì Autodesk Inventor sẽ tạo kích thước nằm ngang, thẳng đướng, hoặc nghiêng tùy theo phương di chuyển con trỏ. Chế độ Snap giúp phân bố các kích thước theo tiêu chuẩn. Có thể điều khiển sự hiển thị kích thước theo các kiểu khác nhau.

Để tạo kích thước mới, chọn công cụ General Diminsion. Chọn đối tượng và di chuột để tạo kích thước. Khi chuyển con trỏ, tại mỗi vị trí phù hợp với khoảng cách (Offset) quy định thì đường kích thước và đường gióng chuyển từ nét liền sang nét đứt, gợi ý người dùng chọn vị trí đặt đường kích thước.

Để gióng một kích thước mới theo kích thước có trước, giữ phím chuột, di con trỏ qua kích thước có trước thì dấu Snaps hiện lên khi hai kích thước đã được gióng với nhau.

## Thay đổi kích thước

Autodesk Inventor cho phép thay đổi kiểu dung sai, giá trị danh định, dung sai và lắp ghép. Khi chọn kiểu dung sai, bạn có thể xem trước kích thước với kiểu ghi dung sai mới.

Để thay đổi kích thước, kích đúp lên kích thước cần sửa để mở hộp thoại Dimension Tolerace. Nhập giá trị danh định mới và xác định cấp chính xác.

Để thay đổi kiểu mũi tên, chọn kích thước, di con trỏ lên một trong các mũi tên, kích đúp để mở hộp thoại Change Arrowhead và chọn kiểu mũi tên trong danh sách.

## Ghi chú trong bản vẽ

Autodesk Inventor cung cấp đủ các loại ký hiệu ghi trên bản vẽ phù hợp với tiêu chuẩn hiện dùng. Ngoài ra, khi cần vẫn có thể tạo ra các ký hiệu theo mục đích riêng.

Để hiện thanh công cụ Drawing Annotation, chọn menu View  Toolbar  Drawing Annotation hoặc mở rộng Panel Drawing Management và chọn Drawing Annotation.

Để tạo một chú thích, chọn phím Text hoặc Leader Text. Chọn vị trí đặt chú thích trong vùng bản vẽ và nhập nội dung của nó. Công cụ text của Autodesk Inventor dùng bộ xử lý ký tự đơn giản nên bạn có thể định dạng text, như font, bold, các ký tự đặc biệt. Leader text được gắn lên đối tượng hình học và sẽ di chuyển theo hình chiếu.

Để tạo một ký hiệu, chọn ký hiệu cần thiết trong menu. Chọn đối tượng hình học cần gắn ký hiệu, kích chuột để tạo leader. Kích phải và chọn Continue để hiện hộp thoại và điền các thông số cần thiết cho ký hiệu.

Để tạo dấu tâm, chọn phím Center Mark trên thanh công cụ Drawing Annotation.

Chọn cung tròn hay vòng tròn, dấu tâm được tự động tạo ra.

Để tạo đường tâm hay đường đối xứng, kích mũi tên bên cạnh phím Center Mark, chọn Center line, Autodesk Inventor cung cấp 3 kiểu ghi đường tâm: theo phân giác (Center line bisector), theo chuỗi vòng (Centered Pattern) và theo 2 điểm (Center line). Chọn kiểu ghi thích hợp rồi chọn đối tượng để ghi. Đối với kiểu Centered Pattern, sau khi chọn kiểu ghi phải chọn tâm chung của chuỗi, sau đó chọn mỗi vòng tròn trong dãy một lần, nhấn phải chuột, chọn Create. Đến đây, vòng tròn tâm chưa kín. Phải kết thúc lệnh, sau đó kéo điểm cuối vòng tròn đến điểm đầu để đóng kín vòng tròn.

## Tạo danh mục chi tiết

Trong Autodesk Inventor, bạn có thể tạo danh mục chi tiết trong cụm lắp. Trong dữ liệu có chứa tính chất chủ yếu của các chi tiết, như số liệu, tên, vật liệu, số lượng… Bạn có thể xác định thông số nào cần đưa vào trong danh mục.

Để tạo danh mục, nhấn Part List, sau đó chọn một hình chiếu để chọn cụm lắp. Trong hộp thoại Part List - Item Numburing, có thể cho hiện toàn bộ chi tiết (All) hay một số (Item) trong danh mục. Khi chọn Items, bạn phải chọn từng chi tiết trong hình chiếu. Số hiệu các chi tiết được chọn sẽ hiện lên khung trong hộp thoại. Xong nhấn OK để kết thúc và xác định vị trí đặt bản danh mục.

Để sửa danh mục, kích đúp vào đó (hoặc kích phải rồi chọn Edit Parts List trong menu) để mở hộp thoại Edit Parts List. Có thể thêm bớt các cột (Column Chooser), sắp xếp (Sort), xuất dữ liệu (Export) ra các form khác nhau, như Excel, Access, dBase, file Text…

Đánh số chi tiết, kích vào phím Balloon (để đánh số từng chi tiết) hoặc Balloon All (để đánh số toàn bộ). Khi đánh số từng chi tiết, trước hết chọn điểm đầu (là một điểm trên chi tiết), rồi điểm cuối để đặt quả bóng.

## Vẽ thêm vào bản vẽ

Bạn có thể dùng chức năng Sketch Overlay để vẽ thêm đối tượng hình học, text vào bản vẽ mà không gây ảnh hưởng đến các hình chiếu. Muốn vậy, nhấn phím Sketch Overlay. Lưới Sketch xuất hiện và thanh công cụ Sketch được kích hoạt, cho phép vẽ như bình thường.

## In bản vẽ

Drawing Manager của Autodesk Inventor sử dụng hộp thoại điều khiển máy in và máy vẽ tương tự chương trình ứng dụng khác của Windows. Bạn có thể chọn máy in, tỷ lệ, số bản in hoặc chọn tờ để in. Muốn in, chọn menu File  Print. Xác định vùng in, tỷ lệ, số bản in... Có thể chọn các tờ để không in. Kích phải vào Sheet trong Browser, chọn Edit Sheet trong menu  chọn Exclude Sheet from Printing.

# Bộ công cụ vẽ

Bộ công cụ vẽ gồm các thanh công cụ Drawing Management (quản lý bản vẽ), Drawing Annotation (chú giải) và Sketch (vẽ).
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Phím</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tên</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Công dụng</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Ghi chú</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><blockquote>
<p><strong>Thanh công cụ Drawing Management</strong></p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_2>|</p>
</blockquote></td>
<td><blockquote>
<p>Base View</p>
</blockquote></td>
<td><blockquote>
<p>Liên kết một mô hình chi tiết với bản vẽ và tạo hình chiếu đầu
tiên</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_3>|</p>
</blockquote></td>
<td><blockquote>
<p>Projected View</p>
</blockquote></td>
<td><blockquote>
<p>Tạo một hình chiếu vuông góc</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_4>|</p>
</blockquote></td>
<td><blockquote>
<p>Auxiliary View</p>
</blockquote></td>
<td><blockquote>
<p>Tạo hình chiếu phụ</p>
</blockquote></td>
<td><blockquote>
<p>Chọn một cạnh làm phướng chiếu</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_5>|</p>
</blockquote></td>
<td><blockquote>
<p>Section View</p>
</blockquote></td>
<td><blockquote>
<p>Tạo hình cắt</p>
</blockquote></td>
<td><blockquote>
<p>Vẽ vết cắt</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_6>|</p>
</blockquote></td>
<td><blockquote>
<p>Detail View</p>
</blockquote></td>
<td><blockquote>
<p>Tạo hình chiếu riêng phần</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_7>|</p>
</blockquote></td>
<td><blockquote>
<p>New Sheet</p>
</blockquote></td>
<td><blockquote>
<p>Thêm tờ giấy vẽ</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_8>|</p>
</blockquote></td>
<td><blockquote>
<p>Draft View</p>
</blockquote></td>
<td><blockquote>
<p>Tạo Draft View</p>
</blockquote></td>
</tr>
<tr>
<td colspan="4">Thanh công cụ Drawing Annotation</td>
</tr>
<tr>
<td><blockquote>
<p>|<image_9>|</p>
</blockquote></td>
<td><blockquote>
<p>General Dimension</p>
</blockquote></td>
<td><blockquote>
<p>Ghi kích thước giữa 2 điểm, đường thẳng hoặc đường cong</p>
</blockquote></td>
<td><blockquote>
<p>Kích đúp lên kích thước để chọn kiểu ghi dung sai và cấp chính
xác</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_10>|</p>
</blockquote></td>
<td><blockquote>
<p>Ordinate Dimension</p>
</blockquote></td>
<td><blockquote>
<p>Ghi kích thước theo tọa độ</p>
</blockquote></td>
<td></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_11>|</p>
</blockquote></td>
<td><blockquote>
<p>Hole/Thread Notes</p>
</blockquote></td>
<td><blockquote>
<p>Ghi chú lỗ, ren với đường dẫn</p>
</blockquote></td>
<td><blockquote>
<p>Chỉ có giá trị với lỗ được tạo bởi công cụ Hole trong Parts</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_12>|</p>
</blockquote></td>
<td><blockquote>
<p>Center Mark</p>
</blockquote></td>
<td><blockquote>
<p>Tạo dấu tâm</p>
</blockquote></td>
<td rowspan="8"></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_13>|</p>
</blockquote></td>
<td rowspan="3"></td>
<td><blockquote>
<p>Tạo đường tâm</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_14>|</p>
</blockquote></td>
<td><blockquote>
<p>Tạo phân giác của góc</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_15>|</p>
</blockquote></td>
<td><blockquote>
<p>Tạo đường tâm cho chuỗi đường tròn</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_16>|</p>
</blockquote></td>
<td><blockquote>
<p>Surface Texture Symbol</p>
</blockquote></td>
<td><blockquote>
<p>Ghi kí hiệu độ nhám bề mặt</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_17>|</p>
</blockquote></td>
<td><blockquote>
<p>Weld Symbol</p>
</blockquote></td>
<td><blockquote>
<p>Ghi ký hiệu mối hàn</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_18>|</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Tạo khối chữ</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_19>|</p>
</blockquote></td>
<td><blockquote>
<p>Leader Text</p>
</blockquote></td>
<td><blockquote>
<p>Tạo chữ với đường dẫn</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_20>|</p>
</blockquote></td>
<td><blockquote>
<p>Balloon</p>
</blockquote></td>
<td><blockquote>
<p>Ghi số hiệu chi tiết</p>
</blockquote></td>
<td><blockquote>
<p>Autodesk Inventor tự xác định số hiệu chi tiết</p>
</blockquote></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_21>|</p>
</blockquote></td>
<td><blockquote>
<p>Balloon Auto</p>
</blockquote></td>
<td><blockquote>
<p>Tự động ghi số hiệu cho tất cả chi tiết trong cụm lắp</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr>
<td><blockquote>
<p>|<image_22>|</p>
</blockquote></td>
<td><blockquote>
<p>Parts List</p>
</blockquote></td>
<td><blockquote>
<p>Tạo bảng danh mục chi tiết</p>
</blockquote></td>
</tr>
</tbody>
</table>