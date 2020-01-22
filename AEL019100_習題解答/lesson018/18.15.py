nums_str = input('請輸入三個數，數字之間加入空格：').split()

nums = []   # 儲存得到的三個數

# 用while迴圈應付數字少於三個的情況。
while True:
    for n in nums_str:
        if n.isdigit():   # 檢查是不是整數
            nums += [int(n)]
        else:   # 檢查是不是小數
            # 找出小數點的位置
            decimal_pnt_position = n.find('.')

            if decimal_pnt_position < 0:
                continue

            # 取出整數和小數
            int_part = n[:decimal_pnt_position]
            decimal_part = n[decimal_pnt_position + 1:]

            # 檢查整數和小數是否都是數字
            if int_part.isdigit() and decimal_part.isdigit():
                nums += [float(n)]

        # 如果已經得到三個數字，就離開迴圈。
        if len(nums) == 3:
            break;

    # 如果數字少於三個，提示使用者繼續輸入。
    if len(nums) < 3:
        nums_str = input('請繼續輸入：').split()
    else:
        break;

print(nums)
