# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 22:26
# @Author  : mqray
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import requests
from lxml import etree
url = 'http://wz.sun0769.com/html/top/ruse.shtml'
html = etree.parse(url,etree.HTMLParser())
tr_lists = html.xpath('//div[contains(@class,"newsHead")]/table[2]/tr')
print(tr_lists)
