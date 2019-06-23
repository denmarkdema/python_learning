#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyClass:
    """A example class"""
    x = 'abc'  #类属性

    def foo(self):  #类属性foo  也是方法
        return 'My Class'

print(MyClass.x)
print(MyClass.foo)
print(MyClass.__doc__)
