# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        res = response.xpath('//div[@class="li_txt"]')
        for r in res:
            item = {}
            item['name'] = r.xpath('./h3/text()').extract_first()
            item['position'] = r.xpath('./h4/text()').extract()[0]
            item['intro'] = r.xpath('./p/text()').extract()[0]
            yield  item

            logger.warning(item)