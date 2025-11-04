# Public_476

# GIỚI THIỆU VỀ PYTHON VÀ AI

Python là ngôn ngữ lập trình phổ biến cho nghiên cứu và ứng dụng trí tuệ nhân tạo (AI) và học máy (Machine Learning). Trong tài liệu này, chúng ta sẽ tìm hiểu cách mô phỏng và thực hành các mô hình AI cơ bản bằng Python, với mục tiêu giúp học viên hiểu và áp dụng lý thuyết vào thực tế.

# DỮ LIỆU VÀ MÔ HÌNH HỌC MÁY

## Yêu cầu trước khi làm thí nghiệm 
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><p>• Có kiến thức cơ bản về Python.</p>
<p>• Hiểu các khái niệm thống kê: trung bình, phương sai, độ lệch
chuẩn.</p>
<ul>
<li><p>Cài đặt thư viện: numpy, pandas, scikit-learn,
matplotlib.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Mục đích của phần thí nghiệm 
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><p>Dùng MATLAB mô phỏng các nội dung sau:</p>
<ul>
<li><p>Làm quen với quy trình xử lý dữ liệu và huấn luyện mô
hình.</p></li>
<li><p>Hiểu cách áp dụng các thuật toán cơ bản và đánh giá kết
quả</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Tóm tắt lý thuyết 

