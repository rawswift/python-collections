#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

# create a dictionary
a = {'first_name': "John",
     'last_name': "Doe",
     'address': "Somewhere out there",
     'email': "johndoe@mail.com"}

# print 'em all out
print a

# how many node/element we have?
print len(a)

# print specific node
print a['email']

# adding key value pair
a['phone'] = "123-4587"

# now, how many node/element we have?
print len(a)

# print 'em again
print a

# iterate through 'em
for x in a:
    print "%s : %s" % (x, a[x])

# print out get dictionary keys
print a.keys()

# print 'em using substitute
s = string.Template("Hi there! My name is $first_name from $address and you can reach me at $email")
print s.substitute(a)
