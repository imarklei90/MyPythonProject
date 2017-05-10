# -*- encoding:utf-8 -*-

class MyClass:
    """
        静态方法定义时，没有self参数，可以被类本身直接调用
    """
    @staticmethod
    def smeth():
        print "this is a static method"

    """
        类方法定义时需要名为cls的类似于self的参数，类成员方法可以直接用类的具体对象调用，cls参数是自动绑定到类的
    """
    @classmethod
    def cmeth(cls):
        print "this is a class method",cls

MyClass.smeth()
MyClass.cmeth()