def increase(num, num_list):
    num += 1   # num中的值加1

    # 資料組num_list中的每一個值都加1
    for i in range(len(num_list)):
        num_list[i] += 1

    # 顯示結果
    print(num, num_list)

a = 1
b = [10, 11, 12]

increase(a, b)

# 顯示呼叫increase()函式之後的結果
print(a, b)
