#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/29 6:24 下午
# @Author  : Lacheln

import requests
# 定义一个代理的配置信息，key值为协议，value为代理工具的配置
proxy = {
    # 端口需要与代理工具Charles监听断开保持一致
    "http":"http://127.0.0.1:8989",
    "https":"http://127.0.0.1:8989"
}
# 通过proxies 传递代理配置
# verify = False 表示发起请求不会认证https
data = {"a":1}
requests.post(url="https://httpbin.testing-studio.com/post",proxies = proxy,json = data)