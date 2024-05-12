import pyautogui
import pyperclip
import time


def brushscreen(cishu, neirong):
    """
    使用自动化工具快速刷屏的函数。

    参数:
    - cishu: int, 刷屏的次数。
    - neirong: str, 要刷屏的内容。

    返回值:
    无
    """
    # 复制粘贴板当前的内容，以便在操作结束后恢复
    pa = pyperclip.paste()
    # 将需要刷屏的内容复制到粘贴板
    pyperclip.copy(neirong)
    # 连续粘贴并换行指定次数
    for i in range(cishu):
        time.sleep(0.1)  # 控制操作间隔，增加真实感
        pyautogui.hotkey('ctrl', 'v')  # 使用Ctrl+V快捷键进行粘贴
        time.sleep(0.1)
        pyautogui.press('enter')  # 按下Enter键进行换行
    # 恢复最初粘贴板的内容
    pyperclip.copy(pa)
