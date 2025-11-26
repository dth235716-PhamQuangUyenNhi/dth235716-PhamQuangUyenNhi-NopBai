#cau 9:
import math

n = int(input("Nhập n: "))
s = 0
for i in range(n):
    s = math.sqrt(2 + s)   #mỗi lần thêm 1 căn bậc 2 với số 2

print(f"S({n}) = {s}")