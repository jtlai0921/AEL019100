a, b, c = input('請輸入三個正整數：').split()
a = int(a)
b = int(b)
c = int(c)

while a <= 0 or b <= 0 or c <= 0:
    a, b, c = input('輸入錯誤，請輸入三個正整數：').split()
    a = int(a)
    b = int(b)
    c = int(c)

nums = [a, b, c]

for i, num in enumerate(nums):
    if i == 0:
        a = num
        continue
    elif i == 1:
        b = num
    else:
        a = num

    # 如果 a < b，把a和b對調
    if a < b:
        a, b = b, a

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

print('GCD是 ' + str(b))
