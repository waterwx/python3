#!/usr/bin/env python
# coding=utf-8

def text_create(name, msg):
    desktop_path = '/home/water/python3/python3/test/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')

text_create('hello', 'hello world')


def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)
text_filter('Python is lame1')
