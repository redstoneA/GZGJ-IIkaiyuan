import tkinter as tk
from tkinter import ttk
import brushscreen
import cclliicckk
import mb
import zp
import ZZCode
from tkinter import messagebox
import time


# 懒得注释
class GZGJ:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GZGJ II实用工具1.7.2(开源版)")
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
        self.notebook.add(self.page4, text='图片格式互转')
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
        self.brsit2 = tk.IntVar()
        self.brscheckbutton2 = tk.Checkbutton(self.page1, text="列表读取模式", variable=self.brsit2)
        self.buttonbrscsysm = tk.Button(self.page1, text="列表读取模式使用说明", command=self.brscsysm)
        self.buttonbrscbj = tk.Button(self.page1, text="编辑列表txt", command=self.brscbj)
        self.brslabel1.pack()
        self.brslabel2.pack()
        self.brsentry1.pack()
        self.brslabel3.pack()
        self.brsentry2.pack()
        self.brslabel4.pack()
        self.brsentry3.pack()
        self.brsbutton1.pack()
        self.brscheckbutton1.pack()
        self.brscheckbutton2.pack()
        self.buttonbrscsysm.pack()
        self.buttonbrscbj.pack()

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
        self.mbit2 = tk.StringVar()
        self.mbentry1 = tk.Entry(self.page3, textvariable=self.mbit1)
        self.mbentry2 = tk.Entry(self.page3, textvariable=self.mbit2)
        self.mbbuttonqueding = tk.Button(self.page3, text="确定", command=self.mb4)
        self.mbbuttonqueding2 = tk.Button(self.page3, text="确定", command=self.mb5)
        self.mbbuttonqueding3 = tk.Button(self.page3, text="确定", command=self.mb6)
        self.mbbuttonback = tk.Button(self.page3, text="返回", command=self.mb7)
        self.mblabel2 = tk.Label(self.page3, text="请输入最大数")
        self.mblabel3 = tk.Label(self.page3, text="请输入最小数")
        self.mblabelerror = tk.Label(self.page3, text="最大数和最小数应为整数", fg="red")
        self.mblabel1.pack()
        self.mbbutton1.pack()
        self.mbbutton2.pack()
        self.mbbutton3.pack()

        self.zplabel1 = tk.Label(self.page4, text="图片格式互转")
        self.zplabeltishi = tk.Label(self.page4, text="初始图片格式")
        self.zpradio_var_1 = tk.IntVar()
        self.zpradiobutton1 = ttk.Radiobutton(self.page4, text=".jpg", value=1, variable=self.zpradio_var_1)
        self.zpradiobutton2 = ttk.Radiobutton(self.page4, text=".png", value=2, variable=self.zpradio_var_1)
        self.zpradiobutton3 = ttk.Radiobutton(self.page4, text=".bmp", value=3, variable=self.zpradio_var_1)
        self.zpradiobutton4 = ttk.Radiobutton(self.page4, text=".gif", value=4, variable=self.zpradio_var_1)
        self.zpradiobutton5 = ttk.Radiobutton(self.page4, text=".tif", value=5, variable=self.zpradio_var_1)
        self.zpradiobutton6 = ttk.Radiobutton(self.page4, text=".webp", value=6, variable=self.zpradio_var_1)
        self.zplabel2 = tk.Label(self.page4, text="图片原路径")
        self.zpbuttonqueding = tk.Button(self.page4, text="确定", command=self.zp1)
        self.zplabeltishi1 = tk.Label(self.page4, text="转换后图片格式")
        self.zpbuttonqueding1 = tk.Button(self.page4, text="确定", command=self.zp2)
        self.zpsv1 = tk.StringVar()
        self.zpsv2 = tk.StringVar()
        self.zplabel3 = tk.Label(self.page4, text="图片初始路径(带文件名不加文件格式)")
        self.zpentry1 = tk.Entry(self.page4, textvariable=self.zpsv1)
        self.zplabel4 = tk.Label(self.page4, text="图片转换后路径(带文件名不加文件格式)")
        self.zpentry2 = tk.Entry(self.page4, textvariable=self.zpsv2)
        self.zpbuttonqueding2 = tk.Button(self.page4, text="确定", command=self.zp3)
        self.zpbuttonfanhui = tk.Button(self.page4, text="返回", command=self.zp4)
        self.zplabel1.pack()
        self.zplabeltishi.pack()
        self.zpradiobutton1.pack()
        self.zpradiobutton2.pack()
        self.zpradiobutton3.pack()
        self.zpradiobutton4.pack()
        self.zpradiobutton5.pack()
        self.zpradiobutton6.pack()
        self.zpbuttonqueding.pack()

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
        brushscreen.brushscreen(self.int_yes, str(self.brstx2.get()), float(self.brstx3.get()), self.brsit1.get(), self.brsit2.get())
        self.brsc_pack()

    def brscsysm(self):
        tk.messagebox.showinfo("提示", "在程序的文件夹下的l.txt中写入一个列表，程序将会自动读取并依次刷屏，使用列表读取模式，“刷屏内容”将不会生效")

    def brscbj(self):
        self.root2 = tk.Tk()
        a = ZZCode.ZZCode(self.root2)
        a.open_file1()
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
        self.mblabel3.pack()
        self.mbentry2.pack()
        self.mbbuttonqueding.pack()
        self.mbbuttonback.pack()

    def mb2(self):
        self.mblabel1.forget()
        self.mbbutton1.forget()
        self.mbbutton2.forget()
        self.mbbutton3.forget()
        self.mblabel2.pack()
        self.mbentry1.pack()
        self.mblabel3.pack()
        self.mbentry2.pack()
        self.mbbuttonqueding2.pack()
        self.mbbuttonback.pack()

    def mb3(self):
        self.mblabel1.forget()
        self.mbbutton1.forget()
        self.mbbutton2.forget()
        self.mbbutton3.forget()
        self.mblabel2.pack()
        self.mbentry1.pack()
        self.mblabel3.pack()
        self.mbentry2.pack()
        self.mbbuttonqueding3.pack()
        self.mbbuttonback.pack()

    def mb4(self):
        self.c = self.mbit1.get()
        self.d = self.mbit2.get()
        try:
            self.c_ok = int(self.c)
            self.d_ok = int(self.d)
            self.mblabelerror.forget()
            mb.mb("Π表", self.c_ok, self.d_ok)
        except ValueError:
            self.mblabelerror.pack()

    def mb5(self):
        self.c = self.mbit1.get()
        self.d = self.mbit2.get()
        try:
            self.c_ok = int(self.c)
            self.d_ok = int(self.d)
            self.mblabelerror.forget()
            mb.mb("平方表", self.c_ok, self.d_ok)
        except ValueError:
            self.mblabelerror.pack()

    def mb6(self):
        self.c = self.mbit1.get()
        self.d = self.mbit2.get()
        try:
            self.c_ok = int(self.c)
            self.d_ok = int(self.d)
            self.mblabelerror.forget()
            mb.mb("乘法表", self.c_ok, self.d_ok)
        except ValueError:
            self.mblabelerror.pack()

    def mb7(self):
        self.mblabel1.pack()
        self.mbbutton1.pack()
        self.mbbutton2.pack()
        self.mbbutton3.pack()
        self.mblabel2.forget()
        self.mbentry1.forget()
        self.mblabel3.forget()
        self.mbentry2.forget()
        self.mbbuttonqueding.forget()
        self.mbbuttonqueding2.forget()
        self.mbbuttonqueding3.forget()
        self.mblabelerror.forget()
        self.mbbuttonback.forget()

    def zp1(self):
        try:
            self.zppanduan = self.zpradio_var_1.get()
            self.zpl = {1: "jpg", 2: "png", 3: "bmp", 4: "gif", 5: "tif", 6: "webp"}
            self.zpchushigeshi = self.zpl[self.zppanduan]
            self.zplabeltishi.forget()
            self.zpradiobutton1.forget()
            self.zpradiobutton2.forget()
            self.zpradiobutton3.forget()
            self.zpradiobutton4.forget()
            self.zpradiobutton5.forget()
            self.zpradiobutton6.forget()
            self.zpbuttonqueding.forget()
            self.zplabeltishi1.pack()
            self.zpradiobutton1.pack()
            self.zpradiobutton2.pack()
            self.zpradiobutton3.pack()
            self.zpradiobutton4.pack()
            self.zpradiobutton5.pack()
            self.zpradiobutton6.pack()
            self.zpbuttonqueding1.pack()
        except KeyError:
            messagebox.showinfo("提示", "请选择图片格式")

    def zp2(self):
        try:
            self.yanzheng = self.zpradio_var_1.get()
            self.zhuanhuanhou = self.zpl[self.yanzheng]
            self.zplabeltishi1.forget()
            self.zpradiobutton1.forget()
            self.zpradiobutton2.forget()
            self.zpradiobutton3.forget()
            self.zpradiobutton4.forget()
            self.zpradiobutton5.forget()
            self.zpradiobutton6.forget()
            self.zpbuttonqueding1.forget()
            self.zplabel3.pack()
            self.zpentry1.pack()
            self.zplabel4.pack()
            self.zpentry2.pack()
            self.zpbuttonqueding2.pack()
            self.zpbuttonfanhui.pack()
        except KeyError:
            messagebox.showinfo("提示", "请选择图片格式")

    def zp3(self):
        try:
            self.zpchushilujing = self.zpsv1.get()
            self.zhuanhuanhoulujing = self.zpsv2.get()
            zp.zp(self.zpchushilujing, self.zpchushigeshi, self.zhuanhuanhoulujing, self.zhuanhuanhou)
        except ValueError:
            messagebox.showinfo("提示", "所有框都要填写")

    def zp4(self):
        self.zplabel1.pack()
        self.zplabeltishi.pack()
        self.zpradiobutton1.pack()
        self.zpradiobutton2.pack()
        self.zpradiobutton3.pack()
        self.zpradiobutton4.pack()
        self.zpradiobutton5.pack()
        self.zpradiobutton6.pack()
        self.zpbuttonqueding.pack()
        self.zplabel3.forget()
        self.zpentry1.forget()
        self.zplabel4.forget()
        self.zpentry2.forget()
        self.zpbuttonqueding2.forget()
        self.zpbuttonfanhui.forget()
