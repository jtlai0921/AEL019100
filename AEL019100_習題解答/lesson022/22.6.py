def fun():
    try:
        fun.__count += 1
    except AttributeError:
        fun.__count = 1

    print(fun.__count)

for i in range(10):
    fun()
