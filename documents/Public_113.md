# Public_113

# Định nghĩa:

Attention là một kĩ thuật được sử dụng trong các mạng neural, kỹ thuật này được sử dụng trong các mô hình thực hiện các task như dịch máy hay ngôn ngữ tự nhiên. BERT và GPT là 2 mô hình điển hình có sử dụng Attention. Attention là thành phần chính tạo nên sự đình đám của mô hình Transformer, mô hình này chính là sự đột phá trong các bài toán xử lý của NLP so với các mạng neural hồi quy. Vậy Attention là gì mà tại sao nó lại là sự khác biệt đến vậy, hãy cũng tôi đi tìm hiểu trong bài viêt ngày hôm nay với tiêu đề “Attention và sự hình thành của mô hình Transformer”

# Động lực cho sự phát triển của Attention

## Recurrent Neural Network (RNN) và sự hạn chế đáng kể

### Ý tưởng cốt lõi của RNN

Con người chúng ta không thể bắt đầu suy nghĩ của mình tại tất cả các thời điểm, cũng giống như việc bạn đang đọc bài viết này, bạn hiểu mỗi chữ ở đây dựa vào các chữ mà bạn đã đọc và hiểu trước đó, chứ không phải đọc xong là quên chữ đó đi rồi đến lúc gặp thì lại phải đọc và tiếp thu lại. Giống như trong bài toán của chúng ta. Các mô hình mạng nơ-ron truyền thống lại không thể làm được việc trên. Vì vậy mạng nơ-ron hồi quy (RNN) được sinh ra để giải quyết việc đó. Mạng này chứa các vòng lặp bên trong cho phép nó lưu lại các thông tin đã nhận được. RNN là một thuật toán quan trọng trong xử lý thông tin dạng chuỗi hay nói cách khác là dạng xử lý tuần tự.

|<image_1>|

Hình 1. Cấu trúc cơ bản của RNN

Vậy như nào là xử lý tuần tự - Xử lý tuần tự là mỗi block sẽ lấy thông tin của block trước và input hiện tại làm đầu vào, được thể hiện qua Hình 2.

|<image_2>|

Hình 2. Công thức tính đầu ra $y^{t}$

|<image_3>|

Hình 3. Cấu trúc một block trong RNN

### Ưu điểm và nhược điểm của RNN
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong><mark>Ưu điểm</mark></strong></td>
<td><strong><mark>Nhược điểm</mark></strong></td>
</tr>
<tr>
<td><mark>Khả năng xử lý các chuỗi đầu vào có độ dài khác
nhau</mark></td>
<td><mark>Tính toán khá chậm</mark></td>
</tr>
<tr>
<td><mark>Kích cỡ mô hình không bị tăng lên theo kích thước đầu
vào</mark></td>
<td><mark>Khó truy cập lại thông tin đã đi qua ở một khoảng thời gian
dài trước đó - hay còn gọi là bị quên thông tin khi gặp nhiều thông tin
mới</mark></td>
</tr>
<tr>
<td><mark>Quá trình tính toán có sử dụng thông tin trước đo</mark></td>
<td><mark>Phải thực hiện tuần tự nên không tận dụng triệt để được khả
năng tính toán song song của GPU</mark></td>
</tr>
<tr>
<td><mark>Trọng số được chia sẻ trong suốt qua trình học</mark></td>
<td><mark>Vanishing gradient</mark></td>
</tr>
</tbody>
</table> 

## Vấn đề gặp phải của Long Short Term Memory (LSTM)

### Ý tưởng cốt lõi của LSTM (Long short term memory)

LSTM là một dạng đặc biệt của RNN, nó có khả năng học các thông tin ở xa. Về cơ bản thì LSTM và RNN không khác nhau là mấy nhưng LSTM có cải tiển một số phép tính trong 1 hidden state và nó đã hiểu quả. Hiệu quả như nào thì chúng ta hãy cũng đọc tiếp nhé!

Cấu trúc của LSTM không khác gì RNN, nhưng sự cải tiến ở đây năm ở phần tính toán trong từng hidden state như sau: Thay vì chỉ có một tầng mạng nơ-ron, LSTM thiết kế với 4 tầng mạng nơ-ron tương tác với nhau một các rất đặc biệt.

Dưới đây là 2 hình ảnh biểu diễn sự khác nhau giữa RNN và LSTM

|<image_4>|

Hình 4. RNN với hàm tanh

|<image_5>|

Hình 5. LSTM với hàm tanh và sigmoid

Chìa khóa để giúp LSTM có thể truyền tải thông tin giữa các hidden state một các xuyên suốt chính là cell state (hình dưới):

|<image_6>|

Hình 6. Cell state LSTM

### Các công thức tính trong LSTM

Forget gate $\mathbf{\Gamma}_{\mathbf{f}}$

Đầu ra là hàm sigmoid chứa các giá trị từ 0 đến 1.

Nếu forget gate có giá trị bằng 0, LSTM sẽ "quên" trạng thái được lưu trữ trong đơn vị tương ứng của trạng thái cell trước đó.

Nếu cổng quên có giá trị bằng 1, LSTM sẽ chủ yếu ghi nhớ giá trị tương ứng ở trạng thái được lưu trữ.

|<image_7>|

Hình 7. Công thức tính Forget gate $\mathbf{\Gamma}_{\mathbf{f}}$

Candidate value ${\widetilde{\mathbf{c}}}^{\mathbf{< t >}}$

Chứa thông tin có thể được lưu trữ từ time step hiện tại.

|<image_8>|

Hình 8. Công thức tính Candidate value ${\widetilde{\mathbf{c}}}^{\mathbf{< t >}}$

Update gate $\mathbf{\Gamma}_{\mathbf{i}}$

|<image_9>|

Hình 9. Công thức tính Update gate $\mathbf{\Gamma}_{\mathbf{i}}$

Cell sate $\mathbf{c}^{\mathbf{< t >}}$

Là bộ nhớ trong của LSTM. Cell state như 1 băng tải truyền các thông tin cần thiết xuyết suất cả quá trình, qua các nút mạng và chỉ tương tác tuyển tính 1 chút. Vì vậy thông tin có thể tuyền đi thông suốt mà không bị thay đổi.

|<image_10>|

Hình 10. Công thức tính Cell state $\mathbf{c}^{\mathbf{< t >}}$

|<image_11>|

Hình 11. Các công thức tính output gate, hidden state và prediction