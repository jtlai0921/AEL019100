import campus as ca

# 這個函式用來顯示教室中的學生
def show_students(classroom1, classroom2):
    print('第一個教室：')
    for s in classroom1.get_all_students():
        print(s.get_data())

    print('第二個教室：')
    for s in classroom2.get_all_students():
        print(s.get_data())

# 建立學生物件
student1 = ca.Student('學生1', 100, 100, 100)
student2 = ca.Student('學生2', 90, 90, 90)
student3 = ca.Student('學生3', 80, 80, 80)
student4 = ca.Student('學生4', 70, 70, 70)
student5 = ca.Student('學生5', 60, 60, 60)

# 建立教室物件
classroom1 = ca.Classroom()
classroom2 = ca.Classroom()

# 把學生加入教室
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
