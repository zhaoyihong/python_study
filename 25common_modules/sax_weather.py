#!/usr/bin/env python
# coding=utf-8

'''
    使用SAX解析雅虎天气
    xml地址：http://weather.yahooapis.com/forecastrss?u=c&w=2151330
    天气地址：https://weather.yahoo.com/
    城市代码在天气地址的url中找
'''



from xml.parsers.expat import ParserCreate
from collections import defaultdict
import urllib


class GetWeather(object):

    def __init__(self, citycode):
        self.citycode = citycode
        self.infos = defaultdict()
        url_template = 'http://weather.yahooapis.com/forecastrss?u=c&w=%s'
        self.url = url_template % citycode
        self.current_name = ''
        self.__parse_xml()

    def __parse_xml(self):
        parser = ParserCreate()
        parser.returns_unicode = True
        parser.StartElementHandler = self.__start_element
        parser.EndElementHandler = self.__end_element
        parser.CharacterDataHandler = self.__char_data
        try:
            xml = urllib.urlopen(self.url).read()
        except:
            print 'new work unreadable'

        parser.Parse(xml)

    def __start_element(self, name, attrs):

        self.current_name = name+'_start'
        # get city
        if name == 'yweather:location':
            if 'city' in attrs:
                self.infos['city'] = attrs['city']
            if 'country' in attrs:
                self.infos['country'] = attrs['country']
        elif name == 'yweather:condition':
            if 'today' not in self.infos:
                self.infos['today'] = defaultdict()
            if 'text' in attrs:
                self.infos['today']['cond'] = attrs['text']
            if 'temp' in attrs:
                self.infos['today']['temp'] = attrs['temp']
            if 'date' in attrs:
                self.infos['today']['date'] = attrs['date']
        elif name == 'yweather:forecast':
                if not self.infos.has_key('forecast'):
                    self.infos['forecast'] = list()
                if attrs.has_key('date') and attrs.has_key('low') and attrs.has_key('high') and attrs.has_key('text'):
                    forecastinfo = dict()
                    forecastinfo['date'] = attrs['date']
                    forecastinfo['low'] = attrs['low']
                    forecastinfo['high'] = attrs['high']
                    forecastinfo['cond'] = attrs['text']
                    self.infos['forecast'].append(forecastinfo)

    def __end_element(self, name):
        self.current_name = name+'_end'

    def __char_data(self, text):
        if self.current_name == 'pubDate'+'_start':
            self.infos['pubDate'] = text

    def get_infos(self):
        return self.infos

    def print_info(self):
        print 'city:' + self.infos['city']
        print 'pubdate:' + self.infos['pubDate']
        print 'today:' 
        print '\tdate:'+ self.infos['today']['date']
        print '\tcond:'+ self.infos['today']['cond']
        print '\ttemp:'+ self.infos['today']['temp']
        print 'forcaste:'
        for i in range(len(self.infos['forecast'])):
            print '\tdate:'+ self.infos['forecast'][i]['date'],
            print '\tcond:'+ self.infos['forecast'][i]['cond'],
            print '\tlow:'+ self.infos['forecast'][i]['low'],
            print '\thigh:'+ self.infos['forecast'][i]['high'],
            print 
if __name__ == '__main__':
    weather = GetWeather(2151330) #北京编号
    weather.print_info() 
