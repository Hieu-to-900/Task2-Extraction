# Public_496

# GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG \- RL

Học tăng cường (Reinforcement Learning – RL) là một lĩnh vực quan trọng trong trí tuệ nhân tạo, tập trung vào việc huấn luyện một tác nhân (agent) học cách đưa ra chuỗi hành động trong môi trường để tối đa hóa phần thưởng tích lũy. RL được ứng dụng trong nhiều lĩnh vực: chơi game (AlphaGo, Dota2 AI), robot tự hành, tối ưu chuỗi sản xuất, tài chính, y học cá nhân hóa…

Khác với học có giám sát (supervised learning), RL không có nhãn cố định cho từng dữ liệu. Thay vào đó, agent phải khám phá (exploration) và khai thác (exploitation) thông tin trong môi trường để cải thiện chính sách hành động.

# MẠNG NƠ-RON NHÂN TẠO

## Yêu cầu trước khi làm thí nghiệm 
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><p>Yêu cầu trước khi thực hành:</p>
<ul>
<li><p>Kiến thức nền tảng: đại số tuyến tính, xác suất – thống kê, học
có giám sát.</p></li>
<li><p>Kỹ năng lập trình: Python, NumPy, hiểu cơ bản
TensorFlow/PyTorch.</p></li>
<li><p>Công cụ: Python 3.x, Jupyter Notebook, thư viện gym (OpenAI
Gym).</p></li>
<li><p>Dữ liệu / môi trường: sử dụng các môi trường RL chuẩn như
CartPole, MountainCar, Atari.</p></li>
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
<th><p>Mục đích của phần thí nghiệm:</p>
<ul>
<li><p>Hiểu rõ khái niệm Markov Decision Process (MDP).</p></li>
<li><p>Nắm được các hàm giá trị
<math><semantics><msup><mi>V</mi><mi>π</mi></msup><annotation>V^{\pi}</annotation></semantics></math>(s),
<math><semantics><msup><mi>Q</mi><mi>π</mi></msup><annotation>Q^{\pi}</annotation></semantics></math>(s,a)</p></li>
<li><p>Làm quen với các phương trình Bellman và ý nghĩa tối ưu.</p></li>
<li><p>Áp dụng các thuật toán Q-learning, SARSA, Policy Gradient,
Actor-Critic.</p></li>
<li><p>Biết các kỹ thuật regularization và exploration trong
RL.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Tóm tắt lý thuyết 

### Định nghĩa
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
<td><h5>Mô hình RL được mô tả dưới dạng Markov
Decision Process: tập trạng thái S, tập hành động A, xác suất chuyển
trạng thái P, phần thưởng R, hệ số chiết khấu γ.</h5></td>
<td><math><semantics><mrow><mi>M</mi><mi>D</mi><mi>P</mi><mo>=</mo><mrow><mo>(</mo><mi>S</mi><mo>,</mo><mi>A</mi><mo>,</mo><mi>P</mi><mo>,</mo><mi>R</mi><mo>,</mo><mi>γ</mi><mo>)</mo></mrow></mrow><annotation>MDP = (S,A,P,R,\gamma)</annotation></semantics></math></td>
</tr>
<tr>
<td><h5>Hàm giá trị trạng thái: kỳ vọng phần
thưởng tích lũy khi bắt đầu từ trạng thái sss và theo chính sách
π.</h5></td>
<td><math><semantics><mrow><msup><mi>V</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>E</mi><mi>π</mi></msub><mrow><mo>[</mo><munderover><mo>∑</mo><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow><mo>∞</mo></munderover><mrow><msup><mi>γ</mi><mi>t</mi></msup><msub><mi>R</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><mspace></mspace><mo>|</mo><mspace></mspace><msub><mi>S</mi><mn>0</mn></msub><mo>=</mo><mi>s</mi><mo>]</mo></mrow></mrow><annotation>V^{\pi}(s) = E_{\pi}\left\lbrack \sum_{t = 0}^{\infty}{\gamma^{t}R_{t + 1}}\, \middle| \, S_{0} = s \right\rbrack</annotation></semantics></math></td>
</tr>
<tr>
<td><h5>Hàm giá trị hành động: kỳ vọng phần
thưởng tích lũy khi bắt đầu từ trạng thái s, chọn hành động aaa và theo
chính sách π.</h5></td>
<td><math><semantics><mrow><msup><mi>Q</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>E</mi><mi>π</mi></msub><mrow><mo>[</mo><munderover><mo>∑</mo><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow><mo>∞</mo></munderover><mrow><msup><mi>γ</mi><mi>t</mi></msup><msub><mi>R</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><mspace></mspace><mo>|</mo><mspace></mspace><msub><mi>S</mi><mn>0</mn></msub><mo>=</mo><mi>s</mi><mo>,</mo><msub><mi>A</mi><mn>0</mn></msub><mo>=</mo><mi>a</mi><mo>]</mo></mrow></mrow><annotation>Q^{\pi}(s,a) = E_{\pi}\left\lbrack \sum_{t = 0}^{\infty}{\gamma^{t}R_{t + 1}}\, \middle| \, S_{0} = s,A_{0} = a \right\rbrack</annotation></semantics></math></td>
</tr>
</tbody>
</table> 

