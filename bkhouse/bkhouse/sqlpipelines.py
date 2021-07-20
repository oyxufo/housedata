# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import sys
# 设置字符集变量default_encoding为utf-8
from importlib import reload

import xlwt
import pymysql


class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="ufo13554497628", database="test1")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into newhouse (title,msg,price,per_meter,place) VALUES (%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql, [item['title'], item['msg'], item['price'], item['per_meter'], item['place']])
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
