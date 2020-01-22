num_list = [n for n in range(1, 101)]
print("原來的資料組：")
print(num_list)

# 用For迴圈複製List資料組
num_list_copy1 = []
for item in num_list:
    num_list_copy1 += [item]

print("複製的資料組：")
print(num_list_copy1)

# 用單行For迴圈複製List資料組
num_list_copy2 = [item for item in num_list]

print("複製的資料組：")
print(num_list_copy2)

# 用Slice複製List資料組
num_list_copy3 = num_list[:]

print("複製的資料組：")
print(num_list_copy3)

