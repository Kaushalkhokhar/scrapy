# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class AmazonPipeline(object):
    # to run at every instance of SrcScrapyPipeline class
    def __init__(self):
        self.create_connectiton()
        self.create_table()

    # create connections
    def create_connectiton(self):
        self.constant = sqlite3.connect('mobile.db')
        self.curser = self.constant.cursor()

    # to create table if not else delete and create new one
    def create_table(self):
        self.curser.execute("""DROP TABLE IF EXISTS mobile_tb""")
        self.curser.execute("""create table mobile_tb(
                brand text,
                price text,
                imagelink text             
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    # to store the item to databse table
    def store_db(self, item):
        self.curser.execute("""insert into mobile_tb values (?,?,?)""",(
                            item['product_name'][0],
                            item['product_price'][0],
                            item['product_imagelink'][0]
        ))
        self.constant.commit()
