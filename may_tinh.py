a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
toan=input("Nhập phép toán (+,-,*,/):")
if toan=='+':
    print("Kết quả phép toán cộng là",a+b)
elif toan=='-':
    print("Kết quả phép toán trừ là",a-b)
elif toan=='*':
    print("Kết quả phép toán nhân là",a*b)
else:
    if b==0:
        print("Không thể thực hiện phép chia co 0")
    else:
        print("Kết quả phép toán chia là:",a/b)