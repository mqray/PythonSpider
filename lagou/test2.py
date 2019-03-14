# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 19:39
# @Author  : mqray
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
import  requests
from lxml import etree
url = 'https://www.lagou.com/jobs/5685848.html'
headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-TW;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.lagou.com/',
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko)  Safari/537.36)'
}
response = requests.get(url,headers=headers)
print(response.text)
# print(response.request.headers)
# print(response.text)
html = etree.HTML(response.text)

job_request = html.xpath('//div[@class="position-content-l"]/dd/p[1]/span/text()')
name = html.xpath('//div[@class="position-content-l"]')

print(name)


# 清洗抓取到的数据
# import  re
# dic = { 'name':'Python工程师','loc':'前海农交所招聘','job_type': '全职', 'work_addr': ['\n                                                ', ' -\n                    ', '\n                                            - 天安科技园总部大厦19号楼伊的家总部大厦\n                                                            ', '\n        ']}
# #TypeError: expected string or bytes-like object
# for key in dic:
#     if isinstance(dic[key],list):
#         dic[key] = [re.sub("\xa0|-|\n|/s| ","",i) for i in dic[key] ]
#         dic[key] = [i for i in dic[key] if len(i)>0]
#         print(dic[key],type(dic[key]))
#     else :
#         dic[key] = re.sub("\xa0|-|\n|/s| ","",dic[key])
#         print(dic[key],type(dic[key]))



