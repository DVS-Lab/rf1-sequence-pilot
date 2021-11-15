function genSharedRewardBlocks(s)
%{

trials per run?
length of a trial: 3.5 (details below)

from Barch 2013:

two partners: computer, stranger, neutral
two conditions: reward/punishment

guess_dur = 1.5; %could be too fast for older adults
ITI_dur = 1;
feedback_dur = 1;


%}



maindir = pwd;
%Shared_Reward/params/SR_blocks/
outfiles = fullfile(maindir,'SharedReward','params');
mkdir(outfiles);

subout = fullfile(outfiles,sprintf('sub-%04d',s));
mkdir(subout);

runs = 6;
ntrials = 52; % 2 partners, 2 outcomes --> 52/4 would be 13 repetitions of each condition in each run. enough?

trial_types = repmat([1 2 3 4],13); % 1 computer punish, 2 computer reward, 3 stranger punish, 4 stranger reward
ISI_distribution = repmat([1 2 3 4],13);
ITI_distribution = repmat([1 2 3 4],13);

for r = 1:runs
    
    
    rand_trials = randperm(ntrials);
    fname = fullfile(subout,sprintf('sub-%04d_run-%d_design.csv',s,r));
    fid = fopen(fname,'w');
    fprintf(fid,'Trialn,TrialType,Partner,Feedback,ITI,ISI\n');
    for t = 1:ntrials
        tt = rand_trials(t);
        switch trial_types(tt)
            case 1 %Computer Punishment
                partner = 1;
                feedback_mat = 1;
            case 2 %Computer Reward
                partner = 1;
                feedback_mat = 2;
            case 3 %Stranger Punishment
                partner = 2;
                feedback_mat = 1;
            case 4 %Stranger Reward
                partner = 2;
                feedback_mat = 2;
        end
        fprintf(fid,'%d,%d,%d,%d,%d,%d\n',t,trial_types(tt),partner,feedback_mat,ITI_distribution(tt),ISI_distribution(tt));
    end
    fclose(fid);
end