#!/usr/bin/env python

import sys
#import fasta
import itertools



aa = sys.argv[1] #to "x"
nt = sys.argv[2] #to "y"

#aa = open(sys.argv[1]) #to "x"
#nt = open(sys.argv[2]) #to "y"

#aa = fasta.FASTAReader(open(sys.argv[1])) #to "x"
#nt = fasta.FASTAReader(open(sys.argv[2])) #to "y"
proteins = []
nucleotides = []


for x in aa:
    proteins.append(x)
    
for y in nt:
    nucleotides.append(y)
    
for i in itertools.izip(proteins, nucleotides):
    rev_trl = []
    n = 0
    aa_seq = i [0][1]
    nt_seq = i [1][1]
    for aa_x in aa_seq:
        if aa_x == "-":
            rev_trl.append("---")
        else:
            nt_y = nt_seq[ n: n+3 ]
            n += 3
            rev_trl.append(nt_y)
    print ">" + str(i [0][0])
    print "".join(rev_trl)

