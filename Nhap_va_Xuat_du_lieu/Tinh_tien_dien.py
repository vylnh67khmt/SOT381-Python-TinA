dien=float(input("Nhập vào số điện đã dùng:"))
if dien<50:
    print(f"Số tiền điện bạn phải trả là: {dien*1678:.0f} VNĐ")
elif 50<=dien<100:
    print(f"Số tiền điện bạn phải trả là: {dien*1734:.0f} VNĐ")
elif 100<=dien<200:
    print(f"Số tiền điện bạn phải trả là: {dien*2014:.0f} VNĐ")
elif 200<=dien<350:
    print(f"Số tiền điện bạn phải trả là: {dien*2536:.0f} VNĐ")
else:
    print(f"Số tiền điện bạn phải trả là: {dien*2927:.0f} VNĐ")