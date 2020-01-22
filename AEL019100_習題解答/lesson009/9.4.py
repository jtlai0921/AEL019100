# 輸入考試成績
score1 = int(input('輸入第一科成績：'))
score2 = int(input('輸入第二科成績：'))
score3 = int(input('輸入第三科成績：'))

if score1 < 60 or score2 < 60 or score3 < 60:
    print("有成績不及格")
else:
    print("全部及格")
