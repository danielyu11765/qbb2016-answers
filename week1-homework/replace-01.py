#!/usr/bin/env python

import sys

for seq in open(sys.argv[1]):
  strand = seq.rstrip("\r\n").split("\t")
  #strand = strand.append(a)
  #print strand
  
  if "-" in strand[3]:
    #print strand    
    strand[3] = strand[3].replace("-", "")
    #print strand[3]
    #print strand
    
  strand = " ".join(strand)
  print strand