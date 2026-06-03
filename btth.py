grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades():
    print('--- BẢNG ĐIỂM HỌC SINH ---')
    print("Mã SV | Tên Học Sinh | Điểm Toán | Điểm Anh | ĐTB")
    for i in grade_book:
        match_score, english_score = i["info"]
        avg_score = (match_score + english_score) / 2
        print(f"{i['id']} | {i['name']} | {match_score} | {english_score} | {avg_score}")
    
def add_student(book):
    while True:
        student_id = input("Nhập mã học sinh mới: ").strip()
        exist = False
        for student in book:
            if student["id"] == student_id:
                exist = True
                break
        if exist:
            print(f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác.")
        else:
            break

        name = input("Nhập tên học sinh: ").strip()
        math_score = float(input("Nhập điểm Toán: "))
        english_score = float(input("Nhập điểm Anh: "))

        new_student = {
            "id": student_id,
            "name": name,
            "info": (math_score, english_score)
        }

        book.append(new_student)
        print(f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!")

def update_scores(book):
    student_id = input("Nhập mã học sinh cần cập nhật: ").strip()
    for student in book:
        if student["id"] == student_id:
            math_score = float(input("Nhập điểm Toán mới: "))
            english_score = float(input("Nhập điểm Anh mới: "))

            student["info"] = (math_score, english_score)

            print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
            return

    print("Không tìm thấy học sinh!")

def delete_student(book):
    student_id = input("Nhập mã học sinh cần xóa: ").strip()
    for student in book:
        if student["id"] == student_id:
            book.remove(student)
            print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!")
            return

    print("Không tìm thấy học sinh!")

    while True:
        print("""
=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
""")

        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("[Lỗi]: Vui lòng nhập số từ 1 đến 5!")
            continue

        match choice:
            case 1:
                display_grades(grade_book)

            case 2:
                add_student(grade_book)

            case 3:
                update_scores(grade_book)

            case 4:
                delete_student(grade_book)

            case 5:
                print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
                break

            case _:
                print("[Lỗi]: Chức năng không hợp lệ!")


