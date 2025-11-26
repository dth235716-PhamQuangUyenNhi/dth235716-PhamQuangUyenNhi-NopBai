#cau 12: Xuất bảng cửu chương
for i in range(1, 11):          # i chạy từ 1 đến 10
    for j in range(2, 10):      # j chạy từ 2 đến 9
        line = "{0} * {1:>2} = {2:>2}".format(j, i, i*j)
        print(line, end='\t')   # in ngang, cách nhau bằng tab
    print()                     # xuống dòng sau mỗi hàng
     