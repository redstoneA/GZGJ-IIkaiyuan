import tkinter as tk
from tkinter import ttk
import brushscreen
import cclliicckk
import mb
from tkinter import messagebox
import time


# 懒得注释
class GZGJ:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GZGJ II实用工具1.2(开源版)")
        self.root.geometry("600x400")
        self.notebook = ttk.Notebook(self.root)
        self.page1 = ttk.Frame(self.notebook)
        self.page2 = ttk.Frame(self.notebook)
        self.page3 = ttk.Frame(self.notebook)
        self.page4 = ttk.Frame(self.notebook)
        self.page5 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="刷屏工具")
        self.notebook.add(self.page2, text="连点器")
        self.notebook.add(self.page3, text="数学表生成器")
        self.notebook.pack(expand=True, fill="both")

        self.brslabel1 = tk.Label(self.page1, text="Brsc全自动刷屏")
        self.brslabel2 = tk.Label(self.page1, text="请输入要刷屏的次数")
        self.brstx1 = tk.StringVar()
        self.brsentry1 = tk.Entry(self.page1, textvariable=self.brstx1)
        self.brslabel3 = tk.Label(self.page1, text="请输入要刷屏的文字")
        self.brstx2 = tk.StringVar()
        self.brsentry2 = tk.Entry(self.page1, textvariable=self.brstx2)
        self.brslabel4 = tk.Label(self.page1, text="请输入要刷屏的间隔时间(秒)")
        self.brstx3 = tk.StringVar()
        self.brsentry3 = tk.Entry(self.page1, textvariable=self.brstx3)
        self.brsbutton1 = tk.Button(self.page1, text="开始刷屏", command=self.brc)
        self.brslabelint = tk.Label(self.page1, text="次数应为整数或间隔应为浮点数", fg="red")
        self.brslabelshua = tk.Label(self.page1, text="将于5秒后启动刷屏")
        self.brslabelyiqidong = tk.Label(self.page1, text="刷屏已启动")
        self.brsit1 = tk.IntVar()
        self.brscheckbutton1 = tk.Checkbutton(self.page1, text="银杏化刷屏", variable=self.brsit1)
        self.brslabel1.pack()
        self.brslabel2.pack()
        self.brsentry1.pack()
        self.brslabel3.pack()
        self.brsentry2.pack()
        self.brslabel4.pack()
        self.brsentry3.pack()
        self.brsbutton1.pack()
        self.brscheckbutton1.pack()

        self.cclabel1 = tk.Label(self.page2, text="Cclliicckk连点器")
        self.ccbutton1 = tk.Button(self.page2, text="有限连点", command=self.cc1)
        self.ccbutton2 = tk.Button(self.page2, text="无限连点", command=self.cc2)
        self.cclabel2 = tk.Label(self.page2, text="请输入要连点的次数")
        self.ccit1 = tk.IntVar()
        self.ccentry1 = tk.Entry(self.page2, textvariable=self.ccit1)
        self.ccbutton3 = tk.Button(self.page2, text="开始有限连点", command=self.cc3)
        self.ccbutton5 = tk.Button(self.page2, text="开始无限连点", command=self.cc5)
        self.cclabel3 = tk.Label(self.page2, text="按esc结束无限连点")
        self.ccbutton4 = tk.Button(self.page2, text="返回", command=self.cc4)
        self.cclabel4 = tk.Label(self.page2, text="次数应为整数", fg="red")
        self.ccit2 = tk.IntVar()
        self.cccheckbutton1 = tk.Checkbutton(self.page2, text="右键连点", variable=self.ccit2)
        self.cclabel1.pack()
        self.ccbutton1.pack()
        self.ccbutton2.pack()

        self.mblabel1 = tk.Label(self.page3, text="MB数学表生成器")
        self.mbbutton1 = tk.Button(self.page3, text="Π表生成器", command=self.mb1)
        self.mbbutton2 = tk.Button(self.page3, text="平方表生成器", command=self.mb2)
        self.mbbutton3 = tk.Button(self.page3, text="乘法表生成器", command=self.mb3)
        self.mbit1 = tk.StringVar()
        self.mbentry1 = tk.Entry(self.page3, textvariable=self.mbit1)
        self.mbbuttonqueding = tk.Button(self.page3, text="确定", command=self.mb4)
        self.mbbuttonqueding2 = tk.Button(self.page3, text="确定", command=self.mb5)
        self.mbbuttonqueding3 = tk.Button(self.page3, text="确定", command=self.mb6)
        self.mbbuttonback = tk.Button(self.page3, text="返回", command=self.mb7)
        self.mblabel2 = tk.Label(self.page3, text="请输入最大数")
        self.mblabelerror = tk.Label(self.page3, text="最大数应为整数", fg="red")
        self.mblabel1.pack()
        self.mbbutton1.pack()
        self.mbbutton2.pack()
        self.mbbutton3.pack()

    def run(self):
        self.root.mainloop()

    def brc(self):
        self.int_or_not = self.brstx1.get()
        self.float_or_not = self.brstx3.get()
        try:
            self.int_yes = int(self.int_or_not)
            self.float_yes = float(self.float_or_not)
            self.brsc_update()
        except ValueError:
            self.brslabelint.pack()

    def brsc_pack(self):
        self.brslabel1.pack()
        self.brslabel2.pack()
        self.brsentry1.pack()
        self.brslabel3.pack()
        self.brsentry2.pack()
        self.brsbutton1.pack()
        self.brslabelint.forget()

    def brsc_update(self):
        self.messagebox1 = messagebox.showinfo("提示", "将于五秒后开始刷屏")
        if self.messagebox1:
            self.brsc_update2()

    def brsc_update2(self):
        time.sleep(5)
        brushscreen.brushscreen(self.int_yes, str(self.brstx2.get()), float(self.brstx3.get()), self.brsit1.get())
        self.brsc_pack()

    def cc1(self):
        self.cclabel2.pack()
        self.ccentry1.pack()
        self.ccbutton3.pack()
        self.ccbutton4.pack()
        self.cccheckbutton1.pack()
        self.cclabel1.forget()
        self.ccbutton1.forget()
        self.ccbutton2.forget()

    def cc2(self):
        self.ccbutton5.pack()
        self.cclabel3.pack()
        self.cccheckbutton1.pack()
        self.ccbutton4.pack()
        self.cclabel1.forget()
        self.ccbutton1.forget()
        self.ccbutton2.forget()

    def cc3(self):
        self.ccci = self.ccentry1.get()
        try:
            self.ccci_ok = int(self.ccci)
            self.cclabel4.forget()
            if self.ccit2.get() == 1:
                cclliicckk.cclliicckk(self.ccci_ok, "right")
            else:
                cclliicckk.cclliicckk(self.ccci_ok, "left")
        except ValueError:
            self.cclabel4.pack()

    def cc4(self):
        self.ccbutton5.forget()
        self.cclabel3.forget()
        self.cccheckbutton1.forget()
        self.ccbutton4.forget()
        self.cclabel2.forget()
        self.ccentry1.forget()
        self.ccbutton3.forget()
        self.cclabel4.forget()
        self.cclabel1.pack()
        self.ccbutton1.pack()
        self.ccbutton2.pack()

    def cc5(self):
        self.b = cclliicckk.CclliicckkWuxian()
        if self.ccit2.get() == 1:
            self.b.cclliicckk_wuxian("right")
        else:
            self.b.cclliicckk_wuxian("left")

    def mb1(self):
        self.mblabel1.forget()
        self.mbbutton1.forget()
        self.mbbutton2.forget()
        self.mbbutton3.forget()
        self.mblabel2.pack()
        self.mbentry1.pack()
        self.mbbuttonqueding.pack()
        self.mbbuttonback.pack()

    def mb2(self):
        self.mblabel1.forget()
        self.mbbutton1.forget()
        self.mbbutton2.forget()
        self.mbbutton3.forget()
        self.mblabel2.pack()
        self.mbentry1.pack()
        self.mbbuttonqueding2.pack()
        self.mbbuttonback.pack()

    def mb3(self):
        self.mblabel1.forget()
        self.mbbutton1.forget()
        self.mbbutton2.forget()
        self.mbbutton3.forget()
        self.mblabel2.pack()
        self.mbentry1.pack()
        self.mbbuttonqueding3.pack()
        self.mbbuttonback.pack()

    def mb4(self):
        self.c = self.mbit1.get()
        try:
            self.c_ok = int(self.c)
            self.mblabelerror.forget()
            mb.mb("Π表", self.c_ok)
        except ValueError:
            self.mblabelerror.pack()

    def mb5(self):
        self.c = self.mbit1.get()
        try:
            self.c_ok = int(self.c)
            self.mblabelerror.forget()
            mb.mb("平方表", self.c_ok)
        except ValueError:
            self.mblabelerror.pack()

    def mb6(self):
        self.c = self.mbit1.get()
        try:
            self.c_ok = int(self.c)
            self.mblabelerror.forget()
            mb.mb("乘法表", self.c_ok)
        except ValueError:
            self.mblabelerror.pack()

    def mb7(self):
        self.mblabel1.pack()
        self.mbbutton1.pack()
        self.mbbutton2.pack()
        self.mbbutton3.pack()
        self.mblabel2.forget()
        self.mbentry1.forget()
        self.mbbuttonqueding.forget()
        self.mbbuttonqueding2.forget()
        self.mbbuttonqueding3.forget()
        self.mblabelerror.forget()
        self.mbbuttonback.forget()
