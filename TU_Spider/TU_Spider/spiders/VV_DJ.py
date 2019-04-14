# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from TU_Spider.items import TuSpiderItem
from scrapy.http import Request
import re

class VvDjSpider(scrapy.Spider):
    name = 'VV_DJ'
    allowed_domains = ['www.tucan.tu-darmstadt.de']
    start_urls = ['http://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=ACTION&ARGUMENTS=-A.wLAkncbR37xocqNZHTlObv-P8iYJKCWNVETg.fMTc5TJ2jP4Y3xcF6qePLL8P0EwGHWjuunm6FbeevQBDzYr55XCsP1ZV6bxtSqCP1Zq5PYZch85M439LziBIV=']

    #def start_requests(self):
    #    pass
        
    def parse(self, response):
        '''
        1.获取目录列表中具体课程url,并交给scrapy进行下载后并进行解析
        2.获取下一页的url并交给scrapy进行下载，下载完成后，交给parse
        :param response:
        :return:
        '''
        html = response.text
        soup = BeautifulSoup(html, features= 'lxml')
        ul = soup.find('ul', class_ = 'auditRegistrationList')
        item = TuSpiderItem()
        if ul is not None:#持续挖掘URL地址
            for each in ul.find_all('li'):
                if each is not None:
                    a = each.find('a')
                    next_url = 'http://' + self.allowed_domains[0] + a.get('href')
                    yield Request(url= next_url)
        else:#捕捉到课程列表
            table = soup.find('table', class_ ="nb eventTable")
            if table is not None:
                for each in table.find_all('tr', class_ = 'tbdata'):
                    td = each.find_all('td')
                    item['name'] = td[1].find('a').get_text()
                    temp = td[1].get_text().replace('\t', '').replace('\n','').replace('\r', '').replace(item['name'], '').strip().split('    ')
                    if len(temp) > 1:
                        item['lehrer'] = temp[0]
                        item['zeitraum'] = temp[-1]
                    elif len(temp) == 1:
                        item['lehrer'] = temp[0]
                        item['zeitraum'] = 'nicht gegeben'
                    yield item