# Public_056

Như đã trình bày trong Chương 1, một kiểu dữ liệu trừu tượng (ADTs) được xác định khi ta xây dựng đầy đủ hai phần: cấu trúc dữ liệu cùng các phép toán trên cấu trúc dữ liệu đó. Nội dung của chương này trình bày ba kiểu dữ liệu trừu tượng quan trọng đó là danh sách liên kết, ngăn xếp và hàng đợi. Mỗi kiểu dữ liệu trừu tượng được xây dựng giải quyết lớp các vấn đề cụ thể của khoa học máy tính. Đối với người học, mỗi cấu trúc dữ liệu trừu tượng cần làm chủ được bốn điểm quan trọng sau:

  * Định nghĩa cấu trúc dữ liệu ADTs.

  * Biểu diễn cấu trúc dữ liệu ADTs.

  * Thao tác (phép toán) trên cấu trúc dữ liệu ADTs.

  * Ứng dụng của cấu trúc dữ liệu ADTs.


# Danh sách liên kết đơn (Single Linked List)

Như ta đã biết mảng (array) là tập có thứ tự các phần tử có cùng chung một kiểu dữ liệu và được tổ chức liên tục nhau trong bộ nhớ. Ưu điểm lớn nhất của mảng là đơn giản và xử lý nhanh nhờ cơ chế truy cập phần tử trực tiếp vào các phần tử của mảng. Hạn chế lớn nhất của mảng là số lượng phần tử không thay đổi gây nên hiện tượng thừa bộ nhớ trong một số trường hợp và thiếu bộ nhớ trong một số trường hợp khác. Đối với một số bài toán có dữ liệu lớn, nhiều khi ta không đủ không gian nhớ tự do liên tục để cấp phát cho mảng. Để khắc phục hạn chế này ta có thể xây dựng kiểu dữ liệu danh sách liên kết đơn được định nghĩa, biểu diễn và thao tác như dưới đây.

## Định nghĩa danh sách liên kết đơn

Tập hợp các node thông tin được tổ chức rời rạc trong bộ nhớ. Trong đó, mỗi node gồm có hai thành phần:

  * Thành phần dữ liệu (data): dùng để lưu trữ thông tin của node.

  * Thành phần con trỏ (pointer): dùng để liên kết với node dữ liệu tiếp theo.


## Biểu diễn danh sách liên kết đơn

Để biểu diễn danh sách liên kết đơn ta sử dụng phương pháp định nghĩa cấu trúc tự trỏ của các ngôn ngữ lập trình. Giả sử thành phần thông tin của mỗi node được định nghĩa như một cấu trúc Item như sau:

struct Item {
<Kiểu 1> <Thành viên 1>;
<Kiểu 2> <Thành viên 2>;
……………………………;
<Kiểu N> <Thành viên N>;
};
Khi đó, danh sách liên kết đơn được định nghĩa như sau: struct node {
Item infor; //Thành phần thông tin của node;_
struct node *next; //thành phần con trỏ của node_
} *Start; //Start là một danh sách liên kết đơn_

|<image_1>|

Hình 3.1. Biểu diễn danh sách liên kết đơn

## Thao tác trên danh sách liên kết đơn

Các thao tác trên danh sách liên kết đơn bao gồm:

  * Tạo node rời rạc có giá trị value cho danh sách liên kết đơn

  * Thêm một node vào đầu danh sách liên kết đơn.

  * Thêm một node vào cuối danh sách liên kết đơn.

  * Thêm node vào vị trí xác định trong danh sách liên kết đơn.

  * Loại node trong sách liên kết đơn.

  * Tìm node trong sách liên kết đơn.

  * Sắp xếp node trong danh sách liên kết đơn.

  * Sửa đổi nội dung node trong sách liên kết đơn.

  * Đảo ngược các node trong danh sách liên kết đơn.

  * Duyệt các node của danh sách liên kết đơn.


Để đơn giản, ta xem thành phần thông tin của node (Item) là một số nguyên. Khi đó, các thao tác trên danh sách liên kết đơn ta định nghĩa một lớp các thao tác như sau:

