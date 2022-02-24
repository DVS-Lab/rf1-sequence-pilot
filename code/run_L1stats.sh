#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
basedir="$(dirname "$scriptdir")"

task=sharedreward # edit if necessary

for ppi in 0; do # putting 0 first will indicate "activation"

	for sub in `ls -d ${basedir}/derivatives/fmriprep/sub-*/`; do

          sub=${sub#*sub-}
          sub=${sub%/}  

	  for acq in mb1me1 mb1me4 mb3me1 mb3me4 mb6me1 mb6me4; do

	  	# Manages the number of jobs and cores
	  	SCRIPTNAME=${basedir}/code/L1stats.sh
	  	NCORES=15
	  	while [ $(ps -ef | grep -v grep | grep $SCRIPTNAME | wc -l) -ge $NCORES ]; do
	    		sleep 5s
	  	done
	  	bash $SCRIPTNAME $sub $acq $ppi &
                echo $SCRIPTNAME $sub $acq $ppi &
			sleep 1s
	  done
	done
done
