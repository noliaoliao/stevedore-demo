from example import base

class Dog(base.SayHelloBase):
    def sayHello(self, msg):
        print "[Dog]: %s" %msg
