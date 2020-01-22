scores = [60, 10, 90, 100, 20, 30, 80, 50, 40, 70]

sorted_scores = []

for i in range(0, len(scores)):   # 控制scores資料組的搜尋次數
    min_score = 101
    min_score_index = 0

    for j, data in enumerate(scores):   # 我們把索引變數換成j，因為上層是用i
        # 檢查是否是最低分
        if data < min_score:
            min_score = data
            min_score_index = j

    # 把最低分從scores資料組取出，放到sorted_scores資料組
    lowest_score = scores.pop(min_score_index)
    sorted_scores += [lowest_score]

print(sorted_scores)