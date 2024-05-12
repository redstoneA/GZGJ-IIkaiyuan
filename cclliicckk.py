import pyautogui
import keyboard


def cclliicckk(ci, fang):
    for i in range(ci):
        if fang == 'left':
            pyautogui.click()
        if fang == 'right':
            pyautogui.rightClick()


class CclliicckkWuxian:
    def cclliicckk_wuxian(self, fang):
        self.ce = True
        while True:
            if fang == 'left':
                pyautogui.click()
                keyboard.add_hotkey('esc', self.cclliicckk_wuxian_stop)
                if self.ce == False:
                    break
                self.ce = True
            if fang == 'right':
                pyautogui.rightClick()
                keyboard.add_hotkey('esc', self.cclliicckk_wuxian_stop)
                if self.ce == False:
                    break
                self.ce = True
        keyboard.unhook_all()

    def cclliicckk_wuxian_stop(self):
        self.ce = False
