#!/bin/bash

for i in {1..20}
do
	echo $i
	python CNFGen.py ex4.bench ex4.state $i | sed -n 1p 
	picosat out | sed -n 1p
done
