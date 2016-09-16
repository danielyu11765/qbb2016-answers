#!/usr/bin/env python

""""

Parse every FASTA record from stdin and print it

"""

import sys

  

class FASTAReader(object):  #class can store function, like function organizer
  def __init__(self, file):
    self.file = file
    self.last_id = None
    
  def next(self):
    if self.last_id is None:  
      line = self.file.readline()
      # read only one line
      # verify is header line

      assert line.startswith(">")
      #extract ID ---- whole line
      #identifier = line[1:].rstrip("\r\n")
  
      identifier = line[1:].split()[0] #try here
    else:
      identifier = self.last_id
      
    sequences = []

    while 1: #1 means always True!!!!
      line = sys.stdin.readline().rstrip("\r\n")
      if line.startswith(">"): #or line == "": #MODIFY here!!!!
        self.last_id = line[1:].split()[0]
        break
      elif line == "":
        return None,None
      else:
        sequences.append(line)
    
    return identifier, "".join(sequences)



#print identifier, "".join(sequences)




# what i wannt:
reader = FASTAReader(sys.stdin)

while 1:
  identifier, sequence = reader.next()
  if identifier is None:
    break
  print identifier, sequence
  #print sequence

    
    