struct node { //biểu diễn node_
int info; //thành phần thông tin của node_
struct node *next; //thành phần con trỏ của node_
}*start; //danh sách liên kết đơn: *start._
class single_linked_list { //biểu diễn lớp danh sách liên kết đơn_
public:
node* create_node(int);//Tạo một node cho danh sách liên kết đơn_
void insert_begin(); //thêm node vào đầu DSLKĐ_
void insert_pos(); //thêm node tại vị trí cụ thể trên DSLKĐ_
void insert_last(); //thêm node vào cuối DSLKĐ_
void delete_pos(); //loại node tại vị trí cho trước trên DSLKĐ_
void sort(); //sắp xếp nội dung các node theo thứ tự tăng dần_
void search(); //tìm kiếm node trên DSLKĐ_
void update(); //sửa đổi thông tin của node trên DSLKĐ_
void reverse(); //đảo ngược danh sách liên kết đơn_
void display(); //hiển thị nội dung DSLKĐ_
single_linked_list(){//constructor của lớp single linked list_. start = NULL;//chú ý start là biến toàn cục_
}
};

Thao tác:tạo một node rời rạc có giá trị value cho DSLKĐ.

node *single_linked_list::create_node(int value){
struct node *temp; //khai báo hai con trỏ node *temptemp = new(struct node); //cấp phát miền nhớ cho tempif (temp == NULL){ //nếu không đủ không gian nhớ_
cout<<“không đủ bộ nhớ để cấp phát"<<endl; return 0;
else {
temp->info = value;//thiết lập thông tin cho node temp_
temp->next = NULL; //thiết lập liên kết cho node temp_
return temp;//trả lại node temp đã được thiết lập_
}

}

Thao tác:thêm node vào đầu DSLKĐ_.

void single_linked_list::insert_begin(){ //chèn node vào đầu DSLKĐ_
int value; cout<<“Nhập giá trị node:"; cin>>value; //giá trị node cần chèn_
struct node *temp, *p; //sử dụng hai con trỏ temp và p_
temp = create_node(value);//tạo một node rời rạc có giá trị value_
if (start == NULL){ //nếu danh sách liên kết rỗng_
start = temp; //danh sách liên kết chính là node temp_
start->next = NULL; //không có liêt kết với node khác_
}
else { //nếu danh sách không rỗng_
p = start; //p trỏ đến node đầu của start_
start = temp; //node temp trở thành node đầu tiên của start_
start->next = p;//các node còn lại chính là p_
}
}

Hình 3.2. dưới đây mô tả phép thêm node vào đầu danh sách liên kết đơn.

|<image_2>|

Hình 3.2. Thêm node vào đầu danh sách liên kết đơn

Thao tác thêm node vào cuối danh sách liên kết đơn :

void single_linked_list::insert_last() { //thêm node vào cuối DSLKĐ_

int value;
cout<<“Nhập giá trị cho node: ";cin>>value; //nhập giá trị node_
struct node *temp, *s; //sử dung hai con trỏ temp và s_
temp = create_node(value);//tạo node rời rạc có giá trị value_
if(start==NULL) {//trường hợp DSLKĐ rỗng_
start = temp;
temp->next=NULL;
}
s = start; //s trỏ đến node đầu danh sách_
while (s->next != NULL){ //di chuyển s đến node cuối cùng_
s = s->next;
}
temp->next = NULL; //temp không chỏ đi đâu nữas->next = temp; //thiết lập liên kết cho scout<<“Hoàn thành thêm node vào cuối"<<endl;

}

|<image_3>|

Hình 3.3. Thêm node vào cuối danh sách liên kết đơn

Thao tác thêm node vào vị trí pos của danh sách liên kết đơn :

