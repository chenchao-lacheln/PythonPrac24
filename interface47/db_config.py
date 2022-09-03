#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 6:26 下午
# @Author  : Lacheln
import pymysql

# 封装建立连接的对象
def get_connect():
    connect = pymysql.connect(
        host= "litemall.hogwarts.ceshiren.com",
        port=13306,
        user="test",
        password="test123456",
        database="litemall",
        charset="utf8mb4"
    )
    return connect

# 执行sql语句
def execute_sql(sql):
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(sql) # 执行sql
    record = cursor.fetchone() # 查询记录(默认的第一条信息)
    # record = cursor.fetchall() # 获取多条
    return record

if __name__ == '__main__':
    print(execute_sql("select * from litemall_cart"))