import math
xe=str(input("Nhập loại xe (xe máy, ô tô):")).strip().lower()
gio=float(input("Nhập số giờ đỗ xe:"))
gio2=math.ceil(gio)
if xe=='xe máy':
    if gio2<=2:
        tien=5000
    else:
        tien=5000+(gio2-2)*2000
    print("Số tiền bạn phải trả là:",tien,"đồng")
else:
    if gio2<=2:
        tien1=20000
    else:
        tien1=20000+(gio2-2)*15000
    print("Số tiền bạn phải trả là:",tien1,"đồng")
