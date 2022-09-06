#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 11:54 上午
# @Author  : Lacheln
import requests
import base64
import json


# 封装，针对不同算法的处理
class ApiRequest:
    def send(self, data: dict):
        # 定义请求
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            # 获取二进制的响应结果,通过base64.b64decode 进行解密,使用json.loads进行格式美化
            return json.loads(base64.b64decode(res.content))
        # 把加密过后的响应值发给第三方服务，让第三方去做解密，然后返回界面过后的信息
        elif data["encoding"] == "private":
            # 该url为第三方url，
            return requests.post("url", data=res.content)


# 调用python自带的base64，直接对返回的响应做解密
def test_ancode(self):
    url = "http://127.0.0.1:9999/demo1.txt"
    r = requests.get(url=url)
    print(r.text)
    # 获取二进制的响应结果,通过base64.b64decode 进行解密,使用json.loads进行格式美化
    res = json.loads(base64.b64decode(r.content))
    print(res)
