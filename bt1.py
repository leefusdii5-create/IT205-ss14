# (1) Phân tích lỗi
# 1.Gán sai tham số:15000 đang được gán cho tham số discount.
# 0.1 đang được gán cho tham số shipping_fee
# 2.Sai lệch công thức:
# Do truyền sai vị trí, phép tính trở thành: 100000 - (100000 * 15000) + 0.1.
# Phép nhân 100000 * 15000 tạo ra con số khổng lồ ($1,500,000,000$), dẫn đến kết quả bị âm nặng
# 3.Lỗi TypeError:
# Hàm calculate_final_price chỉ sử dụng lệnh print() để hiển thị kết quả chứ không có lệnh return
# .Trong Python, một hàm không có return sẽ mặc định trả về giá trị None.
#  Do đó, lệnh order_total + 5000 tương đương với None + 5000, gây ra lỗi kiểu dữ liệu (TypeError)
#  .Giá trị của biến order_total:Mang giá trị None. Vì hàm calculate_final_price không trả về (return)
# bất kỳ giá trị nào.Phân biệt print() và return:print() chỉ hiển thị dữ liệu ra màn hình Console để người
# dùng nhìn thấy, dữ liệu đó không thể đem đi tính toán tiếp.return trả về giá trị cho lời gọi hàm, giúp 
# lưu trữ kết quả vào biến để tái sử dụng cho các phép tính sau đó.Cách sửa đổi:Thay lệnh print("Đã tính xong tổng tiền:", total)
#  ở cuối hàm thành return total.Khi gọi hàm, cần truyền đúng thứ tự các đối số: calculate_final_price(100000, 0.1, 15000).

# code đã sửa:
def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total

order_total = calculate_final_price(100000, 0.1, 15000)
final_payment = order_total + 5000
print("Khách hàng cần thanh toán:", final_payment)