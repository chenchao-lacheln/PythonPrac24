#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 11:13 上午
# @Author  : Lacheln
import requests

'''token鉴权'''

class TestTokenVerify:
    def setup_class(self):
        self.proxy = {
            "http": "http://127.0.0.1:8989",
            "https": "http://127.0.0.1:8989"
        }

    # def litemall_token(self):
        user_data = {"username": "admin123", "password": "admin123", "code": ""}
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        r = requests.post(url=url,json=user_data)
        self.token = r.json()["data"]["token"]
    #  获取token
    def test_litemall_token(self):
        user_data = {"username": "admin123", "password": "admin123", "code": ""}
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        r = requests.post(url=url,json=user_data)
        token = r.json()["data"]["token"]
        print(token)

    # 传入token
    def test_litemall_goods(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/profile/nnotice"
        r = requests.get(url=url,headers = {"X-Litemall-Admin-Token": self.token})
        print(r.json())