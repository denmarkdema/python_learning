#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class student(object):
    def __init__(self,name,score,age):
        self.__name = name
        self.__score = score
        self.__age = age

    def get_score(self):
        print('%s: %s' % (self.__name, self.__score), '123')
        """对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了"""

    """如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法"""
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


    # def get_score(self):
    #     return self.__score

    """又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法"""

    def set_score(self, score):
        #避免传入无效参数
        if 0 <= score <= 100:
            self.__score = score
            # return self.__socre
        else:
            raise ValueError('bad score')

tom = student('tom', 98,18)
tom.get_score()
print(tom.get_name())
#修改分数
tom.set_score(80)
#读取分数
tom.get_score()

