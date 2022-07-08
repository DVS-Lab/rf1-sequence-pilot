#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
basedir="$(dirname "$scriptdir")"

task=sharedreward # edit if necessary

for ppi in 0 VS; do # putting 0 first will indicate "activation"
	for sub in 10024; do # 10017 10024 10035 10041 10043 10054 10059 10069 10074 10078 10080 10085 10094 10108 10125 10130 10136 10137 10142 10150 10154 10186 10188 10221
		for mb in 1 3 6; do
			for me in 1 4; do
				# Manages the number of jobs and cores
				SCRIPTNAME=${basedir}/code/L1stats.sh
				NCORES=15
				while [ $(ps -ef | grep -v grep | grep $SCRIPTNAME | wc -l) -ge $NCORES ]; do
					sleep 5s
				done
				bash $SCRIPTNAME $sub $mb $me $ppi &
				sleep 1s
			done
		done
	done
done
