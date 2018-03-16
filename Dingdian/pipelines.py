# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import os

class DingdianPipeline(object):
    def process_item(self, item, spider):
        return item

class DingdianSQLitePipline(object):

    def __init__(self):
        # 连接数据库
        self.setupDBCon()
        # 创建表
        self.createTables()

    def setupDBCon(self):
        self.con = sqlite3.connect(os.getcwd() + '/dingdian.db')
        self.cur = self.con.cursor()

    def createTables(self):
        self.dropDingdianTables()
        self.createDingdianTable()

    def createDingdianTable(self):
        sql = '''
        CREATE TABLE dingdian(
            id INTEGER PRIMARY KEY NOT NULL ,
            title TEXT,
            author TEXT,
            novelurl TEXT
        )
        '''
        self.cur.execute(sql)
        # pass

    def dropDingdianTables(self):
        sql = '''
        DROP TABLE if EXISTS dingdian
        '''
        self.cur.execute(sql)

    def closeDB(self):
        self.cur.close()

    def process_item(self,item,spider):
        self.storeInDB(item)
        return item

    def storeInDB(self,item):
        print(item.get('title'))
        self.cur.execute('INSERT INTO dingdian(title,author,novelurl) VALUES (?,?,?)',
                         (item.get('title'),item.get('author'),item.get('novelurl'),))

        self.con.commit()


if __name__ == '__main__':
    dingdian = DingdianSQLitePipline()
    item = {'title':'盗墓笔记','author':'南派三叔','novelurl':'www.baidu.com'}
    dingdian.process_item(item=item)