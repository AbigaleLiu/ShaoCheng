from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from threading import Timer
from Scripts.Public.Path import *
from Scripts.Mail.Attachment import *


class Mail:
    def mail(self):
        report_path = Attachment().last_file()  # 邮件绝对路径
        report_name = Attachment().report_name()  # 附件名

        receiver_list = ["liuxue@nutown.cn"]

        # 126邮箱
        # sender = "abigaleliu@126.com"  # 发件人邮箱
        # smtpserver = "smtp.126.com"  # 发件服务器
        # password = "miao2333"  # 发件人SMTP密码（126）

        # 阿里云邮箱
        sender = "liuxue@nutown.cn"  # 发件人阿里云邮箱
        smtpserver = "smtp.mxhichina.com"  # 阿里云企业邮箱服务器
        password = "******"  # 阿里云企业邮箱不设SMTP密码,输入邮箱密码

        # QQ邮箱
        # sender = "abigale_liu@qq.com"  # 发件人邮箱
        # smtpserver = "smtp.qq.com"  # 发件服务器
        # password = "bknznoizcpnnddff"  # 发件人SMTP密码（qq）

        port = 25  # 发件端口:25为非SSL,465/587为SSL

        receiver = ",".join(receiver_list)  # 收件人邮箱

        body = "<h1>各位:</h1><p>附件为本周测试报告,请尽快查收</p>"  # 邮件正文

        # msg = MIMEText(body, "html")  # 邮件正文
        # msg["subject"] = "Test Report"  # 邮件标题
        # msg["from"] = sender  # 发件人
        # msg["to"] = receiver  # 收件人

        msg = MIMEMultipart()  # 带附件的邮件对象
        msg["subject"] = "Test Report"  # 邮件标题
        msg["from"] = sender  # 发件人
        msg["to"] = receiver  # 收件人
        text = MIMEText(body, "html")
        msg.attach(text)

        # 构造附件
        attachment = MIMEApplication(open(report_path, "rb").read())
        attachment.add_header('Content-Disposition', 'attachment', filename=report_name)
        msg.attach(attachment)

        # 发送邮件
        try:
            s = smtplib.SMTP(smtpserver, port)  # SMTP对应端口25;SMTP_SSL对应端口465/587
            s.login(sender, password)
            s.sendmail(sender, receiver, msg.as_string())  # 发送邮件
            print("Succeed")
            s.quit()
        except smtplib.SMTPRecipientsRefused as e:
            print('Recipient refused')
            print(e)
        except smtplib.SMTPAuthenticationError as e:
            print('Auth error')
            print(e)
        except smtplib.SMTPSenderRefused as e:
            print('Sender refused')
            print(e)
        except smtplib.SMTPException as e:
            print("SMTP Exception")
            print(e)

    # def mail_timer(self):
    #     """
    #     每周五晚上18点发送邮件
    #     :return:
    #     """
    #     today = TimeTemp().mail_time()["weekday"]
    #     hour = TimeTemp().mail_time()["hour"]
    #     if today == "Fri" and hour == "18":
    #         self.mail()


if __name__ == '__main__':
    # Mail().mail()
    Mail().mail()

