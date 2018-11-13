function [mu Sigma] = mt_regression(features_train,labels_train,gamma)
% Compute the priors from multiple subjects

% 
% Reference:
% Morteza Alamgir, Moritz Grosse-Wentrup and Yasemin Altun
% Multitask Learning for Brain-Computer Interfaces, AISTATS 2010

%% initialize priors
dim = size(features_train,3);
mu = zeros(1,dim);
Sigma = eye(dim)/dim;

%% learn    
for p=1:20000 % steps on joint learning between mu,Sigma,W and alpha        
    %%learn W
    W = mt_gauss(Sigma,mu',features_train,labels_train,gamma,0);      
    %%update mean(mu) and covariance(Sigma)
    mu = mean(W(:,:));
    V = W(:,:)'*W(:,:);
    Sigma = V/trace(V)+gamma*eye(dim)/dim;
end