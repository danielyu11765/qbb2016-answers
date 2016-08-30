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
total=0

for l in lines:
    if l[0]=="S":
        lists = l.split()
        if lists[4]!="*" and int(lists[4])!=255:
            #print lists[4]
            count += 1
            total = total + int(lists[4])
            
                
print total
print count
                
print float(total)/count     
            
            
            
            #print lists[4]
            #count = count + 1
            #if count==10: 
                #break        
        
print count

#       check if equel: == or iif not equel !=


#print "day2 python Test Test Test"