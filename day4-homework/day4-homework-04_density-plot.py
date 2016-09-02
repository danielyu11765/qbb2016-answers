#!/usr/bin/env python

"""

Usage: ./01-timecourse.py <metadata.csv> <ctab file> <ctab_dir>

~/data/fastq/samples.csv ~/data/fastq/replicates.csv ~/data/results/stringtie/

"""



import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde



df = pd.read_table(sys.argv[1]) #SRR072893 ------------1
df = df["FPKM"].values #collect
df_log = np.log10(df)

#df_f = df[f].values #update

#data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8
density = gaussian_kde(df)
xs = np.linspace(0, max(df_log), 10000)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.title("SRR072893 density plot")         

plt.xlabel("log10(FPKM) value")                   
plt.ylabel("Kernel density ")
plt.savefig("day4-homework-04_density-plot.png")        
#plt.show()
plt.close()






#plt.figure()
#plt.scatter(a, m, alpha = 0.1)
#plt.title("SRR072893 / SRR072915 MA-plot")         
#plt.xlabel("A")                   
#plt.ylabel("M")  
#plt.savefig("day4-homework-03_MA-plot.png")        
#plt.close()                      











