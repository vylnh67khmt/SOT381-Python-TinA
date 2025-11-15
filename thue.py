thu=int(input("Nhập tổng thu nhập hàng tháng của bạn(VNĐ):"))
ban_than = 11000000
chiu_thue = thu - ban_than
if chiu_thue <= 0:
    print("Không phải nộp thuế")
elif chiu_thue>0 and chiu_thue <= 5000000:
    thue=chiu_thue*0.05
    print("Số tiền bạn phải nộp thuê là:",thue,"VNĐ")
else:
    thue1=chiu_thue*0.1
    print("Số tiền bạn phải nộp thuế là:",thue1,"VNĐ")
   