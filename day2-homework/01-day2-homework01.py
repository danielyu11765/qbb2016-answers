#!/usr/bin/env python

import sys

#read in the file name from first argument. Now is flybase
x = sys.argv[1]
print x

#open the file based on the file name
y = open(x)

#read the lines in the opened file
lines = y.readlines()

#not_DROME = 0

for l in lines:
  #make each l in lines as a list
  list = str(l).split()
  #Introduce 2 conditions
  #exclude len(list) == 4 w/o "DROME" ----> other species
  #exclude empty
  #exclude len(list) == 5, ex: CG18543             Dyak   MTRM_DROYA   P83733      FBgn0068364
  if len(list) == 4 and "DROME" in list[1]:
    print "%s\t%s" % (list[3], list[2])
  
  #take len(list) == 2 with "DROME" back -----> alternative splicing or transposon
  #ex: VASA2_DROME  B6JUP5 vs VASA1_DROME  P09052      FBgn0262526, they share the same FlyBaseID
  #must add " "DROME" in list[0] "!!!!!
  elif len(list) == 2 and "DROME" in list[0]:
    print "\t\t%s" % (list[1])
    #print "%s\t%s" % (list[3], list[2])
  #else:
    #not_DROME += 1

#print not_DROME




""""
total_l5_wDROME = 0
total_l5_woDROME = 0

for l5 in lines:
  list = str(l5).split()
  if len(list) == 5 and "DROME" in list[2]:
    total_l5_wDROME += 1
  elif len(list) == 5 and "DROME" not in list[2]:
    total_l5_woDROME += 1
    
    
print total_l5_wDROME, total_l5_woDROME    #(0, 1988)


total_l5 = 0
for l5 in lines:
  list = str(l5).split()
  if len(list) == 5:
    total_l5 += 1

print total_l5   #(1988)
"""

"""
total_l2_wDROME = 0
total_l2_woDROME = 0

for l2 in lines:
  list = str(l2).split()
  if len(list) == 2 and "DROME" in list[0]:
    total_l2_wDROME += 1
    print list [0]
  elif len(list) == 2 and "DROME" not in list[0]:
    total_l2_woDROME += 1
    
    
print total_l2_wDROME, total_l2_woDROME    #(39, 2)


total_l2 = 0
for l2 in lines:
  list = str(l2).split()
  if len(list) == 2:
    total_l2 += 1
print total_l2     #(41)
"""

"""

total_l4_wDROME = 0
total_l4_woDROME = 0


for l4 in lines:
  list = str(l4).split()
  if len(list) == 4 and "DROME" in list[1]:
    total_l4_wDROME += 1
    
  elif len(list) == 4 and "DROME" not in list[1]:
    total_l4_woDROME += 1
    print list[1]
    
print total_l4_wDROME, total_l4_woDROME     #(3408, 593)


total_l4 = 0
for l4 in lines:
  list = str(l4).split()
  if len(list) == 4:
    total_l4 += 1
print total_l4     #(4001)
"""


"""
total_genes_l5 = 0
total_genes_l4 = 0
total_genes_l2 = 0

for genes in lines:
  list = str(genes).split()
  if len(list) == 5 and "FBgn" in list[4]:
    total_genes_l5 += 1
  elif len(list) == 4 and "FBgn" in list[3]:
    total_genes_l4 += 1
  elif len(list) == 2 and "DROME" in list[0]:
    total_genes_l2 += 1

total_genes = total_genes_l5 + total_genes_l4 + total_genes_l2
    
print total_genes, total_genes_l5, total_genes_l4, total_genes_l2
#(6016, 1983, 3994, 39)
"""



    
  
  # print each line as a list
  
  
  #print l[0]
  
  #if l[0]=="S":
        #count = count + 1