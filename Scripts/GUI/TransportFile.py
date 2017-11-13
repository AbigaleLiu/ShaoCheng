import tkinter
import tkinter.filedialog

window = tkinter.Tk()
window.title("文件上传")
window.geometry("400x200")  # 窗口大小

# 标签
label_var = tkinter.StringVar()  # 文字变量存储器
label_var.set("选择文件")  # 标签初始文字
label = tkinter.Label(window, textvariable=label_var)  # 创建标签
label.place(x=170, y=0, anchor='nw')  # 标签放置坐标，以西北角为准

on_hit = 0  # 默认初始状态为0,按钮被点击0次


def hit_me():
    """
    按钮点击事件
    :return:
    """
    global on_hit
    if on_hit == 0:
        on_hit = 1
        label_var.set('打开文件')
        button_var.set("确定")
        file = tkinter.filedialog.askopenfilename(title="选择文件")
        file_var.set(file)
        return file
    elif on_hit == 1:
        on_hit = 2
        label_var.set('文件上传中。。。')
        button_var.set("取消")
    elif on_hit == 2:
        on_hit = 0
        label_var.set("选择文件")
        button_var.set("选择")


# 文本框
file_var = tkinter.StringVar()
text = tkinter.Entry(window, width=40, textvariable=file_var)  # 创建文本框
text.place(x=25, y=75, anchor='nw')


# 按钮
button_var = tkinter.StringVar()
button_var.set("选择")  # 按钮初始文字
button = tkinter.Button(textvariable=button_var, command=hit_me, width=7)  # 创建按钮
button.place(x=325, y=75, anchor='nw')  # 按钮放置坐标，以西北角为准

# window.mainloop()
