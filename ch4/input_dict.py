#!/usr/bin/env python
# -*- coding: utf-8 -*-
studb = dict()
while True:
    info = input('输入姓名和年龄，用逗号隔开: input Q if exit')
    if info == 'Q':
        print('输入结束')
        break
    try:
        name, age = info.split(',')
    except:
        print('Format error: must be YOUR_NAME, age, e.g. "jack, 12"')
        pass
    myage = int(age)
    studb[name] = myage
#sort by age
studb_sort = sorted(studb.items(), key = lambda x: x[1])
print(studb_sort)
