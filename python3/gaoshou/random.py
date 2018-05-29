#!/usr/bin/env python
# coding=utf-8

import random

def roll_dice(numbers=3, points=None):
    print('<<<<<ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

roll_dice()
