diemtb=float(input("Nhập điểm trung bình của bạn:"))
if diemtb<0 or diemtb>10:
    print("Điểm không hợp lệ")
if diemtb >= 8:
    print("Học lực giỏi")
elif diemtb >= 6.5:
    print("Học lực khá")
elif diemtb >= 5:
    print("Học lực trung bình")
else:
    print("Học lực yếu")