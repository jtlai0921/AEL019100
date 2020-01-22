class Classroom:
    def __init__(self):
        self._students = []   # 用來儲存學生的list資料組
        self._teacher = None

    # 這個方法用來加入學生
    def add_student(self, student):
        self._students += [student]

    # 這個方法用來刪除學生
    def delete_student(self, student):
        self._students.remove(student)

    # 這個方法用來取得全部學生
    def get_all_students(self):
        return self._students

    # 這個方法用來清空教室
    def clear(self):
        self._students.clear()

    # 這個方法會傳回教室中的學生人數
    def get_student_number(self):
        return len(self._students)

    def set_teacher(self, teacher):
        self._teacher = teacher

    def get_teacher(self):
        return self._teacher
