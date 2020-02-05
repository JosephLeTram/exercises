# Từ module datetime, mình import class datetime và timedelta để sử dụng những methods

from datetime import datetime, timedelta


strprice = '$27.3'
strtime0 = '2019-12-07T21:31:56.000Z'


# khai báo biến fprice và gán cho nó giá trị bằng với strprice

# Remove dấu dollar rồi thay bằng chuỗi rỗng
# Sau đó, chuổi rỗng sẽ được chuyển sang số thực
fprice = float(strprice.replace("$", ""))

# [1:] để lấy những thứ tự từ 1 trở đi - bỏ đi dấu $S
# sau đó dùng lệnh float để chuyển dạng string thành dạng giá trị thực
fprice_test = float(strprice[1:])

# Thử phép tính giá trị thực nhân với 1.1
fprice1 = fprice * 1.1

# khai báo biến dttime0 và gán cho nó giá trị của stretime0

# Sử dụng method strptime để chuyển thời gian dạng string sang dạng số
# Method Strptime này có 2 arguments (value và format)
# Format của strptime được chọn dựa trên tài liệu Python
dttime0 = datetime.strptime(strtime0, "%Y-%m-%dT%H:%M:%S.000Z")

# tạo biến dttime1 có giá trị bằng giá trị của dttime0 cộng thêm 1 giờ 2 phút 3 giây
# timedelta method là một khoảng thời gian giữa 2 thời điểm
# Sử dụng timedelta method để cộng thêm thời gian, xuất ra giá trị mới dttime1

dttimediff = timedelta(hours=1, minutes=2, seconds=3)
dttime1 = dttime0 + dttimediff

# Xuất 3 giá trị đã tính ra màn hình

# In giá trị của các biến
print(fprice)
print("----")
print(fprice_test)
print(dttime0)
print(dttime1)
print(f"{fprice1:.2f}")

# Xuất kiểu (type) của 3 biến trên ra màn hình
# In kiểu của các biến
print(type(fprice))
print(type(fprice1))
print(type(dttime0))
print(type(dttime1))
