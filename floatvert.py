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
		#	""" """
		#	pass
	
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

	# http://rgruet.free.fr/PQR27/PQR2.7.html search: 'format codes	'
	@staticmethod
	def shortfloat(self, *args): #if 'self' is here, you'll get an error, could make use of it as a switch
		""" Send long floats to shorten them in various ways according to the first parameter passed.\n
		currently: tuple, list\n
		requires: a first parameter, as above, or generic placeholder of type int or str
		"""
		if str(type(self)).__contains__('int'): #check for type
			#consume 'self'
			return args
		if self == 'tuple': # special type according to self
			list = [(float('%.3F'%round(arg, 1))) for arg in args]
			print(list)
			list = list[0], list[1], list[2] #convert to a tuple; omit if you want a list
			return list
		if self == 'list':
			list = [(float('%.3F'%round(arg, 1))) for arg in args]
			print(list)
			return list
		if self == 'dict':
			list = {args.index(arg): float('%.3F'%round(arg, 1)) for arg in args}
			# print(list)
			return(list)
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
# #	Tests of function shortfloat()
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
