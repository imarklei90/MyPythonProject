class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "haha"
            self.hungry = False
        else:
            print "3Q"

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = "SONG"
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()