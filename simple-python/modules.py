#!/bin/python
##import sys
from sys import argv
for arg in argv:
	print "arg is ",arg

##print "sys path is ",sys.path


from mod import say

say()
