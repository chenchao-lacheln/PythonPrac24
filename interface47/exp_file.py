#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 4:05 下午
# @Author  : Lacheln
import requests

r = requests.post("https://httpbin.testing-studio.com/post",
                  # files参数用来解决文件上传接口
                  # files = {"lacheln_file" : open("1.text","rb")},
                  # 不让filename读取文件名，在上传的过程中做修改value即可
                  files = {"lacheln_file" : ("lacheln.txt",open("1.text","rb"))},
                  proxies = {"http" : "http://127.0.0.1:8989",
                             "https" : "http://127.0.0.1:8989"})

print(r.json())
