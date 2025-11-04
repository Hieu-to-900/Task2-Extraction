# Public_481

# GIỚI THIỆU VỀ MẠNG NƠ-RON NHÂN TẠO

Mạng nơ-ron nhân tạo (Artificial Neural Networks – ANN) là nền tảng cốt lõi của trí tuệ nhân tạo hiện đại. Ý tưởng dựa trên cách bộ não sinh học xử lý thông tin thông qua các nơ-ron liên kết.

# MẠNG NƠ-RON NHÂN TẠO

## Yêu cầu trước khi làm thí nghiệm 
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th>Yêu cầu trước khi thực hàn</th>
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
<th><p>Mục đích của phần thí nghiệm:</p>
<ul>
<li><p>Hiểu nguyên lý hoạt động của ANN.</p></li>
<li><p>Làm quen với các công thức toán học mô tả quá trình huấn
luyện.</p></li>
<li><p>Ứng dụng ANN trong bài toán thực tế: phân loại, dự đoán, xử lý
ảnh, ngôn ngữ.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Tóm tắt lý thuyết 

### Nơ-ron nhân tạo
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
<td><h5>Nơ-ron nhân tạo thực hiện phép biến đổi
tuyến tính–tịnh tiến trên vector đặc trưng đầu vào, sau đó qua hàm kích
hoạt phi tuyến để tăng năng lực biểu diễn; bias giúp dịch chuyển biên
quyết định.</h5></td>
<td><p><math><semantics><mrow><mi>z</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mrow><msub><mi>w</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub></mrow><mo>+</mo><mi>b</mi></mrow><annotation>z = \sum_{i = 1}^{n}{w_{i}x_{i}} + b</annotation></semantics></math></p>
<p><math><semantics><mrow><mi>y</mi><mo>=</mo><mi>f</mi><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow></mrow><annotation>y = f(z)</annotation></semantics></math></p></td>
</tr>
<tr>
<td><h5>Sigmoid nén giá trị về (0,1), thường dùng
cho đầu ra nhị phân; nhưng dễ bão hòa gradient ở vùng biên.</h5></td>
<td><p><math><semantics><mrow><mi>σ</mi><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>z</mi></mrow></msup></mrow></mfrac></mrow><annotation>\sigma(z) = \frac{1}{1 + e^{- z}}</annotation></semantics></math></p>
<p>|<image_1>|</p></td>
</tr>
<tr>
<td><h5>Tanh là phiên bản tịnh tiến/scale của
Sigmoid, đầu ra (-1,1), trung bình bằng 0 giúp hội tụ tốt hơn trong một
số mạng</h5></td>
<td><math><semantics><mrow><mo>tanh</mo><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mi>z</mi></msup><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>z</mi></mrow></msup></mrow><mrow><msup><mi>e</mi><mi>z</mi></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>z</mi></mrow></msup></mrow></mfrac></mrow><annotation>\tanh(z) = \frac{e^{z} - e^{- z}}{e^{z} + e^{- z}}</annotation></semantics></math></td>
</tr>
<tr>
<td><h5>ReLU giữ thành phần dương, triệt tiêu âm,
giúp mạng sâu hội tụ nhanh; có biến thể Leaky ReLU khắc phục “neuron
chết”.</h5></td>
<td><math><semantics><mrow><mtext>ReLU</mtext><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow><mo>=</mo><mo>max</mo><mrow><mo>(</mo><mn>0</mn><mo>,</mo><mi>z</mi><mo>)</mo></mrow><mo>,</mo><mspace></mspace><mtext>LeakyReLU</mtext><mrow><mo>(</mo><mi>z</mi><mo>)</mo></mrow><mo>=</mo><mo>max</mo><mrow><mo>(</mo><mi>α</mi><mi>z</mi><mo>,</mo><mi>z</mi><mo>)</mo></mrow></mrow><annotation>\text{ReLU}(z) = \max(0,z),\quad\text{LeakyReLU}(z) = \max(\alpha z,z)</annotation></semantics></math></td>
</tr>
</tbody>
</table> 

