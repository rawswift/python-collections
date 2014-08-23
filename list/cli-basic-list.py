#!/usr/bin/env python
# -*- coding: utf-8 -*-

# create list
a = ["apple", "banana", "carrot"]

# print 'em
print a

# how many node/element we have?
print len(a) # 3

# iterate
for x in a:
    print x

# append
a.append("orange")

# print 'em again
print a

# now, how many node/element we have?
print len(a) # 4

# print out the value from specific index
print a[1] # banana

# change value
a[2] = "grape" # change 'carrot' to 'grape'

print a
