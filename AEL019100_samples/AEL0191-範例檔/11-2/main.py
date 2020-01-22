# 提示使用者輸入學生人數
num_student = int(input("請輸入學生人數："))

score_list = []
for i in range(0, num_student):   # 利用學生人數決定迴圈執行的次數
    score = int(input("請輸入學生成績："))
    score_list += [score]

print("學生成績：", score_list)