### Thuật toán RL
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Cập nhật Q-learning: học chính sách tối ưu bằng cách cập nhật giá
trị Q.</th>
<th><p><math><semantics><mrow><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>←</mo><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>+</mo><mi>α</mi><mrow><mo>[</mo><mi>r</mi><mo>+</mo><mi>γ</mi><munder><mo>max</mo><msup><mi>a</mi><mi>′</mi></msup></munder><mi>Q</mi><mrow><mo>(</mo><msup><mi>s</mi><mi>′</mi></msup><mo>,</mo><msup><mi>a</mi><mi>′</mi></msup><mo>)</mo></mrow><mo>−</mo><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>]</mo></mrow></mrow><annotation>Q(s,a) \leftarrow Q(s,a) + \alpha\left\lbrack r + \gamma\max_{a^{'}}Q\left( s^{'},a^{'} \right) - Q(s,a) \right\rbrack</annotation></semantics></math></p>
<p>|<image_1>|</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Cập nhật SARSA: học theo chính sách đang thực hiện, khác với
Q-learning<em>.</em></td>
<td><math><semantics><mrow><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>←</mo><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>+</mo><mi>α</mi><mrow><mo>[</mo><mi>r</mi><mo>+</mo><mi>γ</mi><mi>Q</mi><mrow><mo>(</mo><msup><mi>s</mi><mi>′</mi></msup><mo>,</mo><msup><mi>a</mi><mi>′</mi></msup><mo>)</mo></mrow><mo>−</mo><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>]</mo></mrow></mrow><annotation>Q(s,a) \leftarrow Q(s,a) + \alpha\left\lbrack r + \gamma Q\left( s^{'},a^{'} \right) - Q(s,a) \right\rbrack</annotation></semantics></math></td>
</tr>
<tr>
<td>Actor-Critic: sai số TD (Temporal Difference) để cập nhật
Critic.</td>
<td><math><semantics><mrow><mi>∇</mi><mi>J</mi><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>E</mi><mi>π</mi></msub><mrow><mo>[</mo><msub><mi>∇</mi><mi>θ</mi></msub><mo>log</mo><msub><mi>π</mi><mi>θ</mi></msub><mrow><mo>(</mo><mi>a</mi><mo>|</mo><mi>s</mi><mo>)</mo></mrow><mspace></mspace><msup><mi>Q</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>]</mo></mrow></mrow><annotation>\nabla J(\theta) = E_{\pi}\left\lbrack \nabla_{\theta}\log\pi_{\theta}\left( a \middle| s \right)\, Q^{\pi}(s,a) \right\rbrack</annotation></semantics></math></td>
</tr>
<tr>
<td>Hàm Advantage: đo lường mức độ tốt hơn trung bình của hành động a
tại trạng thái s.</td>
<td><math><semantics><mrow><msub><mi>δ</mi><mi>t</mi></msub><mo>=</mo><msub><mi>r</mi><mi>t</mi></msub><mo>+</mo><mi>γ</mi><mi>V</mi><mrow><mo>(</mo><msub><mi>s</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>)</mo></mrow><mo>−</mo><mi>V</mi><mrow><mo>(</mo><msub><mi>s</mi><mi>t</mi></msub><mo>)</mo></mrow></mrow><annotation>\delta_{t} = r_{t} + \gamma V\left( s_{t + 1} \right) - V\left( s_{t} \right)</annotation></semantics></math></td>
</tr>
</tbody>
</table> 

### REGULARIZATION & EXPLORATION

#### Entropy Regularization:
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
<th><p><math><semantics><mrow><mi>H</mi><mrow><mo>(</mo><mi>π</mi><mrow><mo>(</mo><mi>s</mi><mo>)</mo></mrow><mo>)</mo></mrow><mo>=</mo><mo>−</mo><munderover><mo>∑</mo><mi>a</mi><mrow></mrow></munderover><mrow><mi>π</mi><mrow><mo>(</mo><mi>a</mi><mo>|</mo><mi>s</mi><mo>)</mo></mrow><mo>log</mo><mi>π</mi><mrow><mo>(</mo><mi>a</mi><mo>|</mo><mi>s</mi><mo>)</mo></mrow></mrow></mrow><annotation>H\left( \pi(s) \right) = - \sum_{a}^{}{\pi\left( a \middle| s \right)\log\pi\left( a \middle| s \right)}</annotation></semantics></math></p>
<p>|<image_2>|</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

#### Epsilon-Greedy Policy

$$
\pi\left( a \middle| s \right) = \left( 1 - \epsilon + \backslash tfrac\epsilon|A| \right)1\left\lbrack a = \arg{\max_{a}Q}(s,a) \right\rbrack + \backslash tfrac\epsilon|A|
$$

#### Softmax Exploration:
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
<th><math><semantics><mrow><mi>π</mi><mrow><mo>(</mo><mi>a</mi><mo>|</mo><mi>s</mi><mo>)</mo></mrow><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mtext>/</mtext><mi>τ</mi></mrow></msup><mrow><munderover><mo>∑</mo><msup><mi>a</mi><mi>′</mi></msup><mrow></mrow></munderover><msup><mi>e</mi><mrow><mi>Q</mi><mrow><mo>(</mo><mi>s</mi><mo>,</mo><msup><mi>a</mi><mi>′</mi></msup><mo>)</mo></mrow><mtext>/</mtext><mi>τ</mi></mrow></msup></mrow></mfrac></mrow><annotation>\pi\left( a \middle| s \right) = \frac{e^{Q(s,a)\text{/}\tau}}{\sum_{a^{'}}^{}e^{Q\left( s,a^{'} \right)\text{/}\tau}}</annotation></semantics></math></th>
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

2.3.4. Phương pháp học nâng cao trong RL
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>hàm advantage: đo lường mức độ “tốt hơn trung bình” của hành động a
tại trạng thái s. được dùng trong actor-critic và policy gradient.</th>
<th><math><semantics><mrow><msup><mi>A</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>=</mo><msup><mi>Q</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>−</mo><msup><mi>V</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>)</mo></mrow></mrow><annotation>A^{\pi}(s,a) = Q^{\pi}(s,a) - V^{\pi}(s)</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
<tr>
<td>sai số td (temporal difference): dùng để cập nhật critic trong
actor-critic.</td>
<td><math><semantics><mrow><mi>∇</mi><mi>J</mi><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>E</mi><mrow><mi>s</mi><mo>,</mo><mi>a</mi><mo>∼</mo><msub><mi>π</mi><mi>θ</mi></msub></mrow></msub><mrow><mo>[</mo><msub><mi>∇</mi><mi>θ</mi></msub><mo>log</mo><msub><mi>π</mi><mi>θ</mi></msub><mrow><mo>(</mo><mi>a</mi><mo>|</mo><mi>s</mi><mo>)</mo></mrow><mspace></mspace><msup><mi>A</mi><mi>π</mi></msup><mrow><mo>(</mo><mi>s</mi><mo>,</mo><mi>a</mi><mo>)</mo></mrow><mo>]</mo></mrow></mrow><annotation>\nabla J(\theta) = E_{s,a \sim \pi_{\theta}}\left\lbrack \nabla_{\theta}\log\pi_{\theta}\left( a \middle| s \right)\, A^{\pi}(s,a) \right\rbrack</annotation></semantics></math></td>
</tr>
<tr>
<td>hàm mất mát trong proximal policy optimization (ppo): giới hạn cập
nhật chính sách để tránh bước nhảy quá lớn.</td>
<td><math><semantics><mrow><msup><mi>L</mi><mrow><mi>p</mi><mi>p</mi><mi>o</mi></mrow></msup><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>E</mi><mi>t</mi></msub><mrow><mo>[</mo><mo>min</mo><mtext>!</mtext><mrow><mo>(</mo><msub><mi>r</mi><mi>t</mi></msub><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><msub><mi>A</mi><mi>t</mi></msub><mo>,</mo><mspace></mspace><mtext>clip</mtext><mrow><mo>(</mo><msub><mi>r</mi><mi>t</mi></msub><mrow><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><mo>,</mo><mn>1</mn><mo>−</mo><mi>ϵ</mi><mo>,</mo><mn>1</mn><mo>+</mo><mi>ϵ</mi><mo>)</mo></mrow><msub><mi>A</mi><mi>t</mi></msub><mo>)</mo></mrow><mo>]</mo></mrow></mrow><annotation>L^{ppo}(\theta) = E_{t}\left\lbrack \min\text{!}\left( r_{t}(\theta)A_{t},\ \text{clip}\left( r_{t}(\theta),1 - \epsilon,1 + \epsilon \right)A_{t} \right) \right\rbrack</annotation></semantics></math></td>
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