#! /usr/bin/env python  
# -*- coding:utf-8 -*-
# for i in range(1,2):
# 	print(str(i)+"\n")
class TestClass:
	name = ''
	age = 0
	def __init__(self):
		self.name = '多多'
		self.age = 10
		print("构造函数执行了")
	def showinfo(self,year):
		print(self.name+year+str(self.age)+"岁了")
	def __del__(self):
		print("析构函数执行了")

testObj = TestClass()
testObj.showinfo("在2019年")
print(testObj.age)




