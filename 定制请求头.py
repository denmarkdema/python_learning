#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

#定制headers

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'HOST': 'www.hao123.com'
}
#r是requests的Response对象
r = requests.get('https://www.hao123.com', headers=headers)

print("响应状态码：", r.status_code)

