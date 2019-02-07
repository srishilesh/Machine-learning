import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv('E:\\Programming\\Python\\Machine Learning\\Linear regression\\Datasets\\graduate-admissions\\Admission_Predict.csv')  # Readin file

reg=linear_model.LinearRegression()
reg.fit(df[['GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA','Research']],df.Chance)        #Fitting model

print("Regression coefficients ",reg.coef_)     # Regression coefficients

print("Intercept ",reg.intercept_)      # Intercepts

# Accepting information from user
gre=input("Enter GRE score: ")
toefl=input("Enter TOEFL score: ")
uni=input("Enter University rating: ")
sop=input("Enter SOP score: ")
lor=input("Enter LOR score: ")
cgpa=input("Enter CGPA: ")
research=input("Enter Research work: ")

X=np.array([gre,toefl,uni,sop,lor,cgpa,research])   # Converting info into numpy array
X = np.reshape(X,(-1,7))            # Reshaping 1D array to 2D array for passing to predict()
X=X.astype(float)                   # Changing the values as float for easy calculation 
print("Chances of Entering University is ",float(reg.predict(X)))       # Predicted value
