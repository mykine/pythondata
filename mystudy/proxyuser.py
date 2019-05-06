#! /usr/local/env python
#coding:utf-8
import urllib.request
import urllib.parse
import json
def user_proxy(url,proxy_addr,paramData):
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url,paramData).read().decode('utf-8')
    return data

url = 'https://family.youban.com/home/index.wxapp'
proxy_addr = '116.209.58.76'
paramData = urllib.parse.urlencode(
    {
        "auth":"a8015425641b7fed90426b7d14f1e89cebf7334c08390fe7ac3ef36da5746339fa17f4abeefe026d3ade7ffbcc007364eabbc890b97cde157efb86806557bb742520979fef093271",
        "version":"1.0.0"
    }
).encode("utf-8")
data = user_proxy(url,proxy_addr,paramData)
data = json.loads(data)
print(data)

