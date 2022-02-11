{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.io import loadmat\n",
    "import pandas as pd\n",
    "import os\n",
    "import re\n",
    "\n",
    "subs=[num for num in os.listdir('../stimuli/logs/')]\n",
    "partner_codes = {1:'Computer',2:'Stranger',3:'Friend'}\n",
    "Button_codes = {2:'Right', 7:'Left'}\n",
    "feedback_codes = {1:'Punish',2:'Neutral',3:'Reward'}\n",
    "\n",
    "for sub in subs:\n",
    "    eventfiles = ['../stimuli/logs/%s/%s'%(sub,file) for file in os.listdir('../stimuli/logs/%s'%(sub)) if file.endswith('raw.csv')]\n",
    "    if int(sub)>3000:\n",
    "        display(eventfiles)\n",
    "        df_list=[]\n",
    "        for file in eventfiles:\n",
    "            x=pd.read_csv(file)\n",
    "            x['Partner'] = x['Partner'].map(partner_codes).astype('str')\n",
    "            x['Feedback'] = x['Feedback'].map(feedback_codes).astype('str')\n",
    "            x['resp'] = x['resp'].map(Button_codes).astype('str')\n",
    "            x['feed_type'] = x[['Partner', 'Feedback']].agg('_'.join, axis=1)\n",
    "            x['resp'] = x[['Partner', 'resp']].agg('_'.join, axis=1)\n",
    "            \n",
    "            data=[]\n",
    "            for index, row in x.iterrows(): #seperating out 2 kinds of events per file\n",
    "                feedback_info=[row['outcome_onset'],\n",
    "                             row['outcome_offset']-row['outcome_onset'],\n",
    "                             row['feed_type'],\n",
    "                             row['rt']]\n",
    "\n",
    "                button_info=[row['decision_onset'],\n",
    "                               row['rt'],\n",
    "                               row['resp'],\n",
    "                               'n/a']\n",
    "                data.append(button_info)\n",
    "                data.append(feedback_info)\n",
    "            df=pd.DataFrame(columns=[['onset','duration','trial_type','response_time']],data=data)\n",
    "            \n",
    "            outdir = '../bids/sub-%s/func'%(sub)\n",
    "            if not os.path.exists(outdir):\n",
    "                os.makedirs(outdir)\n",
    "\n",
    "            fullname = os.path.join(outdir,\n",
    "                                    re.search('/%s/(.*)_raw'%(sub),file).group(1))+'_events.tsv'\n",
    "            \n",
    "            df.to_csv(fullname,sep='\\t',index=False)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['../stimuli/logs/10008/sub-10008_task-sharedreward_run-3_mb-6_me-1_raw.csv',\n",
       " '../stimuli/logs/10008/sub-10008_task-sharedreward_run-4_mb-1_me-4_raw.csv',\n",
       " '../stimuli/logs/10008/sub-10008_task-sharedreward_run-1_mb-1_me-1_raw.csv',\n",
       " '../stimuli/logs/10008/sub-10008_task-sharedreward_run-5_mb-6_me-4_raw.csv',\n",
       " '../stimuli/logs/10008/sub-10008_task-sharedreward_run-2_mb-3_me-1_raw.csv',\n",
       " '../stimuli/logs/10008/sub-10008_task-sharedreward_run-6_mb-3_me-4_raw.csv']"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "../bids/sub-10008/func/sub-10008_task-sharedreward_run-3_mb-6_me-1_events.tsv\n",
      "../bids/sub-10008/func/sub-10008_task-sharedreward_run-4_mb-1_me-4_events.tsv\n",
      "../bids/sub-10008/func/sub-10008_task-sharedreward_run-1_mb-1_me-1_events.tsv\n",
      "../bids/sub-10008/func/sub-10008_task-sharedreward_run-5_mb-6_me-4_events.tsv\n",
      "../bids/sub-10008/func/sub-10008_task-sharedreward_run-2_mb-3_me-1_events.tsv\n",
      "../bids/sub-10008/func/sub-10008_task-sharedreward_run-6_mb-3_me-4_events.tsv\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['../stimuli/logs/10007/sub-10007_task-sharedreward_run-3_acq-mb6me1_raw.csv',\n",
       " '../stimuli/logs/10007/sub-10007_task-sharedreward_run-2_acq-mb3me1_raw.csv',\n",
       " '../stimuli/logs/10007/sub-10007_task-sharedreward_run-5_acq-mb3me4_raw.csv',\n",
       " '../stimuli/logs/10007/sub-10007_task-sharedreward_run-6_acq-mb6me4_raw.csv',\n",
       " '../stimuli/logs/10007/sub-10007_task-sharedreward_run-4_acq-mb1me4_raw.csv',\n",
       " '../stimuli/logs/10007/sub-10007_task-sharedreward_run-1_acq-mb1me1_raw.csv']"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "../bids/sub-10007/func/sub-10007_task-sharedreward_run-3_acq-mb6me1_events.tsv\n",
      "../bids/sub-10007/func/sub-10007_task-sharedreward_run-2_acq-mb3me1_events.tsv\n",
      "../bids/sub-10007/func/sub-10007_task-sharedreward_run-5_acq-mb3me4_events.tsv\n",
      "../bids/sub-10007/func/sub-10007_task-sharedreward_run-6_acq-mb6me4_events.tsv\n",
      "../bids/sub-10007/func/sub-10007_task-sharedreward_run-4_acq-mb1me4_events.tsv\n",
      "../bids/sub-10007/func/sub-10007_task-sharedreward_run-1_acq-mb1me1_events.tsv\n"
     ]
    }
   ],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
