#! /usr/local/env python
#coding:utf-8
import urllib.request
import re

url = 'https://mengkang.net/1003.html'
savePath = '/Users/jianyi/Downloads/books/'
pageHtml = urllib.request.urlopen(url).read().decode('utf-8')
pat = '<br><a href="(.*?).pdf">'
pdfList = re.compile(pat).findall(pageHtml)
# print(pdfList)
for p in range(0,len(pdfList)):
    link = pdfList[p]+'.pdf'
    print(link)
    # urllib.request.urlretrieve(link,savePath+'php进阶'+str(p+1)+'.pdf')
