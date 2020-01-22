def progression(start, stop, step = 1):   # 設定step參數的預設值是1
    # nums資料組用來儲存產生的等差數列
    nums = []

    # 檢查是否三個參數都是整數
    # 如果不是，會直接傳回空的結果
    if (not isinstance(start, int)) or \
       (not isinstance(stop, int)) or \
       (not isinstance(step, int)):
        return nums

    # 判斷start、stop和step的關係是否正確
    # 然後利用while迴圈產生等差數列
    if start < stop and step > 0:
        nums += [start]
        n = start + step
        while n < stop:
            nums += [n]
            n += step
    elif start > stop and step < 0:
        nums += [start]
        n = start + step
        while n > stop:
            nums += [n]
            n += step

    return nums   # 傳回結果

nums1 = progression(0, 5)        # 結果：[0, 1, 2, 3, 4]
nums2 = progression(0, 10, 2)    # 結果：[0, 2, 4, 6, 8]
nums3 = progression(5, 0, -1)    # 結果：[5, 4, 3, 2, 1]
