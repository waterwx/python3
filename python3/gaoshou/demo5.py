#!/usr/bin/env python
# coding=utf-8

def account_login():
    password = input('password:')
    if password == '12345':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()
