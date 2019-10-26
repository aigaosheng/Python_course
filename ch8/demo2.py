# -*- coding: utf-8 -*-

#import a module, so all functions in the module imported
import mymodule

#generate a test input value
v = {
        'arron': ['python'],
        'shengwei': ['python']
    }
print('\nTest value: {}\n'.format(v))

#call function
s = mymodule.isMember('arron', v)
if s:
    print('{} is member\n'.format('arron'))
else:
    print('{} is not member\n'.format('arron'))


name = 'shengwei'
s = mymodule.isMember(name, v)
if s:
    print('{} is member\n'.format(name))
else:
    print('{} is not member\n'.format(name))

name = 'Shengwei'
s = mymodule.isMember(name, v)
if s:
    print('{} is member\n'.format(name))
else:
    print('{} is not member\n'.format(name))


#demo lambda 
lda_func = lambda x, mem_db: x in mem_db
name2 = name.lower()
s = lda_func(name2, v)
if s:
    print('{} is member using lambda function\n'.format(name2))
else:
    print('{} is not member using lambda function\n'.format(name2))


