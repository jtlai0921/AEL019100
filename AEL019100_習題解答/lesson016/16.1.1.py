scores = [60, 10, 90, 100, 20, 30, 80, 50, 40, 70]

sorted_scores = []

for i in range(0, len(scores)):   # 控制scores資料組的搜尋次數
    max_score = 0
    max_score_index = 0

    for j, data in enumerate(scores):   # 我們把索引變數換成j，因為上層是用i
        # 檢查是否是最高分
        if data > max_score:
            max_score = data
            max_score_index = j

    # 把最高分從scores資料組取出，放到sorted_scores資料組
    highest_score = scores.pop(max_score_index)
    sorted_scores += [highest_score]

print(sorted_scores)