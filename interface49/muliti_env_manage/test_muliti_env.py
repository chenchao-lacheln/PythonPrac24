#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 10:20 上午
# @Author  : Lacheln

'''多套被测环境切换'''
import os

import requests
import yaml

# 设置临时环境变量
# windows set interface_env=test
# macOS export interface_env=test
class TestMulitiEnv:
    def setup_class(self):
        # 目的 ： 在接口用例中，只指定path，不指定URL
        # 从yaml文件读取数据
        # 第一种方式：从环境变量读取名称为 interface_env 的配置环境
        path_env = os.getenv("interface_env",default=test)
        # 读取对应的文件内容
        env = yaml.safe_load(open(f"{path_env}.yaml",encoding="utf-8"))
        self.base_url = env["base_url"]
        # self.base_url = "https://httpbin.ceshiren.com/"


    # 编写2条测试用例
    def test_devenv(self):
        """
        验证是否为开发环境
        :return:
        """
        path = "get"
        r = requests.get(self.base_url + path)
        # r = requests.get("https://httpbin.org/get")
        # print(r.json())
        # 假设 httpbin.ceshiren.com 是开发环境，那么就是断言，当前请求是向开发环境发起的
        assert r.json()["headers"]["Host"] == "httpbin.ceshiren.com"

    def test_testenv(self):
        path = "get"
        r = requests.get(self.base_url + path)
        # r = requests.get("https://httpbin.org/get")
        assert r.json()["headers"]["Host"] == "httpbin.org"
