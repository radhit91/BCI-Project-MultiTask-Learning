#!/usr/bin/python
import numpy as np

data_x=np.zeros((5,34,224),dtype=float)
data_y=np.zeros((5,224,1),dtype=int)
a=[168, 224, 84, 56, 28] 
sigmasq=0.5
flag=0
count=0
mu_sum_old=0
mu_sum=0
sig_sum_old=0
sig_sum=0
sigma_1=np.identity(34,dtype=float)
sigma=sigma_1
mu=np.zeros((34,1),dtype=float)
#W=np.random.uniform(0,1,(34,5))
W=np.zeros((34,5),dtype=float)
#print(W)
i=np.identity(34,dtype=float)
epsilon=0.15
eta=0.01

for i in range(5):
 data_x[i][:,0:a[i]]=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-train-x.txt',usecols=range(a[i]))
 data=np.loadtxt('Dataset-IV/Subject_'+str(i+1)+'/Subject_'+str(i+1)+'-train-y.txt',usecols=range(1))
 data_1=data[:,np.newaxis] 
 data_y[i][0:a[i]]=data_1
 

for i in range(5):
 X_t=data_x[i][:,0:a[i]]
 X=np.transpose(X_t)
 b=np.matmul(X_t,X)
 Y=data_y[i][0:a[i],0]
 Y=Y[:,np.newaxis]  
 e=np.matmul(X_t,Y)
  
 
while ((abs(mu_sum_old-mu_sum)/5)>epsilon or (abs(sig_sum_old-sig_sum)/5)>epsilon or flag==0):
 flag=1
 count=count+1 
 print("inv sigma:",np.linalg.inv(sigma))

 for i in range(5):
  
  #if(flag==0):
  # mu=mu[:,np.newaxis]
  # flag_1=1

  c=np.matmul(sigma,b)/sigmasq
  #print(c)
  
  #print(mu.shape)
  d=np.linalg.inv(c+i)
  f=np.matmul(sigma,e)/sigmasq
  #print(f.shape)
  
  
  #if(count==1): 
   #mu=mu[:,np.newaxis]
  g=np.add(f,mu)
  #print(d.shape)
  #print(g.shape)
  #print(g)
  #print(W[:,[i]].shape)
  #W[:,i]=np.expand_dims(W[:,i],axis=0)
  T=np.matmul(d,g)
  #print(T.shape)
  W[:,i]=T.reshape(34)
  

 print("W:",W)
 
 #print(W) 
 #print(mu)
 mu_old=mu
 print("mu before:",mu)
 #print("ds",mu.shape)
 mu=np.sum(W,1)/5
 print("mu after:",mu)
 mu_sum_old=np.sum(mu_old)
 mu_sum=np.sum(mu)
 mu=mu[:,np.newaxis]
 
 #print("as",mu.shape)
 H=W-mu
 #print(H)
 H_t=np.transpose(H)
 sigma_old=sigma
 
 temp=np.matmul(H,H_t)
 print("temp:",temp)

 print("sigma before:",sigma)
 
 sigma=(temp/(np.trace(temp)))+(eta*sigma_1)
 print("sigma after:",sigma)
 sig_sum_old=np.sum(sigma_old)
 sig_sum=np.sum(sigma)
 #print(temp)
 #flag=1
 #mu_num=0 
 #sigma_num=0
 
 
 print("iter = %d, mu_diff = %d, sigma_diff = %d\n" %(count,abs(mu_sum_old-mu_sum),abs(sig_sum_old-sig_sum)))

np.savetxt('Weight.txt',W,fmt='%f',delimiter=' ')
np.savetxt('mu.txt',mu,fmt='%f',delimiter=' ')
np.savetxt('sigma.txt',sigma,fmt='%f',delimiter=' ')

 

