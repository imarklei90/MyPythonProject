# -*- enconding:utf-8 -*-
"""
迭代器：一个实现了__iter__方法的对象是可迭代的，一个实现了next方法的对象是迭代器
"""

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 0
    def next(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a
    def __iter__(self):
        return self

"""
生成器：任何包含yield语句的函数就是生成器，每次返回多个值，每次产生一个值，函数就会被冻结
"""