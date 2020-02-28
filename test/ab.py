#!/usr/bin/env python3
#coding=utf-8

import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')

print(m.group())