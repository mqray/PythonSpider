# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

client = MongoClient('localhost',connect=False)
db = client['tercent']

class TercentPipeline(object):
    def process_item(self, item, spider):
        if db['tercent'].insert(item):
            print('succ to mongodb')
        return item
