von = 100000000  # 100 triệu
lai_suat = 0.07  # 7
nam = 10
print(f"Đầu tư {von} VND với lãi suất {lai_suat*100}")
for i in range(1, nam + 1):
    von = von * (1 + lai_suat)
    print(f"Năm {i}: {von:,.0f} VND")

print(f" Sau {nam} năm: {von:,.0f} VND")