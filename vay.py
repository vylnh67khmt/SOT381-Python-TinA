thu=int(input("Nhập thu nhập hàng tháng:"))
diem=int(input("Nhập điểm tín dụng:"))
vay=float(input("Nhập số tiền muốn vay:"))
if diem<300 and diem>850:
    print("Điểm tín dụng không hợp lệ.")
elif diem>=580 and thu<20000000:
    print("Yêu cầu vay tiền cần xem xét thêm.")
elif diem>=580 and thu>20000000:
    print("Yêu cầu vay tiền đã duyệt.")
else:
    print("Yêu cầu vay tiền bị từ chối.")