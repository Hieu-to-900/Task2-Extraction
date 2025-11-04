# Public_477

# GIỚI THIỆU VỀ PYTHON

Python là ngôn ngữ lập trình mạnh mẽ, hỗ trợ nhiều thư viện khoa học như NumPy , Pandas , Matplotlib , SciPy. Trong lĩnh vực năng lượng tái tạo, Python được sử dụng để:

  * Mô phỏng sản lượng điện mặt trời theo dữ liệu bức xạ.

  * Tính toán hiệu suất hệ thống lưu trữ pin.

  * Phân tích dữ liệu vận hành và tối ưu hóa cấu hình hệ thống.


# HỆ THỐNG NĂNG LƯỢNG MẶT TRỜI Ở MIỀN THỜI GIAN (t)

## Yêu cầu trước khi làm thí nghiệm 
<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th><p>Nắm vững kiến thức về:</p>
<ul>
<li><p>Bức xạ mặt trời và các yếu tố ảnh hưởng.</p></li>
<li><p>Nguyên lý hoạt động của tấm pin quang điện (PV).</p></li>
<li><p>Cách tính dung lượng và hiệu suất pin lưu trữ.</p></li>
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
<th><p>Dùng Python mô phỏng các nội dung sau:</p>
<ul>
<li><p>Công suất phát của hệ thống PV theo giờ trong ngày.</p></li>
<li><p>Chu kỳ sạc/xả của pin lưu trữ.</p></li>
<li><p>Hiệu suất tổng thể của hệ thống PV + pin.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

## Tóm tắt lý thuyết 

### Mô hình nguồn pin mặt trời PV
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Pin mặt trời PV (Photovoltaic cell) gồm các lớp bán dẫn chịu tác
dụng của quang học để biến đổi các năng lượng phôton bức xạ mặt trời
thành năng lượng điện. Theo quan điểm năng lượng điện tử, pin mặt trời
có thể được coi là những nguồn dòng biểu diễn mối quan hệ phi tuyến
I-V.</th>
<th rowspan="2">|<image_1>|</th>
</tr>
<tr>
<th>Hiệu suất của tấm pin mặt trời sẽ lớn nhất khi pin mặt trời cung cấp
cho ta công suất cực đại. Theo đặc tính phi tuyến trên hình 2, nó sẽ xảy
ra khi P-V là cực đại, tức là P-V = Pmax tại thời điểm (Imax ,Vmax )
được gọi là điểm cực đại MPP (Maximum Point Power). Hệ bám điểm công
suất cực đại MPPT (Maximum Point Power Tracking) được sử dụng để đảm bảo
rằng pin mặt trời sẽ luôn luôn làm việc ở điểm MPP bất chấp tải được nối
vào pin.</th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

### Định nghĩa một số đại lượng cơ bản 
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Đại lượng</strong></th>
<th><strong>Ký hiệu</strong></th>
<th><strong>Công thức</strong></th>
<th><strong>Đơn vị</strong></th>
<th><strong>Ý nghĩa</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Bức xạ mặt trời</td>
<td><math><semantics><msub><mi>G</mi><mi>t</mi></msub><annotation>G_{t}</annotation></semantics></math></td>
<td></td>
<td>W/m²</td>
<td>Năng lượng bức xạ tới bề mặt tấm pin</td>
</tr>
<tr>
<td>Hiệu suất tấm pin</td>
<td><math><semantics><msub><mi>η</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><annotation>\eta_{pv}</annotation></semantics></math></td>
<td></td>
<td>%</td>
<td>Tỉ lệ chuyển đổi bức xạ thành điện năng</td>
</tr>
<tr>
<td>Công suất PV</td>
<td><math><semantics><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><annotation>P_{pv}</annotation></semantics></math></td>
<td><math><semantics><mrow><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mo>=</mo><msub><mi>G</mi><mi>t</mi></msub><mo>⋅</mo><mi>A</mi><mo>⋅</mo><msub><mi>η</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub></mrow><annotation>P_{pv} = G_{t} \cdot A \cdot \eta_{pv}</annotation></semantics></math></td>
<td>W</td>
<td>Công suất tức thời của hệ PV. Phụ thuộc vào bức xạ mặt trời, diện
tích tấm pin và hiệu suất tấm pin</td>
</tr>
<tr>
<td>Dung lượng pin</td>
<td><math><semantics><msub><mi>C</mi><mrow><mi>b</mi><mi>a</mi><mi>t</mi></mrow></msub><annotation>C_{bat}</annotation></semantics></math></td>
<td></td>
<td>kWh</td>
<td>Lượng điện năng pin có thể lưu trữ</td>
</tr>
<tr>
<td>Hiệu suất pin</td>
<td><math><semantics><msub><mi>η</mi><mrow><mi>b</mi><mi>a</mi><mi>t</mi></mrow></msub><annotation>\eta_{bat}</annotation></semantics></math></td>
<td></td>
<td>%</td>
<td>Tỉ lệ điện năng thu hồi so với khi sạc</td>
</tr>
</tbody>
</table> 

