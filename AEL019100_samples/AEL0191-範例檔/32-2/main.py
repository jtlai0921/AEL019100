import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

def combox_select(event):
    # 利用傳入的event參數取得使用者點選的項目
    selected_area = event.widget.get()
    lab_result.config(text=selected_area)

# 建立Tk視窗
tk_win = tk.Tk()
tk_win.title('Combobox')

# 取得預設字型，修改字體大小，字形維持不變
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

# 把選項存入一個一維tuple資料組
AREA_OPTIONS = ('亞洲', '美洲', '歐洲', '非洲', '大洋洲')

# 建立StringVar物件，用來記錄被點選的項目
area = tk.StringVar()

# 建立Combobox
combox = ttk.Combobox(tk_win,
                values=AREA_OPTIONS, textvariable=area,
                font=default_font)
combox.bind('<<ComboboxSelected>>', combox_select)
combox.current(0)
combox.pack(padx=10, pady=10)

# 建立一個Label物件，用來顯示結果
lab_result = tk.Label(tk_win, font=default_font,
                      fg='orange red', width=18)
lab_result.pack(padx=10, pady=(5, 10))

# 啟動GUI程式的處理迴圈
tk_win.mainloop()
