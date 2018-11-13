#!/usr/bin/python
import numpy as np

data_x=np.zeros((5,34,252),dtype=float)
data_y=np.zeros((5,252,1),dtype=int)
a=[112, 56, 196, 224, 252]
w=np.zeros((34,1),dtype=float)

for i in range(5):
 data_x[i][:,0:a[i]]=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-test-x.txt',usecols=range(a[i]))
 data=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-test-y.txt',usecols=range(1))
 data1=data[:,np.newaxis]
 print(data[:,np.newaxis].shape)
 data_y[i][0:a[i]]=data1
 w=np.loadtxt('Subject_'+str(i+1)+'-weight.txt',usecols=range(1))
 X_t=data_x[i][:,0:a[i]]
 X=np.transpose(X_t)
 Y=data_y[i][0:a[i],0]
 y_pred=np.matmul(X,w)
 y_pred=y_pred[:,np.newaxis]

 for j in range(a[i]):
  if(y_pred[j]<1.5):
   y_pred[j]=1
  else:
   y_pred[j]=2
 


 false=np.sum(abs(y_pred-Y[i]))
 
 accuracy=(1-(false/a[i]))*100
 print("Subject-"+str(i+1)+": Test Accuracy = %f\n" %(accuracy))
 
 
 
