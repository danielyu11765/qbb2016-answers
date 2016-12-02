#!/usr/bin/env python

#============================================================#
# IMPORTS

import numpy as np
import os
import sys
import pylab
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from matplotlib import pyplot as plt

#============================================================#

gene_exp = open(sys.argv[1])
gene_read = gene_exp.readlines()

header = [] #['CFU', 'poly', 'unk', 'int', 'mys', 'mid'], used for heatmap row
matrix_exp = []
gene_names = [] #["all gene names as a list"], used for heatmap column
#test = []

for line in gene_read:
  #print line
  if line.startswith("anything you want"):
    continue
  
  if line.startswith("gene"):
    header = line.rstrip("\n").split("\t")[1:]
    #test.append(header)
    #print header
    continue
  
  #print line
  #matrix = line.rstrip("\n").split("\t")
  #print matrix
  data = line.rstrip("\n").split("\t")[1:]
  float_data = []
  for string in data:
    number = float(string)
    float_data.append(number)
    
  matrix_exp.append(float_data)
  
  gene_name = line.rstrip("\n").split("\t")[0]
  gene_names.append(gene_name)
#print gene_names
#print list(matrix_exp)
matrix_exp01 = np.matrix(matrix_exp)
#print matrix_exp01

#-#-#-#-#-#- clustering by gene expression #-#-#-#-#-#-

matrix_exp02 = linkage(matrix_exp01, "ward") # the first argument should be a matrix. use linkage to process.
#print matrix_exp02
matrix_exp03 = leaves_list(matrix_exp02) # after transfer this data set to corresponding matrix, it can be uesd for heatmap, but we need to use 2 dimensions to build up a complete heat map
#print matrix_exp03
matrix_exp04 = matrix_exp01[matrix_exp03] #recover the matrix by using the components of matix_exp03 as indexs
#matrix_exp04_1 = matrix_exp01[matrix_exp03, :]

#print matrix_exp01
#print matrix_exp01[368]
#print matrix_exp03[2]
#print matrix_exp04[2]

#-#-#-#-#-#- clustering by cell type #-#-#-#-#-#-

matrix_ct01 = matrix_exp04.transpose()
#print matrix_exp04
#print matrix_ct01
matrix_ct02 = linkage(matrix_ct01, "ward")
matrix_ct03 = leaves_list(matrix_ct02)
#print matrix_ct03
matrix_ct04 = matrix_ct01[matrix_ct03] # This is the final data set for plotting the heat map
#print matrix_ct04

gene_names_update = np.array(gene_names)[matrix_exp03]
#print gene_names_update
#print header
header_update = np.array(header)[matrix_ct03]
#print header_update



#""""
# Make the actual plot
plt.figure()                                 # Open a blank canvas
plt.title("Heatmap of gene expression") # Add a title to the top
plt.imshow(                                  # Treat the values like pixel intensities in a picture
	matrix_ct04.T,                                       # ... Using X as the values
	aspect='auto',                           # ... 'Stretch' the image to fit the canvas, so you don't get a skinny strip that is 4x150 pixels
	interpolation='nearest',                 # ... Don't use any blending between pixel values
	cmap="RdBu",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
	#vmin=-1*m,                               # ... Set the lowest value to show on the scale
	#vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
	)
plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
plt.xticks(            # Edit the xticks being shown
	range(matrix_ct04.T.shape[1]), # ... use the values centered on each column of pixels
	header_update,            # ... which corresponds to the indices of our labels
	rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
	)
plt.yticks([])         # Edit the ticks on the y-axis to show....NOTHING
plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values

#plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
    #left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
    #bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
    #right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
    #top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
#)

plt.savefig("heatmap_gene_exp.png") # Save the image
#plt.show()
plt.close() # Close the canvas
#"""