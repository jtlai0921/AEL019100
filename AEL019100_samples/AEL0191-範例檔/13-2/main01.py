# 用來儲存所有成績的資料組
all_score_list = []

for i in range(0, 3):   # 設定第一層迴圈執行3次，每次處理一個班級
    print('第', i + 1, '班 ----------')

    # 用來儲存一個班級的成績
    score_list = []

    for j in range(0, 10):   # 第二層迴圈執行10次，每次輸入一筆成績
        score = int(input('請輸入學生成績：'))
        score_list += [score]

    # 存入這個班級的成績
    all_score_list += [score_list]

# 顯示每個班級的成績
for i, score_list in enumerate(all_score_list):
    print('第', i + 1, '班學生成績：', score_list)
