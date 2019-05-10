import numpy as np
from matplotlib import pyplot as plt

# Input data of form (x-coordinate , y-coordinate, Bias term)
X =np.array([
    [-2,4,-1],
    [4,1,-1],
    [1,6,-1],
    [2,4,-1],
    [6,2,-1]
])

y = np.array([-1,-1,1,1,1]) # Output labels as -1 and 1 for the 2 categories


for d,samples in enumerate(X):      # To split X in terms of (i,X[i]) i = 0 -> len(X)
    if d<2: # plot negative samples (first 2)
        plt.scatter(samples[0],samples[1],s=120,marker='_',linewidths=2)
    else: # plot positive samples (last 3)
        plt.scatter(samples[0],samples[1],s=120,marker='+',linewidths=2)

# Print a possible hyperplane, that is seperating the two classes.
# we'll two points and draw the line between them (naive guess)        
plt.plot([-2,6],[6,0.5])    
plt.title("Before SVM")    
plt.show()

# Perform Gradient descent for Maximizing the margin width therby reducing the loss function(Hinge loss)

def svm_sgd(X,Y):
    #Initialize the weight vectors with zeros(3 values in X sample)
    w = np.zeros(len(X[0]))
    # The learning rate
    eta = 1
    # Set number of iterations
    epochs = 10000
    # Count misclassifications and visualize 
    errors = []

    # Training part 
    for epoch in range(1,epochs):
        error = 0
        for i,x in enumerate(X):
            # misclassification
            if(Y[i]*np.dot(X[i],w) < 1):
                w = w + eta*(Y[i]*X[i] - 2*(1/epoch)*w)     # misclassified updation
                error = 1
            else:
                w = w + eta*(2*(1/epoch)*w)
        errors.append(error)
    return w

'''
    # Plotting the Error rate during Training
    plt.plot(errors,'|')
    plt.ylim(0.5,1.5)
    plt.axes().set_yticklabels([])
    plt.xlabel("Epoch")
    plt.ylabel("Misclassified")
    plt.show()
'''
    




for d,samples in enumerate(X):      # To split X in terms of (i,X[i]) i = 0 -> len(X)
    if d<2: # plot negative samples (first 2)
        plt.scatter(samples[0],samples[1],s=120,marker='_',linewidths=2)
    else: # plot positive samples (last 3)
        plt.scatter(samples[0],samples[1],s=120,marker='+',linewidths=2)

# Add our test samples
plt.scatter(2,2, s=120, marker='_', linewidths=2, color='yellow')
plt.scatter(4,3, s=120, marker='+', linewidths=2, color='blue')


w = svm_sgd(X,y)

# Printing the hyperplane as calculated
x2=[w[0],w[1],-w[1],w[0]]
x3=[w[0],w[1],w[1],-w[0]]

x2x3 = np.array([x2,x3])
X,Y,U,V = zip(*x2x3)
ax = plt.gca()
ax.quiver(X,Y,U,V,scale=1,color='blue')

plt.show()
