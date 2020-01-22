# 用來儲存所有成績的資料組
all_score_list = []

# 第一層迴圈控制年級
for grade in range(0, 6):
    # 用來儲存目前這個年級的成績
    grade_score_list = []

    # 詢問班級數
    print(grade+1, '年級班級數：', end = '')
    num_class = int(input())

    for i in range(0, num_class):   # 設定第一層迴圈執行3次，每次處理一個班級
        print('第', i + 1, '班 ----------')

        # 詢問學生人數
        num = int(input('學生人數：'))

        # 用來儲存一個班級的成績
        score_list = []

        for j in range(0, num):   # 第二層迴圈執行10次，每次輸入一筆成績
            score = int(input('請輸入學生成績：'))
            score_list += [score]

        # 存入這個班級的成績
        grade_score_list += [score_list]

    # 存入這個年級的成績
    all_score_list += [grade_score_list]

# 顯示每一位學生的成績
for i, grade_score_list in enumerate(all_score_list):
    for j, score_list in enumerate(grade_score_list):
        for k, score in enumerate(score_list):
            print('第', i+1, '年級第',
                  j+1, '班第',
                  k+1, '位學生成績：', score)