### Định nghĩa cơ bản 
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><h5>Định
nghĩa</h5></th>
<th>Công thức</th>
</tr>
</thead>
<tbody>
<tr>
<td><h5>Hồi quy tuyến tính (Linear Regression):
tìm tham số w, b để tối thiểu hóa MSE</h5></td>
<td><p><math><semantics><mrow><mi>ŷ</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>w</mi><mi>ᵀ</mi><mi>x</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>b</mi></mrow><annotation>ŷ\  = \ wᵀx\  + \ b</annotation></semantics></math></p>
<p><math><semantics><mrow><mi>M</mi><mi>S</mi><mi>E</mi><mspace></mspace><mo>=</mo><mspace></mspace><mrow><mo>(</mo><mn>1</mn><mi>/</mi><mi>n</mi><mo>)</mo></mrow><mspace></mspace><mi>Σ</mi><mspace></mspace><mrow><mo>(</mo><mi>y</mi><mi>ᵢ</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>ŷ</mi><mi>ᵢ</mi><mo>)</mo></mrow><mi>²</mi></mrow><annotation>MSE\  = \ (1/n)\ \Sigma\ (yᵢ\  - \ ŷᵢ)²</annotation></semantics></math></p></td>
</tr>
<tr>
<td><p>Hồi quy logistic (Logistic Regression): phân loại nhị phân với
hàm sigmoid</p>
<h5></h5></td>
<td><p><math><semantics><mrow><mi>ŷ</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>σ</mi><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow><mspace></mspace><mo>=</mo><mspace></mspace><mn>1</mn><mspace></mspace><mi>/</mi><mspace></mspace><mrow><mo>(</mo><mn>1</mn><mspace></mspace><mo>+</mo><mspace></mspace><mi>e</mi><mover><mrow></mrow><mo>̂</mo></mover><mrow><mo>(</mo><mo>−</mo><mi>z</mi><mo>)</mo></mrow><mo>)</mo></mrow><mo>,</mo><mspace></mspace><mi>z</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>w</mi><mi>ᵀ</mi><mi>x</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>b</mi></mrow><annotation>ŷ\  = \ \sigma(z)\  = \ 1\ /\ (1\  + \ e\hat{}( - z)),\ z\  = \ wᵀx\  + \ b</annotation></semantics></math></p>
<p><math><semantics><mrow><mi>L</mi><mi>o</mi><mi>s</mi><mi>s</mi><mspace></mspace><mo>=</mo><mspace></mspace><mo>−</mo><mrow><mo>(</mo><mn>1</mn><mi>/</mi><mi>n</mi><mo>)</mo></mrow><mspace></mspace><mi>Σ</mi><mspace></mspace><mo>[</mo><mi>y</mi><mi>ᵢ</mi><mspace></mspace><mi>l</mi><mi>o</mi><mi>g</mi><mrow><mo>(</mo><mi>ŷ</mi><mi>ᵢ</mi><mo>)</mo></mrow><mspace></mspace><mo>+</mo><mspace></mspace><mrow><mo>(</mo><mn>1</mn><mo>−</mo><mi>y</mi><mi>ᵢ</mi><mo>)</mo></mrow><mspace></mspace><mi>l</mi><mi>o</mi><mi>g</mi><mrow><mo>(</mo><mn>1</mn><mo>−</mo><mi>ŷ</mi><mi>ᵢ</mi><mo>)</mo></mrow><mo>]</mo></mrow><annotation>Loss\  = \  - (1/n)\ \Sigma\ \lbrack yᵢ\ log(ŷᵢ)\  + \ (1 - yᵢ)\ log(1 - ŷᵢ)\rbrack</annotation></semantics></math></p></td>
</tr>
<tr>
<td><h5>Mạng nơ-ron (Neural Networks): nhiều tầng
tuyến tính kết hợp hàm kích hoạt</h5></td>
<td><p><math><semantics><mrow><mi>a</mi><mover><mrow></mrow><mo>̂</mo></mover><mrow><mo>(</mo><mi>l</mi><mo>)</mo></mrow><mspace></mspace><mo>=</mo><mspace></mspace><mi>f</mi><mrow><mo>(</mo><mi>W</mi><mover><mrow></mrow><mo>̂</mo></mover><mrow><mo>(</mo><mi>l</mi><mo>)</mo></mrow><mspace></mspace><mi>a</mi><mover><mrow></mrow><mo>̂</mo></mover><mrow><mo>(</mo><mi>l</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><mspace></mspace><mo>+</mo><mspace></mspace><mi>b</mi><mover><mrow></mrow><mo>̂</mo></mover><mrow><mo>(</mo><mi>l</mi><mo>)</mo></mrow><mo>)</mo></mrow></mrow><annotation>a\hat{}(l)\  = \ f(W\hat{}(l)\ a\hat{}(l - 1)\  + \ b\hat{}(l))</annotation></semantics></math></p>
<p>|<image_1>|</p></td>
</tr>
<tr>
<td><h5>Chuẩn hóa dữ liệu
(Standardization)</h5></td>
<td><p><math><semantics><mrow><mi>z</mi><mspace></mspace><mo>=</mo><mspace></mspace><mrow><mo>(</mo><mi>x</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>μ</mi><mo>)</mo></mrow><mspace></mspace><mi>/</mi><mspace></mspace><mi>σ</mi></mrow><annotation>z\  = \ (x\  - \ \mu)\ /\ \sigma</annotation></semantics></math></p>
<p>|<image_2>|</p></td>
</tr>
<tr>
<td>Đánh giá mô hình</td>
<td><p><math><semantics><mrow><mi>A</mi><mi>c</mi><mi>c</mi><mi>u</mi><mi>r</mi><mi>a</mi><mi>c</mi><mi>y</mi><mspace></mspace><mo>=</mo><mspace></mspace><mrow><mo>(</mo><mi>T</mi><mi>P</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>T</mi><mi>N</mi><mo>)</mo></mrow><mspace></mspace><mi>/</mi><mspace></mspace><mrow><mo>(</mo><mi>T</mi><mi>P</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>T</mi><mi>N</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>F</mi><mi>P</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>F</mi><mi>N</mi><mo>)</mo></mrow></mrow><annotation>Accuracy\  = \ (TP\  + \ TN)\ /\ (TP\  + \ TN\  + \ FP\  + \ FN)</annotation></semantics></math></p>
<p><math><semantics><mrow><mi>P</mi><mi>r</mi><mi>e</mi><mi>c</mi><mi>i</mi><mi>s</mi><mi>i</mi><mi>o</mi><mi>n</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>T</mi><mi>P</mi><mspace></mspace><mi>/</mi><mspace></mspace><mrow><mo>(</mo><mi>T</mi><mi>P</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>F</mi><mi>P</mi><mo>)</mo></mrow></mrow><annotation>Precision\  = \ TP\ /\ (TP\  + \ FP)</annotation></semantics></math></p>
<p><math><semantics><mrow><mi>R</mi><mi>e</mi><mi>c</mi><mi>a</mi><mi>l</mi><mi>l</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>T</mi><mi>P</mi><mspace></mspace><mi>/</mi><mspace></mspace><mrow><mo>(</mo><mi>T</mi><mi>P</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>F</mi><mi>N</mi><mo>)</mo></mrow></mrow><annotation>Recall\  = \ TP\ /\ (TP\  + \ FN)</annotation></semantics></math></p>
<p><math><semantics><mrow><mi>F</mi><mn>1</mn><mo>−</mo><mi>s</mi><mi>c</mi><mi>o</mi><mi>r</mi><mi>e</mi><mspace></mspace><mo>=</mo><mspace></mspace><mn>2</mn><mspace></mspace><mo>*</mo><mspace></mspace><mrow><mo>(</mo><mi>P</mi><mi>r</mi><mi>e</mi><mi>c</mi><mi>i</mi><mi>s</mi><mi>i</mi><mi>o</mi><mi>n</mi><mspace></mspace><mo>*</mo><mspace></mspace><mi>R</mi><mi>e</mi><mi>c</mi><mi>a</mi><mi>l</mi><mi>l</mi><mo>)</mo></mrow><mspace></mspace><mi>/</mi><mspace></mspace><mrow><mo>(</mo><mi>P</mi><mi>r</mi><mi>e</mi><mi>c</mi><mi>i</mi><mi>s</mi><mi>i</mi><mi>o</mi><mi>n</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>R</mi><mi>e</mi><mi>c</mi><mi>a</mi><mi>l</mi><mi>l</mi><mo>)</mo></mrow><mspace></mspace></mrow><annotation>F1 - score\  = \ 2\ *\ (Precision\ *\ Recall)\ /\ (Precision\  + \ Recall)\ </annotation></semantics></math></p></td>
</tr>
</tbody>
</table> 

### Một số định nghĩa khác 
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Gradient Descent: thuật toán tối ưu để cập nhật tham số</th>
<th><math><semantics><mrow><mi>θ</mi><mspace></mspace><mo>:</mo><mo>=</mo><mspace></mspace><mi>θ</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>α</mi><mspace></mspace><mi>∇</mi><mi>J</mi><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow></mrow><annotation>\theta\ : = \ \theta\  - \ \alpha\ \nabla J(\theta)</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
<tr>
<td>Chuẩn hóa L2 (Ridge Regression)</td>
<td><math><semantics><mrow><mi>θ</mi><mspace></mspace><mo>:</mo><mo>=</mo><mspace></mspace><mi>θ</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>α</mi><mspace></mspace><mi>∇</mi><mi>J</mi><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow></mrow><annotation>\theta\ : = \ \theta\  - \ \alpha\ \nabla J(\theta)</annotation></semantics></math></td>
</tr>
<tr>
<td>Chuẩn hóa L1 (Lasso Regression)</td>
<td><math><semantics><mrow><mi>J</mi><mrow><mo>(</mo><mi>w</mi><mo>)</mo></mrow><mspace></mspace><mo>=</mo><mspace></mspace><mrow><mo>(</mo><mn>1</mn><mi>/</mi><mi>n</mi><mo>)</mo></mrow><mspace></mspace><mi>Σ</mi><mspace></mspace><mrow><mo>(</mo><mi>y</mi><mi>ᵢ</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>ŷ</mi><mi>ᵢ</mi><mo>)</mo></mrow><mi>²</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>λ</mi><mspace></mspace><mrow><mo>|</mo><mo>|</mo></mrow><mi>w</mi><mrow><mo>|</mo><mo>|</mo></mrow><mi>₁</mi></mrow><annotation>J(w)\  = \ (1/n)\ \Sigma\ (yᵢ\  - \ ŷᵢ)²\  + \ \lambda\ ||w||₁</annotation></semantics></math></td>
</tr>
<tr>
<td>Phân tích thành phần chính (Principal Component Analysis - PCA)</td>
<td><math><semantics><mrow><mi>m</mi><mi>a</mi><mi>x</mi><mi>_</mi><mo>{</mo><mi>w</mi><mo>}</mo><mspace></mspace><mi>V</mi><mi>a</mi><mi>r</mi><mrow><mo>(</mo><mi>w</mi><mi>ᵀ</mi><mi>X</mi><mo>)</mo></mrow><mo>,</mo><mspace></mspace><mi>v</mi><mi>ớ</mi><mi>i</mi><mspace></mspace><mi>r</mi><mi>à</mi><mi>n</mi><mi>g</mi><mspace></mspace><mi>b</mi><mi>u</mi><mi>ộ</mi><mi>c</mi><mspace></mspace><mrow><mo>|</mo><mo>|</mo></mrow><mi>w</mi><mrow><mo>|</mo><mo>|</mo></mrow><mspace></mspace><mo>=</mo><mspace></mspace><mn>1</mn></mrow><annotation>max\_\{ w\}\ Var(wᵀX),\ với\ ràng\ buộc\ ||w||\  = \ 1</annotation></semantics></math></td>
</tr>
<tr>
<td>K-Means Clustering: gom cụm dữ liệu</td>
<td><math><semantics><mrow><mi>J</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>Σ</mi><mspace></mspace><mi>Σ</mi><mspace></mspace><mrow><mo>|</mo><mo>|</mo></mrow><mi>x</mi><mi>ᵢ</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>μ</mi><mi>_</mi><mi>k</mi><mrow><mo>|</mo><mo>|</mo></mrow><mi>²</mi><mo>,</mo><mspace></mspace><mi>v</mi><mi>ớ</mi><mi>i</mi><mspace></mspace><mi>μ</mi><mi>_</mi><mi>k</mi><mspace></mspace><mi>l</mi><mi>à</mi><mspace></mspace><mi>t</mi><mi>â</mi><mi>m</mi><mspace></mspace><mi>c</mi><mi>ụ</mi><mi>m</mi></mrow><annotation>J\  = \ \Sigma\ \Sigma\ ||xᵢ\  - \ \mu\k||²,\ với\ \mu\k\ là\ tâm\ cụm</annotation></semantics></math></td>
</tr>
<tr>
<td>Naive Bayes Classifier: áp dụng định lý Bayes với giả định độc
lập</td>
<td><math><semantics><mrow><mi>P</mi><mrow><mo>(</mo><mi>y</mi><mo>|</mo><mi>x</mi><mo>)</mo></mrow><mspace></mspace><mo>∝</mo><mspace></mspace><mi>P</mi><mrow><mo>(</mo><mi>y</mi><mo>)</mo></mrow><mspace></mspace><mi>Π</mi><mspace></mspace><mi>P</mi><mrow><mo>(</mo><mi>x</mi><mi>ᵢ</mi><mo>|</mo><mi>y</mi><mo>)</mo></mrow></mrow><annotation>P(y|x)\  \propto \ P(y)\ \Pi\ P(xᵢ|y)</annotation></semantics></math></td>
</tr>
<tr>
<td>Support Vector Machine (SVM): tìm siêu phẳng tối ưu</td>
<td><math><semantics><mrow><mi>m</mi><mi>i</mi><mi>n</mi><mi>_</mi><mo>{</mo><mi>w</mi><mo>,</mo><mi>b</mi><mo>}</mo><mspace></mspace><mrow><mo>(</mo><mn>1</mn><mi>/</mi><mn>2</mn><mo>)</mo></mrow><mrow><mo>|</mo><mo>|</mo></mrow><mi>w</mi><mrow><mo>|</mo><mo>|</mo></mrow><mi>²</mi><mo>,</mo><mspace></mspace><mi>v</mi><mi>ớ</mi><mi>i</mi><mspace></mspace><mi>r</mi><mi>à</mi><mi>n</mi><mi>g</mi><mspace></mspace><mi>b</mi><mi>u</mi><mi>ộ</mi><mi>c</mi><mspace></mspace><mi>y</mi><mi>ᵢ</mi><mrow><mo>(</mo><mi>w</mi><mi>ᵀ</mi><mi>x</mi><mi>ᵢ</mi><mspace></mspace><mo>+</mo><mspace></mspace><mi>b</mi><mo>)</mo></mrow><mspace></mspace><mo>≥</mo><mspace></mspace><mn>1</mn></mrow><annotation>min\_\{ w,b\}\ (1/2)||w||²,\ với\ ràng\ buộc\ yᵢ(wᵀxᵢ\  + \ b)\  \geq \ 1</annotation></semantics></math></td>
</tr>
</tbody>
</table> 

### Hệ thống 

#### Cross-Entropy Loss (Entropy chéo cho phân loại đa lớp)
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><ol>
<li></li>
</ol></th>
<th><math><semantics><mrow><mi>L</mi><mspace></mspace><mo>=</mo><mspace></mspace><mo>−</mo><mspace></mspace><mi>Σ</mi><mspace></mspace><mi>y</mi><mi>ᵢ</mi><mspace></mspace><mi>l</mi><mi>o</mi><mi>g</mi><mrow><mo>(</mo><mi>ŷ</mi><mi>ᵢ</mi><mo>)</mo></mrow></mrow><annotation>L\  = \  - \ \Sigma\ yᵢ\ log(ŷᵢ)</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

#### Softmax Function: chuẩn hóa xác suất cho phân loại đa lớp
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><ol>
<li></li>
</ol></th>
<th><math><semantics><mrow><mi>σ</mi><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow><mi>_</mi><mi>j</mi><mspace></mspace><mo>=</mo><mspace></mspace><mi>e</mi><mover><mrow></mrow><mo>̂</mo></mover><mo>{</mo><mi>z</mi><mi>_</mi><mi>j</mi><mo>}</mo><mspace></mspace><mi>/</mi><mspace></mspace><mi>Σ</mi><mspace></mspace><mi>e</mi><mover><mrow></mrow><mo>̂</mo></mover><mo>{</mo><mi>z</mi><mi>_</mi><mi>k</mi><mo>}</mo></mrow><annotation>\sigma(z)\j\  = \ e\hat{}\{ z\j\}\ /\ \Sigma\ e\hat{}\{ z\k\}</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table>