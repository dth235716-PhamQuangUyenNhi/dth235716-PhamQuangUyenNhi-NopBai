#cau 13: Cho biết bao nhiêu dấu * được in ra trên màn hình
a = 0
count = 0   # biến đếm số *

while a < 100:
    print('*', end='')
    count += 1
    a += 1   # cần tăng a lên, nếu không sẽ lặp vô hạn

print()  # xuống dòng
print("Số lượng dấu * được in ra là:", count)