#!/usr/bin/env python

"""

Usage: ./01-timecourse.py <metadata.csv> <ctab file> <ctab_dir>

~/data/fastq/samples.csv ~/data/fastq/replicates.csv ~/data/results/stringtie/

"""

#!/usr/bin/env python


import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv(sys.argv[1]) #sample.csv ------------1
df2 = pd.read_csv(sys.argv[2]) #duplicates.csv -----------2
ctab_dir = sys.argv[3]  #t_data.ctab file ------------- ~/data/results/stringtie/


sx = ["male", "female"]
color = ["blue", "red"]

plt.figure()                            # Open canvas

#for sample.csv
sxl_sex_stg1 = []
for s1 in range (0,2):
  df1_roi = df1["sex"] == sx[s1]   #collect
  df1_sx = df1[df1_roi]  #update
  stages1 = df1_sx["stage"].values   #collect ----- convert from dataframe to list. 10, 11, 12, 13, 14A
  #stages -- for x-axis labeling test test!!!
  
  for sample1 in df1_sx["sample"]: #sample -------SRR072xxx
    filename1 = ctab_dir + "/" + sample1 + "/t_data.ctab"
    df1_read = pd.read_table(filename1)
    df1_read_roi = df1_read["t_name"] == "FBtr0331261" # collect ---- get the transcript    
    sxl_sex_stg1.append(df1_read[df1_read_roi]["FPKM"].values) #get FPKM and store in list --- for y-axis

  plt.plot(sxl_sex_stg1, linestyle = "-", color = color[s1], label = sx[s1], linewidth = 5)
  sxl_sex_stg = [] #clean list


#for duplicates.csv
sxl_sex_stg2 = [0, 0, 0, 0]
for s2 in range (0,2):
  df2_roi = df2["sex"] == sx[s2]   #collect
  df2_sx = df2[df2_roi]  #update
  stages2 = df2_sx["stage"].values   #collect ----- convert from dataframe to list. 10, 11, 12, 13, 14A
  #stages -- for x-axis test test!!!
  
  for sample2 in df2_sx["sample"]: #sample -------SRR072xxx
    filename2 = ctab_dir + "/" + sample2 + "/t_data.ctab"
    df2_read = pd.read_table(filename2)
    df2_read_roi = df2_read["t_name"] == "FBtr0331261" # collect ---- get the transcript    
    sxl_sex_stg2.append(df2_read[df2_read_roi]["FPKM"].values) #get FPKM and store in list --- for y-axis
  
  plt.plot(sxl_sex_stg2, linestyle = "--", color = color[s2], linewidth = 5)
  sxl_sex_stg2 = [0, 0, 0, 0]
  #clean list

  
  #plt.figure()                            # Open canvas
#plt.plot(sxl_sex_stg1, linestyle = '-', color = color[s1], label = sx[s1], linewidth = 5)
#plt.plot(sxl_sex_stg2, linestyle = ':', color = color[s2], label = sx[s2], linewidth = 5)
plt.title("Sxl transcription")           # Will appear above the plot
plt.xlabel("Dev stages")                   # Label the x axis
plt.ylabel("mRNA abundance (FPKM)")  # Label the y axis
plt.savefig("day4-homework-01_timecourse.png")           # Save
plt.close()                             # Close canvas