### 2.3.2 Một số công thức quan trọng 

#### 2.3.2.1 Công suất PV tức thời:
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
<th><math><semantics><mrow><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>G</mi><mi>t</mi></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>⋅</mo><mi>A</mi><mo>⋅</mo><msub><mi>η</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub></mrow><annotation>P_{pv}(t) = G_{t}(t) \cdot A \cdot \eta_{pv}</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

#### 2.3.2.2 Năng lượng PV trong một ngày:
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>[CT2]</th>
<th><math><semantics><mrow><mi>d</mi><mi>t</mi><msub><mi>E</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mo>=</mo><msubsup><mo>∫</mo><mn>0</mn><mn>24</mn></msubsup><mrow><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mspace></mspace><mi>d</mi><mi>t</mi></mrow><annotation>dtE_{pv} = \int_{0}^{24}{P_{pv}(t)}\, dt</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

#### 2.3.2.3 Trạng thái sạc pin (SOC):
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>[CT3]</th>
<th><math><semantics><mrow><mi>S</mi><mi>O</mi><mi>C</mi><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>=</mo><mi>S</mi><mi>O</mi><mi>C</mi><mrow><mo>(</mo><mi>t</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><mo>+</mo><mfrac><mrow><msub><mi>P</mi><mrow><mi>c</mi><mi>h</mi><mi>a</mi><mi>r</mi><mi>g</mi><mi>e</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>⋅</mo><msub><mi>η</mi><mrow><mi>b</mi><mi>a</mi><mi>t</mi></mrow></msub><mo>−</mo><msub><mi>P</mi><mrow><mi>d</mi><mi>i</mi><mi>s</mi><mi>c</mi><mi>h</mi><mi>a</mi><mi>r</mi><mi>g</mi><mi>e</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mtext>/</mtext><msub><mi>η</mi><mrow><mi>b</mi><mi>a</mi><mi>t</mi></mrow></msub></mrow><msub><mi>C</mi><mrow><mi>b</mi><mi>a</mi><mi>t</mi></mrow></msub></mfrac></mrow><annotation>SOC(t) = SOC(t - 1) + \frac{P_{charge}(t) \cdot \eta_{bat} - P_{discharge}(t)\text{/}\eta_{bat}}{C_{bat}}</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
</tbody>
</table> 

### 2.3.3 Một số định nghĩa khác 
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Cộng hai nguồn năng lượng:</th>
<th><p>Nếu có hai hệ PV độc lập:</p>
<p><math><semantics><mrow><msub><mi>P</mi><mrow><mi>t</mi><mi>o</mi><mi>t</mi><mi>a</mi><mi>l</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mspace></mspace><mo>=</mo><mspace></mspace><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi><mn>1</mn></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mspace></mspace><mo>+</mo><mspace></mspace><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi><mn>2</mn></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><annotation>P_{total}(t)\  = \ P_{pv1}(t)\  + \ P_{pv2}(t)</annotation></semantics></math></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Nhân với hằng số (tăng công suất):</td>
<td><math><semantics><mrow><msup><mi>P</mi><mi>′</mi></msup><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>=</mo><mi>k</mi><mo>⋅</mo><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><annotation>P^{'}(t) = k \cdot P_{pv}(t)</annotation></semantics></math></td>
</tr>
<tr>
<td>Dịch thời gian (mô phỏng múi giờ khác):</td>
<td><math><semantics><mrow><msup><mi>P</mi><mi>′</mi></msup><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mspace></mspace><mo>−</mo><mspace></mspace><mi>Δ</mi><mi>t</mi><mo>)</mo></mrow></mrow><annotation>P^{'}(t) = P_{pv}(t\  - \ \Delta t)</annotation></semantics></math></td>
</tr>
<tr>
<td>Đảo thời gian (mô phỏng ngược dữ liệu):</td>
<td><math><semantics><mrow><msup><mi>P</mi><mi>′</mi></msup><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow><mo>=</mo><msub><mi>P</mi><mrow><mi>p</mi><mi>v</mi></mrow></msub><mrow><mo>(</mo><mo>−</mo><mi>t</mi><mspace></mspace><mo>)</mo></mrow></mrow><annotation>P^{'}(t) = P_{pv}( - t\ )</annotation></semantics></math></td>
</tr>
<tr>
<td>Năng lượng lưu trữ:</td>
<td><math><semantics><mrow><msub><mi>E</mi><mrow><mi>s</mi><mi>t</mi><mi>o</mi><mi>r</mi><mi>e</mi><mi>d</mi></mrow></msub><mo>=</mo><munderover><mo>∑</mo><mi>t</mi><mrow></mrow></munderover><mrow><msub><mi>P</mi><mrow><mi>c</mi><mi>h</mi><mi>a</mi><mi>r</mi><mi>g</mi><mi>e</mi></mrow></msub><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow><mo>⋅</mo><msub><mi>η</mi><mrow><mi>b</mi><mi>a</mi><mi>t</mi></mrow></msub></mrow><annotation>E_{stored} = \sum_{t}^{}{P_{charge}(t)} \cdot \eta_{bat}</annotation></semantics></math></td>
</tr>
<tr>
<td>Công suất trung bình:</td>
<td><math><semantics><mrow><msub><mi>P</mi><mrow><mi>a</mi><mi>v</mi><mi>g</mi></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mi>T</mi></mfrac><munderover><mo>∑</mo><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow><mi>T</mi></munderover><mrow><mi>P</mi><mrow><mo>(</mo><mi>t</mi><mo>)</mo></mrow></mrow></mrow><annotation>P_{avg} = \frac{1}{T}\sum_{t = 1}^{T}{P(t)}</annotation></semantics></math></td>
</tr>
</tbody>
</table> 

### 2.3.4 Hệ thống PV + Pin

_Hệ thống bất biến theo thời gian:Nếu điều kiện bức xạ và nhiệt độ không đổi, công suất PV không đổi theo thời gian.

_Hệ thống nhân quả:Công suất tại thời điểm t chỉ phụ thuộc vào dữ liệu bức xạ và SOC trước đó.

_Hệ thống ổn định:SOC luôn nằm trong khoảng [0, 1].

Phương trình cân bằng năng lượng:

$$
P_{load}(t) = P_{pv}(t) + P_{discharge}(t) - P_{charge}(t)
$$

### 2.3.5 Bảng dữ liệu mô phỏng (ví dụ 1 ngày)
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th><strong>Giờ</strong></th>
<th><p><math><semantics><msub><mi>𝐆</mi><mi>𝐭</mi></msub><annotation>\mathbf{G}_{\mathbf{t}}</annotation></semantics></math></p>
<p><strong>(W/m²)</strong></p></th>
<th><p><math><semantics><msub><mi>𝐏</mi><mrow><mi>𝐩</mi><mi>𝐯</mi></mrow></msub><annotation>\mathbf{P}_{\mathbf{pv}}</annotation></semantics></math></p>
<p><strong>(kW)</strong></p></th>
<th><strong>SOC (%)</strong></th>
<th><math><semantics><mrow><msub><mi>𝐏</mi><mrow><mi>𝐜</mi><mi>𝐡</mi><mi>𝐚</mi><mi>𝐫</mi><mi>𝐠</mi><mi>𝐞</mi></mrow></msub><mrow><mo>(</mo><mrow><mi>𝐤</mi><mi>𝐖</mi></mrow><mo>)</mo></mrow></mrow><annotation>\mathbf{P}_{\mathbf{charge}}\left( \mathbf{kW} \right)</annotation></semantics></math></th>
<th><math><semantics><mrow><msub><mi>𝐏</mi><mrow><mi>𝐝</mi><mi>𝐢</mi><mi>𝐬</mi><mi>𝐜</mi><mi>𝐡</mi><mi>𝐚</mi><mi>𝐫</mi><mi>𝐠</mi><mi>𝐞</mi></mrow></msub><mrow><mo>(</mo><mrow><mi>𝐤</mi><mi>𝐖</mi></mrow><mo>)</mo></mrow></mrow><annotation>\mathbf{P}_{\mathbf{discharge}}\left( \mathbf{kW} \right)</annotation></semantics></math></th>
<th><math><semantics><mrow><msub><mi>𝐏</mi><mrow><mi>𝐥</mi><mi>𝐨</mi><mi>𝐚</mi><mi>𝐝</mi></mrow></msub><mrow><mo>(</mo><mrow><mi>𝐤</mi><mi>𝐖</mi></mrow><mo>)</mo></mrow></mrow><annotation>\mathbf{P}_{\mathbf{load}}\left( \mathbf{kW} \right)</annotation></semantics></math></th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0</td>
<td>0.00</td>
<td>65</td>
<td>0.00</td>
<td>0.50</td>
<td>0.50</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>0.00</td>
<td>62</td>
<td>0.00</td>
<td>0.45</td>
<td>0.45</td>
</tr>
<tr>
<td>2</td>
<td>0</td>
<td>0.00</td>
<td>60</td>
<td>0.00</td>
<td>0.40</td>
<td>0.40</td>
</tr>
<tr>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
</tr>
<tr>
<td>12</td>
<td>850</td>
<td>2.55</td>
<td>80</td>
<td>1.00</td>
<td>0.00</td>
<td>1.55</td>
</tr>
<tr>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
<td>...</td>
</tr>
<tr>
<td>23</td>
<td>0</td>
<td>0.00</td>
<td>68</td>
<td>0.00</td>
<td>0.55</td>
<td>0.55</td>
</tr>
</tbody>
</table>