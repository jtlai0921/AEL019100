import student as stu

s = stu.Student('李大中', 200, -5, 90)   # 故意傳入錯誤的成績
print(s)   # 測試類別中的__str__()方法
print('學生成績：' + str(s.get_data()))   # 顯示成績：0, 0, 90

s.set_data('李大中', 70, 80, 90)
print('學生成績：' + str(s.get_data()))   # 顯示成績：70, 80, 90

print('學生人數：' + str(stu.Student.get_count()))   #顯示人數1
