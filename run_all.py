"""执行所有用例入口"""
import unittest
from config import config as cf
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import send_report

suite=unittest.defaultTestLoader.discover(cf.testcase_path)
with open(cf.report_file,"wb") as f:
    HTMLTestRunner(stream=f,title="api test",description="test").run(suite)

if cf.is_send_email:
    send_report()
