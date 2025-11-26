#cau 17:
n, m = 0, 100

while n != m:
    n = int(input())
    if n < 0:
        break   # thoát vòng lặp khi nhập số âm

print("n =", n)