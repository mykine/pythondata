# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TsItem(scrapy.Item):
    courseId = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    stu = scrapy.Field()
