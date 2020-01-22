# 詢問班級數
num_class = int(input('班級數：'))

# 用來儲存所有成績的資料組
all_score_list = []

for i in range(0, num_class):   # 設定第一層迴圈執行num_class次
    print('第', i + 1, '班 ----------')

    # 詢問學生人數
    num = int(input('學生人數：'))

    # 用來儲存一個班級的成績
    score_list = []

    for j in range(0, num):   # 第二層迴圈執行num次，每次輸入一筆成績
        score = int(input('請輸入學生成績：'))
        score_list += [score]

    # 存入這個班級的成績
    all_score_list += [score_list]

# 顯示每個班級的成績
for i, score_list in enumerate(all_score_list):
    print('第', i + 1, '班學生成績：', score_list)
