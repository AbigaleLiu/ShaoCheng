from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import datetime

class PDF_try:
    def report_name(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d _%H_%M_%S")
        report_name = current_time + ".pdf"
        return report_name

    def table(self, page_canvas):
        pass

    def pdf_page(self):
        file_name = self.report_name()  # 保存的文件名
        page_canvas = canvas.Canvas(file_name)  # 定义canvas对象

        pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  # 注册字体（宋体）
        canvas.Canvas.setFont(page_canvas, psfontname="SimSun", size=12)  # 设置字体

        page_canvas.drawString(100, 900, "测试报告", charSpace=1)
        page_canvas.drawString(0,800, "时间")

        self.table(page_canvas)
        page_canvas.showPage()
        page_canvas.save()


if __name__ == '__main__':
    PDF_try().pdf_page()




