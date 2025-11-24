loai=str(input("Nhập loại phòng bạn đang ở (Standard, Deluxe, Suite):"))
dem=float(input("Nhập số đêm bạn ở:"))
loai=loai.capitalize()
x1=1000000*dem
x2=1500000*dem
x3=2500000*dem
if loai=='Standard':
    if dem>3:
        x11=x1-(x1*0.1)
        print("Tổng tiền phòng bạn phải trả là:",x11)
    else:
        print("Tổng tiền phong bạn phải trả là:",x1)
elif loai=='Deluxe':
    if dem>3:
        x21=x2-(x2*0.1)
        print("Tổng tiền phòng bạn phải trả là:",x21)
    else:
        print("Tổng tiền phòng bạn phải trả là:",x2)
else:
    if dem>3:
        x31=x3-(x3*0.1)
        print("Tổng tiền phòng bạn phải trả là:",x31)
    else:
        print("Tổng tiền phòng bạn phải trả là:",x3)