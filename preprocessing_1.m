a=[168,224,84,56,28];
b=[1,2,3,4,5];
c=280-a;

d=dir('Dataset-IV/');

for k=3:length(d)
 currdir=d(k).name;
 cd(strcat('Dataset-IV/',currdir));
 files=dir('*.mat');
 l=-1;
 m=-1;
 for j=1:(a(k-2))
  for i=1:(length(files)/2)
   l=l+2;
   data_train=load(strcat('Train_Subject',num2str(b(k-2)),'band',num2str(i),'.mat'));
   
   %%labels_train=transpose(labels_train);
  
   val_1=log(sum(data_train.EEGsignals.x(:,52,j).^2)/200);
   val_2=log(sum(data_train.EEGsignals.x(:,56,j).^2)/200);
   feature_train((k-2),j,1,i)=val_1;
   feature_train((k-2),j,2,i)=val_2;
   if (j==a(k-2))
    %dlmwrite(strcat(currdir,'-train-x.txt'),feature_train,'delimiter',' ');
    %dlmwrite(strcat(currdir,'-train-y.txt'),labels_train);
   end
  end
  labels_train((k-2),j)=data_train.EEGsignals.y(j);
 end
 for j=1:(c(k-2))
  for i=1:(length(files)/2)
   m=m+2;
   data_test=load(strcat('Test_Subject',num2str(b(k-2)),'band',num2str(i),'.mat'));
   
   %%labels_test=transpose(labels_test);
  
   val_3=log(sum(data_test.test.Data(:,52,a(k-2)+j).^2)/200);
   val_4=log(sum(data_test.test.Data(:,56,a(k-2)+j).^2)/200);
   feature_test((k-2),j,1,i)=val_3;
   feature_test((k-2),j,2,i)=val_4;
   if (j==c(k-2))
   %% disp(feature_test)
    %dlmwrite(strcat(currdir,'-test-x.txt'),feature_test,'delimiter',' ');
    %dlmwrite(strcat(currdir,'-test-y.txt'),labels_test);
   end
  end
  labels_test((k-2),j)=data_test.test.labels(a(k-2)+j);
 end
 cd('../..');
end

save data_file.mat feature_train feature_test labels_train labels_test

  
