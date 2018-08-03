#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:22:35 2018

@author: tim
"""
from collections import OrderedDict as odict

class Timer():
    
    subclasses = odict()

    def __init__(self):
        pass

    def __init_subclass__(cls, **kwargs):
#        print(cls.easyname)
        cls.subclasses[cls.easyname] = []


class Event(Timer):
    easyname = 'Event'

    def __init__(self):
        if self.__class__ in super().subclasses:
            # get the index and link the two
            super().subclasses[self.__class__].append(self)
        if self.easyname in super().subclasses:
            super().subclasses[self.easyname].append(self)

class Login(Timer):
    easyname = 'Login'

    def __init__(self):
        if self.__class__ in super().subclasses:
            # get the index and link the two
            super().subclasses[self.__class__].append(self)
        if self.easyname in super().subclasses:
            super().subclasses[self.easyname].append(self)
            

if __name__ == '__main__':
    date = Event()
    date
    duty = Event()
    duty
    print(Timer.subclasses)
    
 
