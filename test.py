#!/usr/bin/python
import numpy as np

data_x=np.zeros((5,34,280),dtype=float)
data_y=np.zeros((5,280,1),dtype=int)
sigmasq=0.5
mu=np.loadtxt('mu.txt',usecols=range(1))
sigma=np.loadtxt('sigma.txt',usecols=range(34))
W=np.zeros((34,5),dtype=float)
accuracy=np.zeros((1,5),dtype=float)

for i in range(5):
 data_x[i]=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-test-x.txt',usecols=range(280)
 data_y[i]=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-test-y.txt',usecols=range(280)

for i in range(5):
 X_t=data_x[i][:,0:280]
 X=np.transpose(X_t)
 b=np.matmul(X_t,X)
 Y=data_y[i][:,1]
 e=np.matmul(X_t,Y)

for i in range(5):
 c=np.matmul(sigma,b)/sigmasq
 d=np.linalg.inv(c+i)
 f=np.matmul(sigma,e)/sigmasq
 g=f+mu
 W[:,i]=np.matmul(d,g)

for i in range(5):
 X_t=data_x[i][:,0:a[i]]
 X=np.transpose(X_t)
 data_y_calc[i]=np.matmul(X,W[:,i])
 diff=data_y[i]-data_y_calc[i]
 absdiff=abs(diff)
 false=np.sum(absdiff)
 accuracy[i]=(1-(false/280))*100
 print("Subject-"+(i+1)+": Test Accuracy = %f\n" %(accuracy[i]))
  
  
