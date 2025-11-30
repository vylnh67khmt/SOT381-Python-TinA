dau_tu=100000000
lai=0.07
so_nam_dau_tu=float(input("Nhập số năm đầu tư:"))
print(f"---- Báo cáo đầu tư với số vốn 100000000 VNĐ với lãi suất 7% ----")
for i in range (1, int(so_nam_dau_tu)+1):
    print(f"Năm thứ {i} nhận được số tiền là: {dau_tu*lai*i:.0f} VNĐ")
