def find_max(nums):
    max = nums[0]
    for item in nums:
        if item > max:
            max = item

    return max

# 呼叫find_max()
max = find_max([-4, 4, 7, 2, 0])
print('最大值：', max)
