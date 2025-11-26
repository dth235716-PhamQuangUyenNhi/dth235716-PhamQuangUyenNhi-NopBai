#cau 10:  Tính dãy số
import math

#Nhập x và n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

#Tính S(x, n)
S = 0
for i in range(1, n + 1):
    S += x**i / math.factorial(i)

print("Giá trị S(x, n) =", S)