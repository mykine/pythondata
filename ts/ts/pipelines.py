# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):
    __fh = None
    def __init__(self):
       self.fh = open("1.txt","a",-1,'UTF-8')
    def process_item(self, item, spider):
        #print(type(item['title']))#class list类型
        txtCont = str(item['title'][0])+","+str(item['link'][0])+","+str(item['stu'][0])+"\n"
        print(txtCont);
        self.fh.write(txtCont)
        pass
    def __del__(self):
        print("写入完毕")
        self.fh.close()

