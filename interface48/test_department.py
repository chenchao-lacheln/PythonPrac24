#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 00:02
# @Author  : Lacheln
import math


import requests

'''使用指定的信息 创建企业微信的部门'''


class TestDepartment:
    # setup_class
    def setup_class(self):
        # 定义变量
        corpid = "wwa815aa9e1e382434"
        contact_secret = "ztVphExEghBERHnPiErRAd2dykGDHQ1XhXosgPjzWYo"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义get请求的参数（字典）-->> 拼接到URL后边的参数
        param = {
            "corpid": corpid,
            "corpsecret": contact_secret
        }
        r = requests.get(url=url, params=param)
        self.access_token = r.json()["access_token"]

    # 创建部门
    def test_creat_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # 定义url请求参数字段数据
        param = {
            "access_token" : self.access_token
        }
        data = {
            "name": "上海研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 4
        }
        r = requests.post(url=url, params=param, json=data,)
        print(r.json())
