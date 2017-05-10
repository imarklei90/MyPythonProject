
class Person:
    def setName(self,name):
        self.name = name

    def getName(self):
        return name

    def greet(self):
        print "Hello,world!!! %s" %self.name

foo = Person()
bar = Person()

foo.setName("FOO")
bar.setName("BAR")

print foo.greet()
print foo.name

print bar.greet()
print bar.name