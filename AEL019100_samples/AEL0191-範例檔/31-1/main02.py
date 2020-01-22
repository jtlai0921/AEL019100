import tkinter as tk

# 建立Tk視窗
tk_win = tk.Tk()
tk_win.geometry('200x100')
tk_win.title('Pack排列方式')

# 建立GUI物件1
text1 = tk.StringVar(value='GUI物件1')
ent1 = tk.Entry(tk_win, width=10,textvariable=text1,
                justify=tk.CENTER)
ent1.pack(side=tk.TOP)

# 建立GUI物件2
text2 = tk.StringVar(value='GUI物件2')
ent2 = tk.Entry(tk_win, width=10, textvariable=text2,
                justify=tk.CENTER)
ent2.pack(side=tk.TOP, expand=True)

# 啟動GUI處理迴圈
tk_win.mainloop()
