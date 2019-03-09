# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy

class GoverItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()  # 发布日期
    num = scrapy.Field()        #建议编号
    theme = scrapy.Field()      #建议的主题
    location = scrapy.Field()   #所属部门或者地址
    state = scrapy.Field()      #处理状态
    detail_url = scrapy.Field() #建议的内容连接
    detail_content = scrapy.Field() #建议的详细内容
    detail_img = scrapy.Field()     #如果建议中存在内容，则也要爬取

