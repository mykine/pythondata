#视频页面vedioSRC = 'https://www.finger66.com/mobile/post/5109165?channel=wechatSession&from=singlemessage&isappinstalled=0'
#放置ts文件所在目录
import time
import os
nowTimeStr = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
# thisDateTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(thisDateTime)
# exit()
tsPath = "mp4/"+str(nowTimeStr)+"/"
if(os.path.exists(tsPath)==False):
    os.makedirs(tsPath,777)
#获取ts文件参数
hostname = 'https://media.finger66.com'
tsParamUrl = hostname + '/posts/84222300000/MTU1NjEwNDU0ODI2Nw==.mp4.m3u8'
import urllib.request
tsParamData = urllib.request.urlopen(tsParamUrl).read().decode('utf-8')
# print(tsParamData)
# exit()
import re
pat = '(.*?).ts'
tsParamArr = re.compile(pat).findall(tsParamData)
# print(tsParamArr)
# exit()
# import _thread
#from threading import Thread
import threading

def saveTSToLocal(n,tsLink,localPath):
    thisDateTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print("begin: "+str(n)+"  "+thisDateTime+" "+localPath)
    urllib.request.urlretrieve(tsLink,localPath )
    thisDateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("end: "+str(n)+"  "+thisDateTime+"  "+tsLink)
    time.sleep(0.01)

#爬取ts文件到本地
threadList = []
for n in range(0,len(tsParamArr)):
    # print("begin_for: "+str(n))
    strArr = tsParamArr[n].split('/')
    localTSFileName = strArr[len(strArr)-1]+'.ts'
    tsLink = hostname + '/' + tsParamArr[n] + '.ts'
    # urllib.request.urlretrieve(tsLink, tsPath+localTSFileName )
    localPath = tsPath+localTSFileName
    # saveTSToLocal(n,tsLink,localPath)
    # _thread.start_new_thread(saveTSToLocal,(n,tsLink,localPath))
    t = threading.Thread(target=saveTSToLocal,args=(n,tsLink,localPath))
    t.start()
    threadList.append(t)
    # t.join()
    # print("end_for: "+tsLink)

for m in range(0,len(threadList)):
    threadList[m].join()
print("for end~~~~~~")

import platform

#指定输出文件名称
saveMp4file = tsPath + nowTimeStr+'_target.mp4'
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