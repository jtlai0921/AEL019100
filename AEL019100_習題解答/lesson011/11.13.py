# 提示使用者輸入學生人數
num_student = int(input("請輸入學生人數："))

score_list = []
for i in range(0, num_student):   # 根據學生人數決定迴圈執行的次數
    score = int(input("請輸入學生人數："))
    score_list += [score]

print("學生成績：", score_list)

# 計算及格和不及格學生人數
pass_count = fail_count = 0

for score in score_list:
    if score >= 60:
        pass_count += 1
    else:
        fail_count += 1

print("及格人數：", pass_count)
print("不及格人數：", fail_count)
