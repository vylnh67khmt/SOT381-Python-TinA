password=input("Nhập một mật khẩu:")
dai=len(password)
co_chu = any(c.isalpha() for c in password)
co_so = any(c.isdigit() for c in password)
dk=co_chu and co_so
if dai<8:
    if dk:
        print("Mật khẩu Yếu, có chứa chữ và số")
    else:
        print("Mật khẩu Yếu, không chứa cả chữ và số")
elif dai>=8 and dai<=12:
    if dk:
        print("Mật khẩu Trung bình, có chứa chữ và số")
    else:
        print("Mật khẩu Trung bình, không chứa cả chữ và số")
else:
    if dk:
        print("Mật khẩu Mạnh, có chứa chữ và số")
    else:
        print("Mật khẩu Mạnh, không chứa chữ và số")