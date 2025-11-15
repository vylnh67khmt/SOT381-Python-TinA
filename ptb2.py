a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
if a==0:
    if b==0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm:",-c/b)
else:
    delta=b**2-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta==0:
        print("Phương trình có nghiệm kép:",-b/(2*a))
    else:
        x1=(-b+delta**0,5)/(2*a)
        x2=(-b-delta**0,5)/(2*a)
        print("Phương trình có hai nghiệm phân biệt:",x1,"và",x2)