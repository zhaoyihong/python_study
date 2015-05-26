#!/usr/bin/env python
# coding=utf-8

'''
    按照时间分割的日志

'''

import logging
import logging.handlers


fh = logging.handlers.TimedRotatingFileHandler('timelog','S',1,10)
formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s','%a,%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)

logger = logging.getLogger('mylog')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

logger.info('hahaha')
