#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 09:17
# @Author  : Lacheln


# 导入selenium包
from selenium import webdriver
# import sys

# 创建一个Chromedriver实例，Chrome()会从环境变量中寻找浏览器驱动
driver = webdriver.Chrome()

# sys.path.append("..")
# 打开网址
driver.get("https://www.baidu.com/")
# 关闭driver
driver.quit()





