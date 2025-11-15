a=int(input("Nhập cạnh a:"))
b=int(input("Nhập cạnh b:"))
c=int(input("Nhập cạnh c:"))
if a+b>c and a+c>b and b+c>a:
    print("Đây là 3 cạnh của một tam giác")
    if a==b==c:
        print("Và là tam giác đều")
    elif a==b or a==c or b==c:
        print("Và là tam giác cân")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("Và là tam giác vuông")
    else:
        print("Và là tam giác thường")
else:
    print("Đây không phải là 3 cạnh của một tam giác")