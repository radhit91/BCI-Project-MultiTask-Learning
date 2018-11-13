% A Simple test file for applying multitask classification on BCI data
% for motor imagery

% 
% Reference:
% Morteza Alamgir, Moritz Grosse-Wentrup and Yasemin Altun
% Multitask Learning for Brain-Computer Interfaces, AISTATS 2010
%clear all;
%clc;
load data_file.mat % Replace by the name of your data file 

%%%feature_train : subject*trial*channels*features
%%%feature_test  : subject*trial*channels*features
%%%labels_train   : subject*trial
%%%labels_test    : subject*trial

gamma = 0.5; % regularization coefficient
%%%
% here we will concatenate all channels. To improve the speed, (in the BCI case) we only use
% the approx. related channels (For motor imagery: the ones around C3/C4)
%%%
channels = [1 2]; 
train_data(:,:,1:length(channels),:) = feature_train(:,:,channels,:);
test_data(:,:,1:length(channels),:) = feature_test(:,:,channels,:);

for i=1:17
  train_data_1(:,:,i) = train_data(:,:,1,i);
  train_data_1(:,:,17+i) = train_data(:,:,2,i);
end

for i=1:17
  test_data_1(:,:,i) = test_data(:,:,1,i);
  test_data_1(:,:,17+i) = test_data(:,:,2,i);
end

%train_data(:,:,:)=[train_data(:,:,1,:) train_data(:,:,2,:)];
%test_data(:,:,:)=[test_data(:,:,1,:) test_data(:,:,2,:)];

%% learn priors
[mu Sigma] = mt_regression(train_data_1([1 2 3 4 5],:,:),labels_train([1 2 3 4 5],:),gamma);
%disp(size(mu))
%disp(size(Sigma))
%disp(size(labels_test))
%disp(size(labels_train))
%disp(size(feature_train))
%disp(size(feature_test))

%% Sample scenario: 
%  select 100 random trials from new subject for training and keep the rest for test
idx = randperm(size(test_data_1,2));
idx_train = idx(1:150);
idx_test =  idx(151:end);
%%
W = mt_gauss(Sigma,mu',train_data_1(:,:,:),labels_train(:,:),gamma,1);
accuracy = test_err_linreg(W,test_data_1(:,:,:),labels_test(:,:)) 
