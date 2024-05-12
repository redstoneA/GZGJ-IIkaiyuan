import pyautogui
import keyboard


# 定义一个快速点击函数，根据指定次数和点击方式（左键或右键）执行点击操作
def cclliicckk(ci, fang):
    # 根据指定次数进行点击
    for i in range(ci):
        # 判断点击方式，并执行相应的点击操作
        if fang == 'left':
            pyautogui.click()
        if fang == 'right':
            pyautogui.rightClick()


# 定义一个无限制点击类，可以持续进行左键或右键的点击，直至通过按ESC键停止
class CclliicckkWuxian:
    def cclliicckk_wuxian(self, fang):
        # 初始化一个标志位用于控制点击的循环执行
        self.ce = True
        while True:
            # 根据指定的点击方式执行相应的无限点击操作，同时绑定ESC键来停止点击
            if fang == 'left':
                pyautogui.click()
                keyboard.add_hotkey('esc', self.cclliicckk_wuxian_stop)
                # 如果标志位为False，则退出循环
                if self.ce == False:
                    break
                self.ce = True
            if fang == 'right':
                pyautogui.rightClick()
                keyboard.add_hotkey('esc', self.cclliicckk_wuxian_stop)
                if self.ce == False:
                    break
                self.ce = True
        # 停止所有通过keyboard库绑定的热键
        keyboard.unhook_all()

    # 定义一个停止点击的方法，通过调用此方法来停止无限点击操作
    def cclliicckk_wuxian_stop(self):
        self.ce = False

