import campus as ca

# 這個函式用來顯示儲存學生物件的list資料組
def show_students(classroom1, classroom2):
    print('第一個教室：')
    print('教師：' + str(classroom1.get_teacher().get_data()))
    for s in classroom1.get_all_students():
        print(s.get_data())
    print('第二個教室：')
    print('教師：' + str(classroom2.get_teacher().get_data()))
    for s in classroom2.get_all_students():
        print(s.get_data())

# 建立測試用的學生
student1 = ca.Student('學生1', 100, 100, 100)
student2 = ca.Student('學生2', 90, 90, 90)
student3 = ca.Student('學生3', 80, 80, 80)
student4 = ca.Student('學生4', 70, 70, 70)
student5 = ca.Student('學生5', 60, 60, 60)

# 建立教室
classroom1 = ca.Classroom()
classroom2 = ca.Classroom()

# 建立教師
t1 = ca.Teacher('王小玉', 32)
t2 = ca.Teacher('李大龍', 40)

classroom1.set_teacher(t1)
classroom2.set_teacher(t2)

# 把學生加入教室物件
print('----- 學生進入教室 -----')
classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)

classroom2.add_student(student4)
classroom2.add_student(student5)

# 顯示每一個教室的學生
show_students(classroom1, classroom2)

# 把學生從教室刪除
print('----- 學生離開教室 -----')
classroom1.delete_student(student1)
classroom2.delete_student(student4)

# 顯示每一個教室的學生
show_students(classroom1, classroom2)

# 清空教室
print('----- 放學後 -----')
classroom1.clear()
classroom2.clear()

# 顯示每一個教室的學生
show_students(classroom1, classroom2)
