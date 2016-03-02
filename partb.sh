#!/bin/bash

for i in {1..20}
do	
	echo "new line"
	echo $i
	python CNFGen.py ex4.bench ex4.state $i 
	
	

	picosat  out |  sed -n 1p
done
