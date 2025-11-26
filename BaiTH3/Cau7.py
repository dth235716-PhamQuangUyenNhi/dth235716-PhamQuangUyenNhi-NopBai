#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
def nam_nhuan(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def so_ngay(m, y):
    if m in (1,3,5,7,8,10,12):
        return 31
    if m in (4,6,9,11):
        return 30
    return 29 if nam_nhuan(y) else 28

def ngay_ke(d, m, y):
    d += 1
    if d > so_ngay(m, y):
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return d, m, y

def nhap_ngay():
    d = int(input("Nhập ngày: "))
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))
    return d, m, y

# --- Chương trình chính ---
d, m, y = nhap_ngay()
nd, nm, ny = ngay_ke(d, m, y)
print(f"Ngày kế tiếp là: {nd}/{nm}/{y}")