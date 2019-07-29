"""用户登陆测试"""
import unittest
import requests
import json
import sys
sys.path.append("..")
from config import config as cf
from lib.read_execl import get_case_data

class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):
        case_data=get_case_data("test_user_data.xlsx","TestUserLogin","test_user_login_normal")
        url=case_data[1]
        data=case_data[3]
        expect_res = case_data[4]
        expect_dict=json.loads(expect_res)
        # print("expect_dict['code']={}".format(expect_dict["code"]))

        data_dict=json.loads(data)
        res=requests.post(url=url,data=data_dict).json()   #请求类格式转换为字典格式
        # print(type(res))
        # act=res["code"]
        # print(act)
        self.assertEqual(res["code"],expect_dict["code"])

