#!/usr/bin/env python

import sys
import fasta
import math
import numpy

contig = fasta.FASTAReader(open(sys.argv[1]))
count = []

for identifier, sequence in contig:
  ident = identifier.split("_")
  length = int(ident[3])
  count.append(length)
  
num_contig = str(len(count))
mini = str(min(count))
maxi = str(max(count))
ave = str(numpy.mean(count))

print "countig number = " + num_contig + "\nminimun contig = " + mini + "\nmaximum contig = " + maxi + "\naverage contig = " + ave

count.sort()
count_N50 = []
for c in count:
  #print [c]*c  
  count_N50 = count_N50 + [c]*c
#print count_N50
if len(count_N50) % 2 == 0:
  median = len(count_N50) / 2
  #print len(count_N50)
  contig_N50 = str(count_N50[median])
  #print count_N50[median]
  print "N50 = " + contig_N50
else:
  median = len(count_N50) / 2
  #print len(count_N50)
  contig_N50 = str(count_N50[median + 1])
  #print count_N50[median + 1]
  print "N50 = " + contig_N50

