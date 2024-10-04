# Dự án "Xây dựng hệ thống đề xuất sản phẩm laptop dựa trên kỹ thuật lọc theo nội dung"

## Mục tiêu dự án:
Xây dựng một hệ thống hỗ trợ người tiêu dùng trong quá trình chọn sản phẩm laptop phù hợp với nhu cầu của bản thân, bao gồm:
- Thu thập dữ liệu về thông tin của các sản phẩm laptop từ các trang thương mại điện tử để xây dựng hệ thống đề xuất sản phẩm.
- Áp dụng các kỹ thuật tiền xử lý để tạo bộ dữ liệu nhằm hỗ trợ việc xây dựng hệ thống đề xuất sản phẩm.
- Áp dụng kỹ thuật lọc theo nội dung để xác định sản phẩm tương đồng.
- Xây dựng web app đề xuất sản phẩm bằng nền tảng Flask và Python để tạo giao diện trực quan về kết quả đề xuất, nhằm thuận lợi cho người 
dùng
## Phương pháp nghiên cứu:
Thu thập và xử lý dữ liệu được thu thập về từ các trang thương mại điện tử về laptop như FPT shop, Thế giới di động, CellphoneS,... từ đó sử dụng các kỹ thuật lọc theo nội dung và công cụ Flask để xây dựng một hệ thống đề xuất sản phẩm laptop

