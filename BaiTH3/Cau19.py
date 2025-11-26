#cau 19:
import math

# Nhập dữ liệu
x = float(input("Nhập x (số thực): "))
n = int(input("Nhập n (số nguyên không âm): "))

S = 0
for k in range(n+1):   # k chạy từ 0 → n
    S += (x**(2*k+1)) / math.factorial(2*k+1)

print("Giá trị S(x,n) =", S)