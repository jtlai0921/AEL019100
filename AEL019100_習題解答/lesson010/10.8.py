for i in range(1, 11, 1):
    print(i, ': ', end='')

    for j in range(1, i + 1, 1):
        if i % j == 0:
            print(j, ', ', end='')

    print()
