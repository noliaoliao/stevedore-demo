#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = "test stevedore",
    version = "1.0",
    description = "test stevedore desc",
    author = "lyh",
    packages = find_packages(),
    include_package_data = True,
    entry_points = {
        'example.sayhello': [ 
            'dog = example.mydog.dog:Dog',
            'pig = example.mypig.pig:Pig',
        ],
    },
)
