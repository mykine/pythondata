#! /usr/local/env python
#coding:utf-8

import urllib.request
data = urllib.request.urlopen("https://read.douban.com/provider/all").read()
data = data.decode("utf-8")
import re
pat = '<div class="name">(.*?)</div>'
mydata = re.compile(pat).findall(data)
print(mydata)


'''
import re
pat ='<div class="name">(.*?)</div>'
mydata = re.compile(pat).findall(data)
print(mydata)
'''
'''
import codecs
fh = codecs.open("test2.txt","w","utf-8")
#fh = open("/mystudy/test1.txt","w")
for i in range(0,len(mydata)):
    fh.write(mydata[i]+"\n")
fh.close()
'''
'''
import codecs
fp = codecs.open("1.txt","w","utf-8")
fp.write("哈哈哈")
fp.close()
'''