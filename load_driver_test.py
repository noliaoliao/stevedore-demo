#!/usr/bin/env python
from stevedore import driver
from stevedore import extension

def load_as_driver():
    mgr = driver.DriverManager(
        namespace = "example.sayhello",
        name = "dog",
        invoke_on_load = True,
        invoke_args = ("base",),
    )
    
    mgr.driver.sayHello("stevedore")


def sayHello(ext, msg):
    return (ext.name, ext.obj.sayHello(msg))

def load_as_extension():
    mgr = extension.ExtensionManager(
        namespace = "example.sayhello",
        invoke_on_load = True,
        invoke_args = ("base",),
    )
    
    results = mgr.map(sayHello,"load_as_extension")

    #for name, res  in results:
    #    print name 

if __name__ == "__main__":
    load_as_driver()
    load_as_extension()








