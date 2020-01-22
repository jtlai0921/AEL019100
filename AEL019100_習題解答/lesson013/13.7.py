# 用來儲存成績的資料組
score_list = []

for i in range(0, 10):
    score = int(input('請輸入學生成績：'))
    score_list += [score]

# 找出不及格的成績
for i, score in enumerate(score_list):
    if score < 60:
        print('學號：', i + 1, ', 成績：', score)
        
