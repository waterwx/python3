#!/usr/bin/env python
# coding=utf-8

def account_login():
    password = input('password:')
    password_correct = password == '12345'
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()
