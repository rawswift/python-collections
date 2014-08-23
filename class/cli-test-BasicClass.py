#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import the class
from BasicClass import BasicClass

# instantiate
a = BasicClass()

# set name
a.setName("John Doe")

# get and print out the name
print a.getName()

# replace the name
a.setName("Foo Bar")

# get and print out the name, again
print a.getName()
