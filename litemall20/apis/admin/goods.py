#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 23:11
# @Author  : Lacheln
import requests


class Goods:
    def create(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        user_data = {"username": "admin123", "password": "admin123", "code": ""}
        r = requests.post(url, json=user_data)
        self.token = r.json()["data"]["token"]

    def list(self,goods_name,order="desc",sort="add_time"):
        goods_list_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        header = {"X-Litemall-Admin-Token": self.token}
        # get请求，参数需要通过params，也就是url参数传递
        goods_list_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        r = requests.get(goods_list_url, params=goods_list_data, headers=header)
        return r.json()


    def detail(self):
        pass