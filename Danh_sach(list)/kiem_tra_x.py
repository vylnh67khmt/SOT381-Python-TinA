danh_sach=[2,4,6,8,10]
x=input("Nhập một số bất kì: ")
for i in danh_sach:
    if i==x:
        print(f"Số {x} có trong danh sách")
        print(f"Số {x} ở vị trí: {danh_sach.index(x)}")
        break
    else:
        print(f"Số {x} không có trong danh sách")
        break