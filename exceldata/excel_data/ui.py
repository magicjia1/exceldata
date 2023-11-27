import tkinter as tk
from tkinter import filedialog
import os

from exceldata.excel_data import t_excel

if __name__ == '__main__':

    def submit():
        year = entry_year.get()
        month = entry_month.get()
        file_path1 = entry_file1.get()
        file_path2 = entry_file2.get()
        file_path3 = entry_file3.get()
        print(f"Year: {year}, Month: {month}")
        print(f"File 1: {file_path1}")
        print(f"File 2: {file_path2}")
        print(f"File 3: {file_path3}")
        t_excel.gen_day_excel(file_path1,file_path2,file_path3,int(year),int(month))

    def browse_file1():
        initial_dir = os.getcwd()  # 获取当前工作目录
        file_path = filedialog.askopenfilename(initialdir=initial_dir)
        entry_file1.delete(0, tk.END)
        entry_file1.insert(tk.END, file_path)

    def browse_file2():
        initial_dir = os.getcwd()  # 获取当前工作目录
        file_path = filedialog.askopenfilename(initialdir=initial_dir)
        entry_file2.delete(0, tk.END)
        entry_file2.insert(tk.END, file_path)

    def browse_file3():
        initial_dir = os.getcwd()  # 获取当前工作目录
        file_path = filedialog.askopenfilename(initialdir=initial_dir)
        entry_file3.delete(0, tk.END)
        entry_file3.insert(tk.END, file_path)

    root = tk.Tk()
    root.title("Parameter Input")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label_year = tk.Label(frame, text="Year:")
    label_year.grid(row=0, column=0)
    entry_year = tk.Entry(frame)
    entry_year.grid(row=0, column=1)

    label_month = tk.Label(frame, text="Month:")
    label_month.grid(row=1, column=0)
    entry_month = tk.Entry(frame)
    entry_month.grid(row=1, column=1)

    label_file1 = tk.Label(frame, text="启翔楼:")
    label_file1.grid(row=2, column=0)
    entry_file1 = tk.Entry(frame)
    entry_file1.grid(row=2, column=1)
    button_browse1 = tk.Button(frame, text="Browse", command=browse_file1)
    button_browse1.grid(row=2, column=2)

    label_file2 = tk.Label(frame, text="太仓:")
    label_file2.grid(row=3, column=0)
    entry_file2 = tk.Entry(frame)
    entry_file2.grid(row=3, column=1)
    button_browse2 = tk.Button(frame, text="Browse", command=browse_file2)
    button_browse2.grid(row=3, column=2)

    label_file3 = tk.Label(frame, text="校车:")
    label_file3.grid(row=4, column=0)
    entry_file3 = tk.Entry(frame)
    entry_file3.grid(row=4, column=1)
    button_browse3 = tk.Button(frame, text="Browse", command=browse_file3)
    button_browse3.grid(row=4, column=2)

    button_submit = tk.Button(frame, text="Submit", command=submit)
    button_submit.grid(row=5, columnspan=3)

    root.mainloop()
