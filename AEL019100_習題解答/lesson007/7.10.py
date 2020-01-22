a, b, c = input('請輸入一元二次方程式的a, b, c係數：').split()
a = float(a)
b = float(b)
c = float(c)

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('x的解：', x1, x2)
