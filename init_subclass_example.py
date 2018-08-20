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
        When under def run(): and not instanced, __init_subclass invoked by calling run() gives:
            Meta <class '__main__.app.<locals>.ConcreteSub_0'>
            Meta <class '__main__.app.<locals>.ConcreteSub_1'>
            Meta <class '__main__.app.<locals>.ConcreteSub_2'>
            Meta <class '__main__.app.<locals>.ConcreteSub_3'>
            Meta <class '__main__.app.<locals>.ConcreteBase_0'>
        When classes are at the root:
            Meta <class '__main__.ConcreteSub_0'>
            Meta <class '__main__.ConcreteSub_1'>
            Meta <class '__main__.ConcreteSub_2'>
            Meta <class '__main__.ConcreteSub_3'>
            Meta <class '__main__.ConcreteBase_0'>

"""
import sys
import traceback # for callable name
from functools import wraps
import asyncio



def tracename(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        print(def_name)
        return def_name
    return wrapper


def run():
    
    class Registry():
    
        registered = []
        reg = {}
        app = {}
        sub_count = 0
#        basename_instance = None
    
        def __init__(self):
    
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
            
            Registry.basename_instance = def_name
            
#            self.basename = def_name
            
#            print('base instance self.basename', self.basename)
    
        def __init_subclass__(self):
            
            (filename,line_number,function_name,text)=traceback.extract_stack()[-3]
            def_name = text[:text.find('=')].strip()
            
            # this prints if the file hits the interpreter even if Registry
            # or its subclasses aren't themselves instantiated
            # 
#            print('Meta', self)
            # pre reg{} look
#            self.app.append(self)
            
            self.app[f'{def_name}_{Registry.sub_count}'] = [self]
            Registry.sub_count +=1
                
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
                Thanks for stopping by.
                  
                The coroutine needs some work,
                as demonstrations go.
                
                It neither implements a separate
                event loop, nor features concurrency,
                as I'd hoped at this point to feature.
                
                Other examples are forthcoming, or
                can already be found here.
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
    # expose classes    
    #-------------------------------------------------------------------------
                      
if __name__ == '__main__':
    
    def cleanup():
        app.reg['End']._goodbye()
        loop.close()
        try:
            sys.exit()
        finally:
            sys.exit()
    
    def review(app):  
        # now interrogate objects in the run() local scope through app.reg, as above
        print('Common names list,\n non-actionable:', app.registered)
        print('\nCallers in registry.app', app.app)
        # the actionable classes
        print("\nAll app keys: ", app.reg.keys())
        for k, v in app.reg.items():
            print(f"item: {k} = {str(v)}")
        print("\nSingle key 'Login': ", app.reg['Login'].sub)
    
#     import asyncio
#     file:///usr/share/doc/python3.6/html/library/asyncio-task.html
    async def slow_operation(future):
#         code to run in place of sleep
        await asyncio.sleep(5)
        future.set_result('Future is done!')
    
    # return instanced
    app = run()
    
    # setup async loop
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))


    keypress = ''
    # get character = chr(93) and ord()

    while keypress != 'q' or (chr(27)): # or chr(27): # chr(27) and ord(0x01b) are key <ESC> 
        keypress = input("\n's' to show, 'q' to quit\n\t >> ")
        if keypress == 's':
            review(app)
        if keypress == 'q':
            cleanup()
        else:
            # start the async loop now and print the result later
            # you will need to hit enter at the prompt
            # type and enter q or s while waiting  
#             loop.run_until_complete(future)
            try: 
                print(future.result())
            except BaseException as e:
                print('Future is not ready/set yet. Enter to try again.', e)
                loop.run_until_complete(future)
    cleanup()