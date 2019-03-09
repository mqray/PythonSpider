# -*- coding: utf-8 -*-
import scrapy
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from gover.items import GoverItem
class YgzwSpider(scrapy.Spider):
    name = 'ygzw'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/ruse.shtml']#注释一

    def parse(self, response):
        tr_lists = response.xpath('//div[contains(@class,"newsHead")]/table[2]/tr')#注释二
        for tr in tr_lists:
            item = GoverItem()#注释三
            item['date'] = tr.xpath('./td[last()]/text()').extract_first()#注释四
            item['num'] = tr.xpath('./td[1]/text()').extract_first()
            item['theme'] = tr.xpath('./td[3]/a/text()').extract_first()
            item['detail_url'] = tr.xpath('./td[3]/a[1]/@href').extract_first()
            item['location'] = tr.xpath('./td[3]/a[2]/text()').extract_first()
            item['state'] = tr.xpath('./td[4]/span/text()').extract_first()

            #print(items)
            yield scrapy.Request(
                item['detail_url'],
                callback= self.parse_detail,#注释五
                meta = {"item":item}#注释六
            )
        #翻页
        next_url = response.xpath('//a[text()=">"]/@href').extract_first()
        #print(next_url)
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse#注释七
            )

    def parse_detail(self,response):
        item = response.meta["item"]#注释八
        item['detail_content'] = response.xpath('//div[@class="wzy1"]/table[2]/tr[1]/td//text()').extract()
        item['detail_img'] = response.xpath('//div[@class="wzy1"]//a/@src').extract()
        item['detail_img'] = ['http://wz.sun0769.com' + i for i in item['detail_img']]#注释九

        yield item


