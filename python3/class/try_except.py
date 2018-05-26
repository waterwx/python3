#!/usr/bin/env python
# coding=utf-8

try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {0}'.format(text))
