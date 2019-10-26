# -*- coding: utf-8 -*-

def mysum(in_value, in_modulo = 2):
    '''
    The function is to demo how to sum the values which are specified modulo as parameter and demo how to set default values in    parameter
    
    input:
    in_value: integer list or tuple
    in_modulo: the modulo number. if not set when calling function, default value = 2

    return: the sum of number which is the modulo
    
    '''
    print('input modulo: {}'.format(in_modulo))
    sv = 0
    for v in in_value:
        if v % in_modulo == 0:
            sv += v

    return sv

def isMember(usr_name, member_db = {}):
    '''
    demo check is user enrolled as member

    input: 
        usr_name: a string
        member_db: a dict
    '''

    if usr_name in member_db:
        return True
    else:
        return False


class addStr:
    '''
    demo how to define a simple class. The class is to concatenate ingeter/float/string with string 
    '''

    def __init__(self):
        #initialize class, if class need arguments/parameters, defie in __init__()
        pass
    
    def add(self, s):
        return ''.join(map(lambda x: str(x) if not isinstance(x, str) else x, s))

    
