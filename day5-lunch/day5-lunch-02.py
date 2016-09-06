#!/usr/bin/env python
"""ordinary linear regression"""

import sys
import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_table(sys.argv[1]) #t-data.ctab fpkm values
df2 = pd.read_table(sys.argv[2],header=None) #.tab files

fpkm = []
mean = []

for row in df.itertuples():
    fpkm_roi = [row[-1]]
    chrom = row[2]
    if chrom in ["2L", "2R", "3L", "3R", "4", "X"]:
        fpkm.append(fpkm_roi)
  

for row2 in df2.itertuples():
    mean_roi = [row[5]]
    mean.append(mean_roi)

#debugging difference in list length-error due to header     
#print len(fpkm_list)
#print len(mean_list)


model = sm.OLS(mean, fpkm)
res = model.fit()
print res.summary()