#!/usr/bin/env python

import sys, fasta

k = int(sys.argv[1]) # kmer length
q_file = open(sys.argv[2]) # open query
t_file = open(sys.argv[3]) # open target

q_kmer = {}  # query kmer dictionary; key = kmer, value = start position

for ident, sequence in fasta.FASTAReader(q_file):
    sequence = sequence.upper()
    for i in range(0,len(sequence) - k): # st = start, end = end
        st = i
        end = i + k
        kmer = sequence[i : i + k]
        if kmer not in q_kmer:
          q_kmer[kmer] = [st] 
        else:
          q_kmer[kmer].append(st)

kmer_matches = [] #build a list for storing kmer matchers

for ident2, sequence2 in fasta.FASTAReader(t_file):
    sequence2 = sequence2.upper()
    t_kmer = {}
    for i, j in enumerate(range(0,len(sequence2) - k)):
        i = i # i is the start of target seq
        j = i + k # j is the end of target seq
        
        
        kmer2 = sequence2[i : i + k]
        if kmer2 in q_kmer:
           for st in q_kmer[kmer]: # start and end of query seq
               end = st + k
               up = 1 # the kmer can go up or down, set them to variables
               down = 1 
               while True:
                   if sequence2[i - up] == sequence[st - up]:
                       up = up + 1
                   elif i - up == -1 or st - up == -1:
                       break
                   else:
                       break
               up = up - 1
               while True:
                   if j + down == len(sequence2) or end + down == len(sequence): 
                       break
                   if sequence2[j + down] == sequence[end + down]:
                       down = down + 1
                   else:
                       break
                       
               match = sequence2[i - up + 1 : j + down]
               kmer_matches.append(match)
               
kmer_matches.sort( reverse = True, key = len )
            
for match in kmer_matches[:1000]:
    print match