# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo
class GoverPipeline(object):
    def process_item(self, item, spider):
        item['detail_content'] = self.process_content(item['detail_content'])
        return item

    def process_content(self,content):
        content = [re.sub("\xa0|\s","",i) for i in content]
        content = [i for i in content if len(i) > 0]
        return content


class MongodbPipeline(object):
    collection_name = 'gov'

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        self.db[self.collection_name].insert(dict(item))
        print("succ to mongodb")
        return item


    def close_spider(self,spider):
        self.client.close()

