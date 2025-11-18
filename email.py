email=input("Nhập email:")
if (email.count('@') == 1) and ("." in email):
    print("Email có vẻ hợp lệ")
else:
    print("Email không hợp lệ")