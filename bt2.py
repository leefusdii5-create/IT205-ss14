# (1) Phân tích lỗi
# Loại biến total_points ở dòng 2:

# Là biến toàn cục (Global) vì nó được khai báo ở ngoài cùng của file code, không nằm trong bất kỳ hàm nào.

# Giải thích lỗi UnboundLocalError:

# Trong Python, khi ta thực hiện phép gán total_points = ... bên trong hàm, Python sẽ tự động coi total_points là một biến cục bộ (Local) mới của riêng hàm đó.

# Vì là biến cục bộ mới nên nó chưa có giá trị ban đầu. Do đó, việc viết total_points + points_earned 
# (lấy biến cục bộ chưa có giá trị để cộng) sẽ khiến chương trình bị lỗi vì không thể tính toán với một biến "chưa có gì".

# Chỉ đọc (print) biến toàn cục bên trong hàm:

# Chương trình không bị lỗi. Python cho phép các hàm thoải mái đọc (truy cập) 
# giá trị của biến toàn cục nếu trong hàm không có lệnh gán trùng tên.

# Cách sửa 1 (Dùng từ khóa):

# Sử dụng từ khóa global.

# Dòng lệnh khai báo: global total_points

# Cách sửa 2 (Dùng lệnh trả về giá trị):

# Sử dụng lệnh return để trả về tổng điểm mới sau khi cộng.

#  code đã sửa:
total_points = 100

def add_reward_points(current_points, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_points + points_earned

total_points = add_reward_points(total_points, 50)
print("Tổng điểm hiện tại của khách hàng:", total_points)





















