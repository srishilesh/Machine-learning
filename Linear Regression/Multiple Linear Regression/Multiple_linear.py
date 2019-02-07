import numpy as np
import pandas as pd
from sklearn import linear_model

df =pd.read_csv('E:\\Programming\\Python\\Machine Learning\\Linear regression\\Datasets\\housepricing.csv') # Read file

reg = linear_model.LinearRegression()       # Linear regression model
reg.fit(df[['area','bedrooms','age']],df.price)     # Defining the features of the model

print(reg.coef_)        # Regression coefficients of the model

print(reg.intercept_)       # Intercept of the equation

print(reg.predict([[3000,3,40]]))   # Predicted value of the user entered value


