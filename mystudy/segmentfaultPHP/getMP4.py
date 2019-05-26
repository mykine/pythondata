#! /usr/bin/env python  
# -*- coding:utf-8 -*-

import urllib.request
import re
import os
import platform
class DownVedio:
	def downMP4(self,mp4link,savefilepath):
		print( mp4link+"  ==>  " + savefilepath )
		#urllib.request.urlretrieve(mp4link, savefilepath)
		return True

	def downTStoMP4(self,m3u8link,saveTSpath,tsHost,):
		tsData = urllib.request.urlopen(m3u8link).read().decode('utf-8')
		tsParamArr = re.compile('/(.*?).ts').findall(tsData)
		for m in range(0,len(tsParamArr)):
			tsITurl = tsParamArr[m]+'.ts'
			tsLink = tsHost + tsITurl
			tsStrArr = tsITurl.split('/')
			tsSaveFile = saveTSpath+'/'+tsStrArr[len(tsStrArr)-1]
			print(tsITurl)
			print(tsLink)
			print(tsSaveFile)
			print("\n" + tsLink + "  ==>  " + tsSaveFile )
			# 将TS文件保存到本地
			urllib.request.urlretrieve(tsLink,tsSaveFile)
	def mergeTsMp4(self,saveTSpath,targetMP4Path):
		# 根据不同的系统调用不同的命令合成mp4
		if 'Windows' == platform.system():
			# windows下合并
			saveTSpath = saveTSpath+'/'
			saveTSpathWin = saveTSpath.replace('/', '\\')
			targetMP4PathWin = targetMP4Path.replace('/', '\\')
			cmd = 'copy /b ' + saveTSpathWin + '*.ts ' + targetMP4PathWin
			print(cmd)
			res = os.popen(cmd)
			print(res.read())
		else:
			# linux下使用ffmpeg将ts合成mp4文件
			# 获取所有的ts文件
			path_list = os.listdir(saveTSpath)
			# 对文件进行排序并将排序后的ts文件路径放入列表中
			path_list.sort()
			li = [os.path.join(saveTSpath, filename) for filename in path_list]
			# 将ts路径并合成一个字符参数
			tsfiles = '|'.join(li)
			cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s' % (tsfiles, targetMP4Path)
			os.system(cmd)


#第2个视频特殊mp4地址https://media.video.segmentfault.com/live/e6a59548da20bcf3.mp4?sign=1afe9a38678f46602e0b929b3f60430a&t=5cea262c
#第1、3、4、5、6、7个都是m3u8格式视频
mp4url2 = 'https://media.video.segmentfault.com/live/e6a59548da20bcf3.mp4?sign=1afe9a38678f46602e0b929b3f60430a&t=5cea262c'
m3u8Host = 'https://media.video.segmentfault.com/live/'
tsHost = 'https://media.video.segmentfault.com/'
m3u8urlList = [
	'vpg5c6d58eed1735.m3u8?sign=c19fea6fa0d9134aa231539350c2138b&t=5cea2c1d',
	'',
	'nfc595bb532046d4.m3u8?sign=5b4f9aa1a40089e39a8625febe133ad1&t=5cea2c55',
	'a4v59c3bd54ea31f.m3u8?sign=5d554c19091dccd2aef857dc37fc9801&t=5cea2c67',
	'rsa59c3c4d563813.m3u8?sign=d05519d5bd900992f8fff0b3d25ab751&t=5cea2c83',
	'u5g59551ea78c30a.m3u8?sign=7d37838c8639591394b0cc980b7c54a5&t=5cea2c94',
	'5ly597cb1e76d38f.m3u8?sign=99dd04bee71b71af945c2d098c345bf4&t=5cea2ca3',
]
for n in range(0,len(m3u8urlList)):
	num = n+1
	saveMp4path = 'vedio/'+str(num)
	saveTSpath = 'vedio/' + str(num)+'/ts'
	targetMP4Path = saveMp4path + '/'+str(num)+'.mp4'
	if os.path.exists(saveMp4path) is not True:
		os.makedirs(saveMp4path)
	if os.path.exists(saveTSpath) is not True:
		os.makedirs(saveTSpath)
	downObj = DownVedio()
	if m3u8urlList[n] != '':
		#下载TS
		m3u8link = m3u8Host +  m3u8urlList[n]
		downObj.downTStoMP4(m3u8link,saveTSpath,tsHost)
		#转化成mp4
		downObj.mergeTsMp4(saveTSpath, targetMP4Path)

	else:
		downObj.downMP4(mp4url2,targetMP4Path)
		print("直接下载mp4")





