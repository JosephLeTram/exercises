# import datetim
from datetime import datetime, timedelta


strprice = '$27.3'
strtime0 = '2019-12-07T21:31:56.000Z'


# khai báo biến fprice và gán cho nó giá trị bằng với strprice
# fprice = <viết code của em ở đây >
fprice = strprice

# khai báo biến dttime0 và gán cho nó giá trị của stretime0
# dttime0 = <viết code của em ở đây >
dttime0 = datetime.strptime(strtime0, "%Y-%m-%dT%H:%M:%S.000Z")

# tạo biến dttime1 có giá trị bằng giá trị của dttime0 cộng thêm 1 giờ 2 phút 3 giây
# dttime1 = <viết code của em ở đây >
dttime1 = dttime0 + timedelta(hours=1, minutes=2, seconds=3)

# Xuất 3 giá trị đã tính ra màn hình
# <viết code của em ở đây >
print(fprice)
print(dttime0)
print(dttime1)

# Xuất kiểu (type) của 3 biến trên ra màn hình
# <viết code của em ở đây >
print(type(fprice))
print(type(dttime0))
print(type(dttime1))
