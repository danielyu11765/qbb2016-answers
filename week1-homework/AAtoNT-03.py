#!/usr/bin/env python

""""

Parse a single FASTA record from stdin and print it

"""

import sys

line = sys.stdin.readline()
# read only one line
# verify is header line

assert line.startswith(">") #what is assert ?
#extract ID ---- whole line
#identifier = line[1:].rstrip("\r\n")

identifier = line[1:].split()[0] #try here

sequences = []

while 1: #1 means always True!!!!
  line = sys.stdin.readline().rstrip("\r\n")
  if line.startswith(">") or line == "":
    break
  else:
    sequences.append(line)

print identifier, "".join(sequences)





    
    
