import pandas as pd
import numpy as np
from numpy.linalg import matrix_power
import matplotlib.pyplot as plt

df = np.loadtxt('E:/General/Courses/Machine learning- Coursera/Assignment/Ex 1/machine-learning-ex1/ex1/ex1data1.txt', delimiter=',')

#print(df.head())

'''
# Data visualization of the training dataset
plt.scatter(df.Pop,df.Profit,alpha=0.3)
plt.show()
'''
#df.insert(0,'Ones',1)       # To insert a new column of ones for matrix multiplication

cols = df.shape[1]
X = df[:,0]          # To split the training set
y = df[:,1]      # To split the target variable
m = y.size                      # Number of training examples

def plotData(X,y):
    plt.plot(X,y,'ro',ms = 10,mec = 'k')
    plt.ylabel("Profit in $10,000")
    plt.xlabel("Pop. of city in 10,000s")
    plt.show()



def computeCost(X,y,theta):
    m = y.size  # No of features
    J =  0      # Cost computed
    #for i in range(1,m+1):
    h = X.dot(theta)
    J = (1/(2*m))*(np.sum(np.square(h-y)))
    return J

def gradientDescent(X,y,theta=[[0],[0]],alpha=0.01,num_iters = 1500):
    m = y.size
    J_history = np.zeros(num_iters)

    for iter in range(num_iters):
        h = X.dot(theta)
        theta = theta - alpha*(1/m)*(X.T.dot(h-y))  # Reducing the parameters theta
        J_history[iter] = computeCost(X,y,theta)    # Computing the cost function with the particular parameters

    return (theta,J_history)

X = np.stack([np.ones(m),X],axis=1)     # Adding an additional column of ones to the X matrix for easier manipulation


J = computeCost(X, y, theta=np.array([0.0, 0.0]))
print('With theta = [0, 0] \nCost computed = %.2f' % J)
print('Expected cost value (approximately) 32.07\n')
#print(J)

# further testing of the cost function
J = computeCost(X, y, theta=np.array([-1, 2]))
print('With theta = [-1, 2]\nCost computed = %.2f' % J)
print('Expected cost value (approximately) 54.24')


#plotData(X,y)       # Plotting the data in the graph
#print(X.shape)
#theta=np.array([0.0, 0.0])
#print(theta.shape)
theta , Cost_J = gradientDescent(X, y)
print('theta: ',theta.ravel())

# Graph for showing the Cost vs Iterations of the model
plt.plot(Cost_J)
plt.ylabel('Cost J')
plt.xlabel('Iterations')
#plt.show()

xx = np.arange(5,23)
#print(X[].shape+"")
#yy = theta[0] + theta[1]*xx
print(xx.shape)
print(np.dot(theta[1],xx))

plt.scatter(X[:,1],y,s=30,c='r',marker='x',linewidths=10)
#plt.plot(xx,yy,label='LR')
#plt.show()

