#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from HTMLParser import HTMLParser

# HTML Tag Stripper class
class HTMLTagStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.data = []
        self.isScriptTag = False
        self.isStyleTag = False

    def handle_starttag(self, tag, attr):
        # <script> tag flag
        if tag == 'script':
            self.isScriptTag = True
        elif tag == 'style':
            self.isStyleTag = True

    def handle_endtag(self, tag):
        # </script> (end) tag flag
        if tag == 'script':
            self.isScriptTag = False
        elif tag == 'style':
            self.isStyleTag = False

    def handle_data(self, data):
        # as long as it's not a <script> and <style> tag, store the data value
        if not self.isScriptTag and not self.isStyleTag:
            # but wait there's more! ...as long as it's not a line feed or tab
            if data and data != "\n" and data != "\t":
                # store/append the data and while we're at it, strip whitespaces, tags, line feed, and carriage return
                self.data.append(data.strip(' \t\n\r'))

    def get_data(self):
        # filter out null/None nodes
        resp = filter(None, self.data)
        return ' '.join(resp)

# open the url/page
response = urllib2.urlopen("https://www.python.org/")
html = response.read()

# remove HTML tags
hts = HTMLTagStripper()
hts.feed(html)

# get the data and cast it as string
data = str(hts.get_data())

# print it out!
print(data)
