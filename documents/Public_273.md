# Public_273

Trong phần này, bạn sẽ học cách đọc Wireshark TCP/HTTP log cho lưu lượng mạng giữa khách truy cập website nội bộ và web server của công ty. Hầu hết các công cụ phân tích network protocol/traffic analyzer dùng để bắt gói tin đều cung cấp thông tin tương tự.

# Số thứ tự log và thời gian
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>No.</strong></td>
<td><strong>Time</strong></td>
</tr>
<tr>
<td>47</td>
<td>3.144521</td>
</tr>
<tr>
<td>48</td>
<td>3.195755</td>
</tr>
<tr>
<td>49</td>
<td>3.246989</td>
</tr>
</tbody>
</table> 

Phần log của Wireshark TCP này bắt đầu tại log số 47, tức là sau 3.144521 giây kể từ khi công cụ ghi nhận bắt đầu hoạt động. Điều này cho thấy có khoảng 47 thông điệp được gửi và nhận bởi web server trong 3.1 giây đầu. Tốc độ này diễn ra rất nhanh nên công cụ phải đo bằng milliseconds.

# Địa chỉ IP nguồn và đích
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Source</strong></td>
<td><strong>Destination</strong></td>
</tr>
<tr>
<td><mark>198.51.100.23</mark></td>
<td><mark>192.0.2.1</mark></td>
</tr>
<tr>
<td><mark>192.0.2.1</mark></td>
<td><mark>198.51.100.23</mark></td>
</tr>
<tr>
<td><mark>198.51.100.23</mark></td>
<td><mark>192.0.2.1</mark></td>
</tr>
</tbody>
</table> 

Cột Source và Destination thể hiện địa chỉ IP nguồn gửi gói tin và địa chỉ IP đích nhận gói tin. Trong file log này, 192.0.2.1 là web server của công ty, còn dải 198.51.100.0/24 thuộc về máy tính nhân viên.