## Nội dung đề tài:
### Quy trình xây dựng hệ thống đề xuất:
![Framework](https://github.com/user-attachments/assets/93a4b200-e240-4abe-b32a-617d67eca718)

### Thu thập dữ liệu:
![Thu thập dữ liệu](https://github.com/user-attachments/assets/5261e190-60ac-459f-935f-c222ddcc7ec2)

### Tiền xử lý dữ liệu:
![Tiền xử lý dữ liệu](https://github.com/user-attachments/assets/b00f1736-cd14-4033-92d1-113322688f5f)
Từ bộ dữ liệu gốc, qua các bước Làm sạch dữ liệu (Xử lí giá trị rỗng, không nhất quán, trùng nhau), Biến đổi dữ liệu (Phân khúc máy tính dựa trên các đặc điểm, nhu cầu sử dụng), Rời rạc hóa dữ liệu (Phân tổ dữ liệu để tạo cấu trúc thứ bậc, phục vụ cho việc so sánh), Lọc dữ liệu, ta thu được bộ dữ liệu đã qua xử lý.
### Trực quan hóa dữ liệu:
![Số lượng sản phẩm theo hãng](https://github.com/user-attachments/assets/30760648-9164-412a-b7c4-75bced4a5024)

Chiếm lĩnh thị trường Máy tính xách tay hiện nay là thương hiệu Asus với 55 sản phẩm, nối tiếp là các thương hiệu HP, Lenovo, MSI, Acer và Apple. Nguyên nhân có thể là do những thương hiệu này phát hành những sản phẩm liên tục và đáp ứng được phần lớn nhu cầu của thị trường hiện nay.

![Phân phối sản phẩm theo giá bán](https://github.com/user-attachments/assets/d7d48633-309b-4083-82af-2ac2e5886fde)

Ta thấy rằng phần lớn sản phẩm nằm có giá nằm trong khoảng từ 9-33 triệu, trong đó khoảng từ 15-21 triệu có số lượng sản phẩm nhiều nhất. Đây cũng là điều dễ hiểu bởi người tiêu dùng luôn muốn tìm được những sản phẩm tốt với giá rẻ, vì thế hãng sản xuất luôn cố gắng tối ưu hóa chi phí để phát hành những sản phẩm đáp ứng được hoàn hảo những nhu cầu trong tầm giá.

![Biểu đồ tương quan](https://github.com/user-attachments/assets/83f08a33-d899-43cd-b3c4-902d45bf3de5)

Từ biểu đồ tương quan, ta có thể nhận ra được một số cặp biến có điểm tương quan khá cao, cho thấy mối quan hệ sâu sắc giữa chúng như Kích thước màn hình và Trọng lượng; Card đồ họa rời và Tần số quét màn hình; Loại RAM và Tốc độ RAM

![Yếu tố ảnh hướng đến giá bán](https://github.com/user-attachments/assets/646a6d10-10b7-41be-ad14-093c37637c83)

Từ kết quả tương quan giữa các biến thông số kỹ thuật và giá bán, ta có thể thấy được những thông số Độ phân giải, Hệ điều hành, Dung lượng pin, Công nghệ màn hình, Hãng card đồ họa, Loại RAM, Loại CPU,... là những yếu tố ảnh hưởng lớn tới giá bán sản phẩm. Các yếu tố kỹ thuật và tính năng tiên tiến thường là những yếu tố chính quyết định giá bán của sản phẩm.

### Xây dựng hệ thống đề xuất:
#### Kỹ thuật lọc theo nội dung:
![Content-based Filtering](https://github.com/user-attachments/assets/cb5bde19-f8c3-49d6-a036-5f1d1d995e66)

- Xác định các thuộc tính đầu vào: Đảm bảo hệ thống có thể đáp ứng mọi nhu cầu và sở thích của người dùng một cách toàn diện và đa dạng.
- Chuyern hóa vector TF-IDF: Mỗi sản phẩm sẽ được biểu diễn bởi một vector duy nhất, trong đó mỗi chiều của vector đại diện cho một thuộc tính đã được trích chọn. Điều này giúp chúng ta có thể so sánh và tính toán độ tương đồng giữa các sản phẩm dựa trên biểu diễn vector hóa của chúng.
- Tính toán độ tương đồng Cosine: Qua quá trình tính toán, ta sẽ tìm ra được các sản phẩm có mức độ tương đồng cao nhất với yêu cầu của người dùng, là những sản phẩm có điểm gần giá trị 1 nhất.

![Cách thức hoạt động](https://github.com/user-attachments/assets/efa77dc5-9dfe-4baf-9cd7-00777c2d695e)

#### Triển khai WebApp: Hệ thống đề xuất sản phẩm
![Quy trình triển khai web app bằng Flask](https://github.com/user-attachments/assets/81f3ce51-4af3-4ae5-9aa8-77020d60324e)

Hệ thống đề xuất sẽ có hai trang chính là trang biểu mẫu (form) để thu thập đặc điểm về sản phẩm mà người dùng mong muốn và trang kết quả để hiển thị kết quả đề xuất.

**Giao diện trang web:**
![Giao diện trang web](https://github.com/user-attachments/assets/cc4ddcba-372a-4f72-aebb-a5dd131af266)

Và khi người dùng điền đầy đủ thông tin, họ sẽ ấn vào nút ‘Đề xuất sản phẩm’ để đưa họ tới trang kết quả đề xuất.

**Kết quả đề xuất:**
![Kết quả đề xuất](https://github.com/user-attachments/assets/3153a385-da56-4352-b662-7b1908384a53)

Mỗi sản phẩm sẽ có số thứ tự chính là xếp hạng điểm cosine từ cao đến thấp. Bên cạnh đó, mỗi sản phẩm có chứa ba nút là “Xem chi tiết”, “So sánh sản phẩm” và “Nơi bán có giá tốt” để mở ra ba cửa sổ phụ (popup) giúp người dùng có cái nhìn tổng quan hơn về sản phẩm cũng như là có thể so sánh được với sản phẩm khác, tìm được nơi bán với giá rẻ nhất.

### Trang Xem chi tiết
![Screenshot 2024-05-18 231529](https://github.com/user-attachments/assets/b119b57a-09ce-42f7-896e-2b2db26948cf)

### Trang So sánh sản phẩm
![image](https://github.com/user-attachments/assets/2e6dac2a-b7f8-4e4b-86c5-6d62645749bf)
![image](https://github.com/user-attachments/assets/9ccf7cf7-789c-4783-b642-dcd173b13ec4)


### Trang Nơi bán giá tốt
![Screenshot 2024-05-18 231559](https://github.com/user-attachments/assets/21ef666a-0573-49c9-b115-74f30e3573ac)
Thông tin về sản phẩm tại các cửa hàng sẽ được sắp xếp tăng dần theo giá và giảm dần theo số lượng khuyến mãi.
