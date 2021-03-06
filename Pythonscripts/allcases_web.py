#coding=utf-8
import unittest
import sys
import time
import  re
import  HTMLTestRunner
import os
#这里需要导入测试文件
sys.path.append("\webtestcases")
from webtestcases import *
import HTMLTestRunner
listdir=r'D:\Workspace\Pythonscripts\webtestcases'
# testunit=unittest.TestSuite()
dict = {}
pattern = re.compile(r'\d+')
def creatsuite():
    testunit=unittest.TestSuite()
    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(listdir,pattern ='test*.py',top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        keys=re.search(pattern,str(test_suite)).group()
        dict[int(keys)]=test_suite
    dic=sorted(dict.iteritems(),key=lambda d:d[0])
    for k in dic:
        for test_case in k[1]:
            testunit.addTest(test_case)
        # for test_case in test_suite:
        #     testunit.addTests(test_case)
            # print test_suite
    return testunit

alltestcase=creatsuite()

#将测试用例加入到测试容器(套件)中
#testunit.addTest(unittest.makeSuite(test_normal.normal))
#testunit.addTest(unittest.makeSuite(test_sound.tts))
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
#定义个报告存放路径，支持相对路径。
month = time.strftime("%Y-%m",time.localtime(time.time()))
path =  r'D:\\phpStudy\WWW\testreport\\'+month
#path =  r'D:\\'+month
try:
    os.mkdir(path)
except:
    os.path.exists(path)
now = time.strftime("%Y-%m-%d",time.localtime(time.time()))
filename = path+'\\'+now+'-result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'Web端测试报告',
description=u'用例执行情况：')
#执行测试用例
runner.run(alltestcase)