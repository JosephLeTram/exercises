# Từ module datetime, mình import class datetime và timedelta để sử dụng những methods

from datetime import datetime, timedelta


strprice = '$27.3'
strtime0 = '2019-12-07T21:31:56.000Z'


# khai báo biến fprice và gán cho nó giá trị bằng với strprice
# Hàm replace được dùng để thay đổi chuỗi hoặc giá trị
# Remove dấu dollar rồi thay bằng chuỗi rỗng
# Sau đó, chuổi rỗng sẽ được chuyển sang số thực
fprice = float(strprice.replace("$", ""))

# Thử phép tính giá trị thực nhân với 1.1
fprice1 = fprice * 1.1

# khai báo biến dttime0 và gán cho nó giá trị của stretime0

# Sử dụng method strptime để chuyển thời gian dạng string sang dạng số
# Method Strptime này có 2 arguments (value và format)
# Format của strptime được chọn dựa trên tài liệu Python
# %Y là year 4 chữ số, %m là tháng 2 chữ số, %d là ngày, %H là giờ dạng 24h, %M là Phút, %S là giây)
dttime0 = datetime.strptime(strtime0, "%Y-%m-%dT%H:%M:%S.000Z")

# tạo biến dttime1 có giá trị bằng giá trị của dttime0 cộng thêm 1 giờ 2 phút 3 giây

# Sử dụng timedelta method để cộng thêm thời gian, xuất ra giá trị mới dttime1 bằng cách gán giá trị cho biến keyword agruements
# như là giờ, phút, và giây
dttime1 = dttime0 + timedelta(hours=1, minutes=2, seconds=3)

# Xuất 3 giá trị đã tính ra màn hình

# In giá trị của các biến
print(fprice)
print(dttime0)
print(dttime1)
print(f"{fprice1:.2f}")

# Xuất kiểu (type) của 3 biến trên ra màn hình
# In kiểu của các biến
print(type(fprice))
print(type(fprice1))
print(type(dttime0))
print(type(dttime1))
