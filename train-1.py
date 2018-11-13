#!/usr/bin/python
import numpy as np

data_x=np.zeros((5,34,224),dtype=float)
data_y=np.zeros((5,224,1),dtype=int)
a=[168, 224, 84, 56, 28]
l=0.1
w=np.zeros((34,1),dtype=float)
imat=np.identity(34,dtype=float)

for i in range(5):
 data_x[i][:,0:a[i]]=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-train-x.txt',usecols=range(a[i]))
 data=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-train-y.txt',usecols=range(1))
 data_1=data[:,np.newaxis]
 data_y[i][0:a[i]]=data_1
 X_t=data_x[i][:,0:a[i]]
 X=np.transpose(X_t)
 b=np.matmul(X_t,X)
 Y=data_y[i][0:a[i],0]
 Y=Y[:,np.newaxis]
 e=np.matmul(X_t,Y)
 f=l*imat
 d=np.linalg.inv(b+f)
 w=np.matmul(d,e)
 np.savetxt('Subject_'+str(i+1)+'-weight.txt',w,fmt='%f',delimiter=' ')
 
 
 


 
 


 
