import tkinter as tk
import tkinter.font as tkfont

# 選擇Spinbox的選項時會執行這個函式
def spinbox_select():
    selected_month = month.get()
    lab_result.config(text=selected_month)

# 建立Tk視窗
tk_win = tk.Tk()
tk_win.title('選擇月份')

# 取得預設字型，修改字體大小，字形維持不變
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

# 建立IntVar物件，用來記錄目前選擇的月份
month = tk.IntVar()
month.set(1)   # 預設值

# 建立Spinbox
spinbox = tk.Spinbox(tk_win,
            from_=1, to=12,   # 設定數字的起始值和結束值
            textvariable=month, command=spinbox_select,
            font=default_font)
spinbox.pack(padx=10, pady=10)

# 建立一個Label物件，用來顯示結果
lab_result = tk.Label(tk_win, font=default_font, fg='orange red')
lab_result.pack(padx=10, pady=(5, 10))

# 啟動GUI程式的處理迴圈
tk_win.mainloop()
