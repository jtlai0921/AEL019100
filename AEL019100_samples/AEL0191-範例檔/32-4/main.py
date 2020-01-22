import tkinter as tk
import tkinter.font as tkfont

# 把按下按鈕後要執行的程式碼寫成一個函式
def but_click():
    selected_options = ''

    # 檢查Checkbutton是否被勾選
    # 如果有被勾選，取得它的項目名稱，加入selected_options
    if asia.get():
        selected_options += chkbut_asia.cget('text')
    if americas.get():
        selected_options += chkbut_americas.cget('text')
    if europe.get():
        selected_options += chkbut_europe.cget('text')
    if africa.get():
        selected_options += chkbut_africa.cget('text')
    if oceania.get():
        selected_options += chkbut_oceania.cget('text')

    lab_result.config(text=selected_options)

# 建立Tk視窗
tk_win = tk.Tk()
tk_win.title('Checkbutton')

# 取得預設字型，修改字體大小，字形維持不變
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

# 建立Checkbutton，每一個Checkbutton都要有各自的IntVar物件
asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(tk_win, text='亞洲',
                             variable=asia, anchor=tk.W)
chkbut_asia.pack(padx=90, pady=5, fill=tk.X)

americas = tk.IntVar()
chkbut_americas = tk.Checkbutton(tk_win, text='美洲',
                             variable=americas, anchor=tk.W)
chkbut_americas.pack(padx=90, pady=5, fill=tk.X)

europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(tk_win, text='歐洲',
                               variable=europe, anchor=tk.W)
chkbut_europe.pack(padx=90, pady=5, fill=tk.X)

africa = tk.IntVar()
chkbut_africa = tk.Checkbutton(tk_win, text='非洲',
                               variable=africa, anchor=tk.W)
chkbut_africa.pack(padx=90, pady=5, fill=tk.X)

oceania = tk.IntVar()
chkbut_oceania = tk.Checkbutton(tk_win, text='大洋洲',
                                variable=oceania, anchor=tk.W)
chkbut_oceania.pack(padx=90, pady=5, fill=tk.X)

# 建立一個Button物件
but = tk.Button(tk_win, text='確定', command=but_click,
                font=default_font, fg='blue', bg='sky blue', padx=15)
but.pack(padx=10, pady=5)

# 建立一個Label物件，用來顯示結果
lab_result = tk.Label(tk_win, font=default_font, fg='orange red', width=20)
lab_result.pack(padx=10, pady=5)

# 啟動GUI程式的處理迴圈
tk_win.mainloop()
