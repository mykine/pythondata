#! /usr/local/env python
#coding:utf-8
import urllib.request
useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
url = "http://blog.csdn.net/jo_andy"
header = ('User-Agent',useragent)#元组
opener = urllib.request.build_opener()
opener.addheaders = [header]
data = opener.open(url).read().decode('utf-8')
print(data)
import codecs
fh = codecs.open('5.txt','w','utf-8')
fh.write(data)
fh.close()
