num_list = [n for n in range(1, 101)]
print("原來的資料組：")
print(num_list)

# 用For迴圈複製List資料組
num_list_copy1 = []
for item in num_list:
    num_list_copy1.insert(0, item)

print("複製的資料組：")
print(num_list_copy1)

# 用Slice複製List資料組
num_list_copy2 = num_list[::-1]

print("複製的資料組：")
print(num_list_copy2)

