class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize)

r = Rectangle()
r.width = 10
r.height = 5

# print r.getSize()
# r.setSize((100,50))
# print r.getSize()

print r.size
r.size = 180,100
print r.width

# 如果属性的行为很奇怪，就需要确保使用的类为新式类（直接或者间接地子类化object，或者直接设置__metaclass__ = type）