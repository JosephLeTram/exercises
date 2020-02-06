import csv

# Viết một chương trình với mô tả sau
# Khi chạy chương trình sẽ hiện ra như sau

#  Xin chào! Hãy nhập tên đầy đủ bên dưới (gõ luôn cả dấu tiếng Việt nha)
print("Xin chào! Hãy nhập tên đầy đủ bên dưới")


# Sử dụng hàm input() để nhận đầu vào của người dùng
# Hàm titlte() được dùng để in hoa chữ cái đầu trong trường hợp người dùng không viết hoa
# Hàm split() được sử dụng để tách string họ tên đầy đủ thành những phần nhỏ
name = input().title()
full_name = name.split()
# print(name)
# print("----")
# print(full_name)
# print("Hello " + full_name)


# Người dùng sẽ nhập họ tên đầy đủ của mình sau đó chương trình sẽ làm các việc sau
# Tính toán để lấy được họ, tên và chữ lót
# Dùng phương pháp index để lấy họ, tên và chữ lót
# Dùng index -1 (từ trái sang phải) để lấy được tên
ten = full_name[-1]
# Dùng index -2 (từ trái sang phải) để lấy được tên lót (thông thường sẽ sau tên)
ten_lot = full_name[-2]
# Dùng index [:-2] để lấy hết những gì còn lại trước tên lót và tên (thông thường sẽ là họ)
ho = ' '.join(full_name[:-2])

# print(ten)
# print(ten_lot)
# print(ho)

# Sau đó hiện ra câu
#  Chúc bạn <tên đã nhận ra được> một ngày tốt lành!
# print(f"Chúc bạn {ten} một ngày tốt lành!")

# Rồi lưu vào file danhsachten.csv thêm một line với format sau
#  chuỗi họ tên, chuỗi họ, chuỗi tên, chuỗi chữk lót [và xuống dòng]

# Sử dụng with open statement để mở file và đóng tự động khi thực hiện xong lệnh trong block
# mode = "w" là chế độ viết vào files, nếu như không có file, Python sẽ tạo file mới
# newline = "" là để xuống dòng
# encoding ="utf-8" là để viết unicode để viết có dấu
# as dachsachten là một biến và dachsachten.csv là tên của file csv

with open("dachsachten.csv", mode="w", newline="", encoding="utf-8") as dachsachten:
    # sử dụng hàm csv.writer để viết vào danh sách tên
    dachsachten_writer = csv.writer(dachsachten)
    # sử dụng hàm .writerow để viết từng dòng trong file
    dachsachten_writer.writerow([f"Chúc bạn {ten} một ngày tốt lành!"])
    dachsachten_writer.writerow([name, ho, ten_lot, ten])


# ví dụ anh nhập vào Trần Xuân Ngọc Tân thì chương trình sẽ xuất câu "Chúc bạn Tân một ngày tốt lành"
# đồng thời lưu thêm 1 dòng vào file có nội dung sau "Trần Xuân Ngọc Tân, Trần, Tân, Xuân Ngọc"

# Thử suy nghĩ xem nếu user nhập lung tung vào thì họ sẽ nhập những gì và chương trình của mình sẽ đối phó như thế nào
