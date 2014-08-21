#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

response = urllib2.urlopen("https://www.python.org/")
html = response.read()

# print out the HTML response
print(html)
