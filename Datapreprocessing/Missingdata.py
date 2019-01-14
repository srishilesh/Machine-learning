# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #Independent Values
y = dataset.iloc[:, 3].values #Dependent values

# Taking care of missing data
from sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) #Mean strategy by replacing NaN along the columns(axis=0) 
imputer = imputer.fit(X[:, 1:3]) # Fit the replace data
X[:, 1:3] = imputer.transform(X[:, 1:3]) # replace the original data

print(X[:,:])
