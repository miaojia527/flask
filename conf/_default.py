#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'HaoJie Li'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'flask'
    },
    'session': {
        'secret': 'bFjjgZeRpbSubGBB'
    },
    'file': {
        'upload_folder': '/uploads',
        'allow_extensions': {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}, 
    },
    'redis': {
        'host': "127.0.0.1",
        'port': "6379",
        'db'  : "flask",
        'pass': "123456"
    }
}