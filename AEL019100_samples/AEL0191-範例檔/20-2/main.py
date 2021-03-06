# 換成用資料組的方式接收數字字串。
nums_str = input('請輸入三個數，數字之間加入空格：').split()

nums = []   # 儲存得到的三個數。

# 用while迴圈應付數字少於三個的情況。
while True:
    for n in nums_str:
        # 嘗試將字串轉換成整數
        # 如果發生ValueError，就跳到下一個字串
        try:
            n = int(n)
        except ValueError:
            continue

        nums += [n]

        # 如果已經得到三個數字，就離開迴圈。
        if len(nums) == 3:
            break;

    # 如果數字少於三個，提示使用者繼續輸入。
    if len(nums) < 3:
        nums_str = input('請繼續輸入：').split()
    else:
        break;

print(nums)
