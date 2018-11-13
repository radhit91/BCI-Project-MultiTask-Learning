function [W] = mt_gauss(A,mu,trainx,trainy,gamma,flag)
% Regressor with gaussian priors

% 
% Reference:
% Morteza Alamgir, Moritz Grosse-Wentrup and Yasemin Altun
% Multitask Learning for Brain-Computer Interfaces, AISTATS 2010

Task = size(trainx,1);

if(flag == 0)

 for t=1:Task
    x(:,:) = trainx(t,:,:); 
    %disp(size(x))
    y = trainy(t,:);
    %disp(size(y))
    Ax = A* x';
    %disp(size(Ax))
    Coff = (Ax*x+gamma*eye(size(A,1)));
    %disp(size(Coff))
    W(t,:) =  Coff\ (Ax * y' + gamma*mu);
    %disp(size(W))
 end
 
elseif(flag == 1)
 
 a=[168,224,84,56,28];
  
  
 for t=1:Task
    x(1:a(t),:) = trainx(t,1:a(t),:); 
%    disp(size(x))
    y(1:a(t)) = trainy(t,1:a(t));
%    disp(size(y))
    Ax = A* x';
%    disp(size(Ax))
    Coff = (Ax*x+gamma*eye(size(A,1)));
%    disp(size(Coff))
    W(t,:) =  Coff\ (Ax * y' + gamma*mu);
%    disp(size(W))
 end
end
