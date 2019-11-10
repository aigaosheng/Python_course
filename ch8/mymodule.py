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

  
class classAdmin:
    '''
    demo to develop a student management class to manage student basic info such as student number,
    query student.
    
    Functionality:
    - add new student 
    - query student by name
    - query by address
    - query by age

    e.g. student info
    
    name age address
    Mike 12 holland
    John 11 clementi
    Jack 12 holland
    ...

    '''

    def __init__(self):
        #initialize class: add attribute here
        self.size_class = 0
        self.__student_info__ = {
                'name': {}, #key: name 
                'age': {},  #key: age
                'address': {} #key: address
                }

    def insert(self, name = None, age = None, address = None):
        #add student
        #check input parameters
        if name is None or age is None or address is None:
            raise Exception("Warning: please input name, age, and address")
        #update database
        name = name.lower()
        address = address.lower()
        stu_info = 'Name: {}, age: {}, address: {}'.format(name, age, address)
        if name in self.__student_info__['name']:
            self.__student_info__['name'][name].append(stu_info)
        else:
            self.__student_info__['name'][name] = [stu_info]
        
        if age in self.__student_info__['age']:
            self.__student_info__['age'][age].append(stu_info)
        else:
            self.__student_info__['age'][age] = [stu_info]

        if address in self.__student_info__['address']:
            self.__student_info__['address'][address].append(stu_info)
        else:
            self.__student_info__['address'][address] = [stu_info]

        self.size_class += 1


    def queryByName(self, q):
        try:
            return self.__student_info__['name'][q]
        except:
            return None

    def queryByAge(self, q):
        try:
            return self.__student_info__['age'][q]
        except:
            return None

    def queryByAddress(self, q):
        try:
            return self.__student_info__['address'][q]
        except:
            return None


    def show(self):
        for k, v in self.__student_info__['name'].items():
            print('\n'.join(v))
    
    def len(self):
        return self.size_class
