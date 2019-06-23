#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去"""
# class Stdent(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         print('name:', self.name)
#         self.score = score
#         print('score:', self.score)
# tom = Stdent('tom',88)
# print(tom.name)

################################################################

#数据封装
"""面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。
我们可以通过函数来访问这些数据，比如打印一个学生的成绩"""
# def print_scort(std):
#     print('%s: %s' %(std.name, std.score))
#
# print_scort(tom)

#################################################################

"""既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法"""
class Student(object):

    def __init__(self, name, score):
        self.name = name

        self.score = score


    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('lisa', 98)
zhuli = Student('zhuli',58)
lisa.print_score()
zhuli.print_score()
print(lisa.name, lisa.score, lisa.get_grade())
print(zhuli.name, zhuli.score, zhuli.get_grade())



###############################################################





