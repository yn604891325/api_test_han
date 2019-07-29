"""发送邮件"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config as cf
import sys
sys.path.append("..")

def send_report():
    msg=MIMEMultipart()  #混合格式的邮件
    #邮件正文
    body=MIMEText("plat测试报告","plain","utf-8")
    msg.attach(body)
    #邮件头
    msg["From"]=cf.sender
    msg["To"]=cf.receiver
    msg["Subject"]=cf.subject
    #报告附件
    with open(cf.report_file,"rb") as f:
        att_file=f.read()
    att1=MIMEText(att_file,"base64","utf-8")
    att1["Content-Type"]="application/octet-stream"
    att1["Content-Disposition"]="attachment;filename=report.html"
    msg.attach(att1)
    #发送邮件
    smtp=smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_user,cf.smtp_password)
    smtp.sendmail(cf.sender,cf.receiver,msg.as_string())
    cf.logging.info("邮件发送完毕")

# if __name__=="__main__":
#     send_report()


