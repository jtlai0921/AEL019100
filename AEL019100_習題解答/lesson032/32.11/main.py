import tkinter as tk
import tkinter.font as tkfont

# 按下按鈕後要執行的函式
def but_click():
    # 姓名
    result = name.get() + ', '

    # 性別
    selected_gender = gender.get()
    result += GENDER_OPTIONS[selected_gender][0] + ', '

    # 生日
    result += str(year.get()) + '/' + str(month.get()) + '/' + str(day.get()) + ', '

    # 興趣
    if basketball.get():
        result += '籃球'
    if swim.get():
        result += '游泳'
    if music.get():
        result += '音樂'
    if bicycle.get():
        result += '騎單車'
    if reading.get():
        result += '閱讀'

    # 顯示結果
    lab_result.config(text=result)

# 建立Tk視窗
tk_win = tk.Tk()
tk_win.title('輸入個人資料')

# 取得預設字型，修改字體大小，字形維持不變
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

# 姓名欄位的Frame
frame_name = tk.Frame()
frame_name.pack(padx=10, pady=(10, 5), anchor=tk.NW)

lab = tk.Label(frame_name, text='姓名：')
lab.pack(side=tk.LEFT)

name = tk.StringVar()
ent_name = tk.Entry(frame_name, textvariable=name,
                width=15, font=default_font)
ent_name.pack(side=tk.LEFT)

# 性別欄位的Frame
frame_gender = tk.Frame()
frame_gender.pack(padx=10, pady=(10, 5), anchor=tk.NW)

lab = tk.Label(frame_gender, text='性別：')
lab.pack(side=tk.LEFT)

frame_gender_options = tk.Frame()
frame_gender_options.pack(in_=frame_gender)

GENDER_OPTIONS = (('男生', 0), ('女生', 1))
gender = tk.IntVar()
gender.set(0)
for item, value in GENDER_OPTIONS:
    radbut = tk.Radiobutton(frame_gender_options,
             text=item, variable=gender, value=value)
    radbut.pack()

# 生日欄位的Frame
frame_birthday = tk.Frame()
frame_birthday.pack(padx=10, pady=(10, 5))

lab = tk.Label(frame_birthday, text='生日（年月日）：')
lab.pack(side=tk.LEFT)

year = tk.IntVar()
year.set(2000)
spinbox_year = tk.Spinbox(frame_birthday,
            from_=1950, to=2015, width=6,
            textvariable=year, font=default_font)
spinbox_year.pack(padx=10, pady=10, side=tk.LEFT)

month = tk.IntVar()
month.set(1)
spinbox_month = tk.Spinbox(frame_birthday,
            from_=1, to=12, width=2,
            textvariable=month, font=default_font)
spinbox_month.pack(padx=10, pady=10, side=tk.LEFT)

day = tk.IntVar()
day.set(1)
spinbox_day = tk.Spinbox(frame_birthday,
            from_=1, to=31, width=2,
            textvariable=day, font=default_font)
spinbox_day.pack(padx=10, pady=10, side=tk.LEFT)

# 興趣欄位的Frame
frame_hobby = tk.Frame()
frame_hobby.pack(padx=10, pady=(10, 5), anchor=tk.W)

lab = tk.Label(frame_hobby, text='興趣：')
lab.pack(side=tk.LEFT)

frame_hobby_options = tk.Frame()
frame_hobby_options.pack(in_=frame_hobby, anchor=tk.W)

basketball = tk.IntVar()
chkbut_basketball = tk.Checkbutton(frame_hobby_options, text='籃球',
                             variable=basketball, anchor=tk.W)
chkbut_basketball.pack(padx=10, pady=5, fill=tk.X)

swim = tk.IntVar()
chkbut_swim = tk.Checkbutton(frame_hobby_options, text='游泳',
                             variable=swim, anchor=tk.W)
chkbut_swim.pack(padx=10, pady=5, fill=tk.X)

music = tk.IntVar()
chkbut_music = tk.Checkbutton(frame_hobby_options, text='音樂',
                             variable=music, anchor=tk.W)
chkbut_music.pack(padx=10, pady=5, fill=tk.X)

bicycle = tk.IntVar()
chkbut_bicycle = tk.Checkbutton(frame_hobby_options, text='騎單車',
                             variable=bicycle, anchor=tk.W)
chkbut_bicycle.pack(padx=10, pady=5, fill=tk.X)

reading = tk.IntVar()
chkbut_reading = tk.Checkbutton(frame_hobby_options, text='閱讀',
                             variable=reading, anchor=tk.W)
chkbut_reading.pack(padx=10, pady=5, fill=tk.X)

# 建立一個Button物件
but = tk.Button(tk_win, text='確定', command=but_click,
                font=default_font, fg='blue', bg='sky blue', padx=15)
but.pack(padx=10, pady=5)

# 建立一個Label物件，用來顯示結果
lab_result = tk.Label(tk_win, font=default_font, fg='orange red')
lab_result.pack(padx=10, pady=5)

# 啟動GUI程式的處理迴圈
tk_win.mainloop()
