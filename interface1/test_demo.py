#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 4:18 下午
# @Author  : Lacheln
import requests
from hamcrest import *


class TestDemo:
    # get请求目标构造
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r) # <Response [200]>
        print(r.status_code)
        print(r.text) # 返回文本信息
        print(r.json())
        assert r.status_code == 200

    # get query请求构造
    def test_query(self):
        payload = {
            "level":1,
            "name":"todesk"
        }
        r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200

    # form请求参数构造
    def test_post_from(self):
        payload = {
            "level": 1,
            "name": "todesk"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    # header构造
    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get',headers = {"h" : "headers demo"})
        print(r.status_code)
        print(r.text)  # 返回文本信息
        print(r.json())
        assert r.status_code == 200

    # 构造json请求
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "todesk"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    # harmcrest 断言
    def test_harmcrest(self):
        payload = {
            "level": 1,
            "name": "todesk"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert_that( r.json()['json']['level'], equal_to(1))

