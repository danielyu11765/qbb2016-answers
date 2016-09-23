#!/usr/bin/env python
"""
parse a every FASTA record from stdin and print it. 

"""
import sys

class FASTAReader( object ):
    def __init__( self, file ):
        self.file = file
        self.last_id = None
        
        
    def __iter__( self ):
        return self
    
    def next( self ):
        if self.last_id is None:
            line = self.file.readline() #read one line from the file
            if line == "":
                raise StopIteration
            #read line before the loop
            # verify is header line
            assert line.startswith( ">" ) #make sure it starts with >
            # extract id --whole line
            ## identifier = line[1:].rstrip( "\r\n")
            # take away the > before each line

            #extract id -- space
            identifier = line[1:].split()[0] 
        else: 
            identifier = self.last_id

        sequences = []

        while True: #loop forever
            line = self.file.readline().rstrip("\r\n")
            if line.startswith(">"):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                if sequences: 
                    return identifier, "".join( sequences )
                ## return None, None
                raise StopIteration
            else:
                sequences.append( line )
                
        return identifier, "".join( sequences )
        
""""

reader = FASTAReader(sys.stdin)

while 1:
  identifier, sequence = reader.next()
  if identifier is None:
    break
  print identifier, sequence        
  
"""   