# 載入模組檔
import friend as fr

file = fr.open_file()

if file is None:
    exit()

# 使用迴圈讓使用者重複操作
while True:
    # 顯示選項
    print('請選擇以下功能：\n')   # '\n'是換行符號，多加一行空白
    print('1) 加入新朋友')
    print('2) 用姓名搜尋')
    print('3) 用電話搜尋')
    print('4) 列出朋友清單')
    print('5) 清除通訊錄')
    print('6) 結束\n')
    op = input('輸入選項：')

    # 根據使用者輸入的選項，執行對應的功能
    if op == '1':
        # 例外錯誤檢查
        try:
            name, gender, age, tel, addr = input(
                '請輸入朋友姓名、性別(1男生、2女生)、年齡、電話、住址'
                + '，資料用空白分隔\n').split()
            gender = int(gender)
            age = int(age)
        except ValueError:
            print('資料格式錯誤\n')
        else:
            fr.add(file, name, gender, age, tel, addr)
            print('加入成功\n')

    elif op == '2':
        name = input('請輸入朋友姓名\n')
        friend_data = fr.find(file, name)
        if not friend_data:   # friend_data是None
            print('沒有找到\n')
        else:
            print(friend_data, '\n')

    elif op == '3':
        tel = input('請輸入朋友的電話\n')
        friend_data = fr.find_by_tel(file, tel)
        if not friend_data:   # friend_data是None
            print('沒有找到\n')
        else:
            print(friend_data, '\n')

    elif op == '4':
        fr.iterate_start(file)
        while True:
            my_friend = fr.iterate_next(file)
            if not my_friend:  # my_friend是None:
                break

            print(my_friend)
        print()

    elif op == '5':
        file = fr.clear(file)   # 執行後必須更新檔案物件

    elif op == '6':
        fr.close_file(file)
        break

    else:
        print('選項錯誤')
