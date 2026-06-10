# (1) Phân tích Thiết kế Hàm
# 1. Hàm phụ trợ: 
# calculate_average(student)Input (Tham số): 
# student (Dictionary chứa thông tin của một sinh viên).
# Output (Trả về): Giá trị số thực (Float) là điểm trung bình của sinh viên đó.
# Mô tả luồng xử lý: Lấy tổng điểm 3 môn math, physics, chemistry trong dictionary
# chia cho 3 và trả về kết quả.2. Chức năng 1: display_grades(records)Input (Tham số): 
# records (List chứa các dictionary sinh viên).Output (Trả về): None (Chỉ in bảng điểm ra màn hình).
# Mô tả luồng xử lý:Kiểm tra danh sách rỗng. Nếu rỗng, in thông báo và dừng hàm.Nếu có dữ liệu, duyệt
# qua từng sinh viên, gọi hàm calculate_average để lấy điểm trung bình.Dựa vào điểm trung bình để 
# xác định chuỗi phân loại học lực ("Giỏi", "Khá", "Trung bình", "Yếu").In thông tin sinh viên
# theo đúng định dạng yêu cầu.3. Chức năng 2: update_student_score(records)Input (Tham số): records
# (List chứa các dictionary sinh viên).Output (Trả về): None (Cập nhật trực tiếp vào danh sách records).
# Mô tả luồng xử lý:Yêu cầu nhập mã sinh viên, tiến hành chuẩn hóa chuỗi (xóa khoảng trắng, in hoa).
# Tìm kiếm sinh viên trong danh sách. Nếu không thấy, báo lỗi và dừng hàm.Nếu tìm thấy, yêu cầu chọn
# môn học muốn sửa (1, 2, hoặc 3).Sử dụng vòng lặp và try-except để yêu cầu nhập điểm mới, bắt lỗi 
# nếu nhập chữ hoặc nhập điểm ngoài phạm vi $[0, 10]$.Cập nhật điểm mới vào môn học tương ứng của sinh
# viên đó và thông báo thành công.4. Chức năng 3: generate_report(records)Input (Tham số): records
# (List chứa các dictionary sinh viên).Output (Trả về): None (Chỉ in báo cáo thống kê ra màn hình).Mô 
# tả luồng xử lý:Kiểm tra danh sách rỗng để tránh lỗi chia cho 0.Khởi tạo hai biến đếm số lượng sinh 
# viên qua môn và trượt môn bằng 0.Duyệt qua danh sách, gọi hàm calculate_average. Nếu ĐTB >= 5.0 thì
# tăng biến đếm qua môn, ngược lại tăng biến đếm trượt môn.Tính tỷ lệ phần trăm và hiển thị báo cáo.5.
# Chức năng 4: find_valedictorian(records)Input (Tham số): records (List chứa các dictionary sinh viên).
# Output (Trả về): None (Chỉ in thông tin thủ khoa ra màn hình).Mô tả luồng xử lý:Kiểm tra danh sách 
# rỗng.Giả định sinh viên đầu tiên là thủ khoa và lưu điểm trung bình cao nhất hiện tại.Duyệt từ sinh 
# viên tiếp theo, tính ĐTB và so sánh. Nếu tìm thấy ai có ĐTB cao hơn thì cập nhật lại thông tin thủ 
# khoa.In thông tin vinh danh thủ khoa ra màn hình.

# Triển khai code:
student_records = [
    {"student_id": "SV001", "name": "Nguyễn Văn A", "math": 8.5, "physics": 7.0, "chemistry": 9.0},
    {"student_id": "SV002", "name": "Trần Thị B", "math": 4.0, "physics": 5.5, "chemistry": 5.0},
    {"student_id": "SV003", "name": "Lê Văn C", "math": 9.5, "physics": 9.0, "chemistry": 8.5}
]

def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def display_grades(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for i in range(len(records)):
        st = records[i]
        avg = calculate_average(st)
        if avg >= 8.0:
            rank = "Giỏi"
        elif avg >= 6.5:
            rank = "Khá"
        elif avg >= 5.0:
            rank = "Trung bình"
        else:
            rank = "Yếu (Cảnh báo đỏ)"
        print(f"{i+1}. [{st['student_id']}] {st['name']:<15} | Toán: {st['math']:.1f} | Lý: {st['physics']:.1f} | Hóa: {st['chemistry']:.1f} | ĐTB: {avg:.2f} - {rank}")
    print("---------------------------")

def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    target_student = None
    for st in records:
        if st["student_id"] == student_id:
            target_student = st
            break
    if target_student is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return
    print("Chọn môn học (1-Toán, 2-Lý, 3-Hóa):")
    choice = input("Lựa chọn của bạn: ").strip()
    if choice == "1":
        field = "math"
        subject_name = "Toán"
    elif choice == "2":
        field = "physics"
        subject_name = "Lý"
    elif choice == "3":
        field = "chemistry"
        subject_name = "Hóa"
    else:
        print("Lựa chọn môn học không hợp lệ!")
        return
    while True:
        try:
            score_input = input("Nhập điểm mới: ").strip()
            score = float(score_input)
            if 0 <= score <= 10:
                target_student[field] = score
                print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{target_student['name']}' thành {score:.1f}.")
                break
            else:
                print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        except ValueError:
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")

def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total = len(records)
    passed = 0
    failed = 0
    for st in records:
        if calculate_average(st) >= 5.0:
            passed += 1
        else:
            failed += 1
    passed_pct = (passed / total) * 100
    failed_pct = (failed / total) * 100
    print("--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên (Chiếm {passed_pct:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {failed} sinh viên (Chiếm {failed_pct:.2f}%)")
    print("----------------------")

def find_valedictorian(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    valedictorian = records[0]
    max_avg = calculate_average(valedictorian)
    for i in range(1, len(records)):
        current_avg = calculate_average(records[i])
        if current_avg > max_avg:
            max_avg = current_avg
            valedictorian = records[i]
    print("--- VINH DANH THỦ KHOA ---")
    print(f"Sinh viên: {valedictorian['name']} (Mã: {valedictorian['student_id']})")
    print(f"Điểm Trung Bình: {max_avg:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")
    choice = input("Chọn chức năng (1-5): ").strip()
    if choice == "1":
        display_grades(student_records)
    elif choice == "2":
        update_student_score(student_records)
    elif choice == "3":
        generate_report(student_records)
    elif choice == "4":
        find_valedictorian(student_records)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


























