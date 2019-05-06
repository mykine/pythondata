#! /usr/local/env python
#coding:utf-8
import urllib.request
import urllib.parse
url = "http://joyi.family.youban.com/parentchild/storymusic/list.wxapp"
mydata = urllib.parse.urlencode(
    {
        "auth":"a8015425641b7fed90426b7d14f1e89cebf7334c08390fe7ac3ef36da5746339fa17f4abeefe026d3ade7ffbcc007364eabbc890b97cde157efb86806557bb742520979fef093271",
        "mylove":"1",
        "channel":"1"
    }
).encode("utf-8")
req = urllib.request.Request(url,mydata)
data = urllib.request.urlopen(req).read()
#print(data)
data = data.decode('utf-8')
#print(data)
import codecs
fh = codecs.open('4.txt','wb','utf-8')
fh.write(data)
fh.close()