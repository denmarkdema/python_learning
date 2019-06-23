#/usr/bin/python
#-*- coding:UTF-8 -*-

import requests
from bs4 import  BeautifulSoup
import lxml

#定义一个浏览器

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Host': 'movie.douban.com'}

#
def get_movice():
    movie_list = []
        #分析页面代码
    for i in range(0, 10):
        """掌握link的规律"""
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=100)
        print(str(i+1),"页面响应状态码：",r.status_code)
        soup = BeautifulSoup(r.text, "lxml")
        div_list= soup.find_all('div',class_='hd')

    #利用for循环获取出每页的电影名字，然后append到一个新列表
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

    return movie_list
#
def get_director():
    dior_list = []
        # 分析页面代码
    for i in range(0, 10):
        """掌握link的规律"""
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i+1),"页面响应状态码：",r.status_code)
        soup = BeautifulSoup(r.text, "lxml")
        div_list= soup.find_all('div', class_='bd')

        for each in div_list:
            dior = each.p.text.strip()
            dior_list.append(dior)

    return dior_list

# movies = get_movice()
dior = get_director()
# a = len(movies)
# print(a, movies)
print(dior)



