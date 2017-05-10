# -*- encoding:utf-8 -*-
class FooBar:
    '''构造方法定义'''
    def __init__(self,value = 1111):
        self.somevar = value
f = FooBar()
print f.somevar
