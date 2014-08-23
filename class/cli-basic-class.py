#!/usr/bin/env python
# -*- coding: utf-8 -*-

# create the class
class FruitsClass:

    def __init__(self):
        self.fruits = ["apple", "banana", "carrot"]

    def addFruit(self, fruit_name):
        self.fruits.append(fruit_name)

    def getFruit(self, index=None):
        if index:
            return self.fruits[index]
        else:
            return self.fruits

fruits = FruitsClass()

# get and print out all fruits
print fruits.getFruit()

# get and print out specific fruit based on index
print fruits.getFruit(1) # 'banana'

# add fruit
fruits.addFruit("grape")

# get and print out all fruits, again (w/ the newly added fruit, grape)
print fruits.getFruit()

# how many fruits do we have?
print len(fruits.getFruit())
