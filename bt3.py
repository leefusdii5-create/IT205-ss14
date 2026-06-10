# (1) Phân tích và thiết kế giải pháp
# Input/Output của các hàm
# validate_score(score_input)
# Input: Chuỗi nhập vào từ bàn phím.
# Output: Trả về True nếu là số từ 0 đến 10, ngược lại trả về False.
# find_student_by_id(student_list, student_id)
# Input: Danh sách học viên và mã học viên cần tìm.
# Output: Trả về chỉ số (index) của học viên trong danh sách nếu tìm thấy, ngược lại trả về -1.
# get_rank(average_score)
# Input: Điểm trung bình (số thực).
# Output: Trả về chuỗi xếp loại ("Giỏi", "Khá", "Trung bình", "Yếu").
# display_students(student_list)
# Input: Danh sách học viên.
# Output: Không có (chỉ in danh sách ra màn hình).
# add_student(student_list)
# Input: Danh sách học viên hiện tại.
# Output: Không có (thêm trực tiếp học viên mới vào danh sách).
# update_score(student_list)
# Input: Danh sách học viên hiện tại.
# Output: Không có (cập nhật trực tiếp điểm của học viên trong danh sách).
# evaluate_students(student_list)
# Input: Danh sách học viên.
# Output: Không có (chỉ tính toán và in kết quả xếp loại).
# Lý do chia nhỏ chương trình thành các hàm
# Dễ quản lý và sửa lỗi: Khi một chức năng bị lỗi (ví dụ tính sai điểm trung bình), 
# ta chỉ cần tìm đến đúng hàm đó để sửa thay vì phải dò tìm trong một vòng lặp while dài hàng trăm dòng.
# Tái sử dụng mã nguồn: Hàm validate_score và find_student_by_id được sử dụng lại nhiều lần ở cả chức năng
#   thêm mới và cập nhật điểm, giúp giảm thiểu việc viết trùng lặp code.
# Code sạch và rõ ràng: Giúp luồng chính của chương trình (vòng lặp menu) cực kỳ ngắn gọn, dễ đọc và dễ hiểu.

# Triển khai code:
def validate_score(score_input):
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        return False
    except ValueError:
        return False

def find_student_by_id(student_list, student_id):
    for i in range(len(student_list)):
        if student_list[i]["student_id"] == student_id:
            return i
    return -1

def get_rank(average_score):
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def display_students(student_list):
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    for i in range(len(student_list)):
        st = student_list[i]
        print(f"{i+1}. Mã: {st['student_id']} | Tên: {st['name']} | Toán: {st['math_score']} | Anh: {st['english_score']}")

def add_student(student_list):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống!")
            continue
        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue
        break
    while True:
        name = input("Nhập tên học viên: ").strip().title()
        if name:
            break
        print("Tên học viên không được để trống!")
    while True:
        math_input = input("Nhập điểm Toán: ").strip()
        if validate_score(math_input):
            math_score = float(math_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    while True:
        english_input = input("Nhập điểm Anh: ").strip()
        if validate_score(english_input):
            english_score = float(english_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")

def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    index = find_student_by_id(student_list, student_id)
    if index == -1:
        print(f"Không tìm thấy học viên mang mã [{student_id}]!")
        return
    while True:
        math_input = input("Nhập điểm Toán mới: ").strip()
        if validate_score(math_input):
            student_list[index]["math_score"] = float(math_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    while True:
        english_input = input("Nhập điểm Anh mới: ").strip()
        if validate_score(english_input):
            student_list[index]["english_score"] = float(english_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    print("Cập nhật điểm thành công!")

def evaluate_students(student_list):
    if not student_list:
        print("Danh sách học viên trống, không thể đánh giá.")
        return
    for st in student_list:
        avg = (st["math_score"] + st["english_score"]) / 2
        rank = get_rank(avg)
        print(f"Mã: {st['student_id']} | Tên: {st['name']} | ĐTB: {avg:.2f} | Xếp loại: {rank}")

students = [
    {"student_id": "RA001", "name": "Nguyễn Văn A", "math_score": 8.5, "english_score": 7.0},
    {"student_id": "RA002", "name": "Trần Thị B", "math_score": 9.0, "english_score": 9.5}
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")
    choice = input("Lựa chọn của bạn (1-5): ").strip()
    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")




















