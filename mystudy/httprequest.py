#! /usr/local/env python
#coding:utf-8
import urllib.request
keywd = "权利的游戏"
keywd = urllib.request.quote(keywd)
url = "http://www.baidu.com/s?wd="+keywd+"&rsv_spt=1&rsv_iqid=0x9ec9efd50008a465&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=5&rsv_sug7=100"
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
data = data.decode('utf-8')
import codecs
fh = codecs.open('3.txt','wb','utf-8')
fh.write(data)
fh.close()
