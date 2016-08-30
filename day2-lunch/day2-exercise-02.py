#!/usr/bin/env python

import sys


#read in the file name from first argument
x = sys.argv[1]
print x

#open the file based on the file name
y = open(x)

#read the lines in the opened file
lines = y.readlines()



count=0
for l in lines:
    if "NM:i:0" in l:
        count = count + 1
        
        
        
print count




#print "day2 python Test Test Test"