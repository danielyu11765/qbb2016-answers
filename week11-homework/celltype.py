#!/usr/bin/env python

import numpy as np
import os
import sys
import pylab
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

gene_exp = open(sys.argv[1])
gene_read = gene_exp.readlines()

header = [] #['CFU', 'poly', 'unk', 'int', 'mys', 'mid']
matrix_exp = []

for line in gene_read:
  #print line
  if line.startswith("anything you want"):
    continue
  
  if line.startswith("gene"):
    header = line.rstrip("\n").split("\t")[1:]
    #print header
    continue
  
  #print line
  #matrix = line.rstrip("\n").split("\t")
  #print matrix
  data = line.rstrip("\n").split("\t")[1:]
  gene_name = line.rstrip("\n").split("\t")[0]
  #print data
  #print gene_name
  matrix_exp.append(data)
  #print matrix
#print list(matrix_exp)
mat_exp = np.matrix(matrix_exp)
#print mat_exp
mat_ct = np.transpose(mat_exp)
#print mat_ct
#"""
#Z = linkage(mat_exp, "ward")
Z = linkage(mat_ct, "ward") # the first argument should be a matrix!!
#Z = linkage(mat_ct, "single")
#Z = linkage(mat_ct, "complete")
#Z = linkage(mat_ct, "average")


Dendrofig = plt.figure(figsize = (25, 10))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Hematopoietic cell types")
plt.ylabel("Distance")
dendrogram(Z, 
leaf_rotation = 0.,  # rotates the x axis labels
leaf_font_size = 15.,  # font size for the x axis labels
labels = header
)
plt.show()
Dendrofig.savefig("Hema_cell_types.png")
#"""
  
  