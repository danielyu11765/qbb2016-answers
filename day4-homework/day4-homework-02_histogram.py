#!/usr/bin/env python


import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_table(sys.argv[1])
df_roi = df["FPKM"] != 0     #collect

df1 = df[df_roi]     #update, filtered with FPKM
chromo = df1["chr"].values   # list of chromosome

x = np.log10(df1["FPKM"]) 


minimum = np.min(x)
maximum = np.max(x) 

plt.figure()
plt.hist(x)
plt.title("SRR072893")
plt.ylabel("mRNA abundance (FPKM)")
plt.savefig("day4-homework-02_histogram.png")    
plt.close()