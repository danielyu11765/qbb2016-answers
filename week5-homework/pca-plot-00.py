#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

eigenvec = open(sys.argv[1])
line = eigenvec.readline(0)

for line in eigenvec:
  line = line.rstrip("\r\n").split(" ")
  print line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3]