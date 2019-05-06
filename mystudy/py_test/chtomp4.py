import os

#ts文件所在目录
tsPath = "/mystudy/py_test/mp4/"

#获取所有的ts文件
path_list = os.listdir(tsPath)

#对文件进行排序并将排序后的ts文件路径放入列表中
path_list.sort()
li = [os.path.join(tsPath,filename) for filename in path_list]
#将ts路径并合成一个字符参数
tsfiles = '|'.join(li)

#print(tsfiles)

#指定输出文件名称
saveMp4file = tsPath + 'target.mp4'

#调取系统命令使用ffmpeg将ts合成mp4文件
cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s'%    (tsfiles,saveMp4file)
os.system(cmd)