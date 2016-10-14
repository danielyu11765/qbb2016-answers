#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

af = []

allelefreq = open(sys.argv[1])
line = allelefreq.readline()

for line in allelefreq:
  comp = line.rstrip("\r\n").split("\t")
  homA1 = float(comp[4])
  homA2 = float(comp[6])
  freq = homA1 / (homA1 + homA2)
  af.append(freq)

plt.figure()
plt.hist(af, bins = 100)
plt.title("Allele Frequencies of Genotype Data")
plt.xlabel("SNP frquency")
plt.ylabel("Count of SNP Frequency")
plt.savefig("Allele_freq.png")
plt.close()

