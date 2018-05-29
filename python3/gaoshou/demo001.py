#!/usr/bin/env python
# coding=utf-8

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)
