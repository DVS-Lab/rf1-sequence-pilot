#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
maindir="$(dirname "$scriptdir")"

sourcedir=/data/sourcedata/rf1-sequence-pilot/*
DLscript=${scriptdir}/downloadXNAT.py

python $DLscript

for sub_CB in "10024 2" "10017 2" "10035 4" "10043 4" "10041 4" "10059 6" "10054 1" "10069 1" "10080 3" "10074 3" "10085 5" "10094 5" " 10078 2" "10108 2" "10130 4" "10150 6" "10154 4" "10186 5";do
        set -- $sub_CB
	sub=$1
	CB=$2
 

	script=${scriptdir}/prepdata.sh
	NCORES=8
	while [ $(ps -ef | grep -v grep | grep $script | wc -l) -ge $NCORES ]; do
		sleep 1s
	done
        echo "Running prepdata" $script $sub $CB
	bash $script $sub $CB &
	sleep 5s

done

bash ${scriptdir}/run_motioneval.sh
python ${scriptdir}/IDoutliers.py --mriscDir "${sourcedir}/derivatives/mriqc"
bash ${scriptdir}/run_gen3colfiles.sh

