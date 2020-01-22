year = int(input('請輸入一個西元年：'))

if year % 4 == 0 and year % 100 != 0:
    print(year, '是閏年')
elif year % 400 == 0:
    print(year, '是閏年')
else:
    print(year, '是平年')
