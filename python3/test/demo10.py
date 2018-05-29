#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'html.parser')
print(soup.p.string)
