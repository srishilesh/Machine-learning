import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('E:/General/Courses/Machine learning- Coursera/Assignment/Ex 1/machine-learning-ex1/ex1/ex1data1.txt',names=['Pop','Profit'])

#print(df.head())

'''
# Data visualization of the training dataset
plt.scatter(df.Pop,df.Profit,alpha=0.3)
plt.show()
'''
#df.insert(0,'Ones',1)       # To insert a new column of ones for matrix multiplication

#cols = df.shape[1]
X = df.iloc[:,:cols-1]          # To split the training set
y = df.iloc[:,cols-1:cols]      # To split the target variable
m = y.size                      # Number of training examples

def plotData(X,y):
    plt.plot(X,y,'ro',ms = 10,mec = 'k')
    plt.ylabel("Profit in $10,000")
    plt.xlabel("Pop. of city in 10,000s")
