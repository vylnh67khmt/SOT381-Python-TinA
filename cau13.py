toan=float(input("Nhập vào điểm Toán: "))
ly=float(input("Nhập vào điểm Lý: "))
hoa=float(input("Nhập vào điểm Hóa: "))
tong=toan+ly+hoa
if tong >=15 and ((toan>=4) and (ly>=4) and (hoa>=4)):
    print("Đậu")
    if (toan>5) and (ly>5) and (hoa>5):
        print("Học đều các môn")
    else:
        prin("Học chưa đều các môn")
else:
    print("Thi hỏng")
    