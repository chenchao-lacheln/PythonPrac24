#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 4:39 下午
# @Author  : Lacheln
from interface49 import test_requests1


# 测试 封装的加密算法
class TestApiRequest:
    req_data = {
        # 请求方法
        "method": "get",
        # URL
        "url": "http://127.0.0.1:9999/demo1.txt",
        # 请求头
        "headers": None,
        # 控制加解密算法
        "encoding": "base64"
    }

    def test_send(self):
        ar = test_requests1.ApiRequest()
        print(ar.send(self.req_data))
