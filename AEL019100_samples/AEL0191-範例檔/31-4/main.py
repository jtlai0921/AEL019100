import tkinter as tk

tk_win = tk.Tk()
tk_win.title('Grid排列方式')

# 建立GUI物件1
text1 = tk.StringVar(value='GUI物件1')
ent1 = tk.Entry(tk_win, textvariable=text1,
                justify=tk.CENTER)
ent1.grid(row=0, column=0,
          padx=5, pady=5, ipady=10)

# 建立GUI物件2
text2 = tk.StringVar(value='GUI物件2')
ent2 = tk.Entry(tk_win, textvariable=text2,
                justify=tk.CENTER)
ent2.grid(row=0, column=2,
          padx=5, pady=5, sticky=tk.N)

# 建立GUI物件3
text3 = tk.StringVar(value='GUI物件3')
ent3 = tk.Entry(tk_win, textvariable=text3,
                justify=tk.CENTER)
ent3.grid(row=1, column=1,
          padx=5, pady=5)

tk_win.mainloop()
