#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 10:20 上午
# @Author  : Lacheln

'''多套被测环境切换'''

import requests
import yaml

# 设置临时环境变量
# windows set interface_env=test
# macOS export interface_env=test
from interface49.muliti_env_manage.conftest import global_env


class TestMulitiEnvByOption:
    def setup_class(self):
        path_env = global_env.get("env")
        # 读取对应的文件内容
        env = yaml.safe_load(open(f"{path_env}.yaml",encoding="utf-8"))
        self.base_url = env["base_url"]

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
