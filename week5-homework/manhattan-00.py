#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np


highlight_x = []
highlight_y = []

regular_x = []
regular_y = []

input_qassoc = sys.argv[1:]
for qassoc in input_qassoc:
  title = qassoc.split(".")[1]
  #print title
  qassoc_read = open(qassoc)
  
  for i, line in enumerate(qassoc_read):
    if i == 0:
      continue
    comp = line.rstrip("\r\n").split()
    #print comp
    p_value = float(comp[-1])
    #print p_value
    
    if p_value < 0.00001:
      highlight_x.append(i)
      p_value_log_h = -np.log10(float(p_value))
      highlight_y.append(p_value_log_h)
    else:
      regular_x.append(i)
      p_value_log_r = -np.log10(float(p_value))
      regular_y.append(p_value_log_r)
      
  plt.figure()                            
  plt.title("The Manhattan Plot of %s" % title)
  plt.plot(highlight_x, highlight_y, color = "yellow", linewidth = 3)
  plt.plot(regular_x, regular_y, color = "navy", linewidth = 3)
  plt.xlabel("%s SNPs" % title)               
  plt.ylabel("Significant Variation")               
  #plt.show()
  plt.savefig("Man_%s.png" % title)
  plt.close() 

