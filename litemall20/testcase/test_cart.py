#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 23:25
# @Author  : Lacheln
import pytest

from litemall20.apis.admin.goods import Goods
from litemall20.apis.wx.cart import Cart


class TestCart():
    """
    框架优化
    1.先把接口和用例步骤写出来，接口的实现，暂时先设置为空
    2.先初步实现接口，保证可用
    """
    def setup_class(self):
        self.goods = Goods()
        self.cart = Cart()

    @pytest.mark.parametrize("goods_name", ["ADG002", "ADG003"])
    def test_add_cart(self,goods_name):
        """
        添加购物车测试
            上架商品接口
            获取商品列表
            获取商品详情
            添加购物车
        :return:
        """
        # 请求体信息
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "99", "number": "99", "url": ""}],
            "attributes": []}
        self.goods.create(goods_data)
        self.goods.list(goods_name)
        # self.goods.detail()
        # self.cart.add()
