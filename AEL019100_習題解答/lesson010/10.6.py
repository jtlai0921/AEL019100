import random as rand   # 載入亂數需要的套件

for i in range(0, 3, 1):   # 設定執行3次
    # 用二個亂數模擬擲筊結果
    rand_num1 = rand.randint(1, 2)
    rand_num2 = rand.randint(1, 2)

    if rand_num1 != rand_num2:
        print("擲筊成功")
    else:
        print("擲筊失敗")
        break
else:
    # 當沒有用break指令跳出迴圈時執行
    print("成功三次，表示菩薩同意")
