import random

color_balls = ['red', 'yellow', 'black', 'green', 'orange']
count_black_ball = 0

for i in range(100):   # 控制scores資料組的搜尋次數
    selected_ball = random.sample(color_balls, 2)
    if 'black' in selected_ball:
        count_black_ball += 1

print('黑色球被選中的次數：' + str(count_black_ball) + ' 次')
