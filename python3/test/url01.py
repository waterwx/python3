#!/usr/bin/env python
# coding=utf-8


from urllib.request import urlopen
html = urlopen("http://192.168.9.252/index.html")
print(html.read())
