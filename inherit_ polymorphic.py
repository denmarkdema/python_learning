#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写"""

"""在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。"""
#定义一个Animal的类：

class Animal(object):
    def run(self):
        print('Animal is running')

#Dog和Cat类时，就可以直接从Animal类继承

class Dog(Animal):
    #对子类增加一些方法
    def run(self):
        print('Dog is runing')

    def eat(self):
        print("eating meat...")


class Cat(Animal):
    def run(self):
        print('cat is running')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

"""传入Animal的实例时，run_twice()就打印出"""

def run_twice(animal):
    animal.run()
    animal.run()



"""对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
继承最大的好处是子类获得了父类的全部功能。
由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法"""
dog = Dog()
dog.run()
dog.eat()

"""当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()"""


cat = Cat()
cat.run()

#判断一个变量是否是某个类型可以用isinstance()判断
if isinstance(dog, Animal) == True:
# if isinstance(dog, Dog) == Ture:
    print('True')
else:
    print('False')

#Animal的实例时，run_twice()
run_twice(Animal())
#Dog的实例时，run_twice()
run_twice(Dog())
#Cat的实例时，run_twice()就打印
run_twice(Cat())
"""新增一个Animal的子类，不必对run_twice()做任何修改，实际上，
任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态"""
run_twice(Tortoise())

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(Animal))

print(len(Animal))
