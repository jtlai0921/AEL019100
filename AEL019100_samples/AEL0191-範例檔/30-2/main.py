# 載入Tkinter套件
import tkinter as tk

# 把按下按鈕要執行的程式碼寫成一個函式
def but_click():
    input_name = name.get()
    lab_result.config(text=input_name)

# 建立GUI畫面
# 第一步是建立一個Tk視窗
tk_win = tk.Tk()

# 建立一個Label物件，顯示說明文字
lab = tk.Label(tk_win, text='請輸入姓名：')
lab.pack()  # 設定在Tk視窗中顯示的位置

# 建立輸入姓名專用的變數
name = tk.StringVar()

# 建立一個Entry物件，讓使用者輸入姓名
ent_name = tk.Entry(tk_win, textvariable=name)
ent_name.pack()  # 設定在Tk視窗中顯示的位置

# 建立一個Button物件
but = tk.Button(tk_win, text='確定', command=but_click)
but.pack()  # 設定在Tk視窗中顯示的位置

# 建立一個Label物件，用來顯示結果
lab_result = tk.Label(tk_win)
lab_result.pack()  # 設定在Tk視窗中顯示的位置

# 啟動GUI程式的處理迴圈
tk_win.mainloop()
