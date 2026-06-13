def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ")
    for employee in attendance_book:
        if employee["id"] == employee_id:
            print("Lỗi: Mã nhân viên đã tồn tại!")
            return
    employee_name = input("Nhập tên nhân viên: ")
    clock_in_time = input("Nhập giờ vào (HH:MM): ")
    new_employee = {
        "id": employee_id,
        "name": employee_name,
        "times": (clock_in_time, None)
    }
    attendance_book.append(new_employee)
    print(f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc {clock_in_time}!")
def clock_out(attendance_book):
    employee_id = input("Nhập mã nhân viên: ")
    clock_out_time = input("Nhập giờ ra (HH:MM): ")
    for employee in attendance_book:
        if employee["id"] == employee_id:
            clock_in_time = employee["times"][0]
            employee["times"] = (clock_in_time, clock_out_time)
            print("Chấm công ra thành công!")
            return
    print("Không tìm thấy nhân viên!")