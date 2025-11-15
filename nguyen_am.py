nhap=input("Nhập một kí tự bất kì:")
if len(nhap)==1:
    nhap=nhap.lower()
if (nhap=='a' or nhap=='e' or nhap=='i' or nhap=='o' or nhap=='u'):
    print("Kí tự bạn vừa nhập là một nguyên âm")
else:
    print("Kí tự bạn vừa nhập không phải là một nguyên âm ")