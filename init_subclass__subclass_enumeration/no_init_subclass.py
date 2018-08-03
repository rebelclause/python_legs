#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:20:16 2018

@author: tim
# https://docs.python.org/3.6/reference/datamodel.html#metaclasses
# https://stackoverflow.com/questions/1690400/getting-an-instance-name-inside-class-init

Extract the callable to a class instance, using it as a key in a dictionary of subclass instances.

"""
import traceback # for callable name
from collections import defaultdict as ddict
from collections import ChainMap as cmap

def app():
    
    class Registry():
    
        registered = dict()
        basename_instance = None
    
        def __init__(self):
            pass
    
        def __init_subclass__(cls, **kwargs):
            
#            cls.registered[cls] = []
#            del cls.registered[cls]
            pass

    
    class Events():
        ''' '''
        def __init__(self):
            pass
    
    
    class ConcreteSub_0(Registry):
        ''' '''
        def __init__(self, *args, **kwargs):
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            def_name = def_name
            
            if len(args) > 0:
                self.sub = args[0]
            else:
                self.sub = def_name
            
            if def_name in super().registered:
                super().registered[def_name].append([self])
            else:
                super().registered[def_name] = []
                super().registered[def_name].append([self])
                

           
    
    
    class ConcreteSub_1(Registry):
        ''' '''
        def __init__(self, *args, **kwargs):  
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            def_name = def_name
            
            if len(args) > 0:
                self.sub = args[0]
            else:
                self.sub = def_name
            
            if def_name in super().registered:
                super().registered[def_name].append([self])
            else:
                super().registered[def_name] = []
                super().registered[def_name].append([self])
            

        
           
                
    class ConcreteSub_2(Registry):
        ''' '''
        def __init__(self, *args, **kwargs):
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            def_name = def_name
            
            if len(args) > 0:
                self.sub = args[0]
            else:
                self.sub = def_name
            
            print(super().registered.keys())
            
            if def_name in super().registered:
                super().registered[def_name].append([self])
            else:
                super().registered[def_name] = []                
                super().registered[def_name].append([self])

      
             
           
    class ConcreteSub_3(Registry):
        ''' '''
        def __init__(self, *args, **kwargs):
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            def_name = def_name
            
            if len(args) > 0:
                self.sub = args[0]
            else:
                self.sub = def_name
            
            if def_name in super().registered:
                super().registered[def_name].append([self])
            else:
                super().registered[def_name] = []
                super().registered[def_name].append([self])

      
          
                
    class ConcreteBase_0(Registry, Events):
        ''' '''
        def __init__(self, *args, **kwargs):
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            def_name = def_name
            
            if len(args) > 0:
                self.sub = args[0]
            else:
                self.sub = def_name
            
            if def_name in super().registered:
                super().registered[def_name].append([self])
            else:
                super().registered[def_name] = []
                super().registered[def_name].append([self])


            
    Login = ConcreteSub_0('Begin')
    print(Login.sub)
     
    Setup = ConcreteSub_1()
    print(Setup.sub)
     
    Loop = ConcreteSub_2()
    print(Loop.sub)
     
    Event = ConcreteBase_0()
    print(Event.sub)
     
    End = ConcreteSub_3('Exit')
    print(End.sub)
    
#    global registry
    
    # instance Registry
    registry = Registry()
    
    # pass registry to var app which called app()
    return registry
    
    # 
    # expose app classes    
    #-------------------------------------------------------------------------
            
# @coroutine
def run():
    pass

         
if __name__ == '__main__':
    
    myapp = app()
    newapp = app()
    
    bigglob = cmap(myapp.registered, newapp.registered)
    
    print(myapp.registered, '\n')
    print(newapp.registered, '\n')

    for k, v in myapp.registered.items():
        print('myapp', k, str(v))
        
    for k, v in newapp.registered.items():
        print('newapp', k, str(v))
        
    for k, v in bigglob.items():
        print('glob', k, str(v))

