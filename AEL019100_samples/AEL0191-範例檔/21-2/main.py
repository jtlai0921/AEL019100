# 建立sum_scores()函式
def sum_scores(scores):
    try:
        count = 0   # 累計處理的資料個數
        sum = 0
        for n in scores:
            sum += n;
            count += 1
    except TypeError:
        return 0, 0   # 傳回0, 0表示無法處理
    else:
        return sum, count   # 傳回加總結果和資料個數

scores = [70, 80, 90, 95, 100]

# 呼叫sum_scores()，傳入資料組
sum = sum_scores(scores)

print('總分', sum)
