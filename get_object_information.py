#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()
#hasattr() 函数用于判断对象是否包含对应的属性。语法：hasattr(object, name)
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性

setattr(point1, 'no', 99) #设置属性 no  数值为99
print(hasattr(point1, 'no'))

#getattr() 函数用于返回一个对象属性值，语法：getattr(object, name[, default])可以传入一个default参数，如果属性不存在，就返回默认值
getattr(point1,"aa") #报错，AttributeError
print(getattr(point1, 'aa', 404))  #找不到属性，返回默认值







