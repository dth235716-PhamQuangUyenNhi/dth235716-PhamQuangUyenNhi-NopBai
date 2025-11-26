#cau 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập.
# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
ch = input("Nhập ký tự toán tử (+, -, *, /): ")

#Kiểm tra toán tử
if ch == '+':
    print("Kết quả:", a + b)
elif ch == '-':
    print("Kết quả:", a - b)
elif ch == '*':
    print("Kết quả:", a * b)
elif ch == '/':
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Ký tự", ch, "không phải là một toán tử")