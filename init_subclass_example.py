#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:20:16 2018

@author: tim
# https://docs.python.org/3.6/reference/datamodel.html#metaclasses
# https://stackoverflow.com/questions/1690400/getting-an-instance-name-inside-class-init

Extract the callable to a class instance and put it in the registry along with its originating class, or an override supplied as an argument to the class when it is instanced.

Goal:
    Create new app instances which automatically pick up the sub-classes via __init_subclass, and then expose them in a list attached to the app instance as yield(able) coroutines within an app loop, switching state in the process.
    Subclasses shouldn't need a name, as when they are instanced the app should be ready.
        Consider putting the entire class structure inside a function, so that the instances may not be created until the function is called, thereby initializing a major part of the application. Check to see if the globals are still available, as the docs on Data Model suggest should be the case with this construction of namespaces. 
        When under def app(): and not instanced, __init_subclass invoked by calling app() gives:
            Meta <class '__main__.app.<locals>.ConcreteSub_0'>
            Meta <class '__main__.app.<locals>.ConcreteSub_1'>
            Meta <class '__main__.app.<locals>.ConcreteSub_2'>
            Meta <class '__main__.app.<locals>.ConcreteSub_3'>
            Meta <class '__main__.app.<locals>.ConcreteBase_0'>
        When at the document root:
            Meta <class '__main__.ConcreteSub_0'>
            Meta <class '__main__.ConcreteSub_1'>
            Meta <class '__main__.ConcreteSub_2'>
            Meta <class '__main__.ConcreteSub_3'>
            Meta <class '__main__.ConcreteBase_0'>

"""
import traceback # for callable name


def run():
    
    class Registry():
    
        registered = []
        reg = {}
#        basename_instance = None
    
        def __init__(self):
    
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            
            Registry.basename_instance = def_name
            
#            self.basename = def_name
            
#            print('base instance self.basename', self.basename)
    
        def __init_subclass__(self):
            
            # this prints if the file hits the interpreter even if Registry
            # or its subclasses aren't themselves instantiated
            # 
#            print('Meta', self)
            # pre reg{} look
#            self.app.append(self)
                
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
            
            self.registered.append([self.name, self.sub]) 
    
            print('Sub', self)
            self.reg[def_name] = self           
    
    
    class ConcreteSub_1(Registry):
        ''' '''
        def __init__(self, *args):
            if len(args) > 0:
                self.sub = args[0]
      
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            self.name = def_name
            
            self.registered.append([self.name, self.sub])
            self.reg[def_name] = self           
            print('Sub', self)        
           
                
    class ConcreteSub_2(Registry):
        ''' '''
        def __init__(self, *args):
            if len(args) > 0:
                self.sub = args[0]
      
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            self.name = def_name
            
            self.registered.append([self.name, self.sub])
            self.reg[def_name] = self    
            print('Sub', self)        
             
           
    class ConcreteSub_3(Registry):
        ''' '''
        def __init__(self, *args):
            if len(args) > 0:
                self.sub = args[0]
      
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            self.name = def_name 
            
            self.registered.append([self.name, self.sub])
            self.reg[def_name] = self
            print('Sub', self)
        
        def _goodbye(self):
            print("""
                  It's been a good run.
                  
                  Thanks for coming by.
                  
                  See you next time?
                  
                  Over the next few iterations
                  
                  I'll try to sequence with
                  
                  a coroutine and possibly use 
                  
                  the same to invite 
                  
                  concurrency/event handling, 
                  
                  you know, without class handlers.
                 
                  
                  """)
          
                
    class ConcreteBase_0(Registry, Events):
        ''' '''
        def __init__(self, *args):
            if len(args) > 0:
                self.sub = args[0]
      
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            self.name = def_name
            
            self.registered.append([self.name, self.sub])
            self.reg[def_name] = self
            print('Sub', self)
            
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
        
    # instance Registry
    registry = Registry()
    
    # pass registry to var app which called app()
    return registry
    
    # 
    # expose app classes    
    #-------------------------------------------------------------------------
                      
if __name__ == '__main__':
    
    # return instanced run() classes to app
    app = run()
    
    # now enquire objects in the run() local scope through app.reg, as above
    for k, v in app.reg.items():
        print(k, str(v))
    
    print(app.reg.keys())

    print(app.reg['Login'].sub)
    
    keypress = ' '
    while True:
        input('Enter to run _goodbye()')
        
        app.reg['End']._goodbye()
    
