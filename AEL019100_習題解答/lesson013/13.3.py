all_score_list = [
    [70, 80, 90, 100],
    [100, 90, 80, 70],
    [80, 90, 80, 90]
    ]

class_num, num = input('請輸入學生班級和編號（資料中間加入空格）').split()

class_num = int(class_num)
num = int(num)
print('第', class_num, '班第', num, '位同學成績：',
      all_score_list[class_num - 1][num - 1])
