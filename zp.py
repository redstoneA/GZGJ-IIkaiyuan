from PIL import Image
from tkinter import messagebox


def zp(chushilujing, chushigeshi, zhuanhuanhoulujing, zhuanhuanhougeshi):
    """
    功能：将指定路径和格式的图片转换为新的格式并保存至另一路径。

    参数说明：
    - chushilujing: str，原始图片的路径（不含格式）。
    - chushigeshi: str，原始图片的格式（如jpg, png等）。
    - zhuanhuanhoulujing: str，转换后图片保存的路径（不含格式）。
    - zhuanhuanhougeshi: str，转换后图片的格式。

    运行过程：
    1. 使用PIL库读取原始图片。
    2. 保存图片为用户指定的新格式到指定路径。
    3. 通过tkinter的消息框显示转换完成信息，提示检查指定路径以确认转换结果。

    返回值：
    无。
    """
    # 拼接原始图片完整路径
    zhen_chushilujing = chushilujing + "." + chushigeshi
    # 拼接转换后图片的完整路径
    zhen_zhuanhuanhoulujing = zhuanhuanhoulujing + "." + zhuanhuanhougeshi

    # 打开原始图片文件
    with Image.open(zhen_chushilujing) as img:
        # 保存为新格式
        img.save(zhen_zhuanhuanhoulujing, format=zhuanhuanhougeshi)
        # 显示消息框提示转换完成
        messagebox.showinfo('提示', '若你指定的路径中文件出现，则成功，没有出现则失败，可以自行搜索你的图片格式特点以找出失败原因')
