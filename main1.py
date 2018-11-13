#!/usr/bin/python

import numpy as np
import scipy.io as sp
import h5py
from oct2py import octave as oct

def test_err_linreg(x,y):
 s = np.size(W,0)
 a = [168,224,84,56,28]
 c = [112,56,196,224,252]
 

 for i in range(s):
  pr = np.zeros((1,c[i]))
  pr = np.matmul(W[i][:],np.transpose(np.squeeze(x[i][0:c[i]][:])))
  
  for k in range(c[i]):
   if(pr[k]>1.5):
    pr[k]=2
   elif(pr[k]<=1.5):
    pr[k]=1
   
  temp = np.zeros((1,c[i]))
  for j in range(c[i]):
   temp[j] = y[i][j] 
   
  er[i]=0
  for l in range(c[i]):
   er[i] = er[i] + abs(pr[l]-temp[l])
  er[i] = ((np.size(pr,1)-er[i])*100)/np.size(pr,1)
     

def mt_gauss(tx,ty,gamma,flag):
 task = np.size(tx,0)
 x = np.zeros((train_trials,2*features))
 y = np.zeros((1,np.size(ty,1))) 
 A = np.zeros((2*features,train_trials))
 Coff = np.zeros((2*features,2*features))

 if(flag == 0):
  for t in range(task):
   x[:][:] = tx[t][:][:]
   y = ty[t][:]
   A = np.matmul(sigma,np.transpose(x))
   Coff = np.matmul(A,x) + gamma * np.identity(np.size(sigma,0))
   W[t][:] = np.matmul(np.linalg.inv(Coff),(np.matmul(A,np.transpose(y)) + gamma*np.transpose(mu)))

 elif(flag == 1):
 
  a = [168,224,84,56,28]  

  for t in range(task):
   x[0:a[t]][:] = tx[t][0:a[t]][:]
   y[0:a[t]] = ty[t][0:a[t]]
   A = np.matmul(sigma,np.transpose(x))
   Coff = np.matmul(A,x) + gamma * np.identity(np.size(sigma,0))
   W[t][:] = np.matmul(np.linalg.inv(Coff),(np.matmul(A,np.transpose(y)) + gamma*np.transpose(mu)))
   
   

def mt_regression(ft, lt, gamma):
 dim = np.size(ft,2)
 #sigma = sigma/dim
 
 V = np.zeros((2*features,2*features))
 
 for p in range(200):
  mt_gauss(ft, lt, gamma, 0)
  mu = np.mean(W,axis=1)
  V = np.matmul(np.transpose(W),W)
  sigma = V/np.trace(V) + (gamma/dim)*np.identity(2*features)
  
 


#oct.eval("preprocessing_1")
#oct.eval("save -v7 matrix_file.mat")


mat = sp.loadmat('matrix_file.mat',squeeze_me=True)
feature_train = mat['feature_train']
feature_test = mat['feature_test']
labels_train = mat['labels_train']
labels_test = mat['labels_test']
print labels_train

gamma = 0.5

channels = [1,2]
chlen = len(channels)
subjects = 5
max_trials = 280
train_trials = 224
test_trials = 252
features = 17

mu = np.zeros((1,2*features))
sigma = np.identity(2*features)
W = np.zeros((subjects,2*features))
er = np.zeros((1,subjects))


train_data = np.zeros((subjects,train_trials,2*features))
test_data = np.zeros((subjects,test_trials,2*features))

dim = np.size(train_data,2)
sigma = sigma/dim

for i in range(17):
 for j in range(train_trials):
  for k in range(subjects):
   train_data[k][j][i] = feature_train[k][j][0][i]
   train_data[k][j][17+i] = feature_train[k][j][1][i]

for i in range(17):
 for j in range(test_trials):
  for k in range(subjects):
   test_data[k][j][i] = feature_test[k][j][0][i]
   test_data[k][j][17+i] = feature_test[k][j][1][i]
 

mt_regression(train_data[:][:][:],labels_train[:][:],gamma)

mt_gauss(train_data[:][:][:],labels_train[:][:],gamma,1)
test_err_linreg(test_data[:][:][:],labels_test[:][:])

for i in range(subjects):
 print("Accuracy for Subject-%d : %f" %(i+1,er[i]))



