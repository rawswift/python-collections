#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from HTMLParser import HTMLParser

# HTML Hyperlink(s) getter
class GetHyperlinks(HTMLParser):

    def __init__(self):
        self.reset()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

    def get_links(self):
        return self.links

# open the url/page
response = urllib2.urlopen("https://www.python.org/")
html = response.read()

# get HTML's hyperlinks
gh = GetHyperlinks()
gh.feed(html)

# iterate through result and print 'em out
links = gh.get_links()
for link in links:
    print(link)
