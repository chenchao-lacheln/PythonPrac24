#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 23:10
# @Author  : Lacheln
import requests


class TestCookieVerify:
    # 设置代理
    def setup(self):
        self.proxy = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }

    # 简单直接写入cookies，不推荐使用
    def test_cookies(self):
        '''
        在有确定的cookies信息的情况下，可以直接使用cookies参数
        :return:
        '''
        r = requests.get("https://httpbin.ceshiren.com/cookies", cookies={"lacheln": "level"})
        print(r.json())

    # 没有使用session之前，第三次是没有自动获取到cookies信息的
    def test_cookies_with_out_session(self):
        # 1.获取cookies
        # 2.set cookies 设置cookies
        # 3.再次获取cookies，查看是否设置成功
        r1 = requests.get("https://httpbin.ceshiren.com/cookies", headers={"count": "1"}, proxies=self.proxy,
                          verify=False)
        print(f"第一次的响应值为{r1.json()}")
        r2 = requests.get("https://httpbin.ceshiren.com/cookies/set/username/111111", headers={"count": "2"},
                          proxies=self.proxy, verify=False)
        print(f"第二次的响应值为{r2.json()}")
        r3 = requests.get("https://httpbin.ceshiren.com/cookies", headers={"count": "3"}, proxies=self.proxy,
                          verify=False)
        print(f"第三次的响应值为{r3.json()}")


    # 使用通过sessin的方式解决，第三次及之后没有卸载cookies信息的情况
    def test_cookies_session(self):
        req = requests.session()
        r1 = req.get("https://httpbin.ceshiren.com/cookies/set/username/111111", headers={"count": "1"},
                          proxies=self.proxy, verify=False)
        print(f"第一次的响应值为{r1.json()}")
        r2 = req.get("https://httpbin.ceshiren.com/cookies", headers={"count": "2"}, proxies=self.proxy,
                          verify=False)
        print(f"第二次的响应值为{r2.json()}")
        r3 = req.get("https://httpbin.ceshiren.com/cookies", headers={"count": "3"},
                     proxies=self.proxy, verify=False)
        print(f"第三次的响应值为{r3.json()}")
