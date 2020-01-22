import os

DATA_FILE = 'data\\friends.txt'

# 開啟讀寫資料的檔案
def open_file():
    file_path = os.path.dirname(DATA_FILE)   # 取出路徑

    # 檢查路徑是否存在
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # 開啟檔案
    if os.path.isfile(DATA_FILE):
        file = open(DATA_FILE, 'a+t')
    else:
        file = open(DATA_FILE, 'w+t')

    return file

# 把朋友資料寫入檔案
def add(file, name, gender, age, tel):
    if gender == 1:
        gender = '男'
    else:
        gender = '女'

    line = name + ' ' + gender + ' ' + str(age) + ' ' + tel + '\n'
    file.write(line)

# 關閉檔案
def close_file(file):
    file.close()

# 搜尋朋友資料
def find(file, name):
    file.seek(0, 0)
    for line in file:
        name_this_line, *others = line.split()
        if name_this_line == name:
            friend_data = [name_this_line]
            friend_data += others
            return friend_data

    return None

# 準備列出朋友清單
def iterate_start(file):
    file.seek(0, 0)

# 取得下一位朋友資料
def iterate_next(file):
    line = file.readline()
    if line == '':
        return None

    friend = line.split()
    return friend
