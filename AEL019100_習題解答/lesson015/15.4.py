score_list = []

print('請輸入10筆成績')
for i in range(10):
    score = int(input('第' + str(i + 1) + '筆成績：'))
    score_list += [score]

# 找出最高分和最低分
max_score = -1
min_score = 101
print('學生成績：')
for score in score_list:
    print(score, ' ', end='')

    if score > max_score:
        max_score = score

    if score < min_score:
        min_score = score

print()
print('最高分：', max_score)
print('最低分：', min_score)
