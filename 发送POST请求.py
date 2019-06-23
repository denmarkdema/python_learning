#/usr/bin/python
#-*- coding:UTF-8 -*-
import requests

#用字典传递post参数
key_dict = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('http://httpbin.org/post', data=key_dict)
r1 = requests.get("http://www.hao123.com/auto", timeout=22)


print(r.text)
print("状态码：", r1.status_code)

