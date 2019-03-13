# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 19:39
# @Author  : mqray
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
import  requests
url = 'https://www.lagou.com/jobs/5682511.html'
resp = requests.get(url)
print(resp.text)