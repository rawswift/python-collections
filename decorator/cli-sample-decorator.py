#!/usr/bin/env python

class Deco(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        # multiple it by itself
        result = result * result
        return result

@Deco
def process(x=0, y=0):
    return x+y

print process(1, 1) # 4
print process(2, 2) # 16
print process(3, 3) # 36
