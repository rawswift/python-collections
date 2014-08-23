#!/usr/bin/env python
# -*- coding: utf-8 -*-

# create tuple
a = ("one", "two", "three")

# print 'em
print a

# how many node/element we have?
print len(a) # 3

# print using format
print "Counting %s, %s, %s..." % a

# iterate
for x in a:
    print x

# print value from specific index
print a[1] # 'two'

# create another tuple (using previous tuple)
b = (a, "four")

print b[1] # 'four'
print b[0][2] # 'three'

# how many node/element we have?
print len(b) # 2
