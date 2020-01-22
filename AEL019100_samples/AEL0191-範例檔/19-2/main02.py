import random

# students是一個dict資料組，用來儲存學生資料
students = {}
id = 1

for c in range(65, 91):   # 65~90是字母A~Z的字元碼
    # 把c字元碼的字元重複三次當成學生姓名，例如'AAA'
    name = chr(c) + chr(c) + chr(c)

    # 用亂數產生三筆成績
    score1 = random.randint(0, 100)
    score2 = random.randint(0, 100)
    score3 = random.randint(0, 100)

    # 建立學號
    if id < 10:
        id_string = 'T00' + str(id)
    else:
        id_string = 'T0' + str(id)

    # 把學號當成key，存入學生資料
    students[id_string] = (name, score1, score2, score3)

    # 完成20位學生後就停止
    id += 1
    if id > 20:
        break;

input_id = input('請輸入學號（T001 ~ T020）：')
print(students[input_id])
