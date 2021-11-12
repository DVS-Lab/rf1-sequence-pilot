import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    # mag = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')
    # phase = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')


    #me1
    rest_mb1me1 =       create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb1me1_bold')
    rest_mb1me1_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb1me1_sbref')
    rest_mb3me1 =       create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me1_bold')
    rest_mb3me1_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me1_sbref')
    rest_mb6me1 =       create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb6me1_bold')
    rest_mb6me1_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb6me1_sbref')

    #me3
    rest_mb1me3 =            create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb1me3_bold')
    #rest_mb1me3_sbref =      create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb1me3_sbref')
    rest_mb3me3 =            create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me3_bold')
    rest_mb3me3_sbref =      create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me3_sbref')
    rest_mb6me3 =            create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb6me3_bold')
    rest_mb6me3_sbref =      create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb6me3_sbref')
    rest_mb3me3noInt =       create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb6me3noInt_bold')
    rest_mb3me3noInt_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb6me3noInt_sbref')

    # note: didn't get sbref for CMRR_MB1_IP2_ME3_TR1850

    #other
    rest_mb3me4 =       create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me4_bold')
    rest_mb3me4_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me4_sbref')
    rest_mb3me3 =       create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me3_bold')
    rest_mb3me3_sbref = create_key('sub-{subject}/func/sub-{subject}_task-rest_acq-mb3me3_sbref')

        # mag: [],
        # phase: [],

    info = {t1w: [],

            rest_mb1me1: [],
            rest_mb1me1_sbref: [],
            rest_mb3me1: [],
            rest_mb3me1_sbref: [],
            rest_mb6me1: [],
            rest_mb6me1_sbref: [],

            rest_mb1me3: [],
            #rest_mb1me3_sbref: [],
            rest_mb3me3: [],
            rest_mb3me3_sbref: [],
            rest_mb6me3: [],
            rest_mb6me3_sbref: [],

            rest_mb3me4: [],
            rest_mb3me4_sbref: [],
            rest_mb3me3noInt: [],
            rest_mb3me3noInt_sbref: [],
            }

    list_of_ids = [s.series_id for s in seqinfo]
    for s in seqinfo:
        if ('T1w-anat_mpg_07sag_iso' in s.protocol_name) and ('NORM' in s.image_type):
            info[t1w] = [s.series_id]
        if ('gre_field' in s.protocol_name) and ('NORM' in s.image_type):
            info[mag] = [s.series_id]
        if ('gre_field' in s.protocol_name) and ('P' in s.image_type):
            info[phase] = [s.series_id]

        # no multi-echo
        if (s.dim4 >= 100) and ('MB1_IP2_ME1' in s.protocol_name):
            info[rest_mb1me1].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb1me1_sbref].append(list_of_ids[idx -1])
        elif (s.dim4 >= 100) and ('MB3_IP2_ME1' in s.protocol_name):
            info[rest_mb3me1].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb3me1_sbref].append(list_of_ids[idx -1])
        elif (s.dim4 >= 100) and ('MB6_IP2_ME1' in s.protocol_name):
            info[rest_mb6me1].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb6me1_sbref].append(list_of_ids[idx -1])

        # multi-echo standard
        if (s.dim4 >= 100) and ('MB1_IP2_ME3' in s.protocol_name):
            info[rest_mb1me3].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            #info[rest_mb1me3_sbref].append(list_of_ids[idx -1])
        elif (s.dim4 >= 100) and ('MB3_IP2_ME3' in s.protocol_name):
            info[rest_mb3me3].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb3me3_sbref].append(list_of_ids[idx -1])
        elif (s.dim4 >= 100) and ('MB6_IP2_ME3' in s.protocol_name):
            info[rest_mb6me3].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb6me3_sbref].append(list_of_ids[idx -1])

        # extras
        if (s.dim4 >= 100) and ('MB3_IP2_ME4' in s.protocol_name):
            info[rest_mb3me4].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb3me4_sbref].append(list_of_ids[idx -1])
        elif (s.dim4 >= 100) and ('MB3_IP2_ME3' in s.protocol_name) and ('noInterp' in s.protocol_name):
            info[rest_mb3me3noInt].append(s.series_id)
            idx = list_of_ids.index(s.series_id)
            info[rest_mb3me3noInt_sbref].append(list_of_ids[idx -1])


    return info
