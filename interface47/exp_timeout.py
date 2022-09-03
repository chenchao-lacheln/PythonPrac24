#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 3:17 下午
# @Author  : Lacheln
import requests

class TestTimeout():

    def setup_class(self):
        # 设置代理
        self.proxy = {"http": "http://127.0.0.1:8989", "https": "http://127.0.0.1:8989"}

    def test_one(self):
        r = requests.post("https://httpbin.testing-studio.com/get")
        print(r.text)

    # 连接代理，Charles打上断点，模拟堵塞场景
    def test_two(self):
        r = requests.post("https://httpbin.testing-studio.com/post",proxies = self.proxy,timeout = 3)
        print(r.json())
    def test_three(self):
        r = requests.post("https://httpbin.testing-studio.com/get",timeout = 3)
        print(r.text)