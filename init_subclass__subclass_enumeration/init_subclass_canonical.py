#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:13:35 2018

@author: tim

https://docs.python.org/3/reference/datamodel.html
https://docs.python.org/3.6/whatsnew/3.6.html#pep-487-simpler-customization-of-class-creation
https://stackoverflow.com/a/51661030/7955763
"""


class PluginBase:

    subclasses = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class Plugin1(PluginBase):
    
    def __init__(self):
        pass

class Plugin2(PluginBase):
        
    def __init__(self):    
        pass
    

m = Plugin1()
n = Plugin2()

print(PluginBase.subclasses)
print(m, n)
