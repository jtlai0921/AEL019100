gender, age = input('請輸入您的性別和年齡，資料之間請加入空格：').split()
age = int(age)

if gender == '男':
    if age > 35:
        print('趕快結婚')
    elif 30 <= age <= 35:
        print('適婚年齡')
    else:
        print('未達適婚年齡')
else:   # 女生的情況
    if age >= 30:
        print('趕快結婚')
    elif 25 <= age <= 30:
        print('適婚年齡')
    else:
        print('未達適婚年齡')
