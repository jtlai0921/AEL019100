# 載入math套件，我們要用它的圓周率pi值
import math

# 把圓的半徑儲存在一個list資料組
circle_radius = [1, 2, 3, 4, 5]

print('\n圓面積: ', end='')
for radius in circle_radius:
    area = math.pi * radius * radius   # 計算圓面積的公式

    # 利用字串物件的format()方法設定取2位小數
    print('{:.2f}'.format(area), end=' ')

print('\n圓周長: ', end='')
for radius in circle_radius:
    perimeter = 2 * math.pi * radius   # 計算圓周長度的公式

    # 利用字串物件的format()方法設定取2位小數
    print('{:.2f}'.format(perimeter), end=' ')
