#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 09:17
# @Author  : Lacheln

from selenium import webdriver

# Chrome()后面需要添加一个括号，代表实例化一个类
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


