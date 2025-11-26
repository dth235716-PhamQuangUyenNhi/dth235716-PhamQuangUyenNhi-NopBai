#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
#(vd: n=35 => Ba mươi lăm, n=5 => năm). 
def doc_so(n):
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:   #số 1 chữ số
        return hang_don_vi[n]

    chuc = n // 10
    donvi = n % 10

    if donvi == 0:
        return hang_chuc[chuc]
    elif donvi == 1 and chuc > 1:
        return hang_chuc[chuc] + " mốt"
    elif donvi == 5 and chuc > 0:
        return hang_chuc[chuc] + " lăm"
    else:
        return hang_chuc[chuc] + " " + hang_don_vi[donvi]


#Nhập số và in ra cách đọc
n = int(input("Nhập số có tối đa 2 chữ số: "))
if 0 <= n < 100:
    print("Cách đọc:", doc_so(n))
else:
    print("Vui lòng nhập số từ 0 đến 99")