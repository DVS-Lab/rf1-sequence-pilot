#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
maindir="$(dirname "$scriptdir")"

sourcedir=/data/sourcedata/rf1-sequence-pilot/*
DLscript=${scriptdir}/downloadXNAT.py

python $DLscript

for sub_CB in "10024 2" "10017 2" "10035 4" "10043 4" "10041 4" "10059 6" "10054 1" "10069 1" "10080 3" "10074 3" "10085 5" "10094 5" " 10078 2" "10108 2";do
        set -- $subrun
	sub=$1
	CB=$2
 

	script=${scriptdir}/prepdata.sh
	NCORES=8
	while [ $(ps -ef | grep -v grep | grep $script | wc -l) -ge $NCORES ]; do
		sleep 1s
	done
        echo $script $sub $CB
	bash $script $sub $CB&
	sleep 5s

done

<<<<<<< HEAD
python IDoutliers.py --mriscDir "${sourcedir}/derivatives/mriqc"

=======
bash ${scriptdir}/run_motioneval.sh
python ${scriptdir}/IDoutliers.py
>>>>>>> 7896d40ec3b7259e055df85efc06f6c86a60b5d9
