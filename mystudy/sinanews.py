#! /usr/local/env python
#coding:utf-8

#首先，获取新闻首页所有URL
import urllib.request
url = 'http://sports.sina.com.cn/nba/'
data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
import re
pat = 'href="(http://sports.sina.com.cn/basketball/nba/.*?)"'
allurl = re.compile(pat).findall(data)
print(allurl )
import codecs
import urllib.error
#然后，遍历URL依次获取单个新闻详情
for i in range(0,len(allurl)):
    try:
        dataDetail = urllib.request.urlopen(allurl[i]).read().decode('utf-8')
        # 最后，将获取的新闻详情存入本地文件
        filename = 'test/NBA'+str(i)+'.html'
        fh = codecs.open(filename,'w','utf-8')
        fh.write(dataDetail)
        fh.close()
        print(filename + " 爬取成功!\n")
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print("爬取失败!"+e.code)
        if hasattr(e,'reason'):
            print("爬取失败!"+e.reason)