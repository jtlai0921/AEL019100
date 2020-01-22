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

# all_score_list是儲存學生成績的二維資料組
pass_count_list = []   # 儲存及格人數的List資料組
fail_count_list = []   # 儲存不及格人數的List資料組

for score_list in all_score_list:
    pass_count = 0   # 累計目前班級的及格人數
    fail_count = 0   # 累計目前班級的不及格人數

    # 用For迴圈檢查目前班級的每一筆成績
    for score in score_list:
        if score >= 60:
            pass_count += 1
        else:
            fail_count += 1

    # 把累計結果存入資料組
    pass_count_list += [pass_count]
    fail_count_list += [fail_count]

for i in range(0, len(pass_count_list)):
    print('第', i + 1, '班及格人數', pass_count_list[i],
          '不及格人數', fail_count_list[i])
