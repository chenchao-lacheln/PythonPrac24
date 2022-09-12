#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 23:25
# @Author  : Lacheln
from litemall20.apis.admin.goods import Goods
from litemall20.apis.wx.cart import Cart


class TestCart():
    def setup_class(self):
        self.goods = Goods()
        self.cart = Cart()
