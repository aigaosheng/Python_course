# -*- coding: utf-8 -*-
from mymodule import mysum
#generate a test input value
v = range(10)
print('Test value: {}\n'.format(list(v)))

#call function
s = mysum(v)
print('sum of using default {} is {}\n'.format(2, s))

#call function
i_mod = 3
s = mysum(v, i_mod)
print('sum of using {} is {}\n'.format(i_mod, s))

#call function
i_mod = 3
s = mysum(v, in_modulo = i_mod)
print('sum of using {}(call by key) is {}'.format(i_mod, s))


