#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse_and_uppercase(str):
    reversed_string  = ""
    index = len(str)

    while index > 0:
        reversed_string += str[index - 1].upper()
        index = index - 1
        
    return reversed_string
