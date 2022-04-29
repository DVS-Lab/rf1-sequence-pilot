#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import re


# In[2]:


event_files=[os.path.join(root,f) for root,dirs,files in os.walk('../bids') for f in files if f.endswith('events.tsv')]
data=[]
for file in event_files:
    sub='sub-'+re.search('func/sub-(.*)_task',file).group(1)
    acq=re.search('_acq-(.*)_events',file).group(1)
    tmp_df=pd.read_csv(file,sep='\t')
    if tmp_df.shape[0]>0:
        print(sub,acq)
        tmp_df['sub']=sub
        tmp_df['acq']=acq
        data.append(tmp_df)
events_df=pd.concat(data)


# In[ ]:


print(events_df['sub'].unique())


# In[ ]:


data=[]
for sub in events_df['sub'].unique():
    print(sub)
    for acq in events_df['acq'].unique():
        
        absolute=np.loadtxt('../derivatives/fsl/mcflirt/%s/%s/_abs.rms'%(sub,acq))
        FD=np.loadtxt('../derivatives/fsl/mcflirt/%s/%s/_rel.rms'%(sub,acq))
        
        row=[sub,acq,
             np.divide(
                 events_df[(events_df['sub']==sub)&(events_df['acq']==acq)]['trial_type'].str.count('miss').sum()
                 ,2),
            absolute.max(),FD.mean()]
        data.append(row)
        
exclusions_df=pd.DataFrame(data=data,columns=['sub','acq','TrialCount_misses','Max_Abs_motion','FD_mean'])
exclusions_df['FD_exclusion']=exclusions_df['FD_mean']>0.5
exclusions_df['ABS_exclusion']=exclusions_df['Max_Abs_motion']>1.35
exclusions_df['Beh_TrialExclusion']=exclusions_df['TrialCount_misses']>27


# In[ ]:



results=exclusions_df.groupby(by='sub').sum().reset_index().rename(columns={"TrialCount_misses": "TotalCount_misses"})
results['Beh_TotalExclusion']=results['TotalCount_misses']>81
results=results[['sub','TotalCount_misses','Beh_TotalExclusion']]


# In[ ]:


exclusions_df.merge(results,on='sub')
exclusions_df.to_csv('../derivatives/exclusions.csv', index=False)

