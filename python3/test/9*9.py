#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={}\t'.format(i, j, i*j), end='')
    print()
	
