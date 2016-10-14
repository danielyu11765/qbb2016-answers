#!/usr/bin/env python

import sys

pheno = open(sys.argv[1])

for line in pheno:
  if line.startswith("\t"):
    print "FID" + "\t" + "IID" + line.rstrip("\r\n")
    continue
  comp = line.rstrip("\r\n").split("\t") 
  FmID = comp[0].replace("_", "\t")
  print FmID + "\t" + "\t".join(comp[1:])