a, b = input('請輸入二個正整數：').split()
a = int(a)
b = int(b)

# 如果 a < b，把a和b對調
if a < b:
    a, b = b, a

r = a % b

# While迴圈會計算到r=0才會停止
while r != 0:
    a = b
    b = r
    r = a % b

print('GCD是 ' + str(b))
