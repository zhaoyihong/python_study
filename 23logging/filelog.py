#!/usr/bin/env python
# coding=utf-8

'''
    简单的使用方式
'''

import logging


fh = logging.FileHandler('./mylog.txt')
formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s -  %(message)s')
fh.setFormatter(formatter)

logger = logging.getLogger('mylog')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

logger.info('hahaha')
