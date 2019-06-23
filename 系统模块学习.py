#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,sys
#1、文件
f = open('/opt/code/hello.txt', 'w')
#open(路径+文件名，读写模式)
#读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
str = '123\n'
f.write(str)

f.close()
fo = open("/opt/code/test.txt", "w")
print("文件名为: ", fo.name)
str = "菜鸟教程"
fo.write(str)

# 关闭文件
fo.close()

#2、用Python写一个列举当前目录以及所有子目录下的文件，并打印出绝对路径

for root,dirs,files in os.walk('/tmp'):
    for name in files:
        print(os.path.join(root,name))
os.walk()


