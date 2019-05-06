# -*- coding: utf-8 -*-
import scrapy


class Pachong1Spider(scrapy.Spider):
    name = 'pachong1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
