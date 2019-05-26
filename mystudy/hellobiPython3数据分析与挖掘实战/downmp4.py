#! /usr/bin/env python  
# -*- coding:utf-8 -*-
import codecs
filePath = 'course.html'
fp = codecs.open(filePath,'r','utf-8')
data = fp.read()
fp.close()
print(data)