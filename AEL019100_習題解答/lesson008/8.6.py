ch_score, en_score, math_score = input('請輸入國、英、數三科成績，成績之間加入空格：').split()
ch_score = float(ch_score)
en_score = float(en_score)
math_score = float(math_score)

if ch_score >= en_score >= math_score:
    print('國文:', ch_score)
    print('英文:', en_score)
    print('數學:', math_score)
elif ch_score >= math_score >= en_score:
    print('國文:', ch_score)
    print('數學:', math_score)
    print('英文:', en_score)
elif en_score >= ch_score >= math_score:
    print('英文:', en_score)
    print('國文:', ch_score)
    print('數學:', math_score)
elif en_score >= math_score >= ch_score:
    print('英文:', en_score)
    print('數學:', math_score)
    print('國文:', ch_score)
elif math_score >= ch_score >= en_score:
    print('數學:', math_score)
    print('國文:', ch_score)
    print('英文:', en_score)
else:
    print('數學:', math_score)
    print('英文:', en_score)
    print('國文:', ch_score)
