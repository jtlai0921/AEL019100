import os

FILE = 'd:\\data.bin'  # 指定檔案路徑和檔名

# 如果檔案已經存在，就停止執行
if os.path.isfile(FILE):
    print('錯誤：' + FILE + '已經存在')
    exit()

# 用二進位模式開啟檔案
with open(FILE, 'w+b') as file:
    # 寫入1到10000的整數
    for i in range(1, 10001):
        # 把i的值轉換成4個byte的二進位格式，然後寫入檔案
        int_bytes = i.to_bytes(4, 'big')
        file.write(int_bytes)
