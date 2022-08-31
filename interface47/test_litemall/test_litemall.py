#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 11:16 上午
# @Author  : Lacheln
import requests


class TestLitemall:
    # 1.获取管理端登录接口 （token提取）
    # def test_get_admin_token(self):
    def setup_class(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        user_data = {"username":"admin123","password":"admin123","code":""}
        r = requests.post(url, json=user_data)
        self.token = r.json()["data"]["token"]
        # 问题：没有执行test_get_admin_token这个方法，所以self.token就不会被声明就会报错 AttributeError: 'TestLitemall' object has no attribute 'token'
        # 解决：self.token的声明一定要在test_add_goods方法执行之前完成，可以使用setup_class提前完成变量的声明,将test_get_admin_token更改为setup_class 即可

    # 2.获取用户端登录接口 （token提取）
        url = "https://litemall.hogwarts.ceshiren.com/wx/auth/login"
        client_data = {"username":"user123","password":"user123"}
        r = requests.post(url,json=client_data)
        self.client_token = r.json()["data"]["token"]

    # 上架商品接口调试
    def test_add_goods(self):
        # 3.上架商品的接口
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/create"
        goods_name = "ADG001"
        # 请求体信息
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "99", "number": "99", "url": ""}],
            "attributes": []}
        # 问题：token是手动复制进去的，一旦发生变化，还需要再次修改
        # 解决方案：token需要自动完成获取，并且赋值
        header = {"X-Litemall-Admin-Token": self.token}
        r = requests.post(url,json=goods_data,headers = header)
        print(r.json())

    # 4.获取商品列表接口（可以提取商品ID）
        goods_list_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        # get请求，参数需要通过params，也就是url参数传递
        goods_list_data = {
            "name": goods_name,
            "order": "desc",
            "sort": "add_time"
        }
        r = requests.get(goods_list_url,params=goods_list_data,headers = header)
        goods_id = r.json()["data"]["list"][0]["id"]

    # 5.获取商品详情接口（提取商品库存ID）
        goods_detail_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        r = requests.get(goods_detail_url,params={"id":goods_id},headers = header)
        product_id = r.json()["data"]["products"][0]["id"]

    # 6.添加购物车
    # def test_add_cart(self):
        cart_data = {"goodsId":goods_id,"number":1,"productId":product_id}
        url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
        # 问题 ： goodsId 和 productId 是写死的，变量的传递没有完成
        # 解决方案 ： goodsId 和 productId 从其他接口获取，并传递给添加购物车接口
        header = {"X-Litemall-Token": self.client_token}
        r = requests.post(url,json = cart_data,headers = header)
        # print(r.json())
        res = r.json()
        # 问题1：缺少断言
        # 解决：添加断言
        assert res["errmsg"] == "成功"
