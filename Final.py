import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

headers = ['']

data = np.asmatrix(pd.read_csv('arrythmia.data', header=None))
miss_val = np.where(data=='?')
m_rows = miss_val[0]
m_cols = miss_val[1]
qmarks = np.bincount(miss_val[1])  # Number of times qmarks appear by index

'''
Missing Vector angles in degrees on front plane of
T Wave: 8, P Wave: 22 , QRST: 1, J: 376
Missing Heart Rate: 1
This suggests that we should not use J Wave in our analysis.
However, we want to use heart rate because it's clinically relevant, so lets just remove the entry that is missing it
'''

T = 10
P = 11
QRST = 12
J = 13
HR = 14

data[:, [T, P, QRST, J]] = float('NaN')  # Set these to NaN so we don't get errors later
data = np.delete(data, m_rows[m_cols==HR], axis=0)  # Del rows where we're missing HR, because we want to use HR later
labels = data[:, -1]
# labels = np.in1d(labels, [1, 2, 10])  # Only get patients that are normal, have CAD, or right atrial branch block
norm = data[labels==1, :]
cad = data[labels==2, :]
rabb = data[labels==10, :]

features = np.asarray([1, 3, 4, 5, 6, 15]) - 1


