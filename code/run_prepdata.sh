#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
maindir="$(dirname "$scriptdir")"

sourcedir=/data/sourcedata/rf1-sequence-pilot
DLscript=${scriptdir}/prepdata/downloadXNAT.py

python $DLscript

for sub in $sourcedir;do
	sub=${sub%_1};
  	sub=${sub##*-}; 

	script=${scriptdir}/prepdata/prepdata.sh
	NCORES=8
	while [ $(ps -ef | grep -v grep | grep $script | wc -l) -ge $NCORES ]; do
		sleep 1s
	done
	bash $script $sub &
	sleep 5s

done
