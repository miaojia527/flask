#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html
from urllib.request import urlopen
'''
for line in urlopen("http://www.baidu.com"):
    line = line.decode('utf-8')
    #print(line)
'''

'''
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()
'''

p = '&lt;abc&gt;'
p = '<p>abc</p>'
txt= html.escape(p)
print (txt)
ht = html.unescape(txt)
print (ht)