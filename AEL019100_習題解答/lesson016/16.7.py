import random

dice_count = [0] * 6

for i in range(100):   # 控制scores資料組的搜尋次數
    dice = random.randint(1, 6)
    print(i, dice)
    dice_count[dice - 1] += 1

total = 0
for i, count in enumerate(dice_count):
    total += count
    print(str(i + 1) + '點 - ' + str(count) + '次')

print('總共 - ' + str(total) + '次')
