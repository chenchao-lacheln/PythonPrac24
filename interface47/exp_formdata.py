#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 2:59 下午
# @Author  : Lacheln
import requests


# 通过form表单发起请求
class TestRep:
    def setup_class(self):
        # 设置代理
        self.proxy = {"http":"http://127.0.0.1:8989","https":"http://127.0.0.1:8989"}

    # 通过form表单发起请求
    def test_data(self):
        data = {"lacheln" : "level"}
        # 通过data参数传入请求体信息
        r = requests.post("https://httpbin.testing-studio.com/post",data=data,
                      proxies = self.proxy)
        print(r.json())

    # 通过json发起请求
    def test_json(self):
        data = {"lacheln" : "level"}
        # 通过data参数传入请求体信息
        r = requests.post("https://httpbin.testing-studio.com/post",json=data,
                      proxies = self.proxy)
        print(r.json())