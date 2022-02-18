#!/usr/bin/env python
# coding: utf-8

# In[16]:


from scipy.io import loadmat
import pandas as pd
import os
import re

subs=[num for num in os.listdir('../stimuli/logs/')]
partner_codes = {1:'Computer',2:'Stranger',3:'Friend'}
Button_codes = {2:'Right', 7:'Left'}
feedback_codes = {1:'Punish',2:'Neutral',3:'Reward'}

for sub in subs:
    print("running sub-%s"%(sub))
    eventfiles = ['../stimuli/logs/%s/%s'%(sub,file) for file in os.listdir('../stimuli/logs/%s'%(sub)) if file.endswith('raw.csv')]
    if int(sub)>3000:
        for file in eventfiles:
            try:
                x=pd.read_csv(file)
                scan_start=float(x['InitFixOnset'][0])
                x['Partner'] = x['Partner'].map(partner_codes).astype('str')
                x['Feedback'] = x['Feedback'].map(feedback_codes).astype('str')
                x['resp'] = x['resp'].map(Button_codes).astype('str')
                x['feed_type'] = x[['Partner', 'Feedback']].agg('_'.join, axis=1)
                x['resp'] = x[['Partner', 'resp']].agg('_'.join, axis=1)

                data=[]
                for index, row in x.iterrows(): #seperating out 2 kinds of events per file
                    feedback_info=[float(row['outcome_onset'])-scan_start,
                                 float(row['outcome_offset'])-float(row['outcome_onset']),
                                 row['feed_type'],
                                 row['rt']]

                    button_info=[row['decision_onset'],
                                   row['rt'],
                                   row['resp'],
                                   'n/a']
                    data.append(button_info)
                    data.append(feedback_info)
                df=pd.DataFrame(columns=[['onset','duration','trial_type','response_time']],data=data)
                outdir = '../bids/sub-%s/func'%(sub)
                if not os.path.exists(outdir):
                    os.makedirs(outdir)
                fullname = os.path.join(outdir,
                                        re.search('/%s/(.*)_raw'%(sub),file).group(1))+'_events.tsv'

                df.to_csv(fullname,sep='\t',index=False)
            except:
                print("Something went wrong for sub-%s file: %s"%(sub,file))

