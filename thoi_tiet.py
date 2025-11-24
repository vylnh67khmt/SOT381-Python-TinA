do=int(input("Nhập nhiệt độ:"))
thoi_tiet=input("Nhập tình trạng thời tiết(Nắng,Mưa,Âm u):")
if thoi_tiet=="Mưa":
    print("Nhớ mang áo mưa và ô")
elif do>30:
    print("Mặc đồ thoáng mát, cẩn thận say nắng")
elif 20<=do<=30 and thoi_tiet=='Nắng':
    print("Thời tiết đẹp, mặc đồ thoải mái")
else:
    print("Trời lạnh, nhớ mặc áo khoác")