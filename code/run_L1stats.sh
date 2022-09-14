#!/bin/bash

# ensure paths are correct irrespective from where user runs the script
scriptdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
basedir="$(dirname "$scriptdir")"

task=sharedreward # edit if necessary

python ${scriptdir}/MakeConfounds.py --fmriprepDir "${scriptdir}/../derivatives/fmriprep"
for ppi in 0 VS; do # putting 0 first will indicate "activation"
	for sub in 10203 10234 10166 10223 10198 12042 10303; do # 20-channel headcoil participants
	#10017 10024 10035 10043 10054 10059 10074 10078 10080 10108 10125 10136 10137 10142 10150 10154 10186 10188 10221; do
		for mb in 1 3 6; do
			for me in 1 4; do
                            if [ $me == 4 ];then
				for denoise in tedana none;do
				    # Manages the number of jobs and cores
				    SCRIPTNAME=${basedir}/code/L1stats.sh
				    NCORES=15
				    while [ $(ps -ef | grep -v grep | grep $SCRIPTNAME | wc -l) -ge $NCORES ]; do
					    sleep 5s
				    done
				    bash $SCRIPTNAME $sub $mb $me $ppi $denoise &
				    #echo $SCRIPTNAME $sub $mb $me $ppi $denoise &
				    sleep 1s
                                done

                            else 
				denoise=none
                              
			
				# Manages the number of jobs and cores
				SCRIPTNAME=${basedir}/code/L1stats.sh
				NCORES=15
				while [ $(ps -ef | grep -v grep | grep $SCRIPTNAME | wc -l) -ge $NCORES ]; do
					sleep 5s
				done
				bash $SCRIPTNAME $sub $mb $me $ppi $denoise &
				#echo $SCRIPTNAME $sub $mb $me $ppi $denoise &
				sleep 1s
                            fi
			done
		done
	done
done
