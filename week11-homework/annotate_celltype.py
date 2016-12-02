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

mat_exp = np.matrix(matrix_exp)
#print mat_exp
mat_ct = np.transpose(mat_exp)
#print mat_ct

#Z = linkage(mat_exp, "ward")
Z = linkage(mat_ct, "ward") # the first argument should be a matrix
#Z = linkage(mat_ct, "single")
#Z = linkage(mat_ct, "complete")
#Z = linkage(mat_ct, "average")

#ref. -> https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
def anno_dendrogram(*args, **kwargs):
    max_d = kwargs.pop("max_d", None)
    if max_d and "color_threshold" not in kwargs:
        kwargs["color_threshold"] = max_d
    annotate_above = kwargs.pop("annotate_above", 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get("no_plot", False):
        plt.title("Hierarchical Clustering Dendrogram (annotated)")
        plt.xlabel("Hematopoietic cell types")
        plt.ylabel("Distance")
        for i, d, c in zip(ddata["icoord"], ddata["dcoord"], ddata["color_list"]):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, "o", c = c)
                plt.annotate("%.3g" % y, (x, y), xytext = (0, -5),
                             textcoords = "offset points",
                             va = "top", ha = "center")
        if max_d:
            plt.axhline(y = max_d, c = "k")
    return ddata

anno_dendrofig = plt.figure(figsize = (25, 10))
anno_dendrogram(
Z,
truncate_mode = "lastp",
p = 12,
leaf_rotation = 0.,
leaf_font_size = 15.,
show_contracted = True,
annotate_above = 10, # useful in small plots so annotations don't overlap
labels = header
)
plt.show()
anno_dendrofig.savefig("Hema_cell_types_annotated")


"""
plt.figure(figsize = (25, 10))
#Dendrofig = plt.figure(figsize = (25, 10))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Hematopoietic cell types")
plt.ylabel("Distance")

dendrogram(Z, 
leaf_rotation = 0.,  # rotates the x axis labels
leaf_font_size = 15.,  # font size for the x axis labels
labels = header
)
plt.show()
#Dendrofig.savefig("Hema_cell_types.png")
"""
  