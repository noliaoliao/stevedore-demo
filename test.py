#!/usr/bin/env python
from stevedore import driver

mgr = driver.DriverManager(
    namespace = "example.sayhello",
    name = "dog",
    invoke_on_load = True,
    invoke_args = ("5.5",),
)

mgr.driver.sayHello("stevedore")

