# -*- coding: utf-8 -*-

def mysum(in_value, in_modulo = 2):
    '''
    The function is to demo how to sum the values which are specified modulo as parameter and demo how to set default values in    parameter

    in_value: integer list or tuple
    in_modulo: the modulo number. if not set when calling function, default value = 2

    Return: the sum of number which is the modulo
    
    '''
    print('input modulo: {}'.format(in_modulo))
    sv = 0
    for v in in_value:
        if v % in_modulo == 0:
            sv += v

    return sv

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


