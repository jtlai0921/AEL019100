# 詢問班級數
num_class = int(input('班級數：'))

# 用來儲存所有成績的資料組
all_score_list = []

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
    all_score_list += [score_list]

# 顯示每個班級的成績
for i, score_list in enumerate(all_score_list):
    print('第', i + 1, '班學生成績：', score_list)

# all_score_list是儲存學生成績的二維資料組
a_count_list = []   # 儲存A的List資料組
b_count_list = []   # 儲存B的List資料組
c_count_list = []   # 儲存C的List資料組
d_count_list = []   # 儲存D的List資料組
e_count_list = []   # 儲存E的List資料組

for score_list in all_score_list:
    a_count = 0   # 累計A的人數
    b_count = 0   # 累計B的人數
    c_count = 0   # 累計C的人數
    d_count = 0   # 累計D的人數
    e_count = 0   # 累計E的人數

    # 用For迴圈檢查目前班級的每一筆成績
    for score in score_list:
        if 90 <= score <= 100:
            a_count += 1
        elif 80 <= score < 90:
            b_count += 1
        elif 70 <= score < 80:
            c_count += 1
        elif 60 <= score < 70:
            d_count += 1
        else:
            e_count += 1

    # 把累計結果存入資料組
    a_count_list += [a_count]
    b_count_list += [b_count]
    c_count_list += [c_count]
    d_count_list += [d_count]
    e_count_list += [e_count]

for i in range(0, len(a_count_list)):
    print('第', i + 1, '班A人數', a_count_list[i],
          'B人數', b_count_list[i],
          'C人數', c_count_list[i],
          'D人數', d_count_list[i],
          'E人數', e_count_list[i])
