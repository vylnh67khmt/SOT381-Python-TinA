name=input("Nhập vào tên học sinh:")
math=float(input("Nhập điểm toán:"))
physics=float(input("Nhập điểm lý:"))
chemistry=float(input("Nhập điểm hóa:"))
average=(math+physics+chemistry)/3
print("=== QUẢN LÍ ĐIỂM HỌC SINH ===")
print(f"Tên của học sinh là: {name}")
print(f"Điểm toán của học sinh là: {math}")
print(f"Điểm lý của học sinh là: {physics}")
print(f"Điểm hóa của học sinh là: {chemistry}")
if average>=8:
    print(f"=== Học sinh {name} đạt xếp loại Giỏi với điểm trung bình là: {average:.2f} ===")
elif average>= 6.5:
    print(f"=== Học sinh {name} đạt xếp loại Khá với điểm trung bình là: {average:.2f} ===")
elif average>=5:
    print(f"=== Học sinh {name} đạt xếp loại Trung bình với điểm trung bình là: {average:.2f} ===")
else:
    print(f"=== Học sinh {name} đạt xếp loại Yếu với điểm trung bình là: {average:.2f} ===")