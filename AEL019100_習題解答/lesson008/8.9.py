type_AB, score = input('請輸入學生身分和成績，資料之間請加入空格：').split()
score = int(score)

if type_AB == 'A':
    if 90 <= score <= 100:
        score_level = 'A'
    elif score >= 80:
        score_level = 'B'
    elif score >= 70:
        score_level = 'C'
    elif score >= 60:
        score_level = 'D'
    else:
        score_level = 'E'
elif type_AB == 'B':
    if 85 <= score <= 100:
        score_level = 'A'
    elif score >= 75:
        score_level = 'B'
    elif score >= 65:
        score_level = 'C'
    elif score >= 55:
        score_level = 'D'
    else:
        score_level = 'E'
else:
    print('學生身分錯誤')

print('成績等級：', score_level)
