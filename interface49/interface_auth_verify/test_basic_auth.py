#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 3:51 下午
# @Author  : Lacheln
import requests
from requests.auth import HTTPBasicAuth


class TestAuthVerify:
    def setup_class(self):
        self.proxy = {
            "http":"http://127.0.0.1:8989",
            "https":"http://127.0.0.1:8989"
        }

    def test_basic_auth(self):
        url = "https://httpbin.testing-studio.com/basic-auth/ad/123"
        r = requests.get(url=url,auth=HTTPBasicAuth("ad","123"))
        print(r.json())

