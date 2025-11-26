#cau 15:
# (a) range(5)
# Bắt đầu từ 0, kết thúc trước 5, bước mặc định là 1
# => 0, 1, 2, 3, 4

# (b) range(5, 10)
# Bắt đầu từ 5, kết thúc trước 10, bước mặc định là 1
# => 5, 6, 7, 8, 9

# (c) range(5, 20, 3)
# Bắt đầu từ 5, kết thúc trước 20, bước nhảy 3
# => 5, 8, 11, 14, 17

# (d) range(20, 5, -1)
# Bắt đầu từ 20, giảm dần mỗi bước 1, dừng trước 5
# => 20, 19, 18, ..., 6

# (e) range(20, 5, -3)
# Bắt đầu từ 20, giảm dần mỗi bước 3, dừng trước 5
# => 20, 17, 14, 11, 8

# (f) range(10, 5)
# Mặc định bước = 1 (tăng), nhưng start=10 > stop=5 nên không chạy
# => []

# (g) range(0)
# Start=0, stop=0 => không có phần tử nào
# => []

# (h) range(10, 101, 10)
# Bắt đầu từ 10, tăng 10 mỗi bước, dừng trước 101
# => 10, 20, 30, ..., 100

# (i) range(10, -1, -1)
# Bắt đầu từ 10, giảm dần mỗi bước 1, dừng trước -1
# => 10, 9, 8, ..., 0

# (j) range(-3, 4)
# Bắt đầu từ -3, tăng mỗi bước 1, dừng trước 4
# => -3, -2, -1, 0, 1, 2, 3

# (k) range(0, 10, 1)
# Bắt đầu từ 0, tăng mỗi bước 1, dừng trước 10
# => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9