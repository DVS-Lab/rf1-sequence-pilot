#!/bin/bash

# remove phase (?) image. not sure why these are there
rm -rf *_ph.nii

for i in `ls -1 *.nii`; do 

	# remove small files
	nvols=`fslnvols $i`
	if [ $nvols -lt 20 ]; then
		rm -rf $i
	fi
	
	fslmaths $i -Tmean tmp_mean
	fslmaths $i -Tstd tmp_std
	fslmaths tmp_mean -div tmp_std tmp_tsnr
	fslmaths tmp_tsnr -thr 2 thr_tmp_tsnr
	max=`fslstats thr_tmp_tsnr -R | awk '{ print $2 }'`
	mean=`fslstats thr_tmp_tsnr -M`
	echo -e "$i\t mean tsnr: $mean\t max tsnr: $max"
	
done	

