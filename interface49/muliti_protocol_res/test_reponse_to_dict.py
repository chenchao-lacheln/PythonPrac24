#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 22:45
# @Author  : Lacheln
import requests
import xmltodict
from requests import Response


def test_response_to_dict():
    res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    find_res = reponse_to_dict(res)
    # 断言响应值是否为dict类型的格式
    assert isinstance(find_res,dict)


def reponse_to_dict(response: Response):
    res_text = response.text
    # 判断响应文本信息是否以<?xml开头
    if res_text.startswith("<?xml"):
        final_dict = xmltodict.parse(res_text)
    elif res_text.startswith("<!DOCTYPE html>"):
        final_dict = "html"
    # 如果是json 则返回json格式
    else:
        final_dict = response.json()
    return final_dict