void single_linked_list::insert_pos() { //thêm node vào vị trí pos_

int value, pos, counter = 0; cout<<"Nhap gia tri node:";cin>>value; struct node *temp, *s, *ptr; //sử dụng ba con trỏ node_
temp = create_node(value);//tạo node rời rạc có giá trị value_
cout<<“Nhập vị trí node cần thêm: ";cin>>pos; int i; s = start; //s trỏ đến node đầu tiên_
while (s != NULL){ //đếm số node của DSLKĐ_
s = s->next; counter++;

}

if (counter==0) {//trường hợp DSLK đơn rỗng_
cout<<”Danh sách rỗng”; return;
}
if (pos == 1){ //nếu pos là vị trí đầu tiên_

if (start == NULL){ //trường hợp DSLKĐ rỗng_

start = temp; start->next = NULL;

}
else { //thêm node temp vào đầu DSLKĐ_
ptr = start; start = temp; start->next = ptr;
}
}
else if (pos > 1 && pos <= counter){ //trường hợp pos hợp lệ_
s = start; //s trỏ đến node đầu tiên_
for (i = 1; i < pos; i++){ //di chuyển đến node pos-1_
ptr = s; s = s->next;
}
ptr->next = temp; temp->next = s; //thiết lập liên kết cho node_
}
else { cout<<“Vượt quá giới hạn DSLKĐ"<<endl; }

}

|<image_4>|

Hình 3.4. Thêm node vào vị trí pos

Thao tác loại node tại vị trí pos :

void single_linked_list::delete_pos() { //loại node ở vị trí pos_

int pos, i, counter = 0;
if (start == NULL){ //nếu danh sách liê kết đơn rỗng_
cout<<“Không thực hiện được"<<endl; return;
}
cout<<“Vị trí cần loại bỏ:";cin>>pos;
struct node *s, *ptr; s = start; //s trỏ đến đầu danh sách_
if (pos == 1){//nếu vị trí loại bỏ là node đầu tiên_
start = s->next; s->next=NULL; free(s);}
else {
while (s != NULL) { //đếm số node của DSLKĐ_
s = s->next; counter++;}
if (pos > 0 && pos <= counter){ //nếu vị trí pos hợp lệ_
s = start;//s trỏ đến node đầu của danh sách_
for (i = 1;i < pos; i++){ //di chuyển đến vị trí pos-1_
ptr = s; s = s->next;
}
ptr->next = s->next; //thiết lập liên kết cho node_
}
else { cout<<"Vi tri ngoai danh sach"<<endl; } free(s); //giải phóng s_
cout<<"Node da bi loai bo"<<endl;
}

}

|<image_5>|

Hình 3.5. Thao tác loại node ở vị trí pos

Thao tác sửa đổi nội dung của node :

void single_linked_list::update() { //sửa đổi thông tin của node_

int value, pos, i;
if (start == NULL){ //nếu danh sách LKĐ rỗng_
cout<<“Không thực hiện được"<<endl; return;
}
cout<<“Nhập vị trí node cần sửa:";cin>>pos; cout<<“Giá trị mới của node:";cin>>value; struct node *s, *ptr; //sử dụng hai con trỏ s và ptrs = start; //s trỏ đến node đầu tiên_
if (pos == 1) { start->info = value;} //sửa luôn node đầu tiên_
else { //nếu pos không phải là node đầu tiên_
for (i = 0;i < pos - 1;i++){//chuyển s đến vị trí pos-1_
if (s == NULL){//Nếu s là node cuối cùng_
cout<<"Vị trí "<<pos<<"không hợp lệ“; return;
}
s = s->next;
}
s->info = value; //Sửa đổi thông tin cho node_
}
cout<<“Hoàn thành việc sửa đổi"<<endl;

}

Thao tác duyệt danh sách liên kết đơn :

void single_linked_list::display() { //hiển thị nội dung DSLKĐ_

struct node *temp; //sử dụng một con trỏ temp_
if (start == NULL){ //nếu danh sách rỗngcout<<“Có gì đâu mà hiển thị"<<endl; return;
}
temp = start; //temp trỏ đến node đầu trong DSLKĐ_
cout<<“Nội dung DSLKĐ: "<<endl;
while (temp != NULL) { //lặp cho đến node cuối cùngcout<<temp->info<<"->"; //hiển thị thông tin nodetemp = temp->next; //di chuyển đến node tiếp theo_
}
cout<<"NULL"<<endl; //node cuối cùng là NULL_

}

Thao tác tìm node trong danh sách liên kết đơn :

_void single_linked_list::search(){//Tìm kiếm node_

int value, pos = 0; bool flag = false;
if (start == NULL){//nếu danh sách rỗngcout<<“ta không có gì để tìm"<<endl; return;
}
cout<<“Nội dung node cần tìm:";cin>>value; struct node *s; s = start;//s trỏ đến đầu danh sáchwhile (s != NULL){ pos++;
if (s->info == value){//Nếu s- >infor là value_
flag = true;
cout<<“Tìm thấy"<<value<<"tại vị trí"<<pos<<endl;
}
s = s->next;
}
if (!flag) {//đến cuối vẫn không thấy_
cout<<“Giá trị"<<value<<“không tồn tại"<<endl;
}

}

