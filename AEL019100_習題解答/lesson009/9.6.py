# 輸入考試成績
num = int(input('輸入一個整數：'))

if num % 7 != 0 and num % 13 != 0:
    print("不是7和13的公倍數")
elif num % 7 == 0 and num % 13 != 0:
    print("是7的倍數，但不是13的倍數")
elif num % 7 != 0 and num % 13 == 0:
    print("不是7的倍數，是13的倍數")
else:
    print("是7和13的公倍數")
