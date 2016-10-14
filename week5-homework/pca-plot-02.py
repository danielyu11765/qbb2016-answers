#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

x_axis = []
y_axis = []

eigenvec = open(sys.argv[1])
line = eigenvec.readline(0)

for line in eigenvec:
  comp = line.rstrip("\r\n").split(" ")
  x_axis.append(comp[2])
  y_axis.append(comp[3])

plt.figure()
plt.scatter(x_axis , y_axis, s = 10)
plt.title("PCA of Genotype Data")
plt.savefig("PCA_geno_02.png")
plt.close()
