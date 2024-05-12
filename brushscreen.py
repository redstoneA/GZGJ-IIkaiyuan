import pyautogui
import pyperclip
import time


def brushscreen(cishu,neirong):
    pa = pyperclip.paste()
    pyperclip.copy(neirong)
    for i in range(cishu):
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.press('enter')
    pyperclip.copy(pa)
