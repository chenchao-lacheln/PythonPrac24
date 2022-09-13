#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 23:04
# @Author  : Lacheln
import json

import requests

from litemall20.utils.log_utils import logger


class BaseApi:
    # 封装公共的send方法
    # 问题1：接口里直接使用了requests
    # 解决方案：在base_api中添加公共的send方法
    def send(self,method,url,**kwargs):
        r = requests.request(method,url,**kwargs)
        logger.debug(f"{url}接口的响应值为{json.dumps(r.json(),indent=2,ensure_ascii=False)}")
        return r.json()
