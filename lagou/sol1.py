# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 15:47
# @Author  : mqray
# @Site    : 
# @File    : sol1.py
# @Software: PyCharm
import requests
from lxml import etree
import re
from pymongo import MongoClient
# from pyquery import PyQuery as pq
from requests.exceptions import RequestException,ConnectionError
import  time
def get_page_list(url,headers):
    headers = headers
    sess = requests.Session()
    response = requests.get(url,headers=headers)
    cookie = sess.cookies
    try:
        if response.status_code == 200:
            html = etree.HTML(response.text)
            # print(response.text)
            page_lists = html.xpath('//a[@class="position_link"]/@href')
            #print(page_lists)
            return page_lists,cookie

    except RequestException:
        print('RequestionError')
        return None

def get_infos(url,cookie,headers):
    headers = headers
    try:
        response = requests.get(url,headers=headers,cookies=cookie)
        items = {}
        if response.status_code == 200:
            html = etree.HTML(response.text)
            # job_name = html.xpath('//div[@class="position-content-l"]')
            # print(len(job_name))
            items['name'] = html.xpath('//div[@class="job-name"]/span[@class="name"]/text()')
            items['company'] = html.xpath('//div[@class="job-name"]/div[@class="company"]/text()')
            job_request = html.xpath('//div[@class="position-content-l"]/dd/p[1]/span/text()')
            # job_request = html.xpath('//div[@class="position-content-l"]/dd/p[1]')
            # items['salary'] = job_request.xpath('./span[1]/text()')
            # items['loc'] = job_request.xpath('./span[2]/text()')
            # items['work_exp'] = job_request.xpath('./span[3]/text()')
            # items['education'] = job_request.xpath('./span[4]/text()')
            # items['job_type'] = job_request.xpath('./span[last()]/text()')
            items['salary'] = job_request[0]
            items['loc'] = job_request[1]
            items['work_exp'] = job_request[2]
            items['education'] = job_request[3]
            items['job_type'] = job_request[4]
            items['punish_time'] = html.xpath('//div[@class="position-content-l"]/dd/p[2]/text()')
            #content
            content = html.xpath('//dd[@class="job_bt"]/div[@class="job-detail"]//text()')
            # items['description'] = re.match(r'(.*?)职位要求',content)
            # items['requirement'] = re.match(r'职位要求(.*?)')
            #work_address
            items['work_addr'] = html.xpath('//div[@class="work_addr"]/text()')
            return items

    except ConnectionError:
        print('ConnectionError')

def regular_data(dic):
    for key in dic:
        if isinstance(dic[key], list):
            dic[key] = [re.sub("\xa0|/|-|\n|/s| ", "", i) for i in dic[key]]
            dic[key] = [i for i in dic[key] if len(i) > 0]
        else:
            dic[key] = re.sub("\xa0|/|-|\n|/s| ", "", dic[key])
    # for key in dic :
    #     # dic[k] = "".join(dic[k].spilt())
    #     dic[key] = re.sub("/|/xao|/s|/n", "", dic[key])
    return dic

def save_to_mongo(dic):
    client = MongoClient('localhost')#创建连接
    db = client['lg']#连接的数据库
    my_table = db['sol1']#连接的表
    my_table.insert_many(dic)
    print('succ to mongo ')

def main():
    headers = {
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
    for i in range(1,31):
        ori_url = 'https://www.lagou.com/zhaopin/Python/'+ str(i)
        page_lists,cookie=  get_page_list(ori_url, headers=headers)
        print(page_lists)
        for page_list in page_lists:
            infos = get_infos(page_list,cookie,headers)
            #print(type(infos))
            infos = regular_data(infos)
            save_to_mongo(infos)

if __name__ == '__main__':
    main()



