#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv(sys.argv[1], sep="\t")
df2 = pd.read_csv(sys.argv[2], sep="\t")
winSize = int(sys.argv[3]) #windowSize
#read ctab
#2L 2R 3L 3R 4 and X

chromo = ["2L", "2R", "3L", "3R", "4", "X"]

for i in range(0,6):       #6 don't count, select from 0 to 5 ------- 0,1,2,3,4,5
  df_roi = df["chr"] == chromo[i]
  df_chr = df[df_roi]
  
  x = df_chr["FPKM"].rolling(winSize).mean()
  
  df2_roi = df2["chr"] == chromo[i]
  df2_chr = df2[df_roi]
  
  y = df2_chr["FPKM"].rolling(winSize).mean()
  


  plt.figure()                            # Open canvas
  plt.title("Chromosome {} FPKM rolling mean (windowsize = {})".format(chromo[i], winSize))   
# Will appear above the plot
  plt.plot(x, color = "Red") # Plots x vs y with a dotted black line
  plt.plot(y, color = "Orange")
#plt.xlabel(labels[0])                   # Label the x axis
#plt.ylabel(labels[1])                   # Label the y axis
  plt.savefig("chr_{}.png".format(chromo[i]))           # Save
  plt.close()                             # Close canvas


  
  
  
  



  
  

"""

df_roi = df_ctab["FPKM"] > 0
df_ctab2 = df_ctab[df_roi]
df_roi2 = df_ctab2["gene_name"] == "Sxl"
df_sxl = df_ctab2[df_roi2]

x1 = np.log10(df_sxl["FPKM"])

smoothed1 = df_sxl["FPKM"].rolling(200).mean()


plt.figure()
plt.boxplot([x1, x2], labels=["SRR072893", "SRR072915"])
plt.xlabel("developmental stages")
plt.ylabel("log(FPKM)")
#plt.semilogy(df_sxl, df2_sxl)
plt.title(" Sxl isoform in different development stage ")
plt.savefig("smoothed.png")
plt.close()




df2_roi = df_ctab["FPKM"] > 0
df2_ctab2 = df2_ctab[df2_roi]
df2_roi2 = df2_ctab2["gene_name"] == "Sxl"
df2_sxl = df2_ctab2[df2_roi2]

x2 = np.log10(df2_sxl["FPKM"])

smoothed2 = df2_sxl["FPKM"].rolling(200).mean()




plt.figure()
plt.boxplot([x1, x2], labels=["SRR072893", "SRR072915"])
plt.xlabel("developmental stages")
plt.ylabel("log(FPKM)")
#plt.semilogy(df_sxl, df2_sxl)
plt.title(" Sxl isoform in different development stage ")
plt.savefig("smoothed.png")
plt.close()




#semilogy(*args, **kwargs)





#plt.figure()
#plt.


"""


