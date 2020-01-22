import random

# scores是一個List資料組，用來儲存學生姓名和成績
scores = []

for c1 in range(65, 91):   # 65~90是字母A~Z的字元碼
    for c2 in range(65, 91):
        # 把c1和c2字元碼的字元組合起來，變成學生姓名
        name = chr(c1) + chr(c2)

        # 用亂數產生三筆成績
        score1 = random.randint(0, 100)
        score2 = random.randint(0, 100)
        score3 = random.randint(0, 100)

        # 把姓名和成績組成一個資料組，存入scores
        scores += [(name, score1, score2, score3)]

# sorted_scores是一個List資料組，用來儲存排序結果
sorted_scores = []

for i in range(0, len(scores)):
    max_score = 0
    max_score_index = 0

    for j, item in enumerate(scores):
        # 計算三科總分
        sum = item[1] + item[2] + item[3]

        # 檢查是否是最高分
        if sum > max_score:
            max_score = sum
            max_score_index = j

    # 把最高分從scores資料組取出，放到sorted_scores資料組
    highest_score = scores.pop(max_score_index)
    sorted_scores += [highest_score]

# 顯示排序結果
for i, item in enumerate(sorted_scores):
    print(i, item, '總分', item[1] + item[2] + item[3])
