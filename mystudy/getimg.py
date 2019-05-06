#! /usr/local/env python
#coding:utf-8
import urllib.request

urlAll = ['https://g-search3.alicdn.com/img/bao/uploaded/i4/i2/2622053728/O1CN012M0arP1dPT2WrcXiU_!!2622053728.jpg',
          'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/2996327771/O1CN018lOfOr27HAL2SQnMG_!!2996327771.jpg'
          ]
for i in range(0,len(urlAll)):
    print(urlAll[i])
    urllib.request.urlretrieve(urlAll[i],'test/img/'+str(i)+'.png')

mp3urlAll = ['http://cliveimages.youban.com/ab26859040f014b34df6bf20b9695605.mp3',
             'http://cliveimages.youban.com/26a39df7dc026fe9230936add1a67acf.mp3']

for m in range(0,len(mp3urlAll)):
    print(mp3urlAll[m])
    urllib.request.urlretrieve(mp3urlAll[i],'test/audio/'+str(m)+".mp3")

mp4urlAll = ['https://youbansrc.youban.com/yxxjzpy02.mp4']
for n in range(0,len(mp4urlAll)):
    print(mp4urlAll[n])
    urllib.request.urlretrieve(mp4urlAll[n],'test/video/'+str(n)+".mp4")