Thao tác sắp xếp các node trong danh sách liên kết đơn : void single_linked_list::sort() { //sắp xếp theo nội dung các node_

struct node *ptr, *s; //sử dụng hai con trỏ ptr và s_
int value; //giá trị trung gian_
if (start == NULL){//nếu danh sách rỗngcout<<“không có gì để sắp xếp"<<endl; return;
}
ptr = start;//ptr trỏ đến node đầu danh sách_
while (ptr != NULL){ //lặp trong khi ptr khác rỗng_
for (s = ptr->next; s !=NULL; s = s->next){ //s là node tiếp theo_
if (ptr->info > s->info){//nếu điều này xảy ra_
value = ptr->info;//tráo đổi nội dung hai node_
ptr->info = s->info; s->info = value;
}
}
ptr = ptr->next;
}

}

Thao tác đảo ngược các node của DSLKĐ :

void single_linked_list::reverse() { //đảo ngược danh sách_

struct node *ptr1, *ptr2, *ptr3; //sử dụng ba con trỏ node_
if (start == NULL) {//Nếu danh sách rỗng_
cout<<“ta không cần đảo"<<endl; return;
}
if (start->next == NULL){//Nếu danh sách chỉ có một node cout<<“đảo ngược là chính nó"<<endl; return;
}
ptr1 = start; //ptr1 trỏ đến node đầu tiên_
ptr2 = ptr1->next;//ptr2 trỏ đến node kế tiếp của ptr1ptr3 = ptr2->next;//ptr3 trỏ đến nod kế tiếp của ptr2ptr1->next = NULL;//Ngắt liên kết ptr1_
ptr2->next = ptr1;//node ptr2 bây giờ đứng trước node ptr1_
while (ptr3 != NULL){//Lặp nếu ptr3 khác rỗngptr1 = ptr2; //ptr1 lại bắt đầu tại vị trí ptr2ptr2 = ptr3; //ptr2 bắt đầu tại vị trí ptr3_
ptr3 = ptr3->next; //ptr3 trỏ đến node kế tiếp_
ptr2->next = ptr1; //Thiết lập liên kết cho ptr2_
}
start = ptr2; //node đầu tiên bây giờ là ptr2_

}

//Chương trình cài đặt các thao tác trên danh sách liên kết đơn:

#include<iostream> using namespace std;

struct node { //biểu diễn danh sách liên kết đơn_

int info; //thành phần thông tin_
struct node *next; //thành phần liên kết_

}*start;

class single_linked_list { //biểu diễn lớp single_linked_list_

public:
node* create_node(int);//tạo node rời rạc có giá trị value_
void insert_begin();//thêm node vào đầu danh sách liên kết đơn_
void insert_pos();//thêm node vào vị trí pos trong danh sách liên kết đơn_
void insert_last();//thêm node vào cuối danh sách liên kết đơnvoid delete_pos();//loại node tại vị trí pos của sách liên kết đơnvoid sort();//sắp xếp theo giá trị node cho danh sách liên kết đơnvoid search();//tìm node trong danh sách liên kết đơn_
void update(); //cập nhật thông tin cho node_
void reverse(); //đảo ngược các node trong danh sách liên kết đơnvoid display(); //duyệt danh sách liên kết đơnsingle_linked_list(){//constructor của lớp_
start = NULL;
}

};