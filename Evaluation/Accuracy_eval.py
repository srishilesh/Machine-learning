import numpy as np
import pandas as pd
import math

file=pd.read_csv('')  # File directory
#file=[[1,2],[3,4],[5,6],[7,8]]

tp=np.array(file['tp'].values,dtype=np.float64)    # True Positives
tn=np.array(file['tn'].values,dtype=np.float64)    # True Negatives
fp=np.array(file['fp'].values,dtype=np.float64)    # False Positives
fn=np.array(file['fn'].values,dtype=np.float64)    # False Negatives

def recall(tp,fn):  # Calculate Recall 
    i=0
    for i in range(tp.size):
        re=tp[i]/(tp[i]+fn[i])
    return re

def precision(tp,fp):  # Calculate Precision 
    i=0
    for i in range(tp.size):
        re=tp[i]/(tp[i]+fp[i])
    return re

def f1score(tp,fn,fp):  # Calculating F1 score
    f1=2*((precision(tp,fp)*recall(tp,fn))/(precision(tp,fp)+recall(tp,fn)))
    return f1

def mcc(tp,tn,fp,fn):   # Calculate Matthew Correlation Coefficient
    i=0
    for i in range(tp.size):
        val=(((tp[i]*tn[i])-(fp[i]*fn[i]))/(math.sqrt((tp[i]+fp[i])*(tp[i]+fn[i])*(tn[i]+fp[i])*(tn[i]+fn[i]))))
    return val



print("Recall score: ",recall(tp,fn))
print()
print("Precision score: ",precision(tp,fp))
print()
print("F1 score: ",f1score(tp,fn,fp))
print()
print("Matthew Correlation Coefficient: ",mcc(tp,tn,fp,fn))
print()

