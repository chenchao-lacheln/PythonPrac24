#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 2:27 下午
# @Author  : Lacheln

import requests

# 自定义header传递cookie
def test_demo1():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {"Cookie" : "lacheln = level",
              'User-Agent': 'lacheln' # 定制请求头信息
              }
    r = requests.get(url = url,headers = header)
    print(r.request.headers)


# 使用cookies参数
def test_demo2():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        'User-Agent': 'lacheln'
    }
    cookie_data = {
        "lacheln" : "level",
        "teacher": "AD"
    }
    r = requests.get(url = url,headers = header,cookies = cookie_data)
    print(r.request.headers)