#!/usr/bin/env python
import abc

class SayHelloBase(object):
     
    __metaclass__ = abc.ABCMeta 

    def __init__(self, msg = "Base"):
        self.msg = msg

    @abc.abstractmethod 
    def sayHello(self, msg):
        pass


