#!/usr/bin/env python

"""

Read sequencne from a fasta file count the number of times each 
k-mer occurs across all sequences and print kmers and counts.

usage: 01-kmer-counter.py k < fasta_file
"""


import sys, fasta

#from fasta import FASTAReader

k = int(sys.argv[1])

for ident, sequence in fasta.FASTAReader(open(sys.argv[2])): # query file open
  kmer_counts = {}
  
  sequence = sequence.upper()
  for i in range(0, len(sequence) - k):
    kmer = sequence[i : i + k]
    if kmer not in kmer_counts:
      kmer_counts[kmer] = []   #get the i and store in the dictionary
      kmer_counts[kmer].append(i) 
      continue
    kmer_counts[kmer].append(i) 
  
    
for ident2, sequence2 in fasta.FASTAReader(open(sys.argv[3])): #target open
  for i in range(0, len(sequence2) - k):
    kmer2 = sequence[i : i + k]
    if kmer2 in kmer_counts:
      target_gene = ident2
      target_position = str(i)
      query_position = " ".join(map(str, kmer_counts[kmer2]))
    
    print "\t".join([target_gene, target_position, query_position, kmer2])
      
      
    
    

#for kmer in kmer_counts:
#    print kmer, kmer_counts[kmer]

#for kmer, count in kmer_counts.iteritems(): #search iteritems !!!!!!
    #print kmer, count





#for kmer in kmer_counts:
  #print kmer, kmer_counts[kmer]
    
    #if kmer not in kmer_counts:   #this is as same a previous one
      #kmer_counts[kmer] = 1
    #else:
      #kmer_counts[kmer] += 1
    
    
    
    






