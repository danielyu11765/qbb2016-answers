#!/usr/bin/env python
"""Determine the approximation of the promoter region for each of the trascripts in SRR072893"""

import sys
import numpy as np
import pandas as pd

"""
find promoter and extend its promoter region by +/- 500 bp. If +strand, use start; If -strand, use end. Collect data under chrmosome
2L, 2R, 3L, 3R, 4, X.
"""


base = sys.argv[1]
df = pd.read_table(sys.argv[1])


col = ["chr", "start", "end", "t_name"]
promoter = []

for row in df.itertuples():
    strand = row[3]
    chrom = row[2]
    if chrom in ["2L", "2R", "3L", "3R", "4", "X"]:
        if strand == "+":
          table_plus = [row[2], row[4] - 500, row[4] + 500, row[6]]  
          #print table_plus 
          promoter.append(table_plus)
        elif strand == "-":
          table_minus = [row[2], row[5] + 500, row[5] - 500, row[6]]   
          #print table_minus
          promoter.append(table_minus)
        else:
            print "x-x-x-x-x-x"
            
df_promoter = pd.DataFrame(promoter)  #build up dataframe
df_promoter.to_csv("day5-lunch-01_2.bed", sep="\t", header=False, index=False)

#for i in new_df_promoter.itertuples(): print i


# for _, chr, strand, start, end, t_name in df.itertuples():
#     d[chr + start + end + t_name] = pd.read_table(base + "/")