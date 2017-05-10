class Secretive:
    def __inaccessable(self):
        print "can't access"

    def accessable(self):
        print "can access"
        self.__inaccessable()

s = Secretive()

s.accessable()
