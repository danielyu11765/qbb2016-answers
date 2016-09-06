#!/usr/bin/env python

"""

Read sequencne from a fasta file count the number of times each 
k-mer occurs across all sequences and print kmers and counts.

usage: 01-kmer-counter.py k < fasta_file

This is k-mer matcher
"""


import sys, fasta

#from fasta import FASTAReader

k = int(sys.argv[1])

for ident, sequence in fasta.FASTAReader(open(sys.argv[2])): # query file open
  kmer_counts = {} #this is a dictionary
  
  sequence = sequence.upper()
  for i in range(0, len(sequence) - k):
    kmer = sequence[i : i + k]
    if kmer not in kmer_counts:
      kmer_counts[kmer] = []   #get the i and store in the dictionary
      kmer_counts[kmer].append(i + 1)
      continue
    kmer_counts[kmer].append(i + 1) #update kmer_counts if it gets the same kmer !!!!!!
    #kmer_counts = kmer, kmer_counts[kmer]

#for kmer in sorted(kmer_counts, key=kmer_counts.get, reverse=False):#search iteritems !!!!!! .get !!use the function .get to sort the key=kmer_counts in kmer
    
    #print kmer, kmer_counts[kmer]
     
for ident2, sequence2 in fasta.FASTAReader(open(sys.argv[3])): #target open  
  
  sequence2 = sequence2.upper()
  for i2 in range(0, len(sequence2) - k):
    kmer2 = sequence[i2 : i2 + k]    
    if kmer2 in kmer_counts:      
      t_gene = ident2
      t_position = str(i2 + 1)
      q_position = " ".join(map(str, kmer_counts[kmer2]))
      print "\t".join([t_gene, t_position, q_position, kmer2])
      
      
      
      

    
    
    






