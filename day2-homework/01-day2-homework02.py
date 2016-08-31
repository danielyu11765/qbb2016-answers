#!/usr/bin/env python

#import sys

#read in the file name from first argument
#x = sys.argv[1]
#open the file based on the file name
#gene_map_head = open(x) #read the lines in the opened file
#gene_map = gene_map_head.readlines()


#y = sys.argv[2]

#ctab_head = open(y)
#ctab = ctab_head.readlines()


#gene_dic = {}


#for line in gene_map:
  #column = line.rstrip("\r\n").split(9)


import sys



def flymapping(fly, ctab):
  make_dic = {}
  for line in open(fly):
    field = line.rstrip("\r\n").split("\t")
    flygene = field[0]
    swiss_ac = field[1]
    #make_dic[key]=val
    make_dic[flygene] = swiss_ac
  #print make_dic
  
  #for genename_ctab, output in enumerate(open(ctab)):
  for lines in open(ctab):
    fields = lines.rstrip("\r\n").split("\t")
    genename_ctab = fields[8]

    if genename_ctab in make_dic: 
      value = make_dic[genename_ctab]
      
    else:
      value = "None"
    
    #print value
    
    print lines.strip(), "\t", value

    


"""
    if genename_ctab == flygene:
      make_dic[1] = swiss_ac
      output = 
    elif:
      make_dic[1] = "None"
"""

flymapping(sys.argv[1], sys.argv[2])



#for line in open(flymapping):
  








