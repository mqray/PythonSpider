# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 15:34
# @Author  : mqray
# @Site    : 
# @File    : log1.py
# @Software: PyCharm
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')#设置日志的输出样式

logger= logging.getLogger(__name__)



if __name__ == '__main__':
    logger.info('this is a info log')
    logger.info('this is a info log')