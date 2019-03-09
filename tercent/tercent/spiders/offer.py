# -*- coding: utf-8 -*-
import scrapy
import  logging
import  datetime
logger = logging.getLogger(__name__)

class OfferSpider(scrapy.Spider):
    name = 'offer'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        start = datetime.datetime.now()
        tr_list = response.xpath('//table[@class="tablelist"]/tr')[1:-1]
        for tr in tr_list:
            item = {}
            item['intro'] = tr.xpath('./td[1]/a/text()').extract_first()
            item['category'] = tr.xpath('./td[2]/text()').extract_first()
            item['nums'] = tr.xpath('./td[3]/text()').extract_first()
            item['location'] = tr.xpath('./td[4]/text()').extract_first()
            item['date'] = tr.xpath('./td[last()]/text()').extract_first()
            logger.warning(item)
            yield item
        next_url = response.xpath('//a[@id="next"]/@href').extract_first()
        if next_url != "javascript:;":
            next_url = 'https://hr.tencent.com/' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
