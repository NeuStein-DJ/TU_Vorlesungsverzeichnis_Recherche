# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #kurs_Name = scrapy.Field()
    #kurs_Lehrer = scrapy.Field()
    #kurs_Zeitraum = scrapy.Field()
    name = scrapy.Field()
    lehrer = scrapy.Field()
    zeitraum = scrapy.Field()
