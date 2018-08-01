#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:20:16 2018

@author: Tim Pozza
@email: rebelclause@gmail.com

# https://docs.python.org/3.6/reference/datamodel.html#metaclasses
# https://stackoverflow.com/questions/1690400/getting-an-instance-name-inside-class-init

Extract the callable to a class instance and put it in the registry along with its originating class, or an override supplied as an argument to the class when it is instanced.

"""
import inspect # for get_my_name_0
import traceback # for get_my_name_1

class Registry():

    registered = []

    def __init__(self):
        pass

    def __init_subclass__(self):
        
        # lets instance override meta_init???
#        self.__init__(self) 
        
        if self.__name__ == 'ConcreteSub_0':
            self.sub = self.__name__
        if self.__name__ == 'ConcreteSub_1':
            self.sub = self.__name__
        if self.__name__ == 'ConcreteSub_2':
            self.sub = self.__name__
        if self.__name__ == 'ConcreteSub_3':
            self.sub = self.__name__
        if self.__name__ == 'ConcreteBase_0':
            self.sub = self.__name__
        
# =============================================================================
#         (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
#         def_name = text[:text.find('=')].strip()
#         self.defined_name = def_name
# =============================================================================
        
#        print('init_subclass', self.__name__, self.name)
        
#        self.registered.append([self.sub])
        
#        self._register(self)

    def get_my_name_0(self):
        ans = []
        frame = inspect.currentframe().f_back
#        tmp = dict(frame.f_globals.items() + frame.f_locals.items())
        tmp = dict(**frame.f_globals, **frame.f_locals)
        for k, var in tmp.items():
            if isinstance(var, self.__class__):
                if hash(self) == hash(var):
                    ans.append(k)
        return ans


class Events():
    ''' '''
    def __init__(self):
        pass

class ConcreteSub_0(Registry):
    ''' '''
    def __init__(self, *args):
        if len(args) > 0:
            self.sub = args[0]
  
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        self.name = def_name
        
        # can't call on _register b/c _init_subclass from Registry() doesn't make the list available until it completes. so the latest entry is unavailable... dict???
#        self._register(self)
        
        self.registered.append([self.name, self.sub])         

            
class ConcreteSub_1(Registry):
    ''' '''
    def __init__(self, *args):
        if len(args) > 0:
            self.sub = args[0]
  
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        self.name = def_name
        
        self.registered.append([self.name, self.sub])         
       
            
class ConcreteSub_2(Registry):
    ''' '''
    def __init__(self, *args):
        if len(args) > 0:
            self.sub = args[0]
  
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        self.name = def_name
        
        self.registered.append([self.name, self.sub])         
       

class ConcreteSub_3(Registry):
    ''' '''
    def __init__(self, *args):
        if len(args) > 0:
            self.sub = args[0]
  
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        self.name = def_name 
        
        self.registered.append([self.name, self.sub])         
      
            
class ConcreteBase_0(Registry, Events):
    ''' '''
    def __init__(self, *args):
        if len(args) > 0:
            self.sub = args[0]
  
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        self.name = def_name
        
        self.registered.append([self.name, self.sub])         
        
            
if __name__ == '__main__':
    

    # class arguments override ConcreteClass name assignment to registry    
    registry = Registry()
    Login = ConcreteSub_0('conflict')
    Setup = ConcreteSub_1('waiting')
    Loop = ConcreteSub_2()
    Event = ConcreteBase_0()
    End = ConcreteSub_3('bye')
    print(Login.sub)
    print(Setup.sub)
    print(Loop.sub)
    print(Event.sub)
    print(Loop.registered)
    print(Event.registered)
    print(End.sub)
    # print(registry.sub) # sub is not on the baseclass