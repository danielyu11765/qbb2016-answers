#!/bin/bash


./day5-lunch-01_2.py ~/data/results/stringtie/SRR072893/t_data.ctab

for i in *.bw
do
	bigWigAverageOverBed -bedOut=${i%bw}bed $i day5-lunch-01_2.bed ${i%bw}tab
done

./day5-lunch-02.py *3.bed