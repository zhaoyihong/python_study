#!/usr/bin/env python
# coding=utf-8
import logging
import logging.config

logging.config.fileConfig('log.conf')

clogger = logging.getLogger('c')
flogger = logging.getLogger('f')

clogger.info('hello console')
flogger.info('hello file')



