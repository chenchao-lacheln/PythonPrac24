#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 22:23
# @Author  : Lacheln
import requests
import xmltodict


def test_xml_to_dict():
    res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    # 注意不是直接打印res，而是打印res的text属性
    # print(res.text)
    # 转换为python标准的dict格式
    res_dict = xmltodict.parse(res.text)
    print(res_dict)