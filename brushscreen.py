import pyautogui
import pyperclip
import time


def brushscreen(cishu, neirong, jiange, yinxin):
    """
    在屏幕上自动刷指定内容。

    参数:
    - cishu: int, 刷屏次数。
    - neirong: str, 要刷屏的内容。
    - jiange: float, 每次刷屏之间的间隔时间（秒）。
    - yinxin: int, 是否在内容前后添加额外信息。1 表示添加，其他值不添加。

    返回值:
    无
    """
    # 备份当前剪贴板内容
    pa = pyperclip.paste()
    # 将需要刷屏的内容复制到剪贴板
    pyperclip.copy(neirong)
    # 循环执行刷屏操作指定次数
    for i in range(cishu):
        # 如果 yinxin 为 1，则在内容前后添加额外信息
        if yinxin == 1:
            pyperclip.copy(neirong+"(总次数"+str(cishu)+"剩余"+str(cishu-i-1)+"次"+")")
        # 按指定间隔时间等待
        time.sleep(jiange)
        # 使用 Ctrl+V 快捷键粘贴内容，并按下 Enter 键
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    # 刷屏完成后，恢复原始剪贴板内容
    pyperclip.copy(pa)

