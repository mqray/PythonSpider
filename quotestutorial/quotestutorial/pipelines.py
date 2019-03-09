# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#如果需要将抓取到的数据保存到数据库中，就不能采用刚才的那种方式了。
class TextPipeline(object):
    def __init__(self):
        self.limit = 50 #限制名人名言的长度


    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
                return item
        else:
            return DropItem('Missing Text')

   
#pipeline未生效，需要在settings里设置
class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod#类方法
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB','items')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_items(self,item,spider):
        name = item.__class__.__name__
        self.db[self.collection_name].insert(dict(item))
        return  item

    def close_spider(self,spider):
        self.client.close()

