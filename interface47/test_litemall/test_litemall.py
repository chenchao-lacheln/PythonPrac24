#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 11:16 上午
# @Author  : Lacheln
import requests


class TestLitemall:
    # 自动获取token
    def setup_class(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        user_data = {"username":"admin123","password":"admin123","code":""}
        r = requests.post(url, json=user_data)
        self.token = r.json()["data"]["token"]
        # 问题：没有执行test_get_admin_token这个方法，所以self.token就不会被声明就会报错 AttributeError: 'TestLitemall' object has no attribute 'token'
        # 解决：self.token的声明一定要在test_add_goods方法执行之前完成，可以使用setup_class提前完成变量的声明,将test_get_admin_token更改为setup_class 即可

    # 获取用户登录token
        url = "https://litemall.hogwarts.ceshiren.com/wx/auth/login"
        client_data = {"username":"user123","password":"user123"}
        r = requests.post(url,json=client_data)
        self.client_token = r.json()["data"]["token"]

    # 上架商品接口调试
    def test_add_goods(self):
        # url
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/create"
        # 请求体信息
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": "ADG"}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "99", "number": "99", "url": ""}],
            "attributes": []}
        # 问题：token是手动复制进去的，一旦发生变化，还需要再次修改
        # 解决方案：token需要自动完成获取，并且赋值
        header = {"X-Litemall-Admin-Token": self.token}
        r = requests.post(url,json=goods_data,headers = header)
        print(r.json())

    # 添加购物车
    def test_add_cart(self):
        cart_data = {"goodsId":1181982,"number":1,"productId":1229}
        url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
        header = {"X-Litemall-Token": self.client_token}
        r = requests.post(url,json = cart_data,headers = header)
        print(r.json())