### Mất mát và phân phối
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><em>Softmax</em> chuyển vector logit thành phân phối xác suất trên K
lớp; nhạy cảm với chênh lệch lớn giữa các logit.</th>
<th><math><semantics><mrow><mtext>softmax</mtext><mrow><mo>(</mo><msub><mi>z</mi><mi>i</mi></msub><mo>)</mo></mrow><mo>=</mo><mfrac><msup><mi>e</mi><msub><mi>z</mi><mi>i</mi></msub></msup><mrow><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>K</mi></munderover><msup><mi>e</mi><msub><mi>z</mi><mi>j</mi></msub></msup></mrow></mfrac></mrow><annotation>\text{softmax}\left( z_{i} \right) = \frac{e^{z_{i}}}{\sum_{j = 1}^{K}e^{z_{j}}}</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Cross-Entropy đa lớp</em> đo độ lệch giữa nhãn thật 1-hot và
phân phối dự đoán; kết hợp Softmax cho huấn luyện phân loại.</td>
<td><math><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>K</mi></munderover><msub><mi>y</mi><mi>i</mi></msub><mo>log</mo><mtext>!</mtext><mrow><mo>(</mo><mfrac><msup><mi>e</mi><msub><mi>z</mi><mi>i</mi></msub></msup><mrow><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>K</mi></munderover><msup><mi>e</mi><msub><mi>z</mi><mi>j</mi></msub></msup></mrow></mfrac><mo>)</mo></mrow></mrow><annotation>L = - \sum_{i = 1}^{K}y_{i}\log\text{!}\left( \frac{e^{z_{i}}}{\sum_{j = 1}^{K}e^{z_{j}}} \right)</annotation></semantics></math></td>
</tr>
<tr>
<td><em>Binary Cross-Entropy</em> dùng cho nhị phân/đa nhãn; khuyến nghị
dùng logit-stable triển khai để tránh tràn số.</td>
<td><p><math><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mfrac><mn>1</mn><mi>N</mi></mfrac><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><mrow><msup><mrow><mrow><mo>(</mo><msub><mi>y</mi><mi>i</mi></msub><mi>.</mi><mi>l</mi><mi>o</mi><mi>g</mi><mo>(</mo><mover><msub><mi>y</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>)</mo></mrow><mspace></mspace><mo>+</mo><mrow><mo>(</mo><mspace></mspace><mn>1</mn><mspace></mspace><mo>−</mo><mspace></mspace><msub><mi>y</mi><mi>i</mi></msub><mo>)</mo></mrow><mi>.</mi><mi>l</mi><mi>o</mi><mi>g</mi><mo>(</mo><mn>1</mn><mo>−</mo></mrow><mrow></mrow></msup><mover><msub><mi>y</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>)</mo></mrow></mrow><annotation>L = - \frac{1}{N}\sum_{i = 1}^{N}{{\left( y_{i}.log(\widehat{y_{i}} \right)\  + (\ 1\  - \ y_{i}).log(1 -}^{}\widehat{y_{i}})}</annotation></semantics></math></p>
<p>|<image_2>|</p></td>
</tr>
<tr>
<td><em>MSE</em> thường dùng cho hồi quy; nhạy cảm với ngoại lai do bình
phương sai số.</td>
<td><math><semantics><mrow><mi>L</mi><mo>=</mo><mfrac><mn>1</mn><mi>N</mi></mfrac><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><msup><mrow><mo>(</mo><msub><mi>y</mi><mi>i</mi></msub><mo>−</mo><mover><msub><mi>y</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>)</mo></mrow><mn>2</mn></msup></mrow><annotation>L = \frac{1}{N}\sum_{i = 1}^{N}\left( y_{i} - \widehat{y_{i}} \right)^{2}</annotation></semantics></math></td>
</tr>
<tr>
<td><em>Hinge loss</em> dùng trong SVM/NN phân biệt biên cứng; khuyến
khích lề phân tách lớn.</td>
<td><math><semantics><mrow><mi>L</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><mrow><mo>max</mo><mrow><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>−</mo><msub><mi>y</mi><mi>i</mi></msub><mover><msub><mi>y</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>)</mo></mrow></mrow></mrow><annotation>L = \sum_{i = 1}^{N}{\max\left( 0,1 - y_{i}\widehat{y_{i}} \right)}</annotation></semantics></math></td>
</tr>
</tbody>
</table> 

### Tối ưu hoá 

#### Gradient Descent/SGD
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
<th><math><semantics><mrow><msub><mi>θ</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>θ</mi><mi>t</mi></msub><mo>−</mo><mi>η</mi><msub><mi>∇</mi><mi>θ</mi></msub><mi>L</mi><mrow><mo>(</mo><msub><mi>θ</mi><mi>t</mi></msub><mo>)</mo></mrow></mrow><annotation>\theta_{t + 1} = \theta_{t} - \eta\nabla_{\theta}L\left( \theta_{t} \right)</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

#### Gradient Descent/SGD

$$
v_{t} = \mu v_{t - 1} + \eta\nabla_{\theta}L_{t},\,\,\theta_{t + 1} = \theta_{t} - v_{t}
$$

#### Adam
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
<th><math><semantics><mrow><msub><mi>m</mi><mi>t</mi></msub><mo>=</mo><msub><mi>β</mi><mn>1</mn></msub><msub><mi>m</mi><mrow><mi>t</mi><mo>−</mo><mn>1</mn></mrow></msub><mo>+</mo><mrow><mo>(</mo><mn>1</mn><mo>−</mo><msub><mi>β</mi><mn>1</mn></msub><mo>)</mo></mrow><msub><mi>g</mi><mi>t</mi></msub><mo>,</mo><mspace></mspace><msub><mi>v</mi><mi>t</mi></msub><mo>=</mo><msub><mi>β</mi><mn>2</mn></msub><msub><mi>v</mi><mrow><mi>t</mi><mo>−</mo><mn>1</mn></mrow></msub><mo>+</mo><mrow><mo>(</mo><mn>1</mn><mo>−</mo><msub><mi>β</mi><mn>2</mn></msub><mo>)</mo></mrow><msubsup><mi>g</mi><mi>t</mi><mn>2</mn></msubsup><mo>,</mo><mspace></mspace><mover><msub><mi>m</mi><mi>t</mi></msub><mo>̂</mo></mover><mo>=</mo><mfrac><msub><mi>m</mi><mi>t</mi></msub><mrow><mn>1</mn><mo>−</mo><msubsup><mi>β</mi><mn>1</mn><mi>t</mi></msubsup></mrow></mfrac><mo>,</mo><mspace></mspace><mover><msub><mi>v</mi><mi>t</mi></msub><mo>̂</mo></mover><mo>=</mo><mfrac><msub><mi>v</mi><mi>t</mi></msub><mrow><mn>1</mn><mo>−</mo><msubsup><mi>β</mi><mn>2</mn><mi>t</mi></msubsup></mrow></mfrac><mo>,</mo><mspace></mspace><msub><mi>θ</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>θ</mi><mi>t</mi></msub><mo>−</mo><mi>η</mi><mfrac><mover><msub><mi>m</mi><mi>t</mi></msub><mo>̂</mo></mover><mrow><msqrt><mover><msub><mi>v</mi><mi>t</mi></msub><mo>̂</mo></mover></msqrt><mo>+</mo><mi>ϵ</mi></mrow></mfrac></mrow><annotation>m_{t} = \beta_{1}m_{t - 1} + \left( 1 - \beta_{1} \right)g_{t},\, v_{t} = \beta_{2}v_{t - 1} + \left( 1 - \beta_{2} \right)g_{t}^{2},\,\widehat{m_{t}} = \frac{m_{t}}{1 - \beta_{1}^{t}},\,\widehat{v_{t}} = \frac{v_{t}}{1 - \beta_{2}^{t}},\,\theta_{t + 1} = \theta_{t} - \eta\frac{\widehat{m_{t}}}{\sqrt{\widehat{v_{t}}} + \epsilon}</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

#### Weight Decay (L2)
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
<th><math><semantics><mrow><msub><mi>θ</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mrow><mo>(</mo><mn>1</mn><mo>−</mo><mi>η</mi><mi>λ</mi><mo>)</mo></mrow><msub><mi>θ</mi><mi>t</mi></msub><mo>−</mo><mi>η</mi><msub><mi>∇</mi><mi>θ</mi></msub><mi>L</mi><mrow><mo>(</mo><msub><mi>θ</mi><mi>t</mi></msub><mo>)</mo></mrow></mrow><annotation>\theta_{t + 1} = (1 - \eta\lambda)\theta_{t} - \eta\nabla_{\theta}L\left( \theta_{t} \right)</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

2.3.4. Regularization & Normalization
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>L1/L2 Regularization lần lượt khuyến khích thưa (sparsity) và nhỏ
hoá tham số; tác động khác nhau lên giải pháp tối ưu.</th>
<th><math><semantics><mrow><msub><mi>Ω</mi><mrow><mi>L</mi><mn>1</mn></mrow></msub><mo>=</mo><mi>λ</mi><munderover><mo>∑</mo><mi>i</mi><mrow></mrow></munderover><mrow><mo>|</mo><msub><mi>w</mi><mi>i</mi></msub><mo>|</mo></mrow><mo>,</mo><mspace></mspace><mspace></mspace><msub><mi>Ω</mi><mrow><mi>L</mi><mn>2</mn></mrow></msub><mo>=</mo><mi>λ</mi><munderover><mo>∑</mo><mi>i</mi><mrow></mrow></munderover><msubsup><mi>w</mi><mi>i</mi><mn>2</mn></msubsup></mrow><annotation>\Omega_{L1} = \lambda\sum_{i}^{}\left| w_{i} \right|,\,\,\Omega_{L2} = \lambda\sum_{i}^{}w_{i}^{2}</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
<tr>
<td>Dropout vô hiệu ngẫu nhiên đơn vị trong huấn luyện để phá đồng thích
nghi; scale ở suy luận để bảo toàn kỳ vọng.</td>
<td><math><semantics><mrow><mover><msub><mi>h</mi><mi>i</mi></msub><mo>̃</mo></mover><mo>=</mo><msub><mi>h</mi><mi>i</mi></msub><mo>⋅</mo><msub><mi>d</mi><mi>i</mi></msub><mo>,</mo><mspace></mspace><mspace></mspace><mover><msub><mi>h</mi><mi>i</mi></msub><mo>̃</mo></mover><mo>∼</mo><mtext>Bernoulli</mtext><mi>p</mi></mrow><annotation>\widetilde{h_{i}} = h_{i} \cdot d_{i},\,\,\widetilde{h_{i}} \sim \text{Bernoulli}p</annotation></semantics></math></td>
</tr>
<tr>
<td>BatchNorm (train) chuẩn hoá theo mini-batch rồi affine transform với
(γ,β); cải thiện ổn định và tốc độ học.tránh tràn số.</td>
<td><math><semantics><mrow><msub><mi>μ</mi><mi>B</mi></msub><mo>=</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><munderover><mo>∑</mo><mi>i</mi><mrow></mrow></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>,</mo><mspace></mspace><msubsup><mi>σ</mi><mi>B</mi><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><munderover><mo>∑</mo><mi>i</mi><mrow></mrow></munderover><msup><mrow><mo>(</mo><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><msub><mi>μ</mi><mi>B</mi></msub><mo>)</mo></mrow><mn>2</mn></msup><mo>,</mo><mspace></mspace><mover><msub><mi>x</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><msub><mi>μ</mi><mi>B</mi></msub></mrow><msqrt><mrow><msubsup><mi>σ</mi><mi>B</mi><mn>2</mn></msubsup><mo>+</mo><mi>ϵ</mi></mrow></msqrt></mfrac><mo>,</mo><mspace></mspace><mspace></mspace><mover><msub><mi>x</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>=</mo><mi>γ</mi><mover><msub><mi>x</mi><mi>i</mi></msub><mo>̂</mo></mover></mrow><annotation>\mu_{B} = \frac{1}{m}\sum_{i}^{}x_{i},\,\sigma_{B}^{2} = \frac{1}{m}\sum_{i}^{}\left( x_{i} - \mu_{B} \right)^{2},\,\widehat{x_{i}} = \frac{x_{i} - \mu_{B}}{\sqrt{\sigma_{B}^{2} + \epsilon}},\,\,\widehat{x_{i}} = \gamma\widehat{x_{i}}</annotation></semantics></math></td>
</tr>
<tr>
<td><em>MSE</em> thường dùng cho hồi quy; nhạy cảm với ngoại lai do bình
phương sai số.</td>
<td><math><semantics><mrow><mi>L</mi><mo>=</mo><mfrac><mn>1</mn><mi>N</mi></mfrac><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><msup><mrow><mo>(</mo><msub><mi>y</mi><mi>i</mi></msub><mo>−</mo><mover><msub><mi>y</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>)</mo></mrow><mn>2</mn></msup></mrow><annotation>L = \frac{1}{N}\sum_{i = 1}^{N}\left( y_{i} - \widehat{y_{i}} \right)^{2}</annotation></semantics></math></td>
</tr>
<tr>
<td><em>Hinge loss</em> dùng trong SVM/NN phân biệt biên cứng; khuyến
khích lề phân tách lớn.</td>
<td><math><semantics><mrow><mi>L</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><mrow><mo>max</mo><mrow><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>−</mo><msub><mi>y</mi><mi>i</mi></msub><mover><msub><mi>y</mi><mi>i</mi></msub><mo>̂</mo></mover><mo>)</mo></mrow></mrow></mrow><annotation>L = \sum_{i = 1}^{N}{\max\left( 0,1 - y_{i}\widehat{y_{i}} \right)}</annotation></semantics></math></td>
</tr>
</tbody>
</table>