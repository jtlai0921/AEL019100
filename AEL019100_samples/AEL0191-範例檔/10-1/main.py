import random as rand   # 載入亂數套件

for i in range(0, 5, 1):   # 設定執行5次
    # 產生一個介於1和100（含）之間的亂數
    rand_num = rand.randint(1, 100)

    # 根據亂數決定檢測結果
    if rand_num < 90:
        print("通過檢測")
    else:
        print("檢測失敗")
        break
else:
    # 當沒有用break指令跳出迴圈時執行
    print("通過品管檢測")
