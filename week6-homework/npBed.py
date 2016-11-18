#!/usr/bin/env python

import sys

np_file = open(sys.argv[1])
np_line = np_file.readline(0)

for np_line in np_file:
  np_line = np_line.rstrip("\r\n")
  np_column = np_line.split("\t")
  np_list = "\t".join(np_column[0:6])
  print np_list
