import tkinter
import tkinter.filedialog


class Try:
    def __init__(self, label_var, button_var, file_var, on_hit):
        self.label_var = label_var
        self.button_var = button_var
        self.file_var = file_var
        self.on_hit = on_hit


    def hit_me(self):
        """
        按钮点击事件
        :return:
        """
        # global on_hit
        if self.on_hit == 0:
            self.on_hit = 1
            self.label_var = '打开文件'
            self.button_var = "确定"
            file = tkinter.filedialog.askopenfilename(title="选择文件")
            self.file_var = file
            return file
        elif self.on_hit == 1:
            self.on_hit = 2
            self.label_var = '文件上传中。。。'
            self.button_var = "取消"
        elif self.on_hit == 2:
            self.on_hit = 0
            self.label_var = "选择文件"
            self.button_var = "选择"

    def window(self):

        window = tkinter.Tk()
        window.title("文件上传")
        window.geometry("400x200")  # 窗口大小

        # 标签
        # label_var = tkinter.StringVar()  # 文字变量存储器
        # label_var.set("选择文件")  # 标签初始文字
        label = tkinter.Label(window, textvariable=self.label_var)  # 创建标签
        label.place(x=170, y=0, anchor='nw')  # 标签放置坐标，以西北角为准

        # on_hit = 0  # 默认初始状态为0,按钮被点击0次


        # 文本框
        # file_var = tkinter.StringVar()
        text = tkinter.Entry(window, width=40, textvariable=self.file_var)  # 创建文本框
        text.place(x=25, y=75, anchor='nw')


        # 按钮
        # button_var = tkinter.StringVar()
        # button_var.set("选择")  # 按钮初始文字
        button = tkinter.Button(textvariable=self.button_var, command=self.hit_me, width=7)  # 创建按钮
        button.place(x=325, y=75, anchor='nw')  # 按钮放置坐标，以西北角为准

        window.mainloop()


if __name__ == '__main__':
    _r = Try("选择文件", "选择", '',0)
    _r.window()