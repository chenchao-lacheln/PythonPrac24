#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 23:35
# @Author  : Lacheln
import requests

class TestToken:
    # 获取token的第一种方式
    def test_get_token1(self):
        # 定义变量
        corpid = "wwa815aa9e1e382434"
        contact_secret = "ztVphExEghBERHnPiErRAd2dykGDHQ1XhXosgPjzWYo"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={contact_secret}"
        r = requests.get(url=url)
        print(r.json())

    # 获取token的第二种方式:针对URL较长的情况，进行参数化
    def test_get_token2(self):
        # 定义变量
        corpid = "wwa815aa9e1e382434"
        contact_secret = "ztVphExEghBERHnPiErRAd2dykGDHQ1XhXosgPjzWYo"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义get请求的参数（字典）-->> 拼接到URL后边的参数
        param = {
            "corpid" : corpid,
            "corpsecret" : contact_secret
        }
        r = requests.get(url=url, params=param)
        print(r.json())