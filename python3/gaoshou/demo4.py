#!/usr/bin/env python
# coding=utf-8

def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)
text_filter('Python is lame1')
