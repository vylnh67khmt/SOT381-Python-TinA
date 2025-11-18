loai=str(input("Nhập loại hành khách:"))
loai=loai.lower()
if loai=='học sinh':
    print("Giá vé là 3000 đồng")
elif loai=='sinh viên':
    print("Giá vé là 5000 đồng")
elif loai=='người cao tuổi':
    print("Miễn phí (0đ)")
else:
    print("Giá vé là 7000 đồng")