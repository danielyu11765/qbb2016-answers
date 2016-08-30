#!/usr/bin/env python

import sys


#read in the file name from first argument
x = sys.argv[1]
print x

#open the file based on the file name
y = open(x)

#read the lines in the opened file
lines = y.readlines()


# iterate to every line, count the lines starts with "S" 


count=0
for l in lines:
    if l[0]=="S":
        count = count + 1
        
        
        
print count




#print "day2 python Test Test Test"