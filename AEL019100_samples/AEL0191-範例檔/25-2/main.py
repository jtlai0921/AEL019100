import os

FILE = 'd:\\note.txt'  # 指定檔案路徑和檔名

# 如果檔案已經存在，就停止執行
if os.path.isfile(FILE):
    print('錯誤：' + FILE + '已經存在')
    exit()

with open(FILE, 'w+t') as file:
    # 寫入資料
    for i in range(1, 11):
        line = '這是第' + str(i) + '行\n'
        file.write(line)

    file.seek(0)  # 把讀取指標設定到檔案開頭

    # 讀取每一行並顯示
    for line in file:
        print(line)

os.remove(FILE)  # 刪除檔案
