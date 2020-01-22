num_list = [n for n in range(1, 101)]
print("原來的資料組：")
print(num_list)

# 用單行For迴圈複製List資料組
num_list_copy1 = [data for i, data in enumerate(num_list) if i % 3 == 0]

print("複製的資料組：")
print(num_list_copy1)

# 用Slice複製List資料組
num_list_copy2 = num_list[::3]

print("複製的資料組：")
print(num_list_copy2)

