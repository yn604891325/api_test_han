"""项目配置文件"""
import os
import logging
#项目路径【当前文件的绝对路径：os.path.abspath(__file__)】
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#数据文件路径
data_path=os.path.join(prj_path,"data")
#报告绝对路径
report_file=os.path.join(prj_path,"report","report.html")
#日志绝对路径
log_file=os.path.join(prj_path,"log","log.txt")
#测试用例路径
testcase_path=os.path.join(prj_path,"testcase")

#日志配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

#数据库配置
db_host = "192.168.32.131:1433"
db_user = "sa"
db_password = "platAdmin*123"
db = "PT_STORE"

#邮件配置
smtp_server="smtp.qq.com"       #smtp服务器地址
smtp_user="604891325@qq.com"
smtp_password="fyzbikcolvymbbei"

subject="接口测试报告"          #邮件主题
sender=smtp_user                 #邮件发送人
receiver="yn604891325@126.com"   #邮件接收人
is_send_email=False               #是否发送邮件 Ture发送，False不发送





# if __name__=="__main__":
#     logging.info("hrllo")