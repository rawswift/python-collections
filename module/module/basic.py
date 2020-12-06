#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import helper

class BasicClass:
    def __init__(self):
        self.name = None

    def setName(self, name):
        self.name = name

    def  getName(self):
        return helper.reverse_and_uppercase(self.name)
