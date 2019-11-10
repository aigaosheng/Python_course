# -*- coding: utf-8 -*-
'''
demo class
'''
#import a module, so all functions in the module imported
import mymodule

#declare a class instance
adm = mymodule.classAdmin()
name, age, address = 'Aa', 12, 'aaa'
adm.insert(name, age, address)
adm.insert('BB', 11, 'bbb')
adm.insert('BB', 12, 'ccc')
adm.insert('BC', 12, 'aaa')

print('\n--- Show database ---')
adm.show()
print('number of student: {}\n'.format(adm.len()))

name = 'aa'
q = adm.queryByName(name)
print('-------------------')
print('query_name={} info: {}\n'.format(name, '\n'.join(q)))

age = 12
q = adm.queryByAge(12)
print('-------------------')
print('query_age={} info: {}\n'.format(age, '\n'.join(q)))

address = 'aaa'
q = adm.queryByAddress(address)
print('-------------------')
print('query_adress={} info: {}\n'.format(address, '\n'.join(q)))
