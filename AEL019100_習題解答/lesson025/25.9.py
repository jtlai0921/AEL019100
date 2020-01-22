import os

FILE = 'd:\\data.txt'  # 指定檔案路徑和檔名

# 如果檔案已經存在，就停止執行
if os.path.isfile(FILE):
    print('錯誤：' + FILE + '已經存在')
    exit()

# 用文字模式開啟檔案
with open(FILE, 'w+t') as file:
    # 寫入1到10000的整數
    for i in range(1, 10001):
        file.write(str(i) + '\n')

