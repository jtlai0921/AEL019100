int_num = input('請輸入小於100000的整數：')
int_num = int(int_num)

if 0 <= int_num < 10:
    print('1位數')
elif int_num < 100:
    print('2位數')
elif int_num < 1000:
    print('3位數')
elif int_num < 10000:
    print('4位數')
elif int_num < 100000:
    print('5位數')
else:
    print('數字超出範圍')
