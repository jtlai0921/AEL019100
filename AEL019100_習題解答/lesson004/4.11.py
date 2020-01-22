import turtle as tutl

# 畫第一個三角形
tutl.circle(100, 360, 3)

# 提起畫筆，依照圓弧轉60度
tutl.penup()
tutl.circle(100, 60, 3)

# 放下畫筆，畫第二個三角形
tutl.pendown()
tutl.circle(100, 360, 3)
