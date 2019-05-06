#! /usr/local/env python
#coding:utf-8
import urllib.request
'''
urllib.request.urlretrieve("https://edu.hellobi.com/my/courses/learning","2.txt")
res = urllib.request.urlcleanup()
print(res)
file = urllib.request.urlopen("https://edu.hellobi.com/my/courses/learning")
print(file)
res = file.info()
print(res)
res = file.getcode()
print(res)
res = file.geturl()
print(res)
'''
#file2 = urllib.request.urlopen("https://edu.hellobi.com/",timeout=1)
#print(file2.info())
for i in range(0,10):
    try:
        file = urllib.request.urlopen("http://edu.hellobi.com/", timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("爬去异常"+str(e))


