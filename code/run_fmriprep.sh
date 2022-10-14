#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
maindir="$(dirname "$scriptdir")"
bidsdir=$maindir/bids

for sub in 'sub-10296' 'sub-10321' 'sub-10318' 'sub-10319' 'sub-10198' 'sub-10234' 'sub-10303'; do #$bidsdir/sub*; do

	sub="${sub##*/}"

	script=${scriptdir}/fmriprep.sh
	NCORES=3
	while [ $(ps -ef | grep -v grep | grep $script | wc -l) -ge $NCORES ]; do
		sleep 1s
	done
	echo $script $sub
	bash $script $sub &
	sleep 5s
done
#python ${scriptdir}/MakeConfounds.py --fmriprepDir "${scriptdir}/../derivatives/fmriprep
