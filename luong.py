gio=float(input("Nhập số giờ làm việc thực tế trong tuần:"))
luong=int(input("Nhập mức lương mỗi giờ:"))
gio_chuan=40
gio_ot=gio-gio_chuan
if gio<=gio_chuan:
    luong1=gio*luong 
    print("Lương của bạn trong tuần này là:",round(luong1))
elif gio>gio_chuan:
    luong2=(gio_chuan*luong)+(gio_ot*luong*1.5)
    print("Lương của bạn trong tuần này là:",round(luong2))