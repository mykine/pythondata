'''
import urllib.request
import urllib.parse
url="http://www.iqianyue.com/mypost/"
mydata=urllib.parse.urlencode({
"name":"ceo@iqianyue.com",
"pass":"1235jkds"
    }).encode("utf-8")
req=urllib.request.Request(url,mydata)
data=urllib.request.urlopen(req).read()
fh=open("F:/天善-Python数据分析与挖掘课程/result/22/3.html","wb")
fh.write(data)
fh.close()
''' 
'''
URLError:
1、
2、
3、
4、HTTPE…
'''
'''
import urllib.error
import urllib.request
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError  as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
'''
'''
import urllib.request
url="http://blog.csdn.net/weiwei_pig/article/details/52123738"
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open("F:/天善-Python数据分析与挖掘课程/result/22/4.html","wb")
fh.write(data)
fh.close()
'''
import urllib.request
import re
data=urllib.request.urlopen("http://news.sina.com.cn/").read()
data2=data.decode("utf-8","ignore")
pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl=allurl[i]
        file="F:/天善-Python数据分析与挖掘课程/result/22/sinanews/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("-------成功-------")
    except urllib.error.URLError  as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)








