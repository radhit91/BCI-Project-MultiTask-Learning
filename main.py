#!/usr/bin/python

import numpy as np
import scipy.io as sp
import h5py
from oct2py import octave as oct

oct.eval("preprocessing_1")
oct.eval("save -v7 matrix_file.mat")


mat = sp.loadmat('matrix_file.mat',squeeze_me=True)
feature_train = mat['feature_train']
feature_test = mat['feature_test']
labels_train = mat['labels_train']
labels_test = mat['labels_test']
print labels_train
