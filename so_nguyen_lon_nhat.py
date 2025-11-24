a,b,c=input("Nhập ba số nguyên bất kì:").split()
if a>=b and a>=c:
    print(a," là số lớn nhất")
elif b>=a and b>=c:
    print(b," là số lớn nhất")
else:
    print(c," là số lớn nhất")
