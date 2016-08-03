from example import base

class Pig(base.SayHelloBase):
    def sayHello(self, msg):
        print "[Pig]: %s" %msg 
