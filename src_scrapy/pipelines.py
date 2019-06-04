# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class SrcScrapyPipeline(object):
    # to run at every instance of SrcScrapyPipeline class
    def __init__(self):
        self.create_connectiton()
        self.create_table()

    # create connections
    def create_connectiton(self):
        self.constant = sqlite3.connect('quotes.db')
        self.curser = self.constant.cursor()

    # to create table if not else delete and create new one
    def create_table(self):
        self.curser.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curser.execute("""create table quotes_tb(
                quotes text,
                authors text,
                tags text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    # to store the item to databse table
    def store_db(self, item):
        self.curser.execute("""insert into quotes_tb values (?,?,?)""",(
                            item['text'][0],
                            item['author'][0],
                            item['tags'][0]
        ))
        self.constant.commit()