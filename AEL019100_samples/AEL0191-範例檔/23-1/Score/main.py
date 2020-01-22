# 載入前面步驟建立的scocheck模組程式檔，並指定簡稱sc
import scocheck as sc

# 建立一個成績資料組
scores = [80, 95, 70, 40, 65, 55, 75, 50, 90]

# 呼叫scocheck模組中的函式處理成績資料組，並且顯示結果
print('最高分：', str(sc.highest(scores)))
print('最低分：', str(sc.lowest(scores)))
print('平均分數：', str(sc.average(scores)))
print('及格：', list(sc.get_pass_scores(scores)))
print('不及格：', list(sc.get_fail_scores(scores)))
