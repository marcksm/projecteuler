#!/usr/bin/bash

for d in [p][0-9]*
do
	( cd $d 
	if [ ! -d "python" ]; then
		mkdir python
	fi
	mv p.py python/p.py 2>/dev/null )
done

