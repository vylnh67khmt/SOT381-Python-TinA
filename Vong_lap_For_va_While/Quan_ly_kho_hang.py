o_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
for ten_san_pham, o_luong in zip(ten_san_pham, o_luong):
    if o_luong<10:
        print(f"Cần nhập thêm {ten_san_pham}")