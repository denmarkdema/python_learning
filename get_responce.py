#/usr/bin/python

#获取响应内容：
import requests

r = requests.get('https://www.w3cschool.cn')
print("文本编码：", r.encoding)
print("响应状态码：", r.status_code)
print("字符串方式的响应体：", r.text)
"""
r.content 是字节方式的响应体，会自动解码gzip 和 deflate 编码的响应数据
r.json()是Requests 中内置的JSON解码器

"""

