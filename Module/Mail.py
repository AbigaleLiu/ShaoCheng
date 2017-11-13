from email.mime.multipart import MIMEMultipart
import smtplib
from Scripts.Public.Path import *

class Mail:
    def mail(self):
        report_path = Path().report_path()

        sender = ["2792319254@qq.com"]
        reciever = ["2792319254@qq.com"]
        subject = ["测试周报"]
        smtpserver = "smtp.qq.com"
        username = "Tester"
        password = ""
        msg = MIMEMultipart(open(report_path))
