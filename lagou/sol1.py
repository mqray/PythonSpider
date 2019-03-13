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
def get_page_list(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    try:
        if response.status_code == 200:
            html = etree.HTML(response.text)
            # print(response.text)
            page_lists = html.xpath('//a[@class="position_link"]/@href')
            #print(page_lists)
            return page_lists

    except RequestException:
        print('RequestionError')
        return None

def get_infos(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        items = {}
        if response.status_code == 200:
            html = etree.HTML(response.text)
            job_name = html.xpath('//div[@class="position-content-l"]')[0]
            items['name'] = job_name.xpath('./div[@class="job-name"]/span[@class="name"]/text()')
            items['company'] = job_name.xpath('./div[@class="job-name"]/div[@class="company"]/text()')

            job_request = html.xpath('//div[@class="position-content-l"]/dd[@class="job_request"]')[0]

            items['salary'] = job_request.xpath('./p/span[1]/text()')
            items['loc'] = job_request.xpath('./p/span[2]/text()')
            items['work_exp'] = job_request.xpath('./p/span[3]/text()')
            items['education'] = job_request.xpath('./p/span[4]/text()')
            items['job_type'] = job_request.xpath('./p/span[last()]/text()')
            items['punish_time'] = job_request.xpath('.//p[@class="publish_time"]/text()')
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
    for k in dic.items() :
        dic[k] = re.sub("\xa0|\s|/","",dic[k])
    return dic

def save_to_mongo(dic):
    conn = MongoClient('localhost')
    db = conn.LG
    my_set = db.file1
    my_set.insert(dict)
    print('succ to mongo ')

def main():
    for i in range(1,30):
        ori_url = 'https://www.lagou.com/zhaopin/Python/'+ str(i)
        page_lists =  get_page_list(ori_url)
        for page_list in page_lists:
            infos = get_infos(page_list)
            infos = regular_data(infos)
            save_to_mongo(infos)



if __name__ == '__main__':
    main()



