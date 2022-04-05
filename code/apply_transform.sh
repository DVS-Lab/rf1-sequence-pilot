
sub=$1
task=sharedreward
acq=$2

tedana_dir=/data/projects/rf1-sequence-pilot/derivatives/tedana
fmriprep_dir=/data/projects/rf1-sequence-pilot/derivatives/fmriprep

vol_to_warp=${tedana_dir}/sub-${sub}/

MNI_reference=${fmriprep_dir}/mni152.nii.gz

xform_scanner_to_T1w=${fmriprep_dir}/sub-${sub}/func/sub-${sub}_task-${task}_acq-${acq}clea_from-scanner_to-T1w_mode-image_xfm.txt


xform_T1w_to_MNI=${fmriprep_dir}/sub-${sub}/anat/sub-${sub}_from-T1w_to-MNI152NLin2009cAsym_mode-image_xfm.h5

singularity exec --contain --cleanenv \
	-B ${fmriprep_dir} \
	-B ${tedana_dir} \
	/data/tools/fmriprep-21.0.1.simg
	-e 3 \
	-i ${vol_to_warp}
	-r ${MNIReferenceimage}
	-o ${fmriprep_dir}/sub-${sub}/warped_tedana_image \
	-n LanczosWindowedSinc
	-t ${xformscanner_to_T1w}
	-t ${xform_T1w_to_MNI}
