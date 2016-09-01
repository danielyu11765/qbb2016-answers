#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




df_ctab = pd.read_csv(sys.argv[1], sep="\t")
df2_ctab = pd.read_csv(sys.argv[2], sep="\t")






#read ctab

df_roi = df_ctab["FPKM"] > 0
df_ctab2 = df_ctab[df_roi]
df_roi2 = df_ctab2["gene_name"] == "Sxl"
df_sxl = df_ctab2[df_roi2]
x1 = np.log10(df_sxl["FPKM"])





df2_roi = df_ctab["FPKM"] > 0
df2_ctab2 = df2_ctab[df2_roi]
df2_roi2 = df2_ctab2["gene_name"] == "Sxl"
df2_sxl = df2_ctab2[df2_roi2]
x2 = np.log10(df2_sxl["FPKM"])





plt.figure()
plt.boxplot([x1, x2], labels=["SRR072893", "SRR072915"])
plt.xlabel("developmental stages")
plt.ylabel("log(FPKM)")
#plt.semilogy(df_sxl, df2_sxl)
plt.title(" Sxl isoform in different development stage ")
plt.savefig("day4-lunch-01.png")
plt.close()




#semilogy(*args, **kwargs)





#plt.figure()
#plt.





