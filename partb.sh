#!/bin/bash

for i in {1..1000}
do	
	echo "new line"
	echo $i
	python CNFGen.py ex3.bench ex3.state $i 
	
	
	picosat out | sed -n 1p
	#picosat -v out | tail >> picoTail.txt
done
