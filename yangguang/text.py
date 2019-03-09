# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 20:57
# @Author  : mqray
# @Site    : 
# @File    : text.py
# @Software: PyCharm

from lxml import etree
html = etree.parse('http://wz.sun0769.com/html/top/ruse.shtml',etree.HTMLParser())
res = html.xpath('//td[4]/span/text()')
print(res)

