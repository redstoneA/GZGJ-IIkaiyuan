import tkinter as tk
from tkinter import filedialog , messagebox
import subprocess
import os
class ZZCode:
    def __init__(self, master):
        self.master = master
        master.title("ZZ 文本编辑器 (V1.0 改自ZZCodeV1.0)")
        self.text_area = tk.Text(master)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="文件", menu=self.file_menu)
        # self.file_menu.add_command(label="打开", command=self.open_file)
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.file_menu.add_separator()
        # self.file_menu.add_command(label="运行", command=self.run_code)
        self.file_path = None
    def open_file1(self):
        self.file_path = 'l.txt'
        if self.file_path:
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    # 优化大文件读取，此处保留一次性读取为示例，实际应用中可考虑逐行读取
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
            except IOError as e:
                messagebox.showinfo('提示',"无法打开文件：", e)

    def open_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    # 优化大文件读取，此处保留一次性读取为示例，实际应用中可考虑逐行读取
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
            except IOError as e:
                messagebox.showinfo('提示',"无法打开文件：", e)
    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file_content = self.text_area.get(1.0, tk.END)
                    file.write(file_content)
            except IOError as e:
                messagebox.showinfo('错误',"无法保存文件：",e)
        else:
            # 提示用户指定文件扩展名
            default_ext = '.txt'  # 设定默认扩展名为 Python 脚本
            file_path = filedialog.asksaveasfilename(defaultextension=default_ext)
            if file_path:
                # 去掉可能存在的其他扩展名，确保最终文件扩展名为.py
                if os.path.splitext(file_path)[1] != '.txt':
                    file_path += '.txt'
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.file_path = file_path

    """
    def run_code(self):
        if self.file_path and self.file_path.endswith('.txt'):
            try:
                # 使用Python的subprocess模块运行当前编辑的脚本
                subprocess.run(['python', self.file_path])
            except Exception as e:
                messagebox.showinfo('提示',"运行代码出错：",e)
        else:
            messagebox.showinfo('提示',"请先保存Python(.py后缀名)脚本文件。")
            由ZZCode改来，此部分源于ZZCode
            
    """

if __name__ == "__main__":
    root = tk.Tk()
    editor = ZZCode(root)
    root.mainloop()