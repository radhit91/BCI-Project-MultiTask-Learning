function [er] = test_err_linreg(W,x,testy)
% Compute the test error 
% W : classifier

% 
% Reference:
% Morteza Alamgir, Grosse-Wentrup and Yasemin Altun
% Multitask Learning for Brain-Computer Interfaces, AISTATS 2010
subjects = size(W,1);

a=[168,224,84,56,28];
c=[112,56,196,224,252];

for i=1:subjects
    pr = W(i,:)*squeeze(x(i,1:c(i),:))';
%    disp(size(pr)); 
%    disp(pr);
    for k=1:c(i)
     if(pr(k)>1.5)
      pr(k)=2;
     elseif(pr(k)<=1.5)
      pr(k)=1;
     end
    end
%    disp(size(pr))
%    disp(c(1))
%   disp(size(testy(i,a(i)+1:end)))
%   er(i)= length(testy(i,a(i)+1:end))-length(find(sign(pr)==testy(i,a(i)+1:end)));  
    for j=1:c(i)
%     disp(j)
     temp(j) = testy(i,j);
     if(j==c(i)) 
%     disp(temp)
     end
    end 
%    disp(length(temp(:)));
%    disp(length(find(sign(pr)==temp(:))));p
%    er(i) = abs(length(temp(:))-length(find(sign(pr)==temp(:)))); 
    er(i)=0;
    for l=1:c(i)
     er(i) = er(i)+abs(pr(l)-temp(l));
    end
    er(i) = ((length(pr)-er(i))*100)/length(pr);
end
