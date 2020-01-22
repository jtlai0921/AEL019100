num1 = int(input("輸入第一個正整數："))
num2 = int(input("輸入第二個正整數："))

# 比較num1和num2的大小，讓num1 <= num2
if num1 > num2:
    num1, num2 = num2, num1

for i in range(1, num1 + 1, 1):   # 公因數一定是1到num1之間的整數
    if num1 % i == 0 and num2 % i == 0:
        print(i)
