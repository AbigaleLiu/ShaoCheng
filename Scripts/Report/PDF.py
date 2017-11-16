import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  # 注册字体（宋体）
from reportlab.lib import fonts, colors
fonts.addMapping('SimSun', 0, 0, 'SimSun')
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from Scripts.Public.TimeTemp import *


class PDF:
    def report_name(self):
        current_time = TimeTemp().time_temp()
        report_name = current_time + ".pdf"
        return report_name

    def pdf_page(self, start, end, all_num, pass_num, fail_num):

        report_name = self.report_name()
        story = []  # 用于存储段落、图片等对象
        style_sheet = getSampleStyleSheet()  # 样式集

        # 新增标题样式
        style_sheet.add(ParagraphStyle(name='Title_zh',
                                       fontSize=14,
                                       alignment=TA_CENTER,
                                       leading=50))
        style_sheet['Title_zh'].fontName = 'SimSun'  # 设置新增样式字体（宋体）

        # 新增正文样式
        style_sheet.add(ParagraphStyle(name='Normal_zh',
                                       fontSize=10,
                                       alignment=TA_LEFT))
        style_sheet["Normal_zh"].fontName = "SimSun"

        # 通过用例个数字体样式
        style_sheet.add(ParagraphStyle(name='Normal_pass',
                                       fontSize=10,
                                       textColor=colors.green))
        style_sheet["Normal_pass"].fontName = "SimSun"

        # 失败用例个数字体样式
        style_sheet.add(ParagraphStyle(name='Normal_fail',
                                       fontSize=10,
                                       textColor=colors.red))
        style_sheet["Normal_fail"].fontName = "SimSun"

        story.append(Paragraph("测试报告", style_sheet["Title_zh"]))

        # pass_style = style_sheet["Normal_pass"]
        # fail_style = style_sheet["Normal_fail"]
        start_time = "报告生成时间：%s" % start
        end_time = "执行时长：%s" % end
        # count0 = Paragraph("执行统计：", style_sheet["Normal_zh"])
        # pass_p = Paragraph(str(pass_num), style_sheet["Normal_pass"])
        # count1 = Paragraph("个用例通过，", style_sheet["Normal_zh"])
        # fail_p = Paragraph(str(fail_num), style_sheet["Normal_fail"])
        # count2 = Paragraph("个用例失败", style_sheet["Normal_zh"])
        story.append(Paragraph(start_time, style_sheet["Normal_zh"]))
        story.append(Paragraph(end_time, style_sheet["Normal_zh"]))
        # for i in [count0, pass_p, count1, fail_p, count2]:
        #     story.append(i)

        count = Paragraph("<p>共执行用例%(all_num)s个，通过<font color=#00ff00>%(pass_num)s</font>个，失败<font color=#ff0000>%(fail_num)s</font></p>个",
                          style_sheet["Normal_zh"])
        story.append(count)

        self.chart()

        file = SimpleDocTemplate(report_name)
        file.build(story)

    def chart(self):
        pass

if __name__ == '__main__':
    PDF().pdf_page('k', 'j', 100,12, 465)