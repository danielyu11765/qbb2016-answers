#!/usr/bin/env python

"""

Usage: ./01-timecourse.py <metadata.csv> <ctab file> <ctab_dir>

~/data/fastq/samples.csv ~/data/fastq/replicates.csv ~/data/results/stringtie/

"""



import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_table(sys.argv[1]) #SRR072893 ------------1
df2 = pd.read_table(sys.argv[2]) #SRR072915 -----------2

x = df1["FPKM"].values +1
y = df2["FPKM"].values +1


m = np.log2(x) - np.log2(y)
a = 0.5 * np.log2(x * y)




plt.figure()
plt.scatter(a, m, alpha = 0.1)
plt.title("SRR072893 / SRR072915 MA-plot")         
plt.xlabel("A")                   
plt.ylabel("M")  
plt.savefig("day4-homework-03_MA-plot.png")        
plt.close()                      











