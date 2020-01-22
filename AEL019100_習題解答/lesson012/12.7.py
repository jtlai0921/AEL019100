num_list = [n for n in range(1, 101) if n % 2 == 0 and n % 6 != 0]

for i, data in enumerate(num_list, 1):
    print(i, data)
