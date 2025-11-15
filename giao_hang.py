gia=float(input("Nhập tổng giá trị đơn hàng (nghìn đồng):"))
if gia<500:
    print("Miễn phí giao hàng (0đ)")
elif gia>=100 and gia<=500:
    print("Phí giao hàng là 20.000đ")
else:
    print("Phí giao hàng là 35.000đ")