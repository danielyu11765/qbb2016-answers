#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_table(sys.argv[1], index_col = None)




#df_ext = df[["t_name", "chr", "start", "end"]]
#print df_ext



df_roi_plus = df["strand"] == "+"
df_prom_plus = df[df_roi_plus]
x = df_prom_plus[["chr", "start", "end", "t_name"]]
#print x
x["start"] = x["start"]-500
x["end"] = x["start"]+1000


#print df_prom_plus


df_roi_min = df["strand"] == "-"
df_prom_min = df[df_roi_min]
y = df_prom_min[["chr", "start", "end", "t_name"]]

y["start"] = y["start"]-500
y["end"] = y["start"]+1000






#print y

frames = [x, y]
df_promoter = pd.concat(frames).sort_index()

df_roi = df_promoter["chr"].str.len() < 4
df_promoter = df_promoter[df_roi]


df_promoter.to_csv(sys.stdout, sep = "\t", index = False, header = False)

print df_promoter



#df_roi_min = df["strand"] == "-"
#df_prom_min = df[df_roi_min]
#print df_prom_min




