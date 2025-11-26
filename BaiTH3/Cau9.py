#cau 9 Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
th = int(input("Nhập tháng (1-12): "))
if 1 <= th <= 3:
    print("Tháng", th, "thuộc Quý 1")
elif 4 <= th <= 6:
    print("Tháng", th, "thuộc Quý 2")
elif 7 <= th <= 9:
    print("Tháng", th, "thuộc Quý 3")
elif 10 <= th <= 12:
    print("Tháng", th, "thuộc Quý 4")
else:
    print("Tháng không hợp lệ!")