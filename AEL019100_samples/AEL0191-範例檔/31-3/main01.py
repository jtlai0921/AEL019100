import tkinter as tk

tk_win = tk.Tk()

# 建立GUI物件1
text1 = tk.StringVar(value='GUI物件1')
ent1 = tk.Entry(tk_win, textvariable=text1,
                justify=tk.CENTER)
ent1.grid(row=0, column=0)   # 指定放在第0列、第0欄

# 建立GUI物件2
text2 = tk.StringVar(value='GUI物件2')
ent2 = tk.Entry(tk_win, textvariable=text2,
                justify=tk.CENTER)
ent2.grid(row=0, column=2)   # 指定放在第0列、第2欄

# 建立GUI物件3
text3 = tk.StringVar(value='GUI物件3')
ent3 = tk.Entry(tk_win, textvariable=text3,
                justify=tk.CENTER)
ent3.grid(row=1, column=1)   # 指定放在第1列、第1欄

tk_win.mainloop()
