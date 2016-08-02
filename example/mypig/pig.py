from example import base

class Pig(base.SayHelloBase):
    def sayHello(self, msg):
        print "hello,pig. %s" %msg 
