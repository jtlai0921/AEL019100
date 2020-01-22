import random

# scores是一個List資料組，用來儲存學生姓名和成績
scores = []

for c0 in range(65, 75):   # 在最前面加入A~J
    for c1 in range(65, 91):   # 65~90是字母A~Z的字元碼
        for c2 in range(65, 91):
            # 修改為c0, c1和c2字元碼的組合
            name = chr(c0) + chr(c1) + chr(c2)

            # 用亂數產生三筆成績
            score1 = random.randint(0, 100)
            score2 = random.randint(0, 100)
            score3 = random.randint(0, 100)

            # 把姓名和成績組成一個資料組，存入scores
            scores += [[name, score1, score2, score3]]

# 用氣泡排序法，依照總分，由高到低排序
for i in range(len(scores) - 1):
    for j in range(len(scores) - 1 - i):
        # 計算相鄰二個學生的成績總分
        sum1 = scores[j][1] + scores[j][2] + scores[j][3]
        sum2 = scores[j+1][1] + scores[j+1][2] + scores[j+1][3]

        # 比較成績總分，決定是否對調
        if sum1 < sum2:
            # 利用資料組的設定功能完成資料的對調
            scores[j][0], scores[j+1][0] = scores[j+1][0], scores[j][0]
            scores[j][1], scores[j+1][1] = scores[j+1][1], scores[j][1]
            scores[j][2], scores[j+1][2] = scores[j+1][2], scores[j][2]
            scores[j][3], scores[j+1][3] = scores[j+1][3], scores[j][3]

# 顯示排序結果
for i, item in enumerate(scores):
    print(i, item, '總分', item[1] + item[2] + item[3])
