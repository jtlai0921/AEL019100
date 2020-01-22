# 學生成績資料組
scores = [90, 50, 80, 40, 100]

# 建立篩選不及格成績的lambda函式
f = lambda x: True if x < 60 else False

# 呼叫filter()函式，傳入篩選函式和資料組
fail_scores = filter(f, scores)

# 顯示篩選後的成績，執行結果：[50, 40]
for item in fail_scores:
    print(item)
