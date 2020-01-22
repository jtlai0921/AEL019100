# 載入shape套件
import shape as sh

circle_radius = [1, 2, 3, 4, 5]
circles = []   # 儲存Circle物件的資料組

# 用for迴圈建立5個Circle物件，把它們存入circles資料組
for radius in circle_radius:
    c = sh.Circle(radius)
    circles += [c]

# 顯示Circle物件的面積
print('\n圓面積: ', end='')
for c in circles:
    # 利用字串物件的format()方法設定取2位小數
    print('{:.2f}'.format(c.get_area()), end=' ')

# 顯示Circle物件的周長
print('\n圓周長: ', end='')
for c in circles:
    # 利用字串物件的format()方法設定取2位小數
    print('{:.2f}'.format(c.get_perimeter()), end=' ')
