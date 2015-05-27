#!/usr/bin/env python
# coding=utf-8

'''
    简单的使用方式
'''

import logging


fh = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s','%a,%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)

logger = logging.getLogger('mylog')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

logger.info('hahaha')
