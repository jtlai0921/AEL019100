# 必須先把學生成績儲存到scores資料組裏頭
scores = [50, 40, 90, 10, 20, 80, 30, 70, 60]

# sorted_scores資料組用來儲存排序後的成績
sorted_scores = []

for i in range(0, len(scores)):   # 控制scores資料組的搜尋次數
    max_score = 0
    max_score_index = 0

    # 我們把索引變數換成j，因為上層是用i
    for j, data in enumerate(scores):
        # 檢查是否是最高分
        if data > max_score:
            max_score = data
            max_score_index = j

    # 把最高分從scores資料組取出，放到sorted_scores資料組
    highest_score = scores.pop(max_score_index)
    sorted_scores += [highest_score]

print(sorted_scores)