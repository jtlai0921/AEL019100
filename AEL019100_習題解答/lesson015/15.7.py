num1, num2 = input('請輸入二個介於0和100之間的數字：').split()
num1 = float(num1)
num2 = float(num2)

if num1 < 0 or num1 > 100 or num2 < 0 or num2 > 100:
    print('數字範圍不符合條件')
else:
    average = (num1 + num2) / 2;
    print("二個數字的平均：", average)
