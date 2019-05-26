#视频页面vedioSRC = 'https://www.finger66.com/mobile/post/5109165?channel=wechatSession&from=singlemessage&isappinstalled=0'
#放置ts文件所在目录
tsPath = "mp4/"
#获取ts文件参数
hostname = 'https://media.finger66.com'
tsParamUrl = hostname + '/posts/84222300000/MTU1NjEwNDU0ODI2Nw==.mp4.m3u8'
import urllib.request
tsParamData = urllib.request.urlopen(tsParamUrl).read().decode('utf-8')
# print(tsParamData)
import re
pat = '/(.*?).ts'
tsParamArr = re.compile(pat).findall(tsParamData)
#爬取ts文件到本地
for n in range(0,len(tsParamArr)):
    strArr = tsParamArr[n].split('/')
    localTSFileName = strArr[len(strArr)-1]+'.ts'
    tsLink = hostname + '/' + tsParamArr[n] + '.ts'
    urllib.request.urlretrieve(tsLink, tsPath+localTSFileName )
    # print(tsLink)

import os
import platform

#指定输出文件名称
saveMp4file = tsPath + 'target.mp4'
#根据不同的系统调用不同的命令合成mp4
if 'Windows' == platform.system():
    #windows下合并
    tsPathWin = tsPath.replace('/', '\\')
    saveMp4fileWin = saveMp4file.replace('/', '\\')
    cmd = 'copy /b ' + tsPathWin + '*.ts ' + saveMp4fileWin
    res = os.popen(cmd)
    print(res.read())
else:
    #linux下使用ffmpeg将ts合成mp4文件
    # 获取所有的ts文件
    path_list = os.listdir(tsPath)
    # 对文件进行排序并将排序后的ts文件路径放入列表中
    path_list.sort()
    li = [os.path.join(tsPath, filename) for filename in path_list]
    # 将ts路径并合成一个字符参数
    tsfiles = '|'.join(li)
    cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s'%    (tsfiles,saveMp4file)
    os.system(cmd)