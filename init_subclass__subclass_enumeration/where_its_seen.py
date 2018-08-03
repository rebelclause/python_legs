#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:22:35 2018

@author: tim
"""

class Timer():
    
    subclasses = {}

    def __init__(self):
        pass

    def __init_subclass__(cls, **kwargs):
        print('Runner.', cls)
        print('Timer Dictionary :', Timer.__dict__.keys())
        # print(Timer.__init_subclass__()) # Forbidden fruit...
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls] = []


class Event(Timer):
    print("I'll take my own bathroom selfies...thanks anyway.")

    def __init__(self):
        print('This is nice, meeting on a real date.')
        if self.__class__ in super().subclasses:
            # get the index and link the two
            super().subclasses[self.__class__].append(self)

if __name__ == '__main__': # a good place for a breakpoint
    date = Event()
    date
    duty = Event()
    duty
    print(Timer.subclasses)
    
# 
