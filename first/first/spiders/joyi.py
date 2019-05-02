#! /usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from first.items import FirstItem
class JoyiSpider(scrapy.Spider):
	name = 'joyi'
	allowed_domains = ['baidu,com']
	start_urls = [
		'http://www.baidu.com/'
	]
	print("parse之前")
	#在settings中设置ROBOTSTXT_OBEY = False
	def parse(self, response):
		print("parse中")
		item = FirstItem()
		item['content'] = response.xpath("/html/head/title/text()").extract()
		yield item
