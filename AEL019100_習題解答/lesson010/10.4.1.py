sum = 0
for i in range(1, 100000001, 1):
    if i % 43 == 0:
        sum += i

print(sum)
