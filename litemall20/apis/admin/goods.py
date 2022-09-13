#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 23:11
# @Author  : Lacheln
import requests

from litemall20.apis.base_api import BaseApi

# 继承BaseApi
class Goods(BaseApi):

    def __init__(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        user_data = {"username": "admin123", "password": "admin123", "code": ""}
        r = requests.post(url, json=user_data)
        self.token = r.json()["data"]["token"]
    def create(self,goods_data):
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/create"
        # 问题1：token是手动复制进去的，一旦发生变化，还需要再次修改
        # 解决方案：token需要自动完成获取，并且赋值
        header = {"X-Litemall-Admin-Token": self.token}
        # r = requests.post(url, json=goods_data, headers=header)
        r = self.send("post",url, json=goods_data, headers=header)
        # 问题1：接口里直接使用了requests
        # 解决方案：在base_api中添加公共的send方法
        return r

    def list(self,goods_name,order="desc",sort="add_time"):
        goods_list_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        header = {"X-Litemall-Admin-Token": self.token}
        # get请求，参数需要通过params，也就是url参数传递
        goods_list_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        # r = requests.get(goods_list_url, params=goods_list_data, headers=header)
        r = self.send("get",goods_list_url, params=goods_list_data, headers=header)
        return r


    def detail(self,goods_id):
        goods_detail_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        header = {"X-Litemall-Admin-Token": self.token}
        # r = requests.get(goods_detail_url,params={"id":goods_id},headers = header)
        r = self.send("get",goods_detail_url,params={"id":goods_id},headers = header)
        return r
        # product_id = r.json()["data"]["products"][0]["id"]