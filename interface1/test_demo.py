#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 4:18 下午
# @Author  : Lacheln
import requests

class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r) # <Response [200]>
        print(r.status_code)
        print(r.text) # 返回文本信息
        print(r.json())
        assert r.status_code == 200