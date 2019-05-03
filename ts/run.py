#! /usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy import cmdline
cmd = "scrapy crawl lesson --nolog".split()
cmdline.execute(cmd)