# Loại protocol và thông tin liên quan
<table>
<colgroup>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>Protocol</strong></td>
<td><strong>Info</strong></td>
</tr>
<tr>
<td>TCP</td>
<td>42584-&gt;443 [SYN] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>TCP</td>
<td>443-&gt;42584 [SYN, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>TCP</td>
<td>42584-&gt;443 [ACK] Seq=1 Win-5792 Len=120...</td>
</tr>
</tbody>
</table> 

  * Cột Protocol cho biết các gói tin đang được gửi bằng TCP protocol (thuộc transport layer trong mô hình TCP/IP ). Sau khi kết nối thành công, protocol sẽ chuyển sang HTTP (application layer).

  * Cột Info liệt kê port nguồn và port đích. Ở đây port 443 là của web server, thường dùng cho web traffic mã hóa.


Ba bước bắt tay TCP (three-way handshake):

  * [SYN] : Máy nhân viên gửi yêu cầu kết nối đến web server.

  * [SYN, ACK] : Web server phản hồi chấp nhận yêu cầu và dự trữ tài nguyên.

  * [ACK] : Máy nhân viên xác nhận, hoàn tất kết nối TCP.


# Lưu lượng website bình thường

Ví dụ một giao dịch bình thường
<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr>
<td><strong>No.</strong></td>
<td><strong>Time</strong></td>
<td><strong>Source</strong></td>
<td><strong>Destination</strong></td>
<td><strong>Protocol</strong></td>
<td><strong>Info</strong></td>
</tr>
<tr>
<td>47</td>
<td>3.144521</td>
<td>198.51.100.23</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>42584-&gt;443 [SYN] Seq=0 Win=5792 Len=120...</td>
</tr>
<tr>
<td>48</td>
<td>3.195755</td>
<td>192.0.2.1</td>
<td>198.51.100.23</td>
<td>TCP</td>
<td>443-&gt;42584 [SYN, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>49</td>
<td>3.246989</td>
<td>198.51.100.23</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>42584-&gt;443 [ACK] Seq=1 Win-5792 Len=120...</td>
</tr>
<tr>
<td>50</td>
<td>3.298223</td>
<td>198.51.100.23</td>
<td>192.0.2.1</td>
<td>HTTP</td>
<td>GET /sales.html HTTP/1.1</td>
</tr>
<tr>
<td>51</td>
<td>3.349457</td>
<td>192.0.2.1</td>
<td>198.51.100.23</td>
<td>HTTP</td>
<td>HTTP/1.1 200 OK (text/html)</td>
</tr>
</tbody>
</table> 

# Cuộc tấn công

Kẻ tấn công có thể lợi dụng TCP bằng cách gửi SYN flood (rất nhiều gói SYN) khiến web server không còn tài nguyên để phản hồi. Đây là DoS attack (tấn công từ chối dịch vụ) ở mức network layer.

  * Nếu từ một nguồn duy nhất: DoS direct attack.

  * Nếu từ nhiều nguồn: DDoS attack , khó phát hiện hơn.


|<image_1>|

TCP log đánh dấu màu

Trong log có hai tab:

  * Một tab bình thường.

  * Một tab Color coded TCP log : hiển thị tương tác giữa server và IP attacker 203.0.113.0 (đánh dấu màu đỏ).
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
<tbody>
<tr>
<td><strong>Color as text</strong></td>
<td><strong>No.</strong></td>
<td><strong>Time</strong></td>
<td><strong>Source<br/>
(x= redacted)</strong></td>
<td><strong>Destination<br/>
(x = redacted)</strong></td>
<td><strong>Protocol</strong></td>
<td><strong>Info</strong></td>
</tr>
<tr>
<td>red</td>
<td>52</td>
<td>3.390692</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>53</td>
<td>3.441926</td>
<td>192.0.2.1</td>
<td>203.0.113.0</td>
<td>TCP</td>
<td>443-&gt;54770 [SYN, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>54</td>
<td>3.493160</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [ACK Seq=1 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>55</td>
<td>3.544394</td>
<td>198.51.100.14</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>14785-&gt;443 [SYN] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>green</td>
<td>56</td>
<td>3.599628</td>
<td>192.0.2.1</td>
<td>198.51.100.14</td>
<td>TCP</td>
<td>443-&gt;14785 [SYN, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>57</td>
<td>3.664863</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>58</td>
<td>3.730097</td>
<td>198.51.100.14</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>14785-&gt;443 [ACK] Seq=1 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>59</td>
<td>3.795332</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>green</td>
<td>60</td>
<td>3.860567</td>
<td>198.51.100.14</td>
<td>192.0.2.1</td>
<td>HTTP</td>
<td>GET /sales.html HTTP/1.1</td>
</tr>
<tr>
<td>red</td>
<td>61</td>
<td>3.939499</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>green</td>
<td>62</td>
<td>4.018431</td>
<td>192.0.2.1</td>
<td>198.51.100.14</td>
<td>HTTP</td>
<td>HTTP/1.1 200 OK (text/html)</td>
</tr>
</tbody>
</table> 
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
<tbody>
<tr>
<td><strong>Color as text</strong></td>
<td><strong>No.</strong></td>
<td><strong>Time</strong></td>
<td><strong>Source</strong></td>
<td><strong>Destination</strong></td>
<td><strong>Protocol</strong></td>
<td><strong>Info</strong></td>
</tr>
<tr>
<td>green</td>
<td>63</td>
<td>4.097363</td>
<td>198.51.100.5</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>33638-&gt;443 [SYN] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>64</td>
<td>4.176295</td>
<td>192.0.2.1</td>
<td>203.0.113.0</td>
<td>TCP</td>
<td>443-&gt;54770 [SYN, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>green</td>
<td>65</td>
<td>4.255227</td>
<td>192.0.2.1</td>
<td>198.51.100.5</td>
<td>TCP</td>
<td>443-&gt;33638 [SYN, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>66</td>
<td>4.256159</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>67</td>
<td>5.235091</td>
<td>198.51.100.5</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>33638-&gt;443 [ACK] Seq=1 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>68</td>
<td>5.236023</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>69</td>
<td>5.236955</td>
<td>198.51.100.16</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>32641-&gt;443 [SYN] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>70</td>
<td>5.237887</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>71</td>
<td>6.228728</td>
<td>198.51.100.5</td>
<td>192.0.2.1</td>
<td>HTTP</td>
<td>GET /sales.html HTTP/1.1</td>
</tr>
<tr>
<td>red</td>
<td>72</td>
<td>6.229638</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>yellow</td>
<td>73</td>
<td>6.230548</td>
<td>192.0.2.1</td>
<td>198.51.100.16</td>
<td>TCP</td>
<td>443-&gt;32641 [RST, ACK] Seq=0 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>74</td>
<td>6.330539</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>75</td>
<td>6.330885</td>
<td>198.51.100.7</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>42584-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>76</td>
<td>6.331231</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>yellow</td>
<td>77</td>
<td>7.330577</td>
<td>192.0.2.1</td>
<td>198.51.100.5</td>
<td>TCP</td>
<td>HTTP/1.1 504 Gateway Time-out (text/html)</td>
</tr>
<tr>
<td>red</td>
<td>78</td>
<td>7.331323</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>green</td>
<td>79</td>
<td>7.340768</td>
<td>198.51.100.22</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>6345-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>yellow</td>
<td>80</td>
<td>7.340773</td>
<td>192.0.2.1</td>
<td>198.51.100.7</td>
<td>TCP</td>
<td>443-&gt;42584 [RST, ACK] Seq=1 Win-5792 Len=120...</td>
</tr>
<tr>
<td>red</td>
<td>81</td>
<td>7.340778</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>82</td>
<td>7.340783</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>83</td>
<td>7.439658</td>
<td>192.0.2.1</td>
<td>203.0.113.0</td>
<td>TCP</td>
<td>443-&gt;54770 [RST, ACK] Seq=1 Win=5792 Len=0...</td>
</tr>
</tbody>
</table> 
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
<tbody>
<tr>
<td><p><strong>Color</strong></p>
<p><strong>as text</strong></p></td>
<td><strong>No.</strong></td>
<td><strong>Time</strong></td>
<td><p><strong>Source</strong></p>
<p><strong>(x = redacted)</strong></p></td>
<td><p><strong>Destination</strong></p>
<p><strong>(x = redacted)</strong></p></td>
<td><strong>Protocol</strong></td>
<td><strong>Info</strong></td>
</tr>
<tr>
<td>red</td>
<td>119</td>
<td>19.198705</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>120</td>
<td>19.521718</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>yellow</td>
<td>121</td>
<td>19.844731</td>
<td>192.0.2.1</td>
<td>198.51.100.9</td>
<td>TCP</td>
<td>443-&gt;4631 [RST, ACK] Seq=1 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>122</td>
<td>20.167744</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>123</td>
<td>20.490757</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>124</td>
<td>20.81377</td>
<td>192.0.2.1</td>
<td>203.0.113.0</td>
<td>TCP</td>
<td>443-&gt;54770 [RST, ACK] Seq=1 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>125</td>
<td>21.136783</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>126</td>
<td>21.459796</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>127</td>
<td>21.782809</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>128</td>
<td>22.105822</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>129</td>
<td>22.428835</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>130</td>
<td>22.751848</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>131</td>
<td>23.074861</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>132</td>
<td>23.397874</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>133</td>
<td>23.720887</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>134</td>
<td>24.0439</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>135</td>
<td>24.366913</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>136</td>
<td>24.689926</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>137</td>
<td>25.012939</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>138</td>
<td>25.335952</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>139</td>
<td>25.658965</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>140</td>
<td>25.981978</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>141</td>
<td>26.304991</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>142</td>
<td>26.628004</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>143</td>
<td>26.951017</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>144</td>
<td>27.27403</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>145</td>
<td>27.597043</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>146</td>
<td>27.920056</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>147</td>
<td>28.243069</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>148</td>
<td>28.566082</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>149</td>
<td>28.889095</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>150</td>
<td>29.212108</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>151</td>
<td>29.535121</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
<tr>
<td>red</td>
<td>152</td>
<td>29.858134</td>
<td>203.0.113.0</td>
<td>192.0.2.1</td>
<td>TCP</td>
<td>54770-&gt;443 [SYN] Seq=0 Win=5792 Len=0...</td>
</tr>
</tbody>
</table> 

Từ log số 125 trở đi, web server không còn phản hồi traffic hợp lệ nữa, chỉ ghi nhận các gói SYN từ attacker. Vì chỉ có một IP tấn công, đây là direct DoS SYN flood attack.