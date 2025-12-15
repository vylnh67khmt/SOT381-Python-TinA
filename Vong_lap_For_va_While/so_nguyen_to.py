num = int(input("Nhập số cần kiểm tra: "))
if num< 2:
    print("Không phải số nguyên tố")
else:
    so_nguyen_to= True
    for i in range(2, int(num**0.5) + 1):
        if num%i==0 :
            so_nguyen_to = False
            break
        else:
            so_nguyen_to = True
    print("Là số nguyên tố" if so_nguyen_to else "Không phải số nguyên tố")