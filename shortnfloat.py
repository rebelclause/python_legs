#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:39:20 2018

@author: tim
"""

import re, os, sys
from collections import namedtuple as nt
# import pandas as pd
import numpy as np

class generic(object):
    """

    """
    name = 'yourname'

    def __init__(self, *args, **kwargs):
        """ """
        self.arg1 = arg1

    def __str__(self):
        """ """
        pass

    def __repr__(self):
        """ """
        pass

    def __iter__(self):
        """ """
        pass
        # def __next__(self): #for the other
        #    """ """
        #    pass

    def __get__(self, *args):
        """ """
        pass

    def __set__(self, *args):
        """ """
        pass

    def __del__(self, *args):
        """ """
        pass

    @classmethod
    def __clsmethod__(self):
        """ """
        pass

    # http://rgruet.free.fr/PQR27/PQR2.7.html search: 'format codes    '
    @staticmethod
    def shortfloat(self, *args): #if 'self' is here, you'll get an error, could make use of it as a switch
        """ Send long floats to shorten them in various ways according to the first parameter passed.\n
        currently: tuple, list, dict\n
        requires: a first parameter, as above, or generic placeholder of type int or str
        * can also take a generator object in place of value args
        """
# =============================================================================
#         try: # handle an incoming generator of any length, getting all values
#             gen = [] #args
#             try:
#                 while True:
#                     gen.append(next(*args)) # could use the default param instead of StopIteration to flag the generator's end ie. gen.append(next(*args, 'OXEoA'))
#                     # print(next(*args)) # any next() iteration consumes another generator element, making it unrecoverable without another call
#             except StopIteration as _e:
#                 ERR = _e.value
#             args = tuple(gen)
#         except:
#             pass
# =============================================================================
#        print('args[0] ', args[0])
#        print('args[1] ', args[1])
        try: # handle an incoming generator of any length, getting all values
            gen = list(args[0]) # quick unpacking/conversion of a finite length generator
            args = tuple(gen)
            print('gen ran fine: ', gen)
        except TypeError:
            print('gen got TypeError')

        if str(type(self)).__contains__('int'): #check for type
            #consume 'self'
            return args
        if self == 'tuple': # special type according to self
#            thislist = [(float('%.3F'%round(arg, 1))) for arg in args] # one string method
            thislist = [('{:.1F}'.format(float(round(arg,1)))) for arg in args] # second string method
#            thislist = list[0], list[1], list[2] #convert to a tuple; omit if you want a list
            thislist = tuple(thislist) # universally extensible method of converting list to tuple
            return thislist
        if self == 'list':
#            thislist = [(float('%.3F'%round(arg, 1))) for arg in args]
            thislist = []
            for arg in args: # third string method
                short = round(arg, 1)/1
                thislist.append(f'{short:.3F}')
            return thislist
        if self == 'dict':
            thislist = {args.index(arg): float('%.3F'%round(arg, 1)) for arg in args}
            # print(thislist)
            return(thislist)
        else:
            pass

def main():
    """ Who's calling main()? I'm not calling main(). But if I did, I'd see the filename. """
    print('sys.argv[:]:', vars)
    pass

if __name__=="__main__":
    #vars=[]
    vars=sys.argv[:]

# =============================================================================
# #    Tests of function shortfloat()
# =============================================================================
    # return a tuple
    shortcoord = x, y, z = generic.shortfloat('tuple', 2.55555555, 9.00000000012, 666.36) #send floats
    print('x:{}, y:{}, z:{}; shortcoord:{}; shortcoord[0]:{}'.format(x, y, z, shortcoord, shortcoord[0]))

    # return a list
    shortcoord = x, y, z = generic.shortfloat('list', 2.55555555, 9.00000000012, 666.36) #send floats
    print('x:{}, y:{}, z:{}; shortcoord:{}; shortcoord[2]:{}'.format(x, y, z, shortcoord, shortcoord[2]))

    # cut the params short and return the positional *args the same way they were sent (a tuple)
    shortcoord = x, y = generic.shortfloat(0, 1, 2)
    print('Args returned as sent (1st param stripped):{}'.format(shortcoord))

    # return a dictionary and see the keys assigned to x, y, z
    shortcoord = x, y, z = generic.shortfloat('dict', 2.55555555, 9.00000000012, 666.36) #send floats
    print(x, y, z)
    # dict key vars return populated
    print('Key \'x\':', shortcoord[x])
    print('Key \'y\':', shortcoord[y])
    print('Key \'z\':', shortcoord[z])
    print('shortcoord:{}'.format(shortcoord))
    # print('x:{}, y:{}, z:{}; shortcoord:{}; shortcoord[2]:{}'.format(x, y, z, shortcoord, shortcoord[2]))

    # print(dir(generic.shortfloat))
    # main(vars)

    # send a list of values
    myvals = [33.464636, 932.23423, 34232.2346432427]

    # send a generator composed from a list, return a tuple
    shortcoord = x, y, z = generic.shortfloat('tuple', (x for x in myvals) ) #send floats via generator
    print('x:{}, y:{}, z:{}; shortcoord:{}; shortcoord[0]:{}\n'.format(x, y, z, shortcoord, shortcoord[0]))
