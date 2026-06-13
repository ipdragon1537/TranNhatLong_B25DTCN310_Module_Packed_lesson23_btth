from datetime import datetime
def evaluate_flex_time(attendance_book):
    for employee in attendance_book:
        clock_in = employee["times"][0]
        clock_out = employee["times"][1]
        if clock_out is None:
            print(f"{employee['id']} - Chưa đủ dữ liệu chấm công.")
            continue
        in_time = datetime.strptime(clock_in,"%H:%M")
        out_time = datetime.strptime(clock_out,"%H:%M")
        latest_allowed = datetime.strptime("10:00","%H:%M")
        if in_time > latest_allowed:
            print(f"{employee['id']} - Vi phạm: Đến muộn quá 90 phút.")
            continue
        working_hours = (out_time - in_time).total_seconds() / 3600
        if working_hours < 9:
            print(f"{employee['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")
        else:
            print(f"{employee['id']} - Hợp lệ: Hoàn thành ca làm việc.")