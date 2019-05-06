import requests
import os

# 字符（十六进制）转ASCII码
def hexToAscii(h):
    d = int(h,16)   # 转成十进制
    return chr(d)   # 转成ASCII码

# 从得到的html代码中获取m3u8链接（不同网站有区别）
def getM3u8(http_s):
    ret1 = http_s.find("unescape")
    ret2 = http_s.find(".m3u8")
    ret3 = http_s.find("http", ret1, ret2)  # "unescape"和".m3u8"之间找"http"
    m3u8_url_1 = http_s[ret3: ret2 + 5]  # 未解码的m3u8链接
    # 下面对链接进行解码
    while True:
        idx = m3u8_url_1.find('%')
        if idx != -1:
            m3u8_url_1 = m3u8_url_1.replace(m3u8_url_1[idx:idx+3], hexToAscii(m3u8_url_1[idx+1:idx+3]))
        else:
            break
    return m3u8_url_1

# 寻找字符串s中最后出现字符c的index
def findLastchr(s, c):
    ls = []
    sum = 0
    while True:
        i = s.find(c)
        if i != -1:
            s = s[i+1:]
            ls.append(i)
        else:
            break
    for i in range(len(ls)):
      sum += (ls[i] + 1)
    return sum - 1

def getM3u8_2(m3u8_url_1):
    r1 = requests.get(m3u8_url_1)
    r1.raise_for_status()
    text = r1.text
    idx = findLastchr(text, '\n')
    key = text[idx + 1:]  # 得到第一层m3u8中的key
    idx = findLastchr(m3u8_url_1, '/')
    m3u8_url_2 = m3u8_url_1[:idx + 1] + key  # 组成第二层的m3u8链接
    return m3u8_url_2

# 从最原始的url-->生成一个ts列表的文件
def getTsFile(url, filename):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        http_s = r.text
        m3u8_url_1 = getM3u8(http_s)
        print("第一层m3u8链接" + m3u8_url_1)
        m3u8_url_2 = getM3u8_2(m3u8_url_1)
        print("第二层m3u8链接" + m3u8_url_2)
        # 通过新的m3u8链接，获取真正的ts播放列表
        # 由于列表比较长，为他创建一个txt文件
        r2 = requests.get(m3u8_url_2)
        f = open(filename, "w", encoding="utf-8")   # 这里要改成utf-8编码，不然默认gbk
        f.write(r2.text)
        f.close()
        print("创建ts列表文件成功")
        return "success"
    except:
        print("爬取失败")
        return "failed"

# 提取ts列表文件的内容，逐个拼接ts的url，形成list
def getPlayList(filename, m3u8_url_2):
    ls = []
    f = open(filename, "r")
    line = " "      # line不能为空，不然进不去下面的循环
    idx = findLastchr(m3u8_url_2, '/')
    while line:
        line = f.readline()
        if line != '' and line[0] != '#':
            line = m3u8_url_2[:idx+1] + line
            ls.append(line[:-1])    # 去掉'\n'
    return ls

# 批量下载ts文件
def loadTs(ls):
    #root = "D://mp4//"
    root = "mp4/"
    length = len(ls)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        for i in range(length):
            path = root + ls[i][-7:]
            r = requests.get(ls[i])
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print(path + " --> OK ( {} / {} ){:.2f}%".format(i , length, i*100/length))
        print("全部ts下载完毕")
    except:
        print("批量下载失败")

# 整合所有ts文件，保存为mp4格式
def tsToMp4():
    print("开始合并...")
    #root = "D://mp4//"
    root = "mp4/"
    outdir = "output"
    os.chdir(root)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    os.system("copy /b *.ts new.mp4")
    os.system("move new.mp4 {}".format(outdir))
    print("结束合并...")

if __name__ == "__main__":
    url = "http://www.5nj.com/?m=vod-play-id-86793-src-1-num-1.html"
    file = "ts.txt"
    m3u8_url_1 = getM3u8(requests.get(url).text)
    m3u8_url_2 = getM3u8_2(m3u8_url_1)
    ret = getTsFile(url, file)
    if ret == "success":
        ls = getPlayList(file, m3u8_url_2)
        print(ls)
    loadTs(ls)
    tsToMp4()
