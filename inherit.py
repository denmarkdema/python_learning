#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml

#第一步：获取网页代码
link = "http://www.xinhuanet.com/"

#伪装浏览器
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.2.6'}

#r是requests的Response对象
r = requests.get(link, headers =  headers)
#解决乱码
r.encoding = 'UTF-8'

#第二步：分析数据
soup = BeautifulSoup(r.text, "lxml") #使用BeautifulSoup解析这段代码
title = soup.find("h3", class_="name").a.text.strip()
print(title)

#第三步：存储数据
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()


#r.text是获取网页内容代码
#print(r.text)



