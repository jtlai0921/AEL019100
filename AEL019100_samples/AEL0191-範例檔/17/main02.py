a, b = input('請輸入二個正整數：').split()
a = int(a)
b = int(b)

while a > 0:
    # 如果 a < b，把a和b對調
    if a < b:
        a, b = b, a

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    a = input('請輸入下一個正整數（0或負數表示結束）：')
    a = int(a)

print('GCD是 ' + str(b))
