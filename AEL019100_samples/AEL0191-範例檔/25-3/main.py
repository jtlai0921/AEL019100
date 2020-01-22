import os

FILE = 'd:\\data.bin'  # 指定檔案路徑和檔名

# 如果檔案已經存在，就停止執行
if os.path.isfile(FILE):
    print('錯誤：' + FILE + '已經存在')
    exit()

# 用二進位模式開啟檔案
with open(FILE, 'w+b') as file:
    # 寫入1到100的整數
    for i in range(1, 101):
        # 把i的值轉換成4個byte的二進位格式，然後寫入檔案
        int_bytes = i.to_bytes(4, 'big')
        file.write(int_bytes)

    file.seek(0)  # 把讀取指標設定到檔案開頭

    while True:
        # 每一次讀取4個byte
        int_bytes = file.read(4)

        # 如果int_bytes是空字串，not int_bytes會是True，表示檔案結尾
        if not int_bytes:
            break

        # 把byte值轉換成整數，並顯示結果
        num = int.from_bytes(int_bytes, 'big')
        print(num)

os.remove(FILE)  # 刪除檔案
