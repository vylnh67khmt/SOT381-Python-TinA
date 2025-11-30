diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for i in diem_so:
    if i>=8.0:
        print(f"Học sinh có điểm số {i} xếp loại Giỏi")
    elif 6.5<=i<=7.9:
        print(f"Học sinh có điểm số {i} xếp loại Khá")
    else:
        print(f"Học sinh có điểm số {i} xếp loại Trung bình")