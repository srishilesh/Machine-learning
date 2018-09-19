import numpy as np
import matplotlib.pyplot as plt
import csv

def estimate_coef(x, y):
    n = np.size(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    ss_xy = np.sum(x*y - n*mean_x*mean_y)
    ss_xx = np.sum(x*x - n*mean_x*mean_x) 
    c_1 = ss_xy/ss_xx
    c_0 = mean_y  - c_1 * mean_x
    return(c_0,c_1)


    

def plot_line(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_pred = b[0] + b[1]*x
    plt.plot(x,y_pred,color="g")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def main():
    f=open("E:\Programming\Python\Learning\Datasets\Pricing.csv","r")    
    csv_f= csv.reader(f)
    

    p= []
    q= []
    for row in csv_f:
        p.append(float(row[0]))
        q.append(float(row[1]))
    x= np.array(p)    
    y= np.array(q)

    s= float(input("Enter the value of x:"))
    b= estimate_coef(x,y)
    print("The estimated value of y is ",b[0]+b[1]*s)
    print("Estimated Coefficients:\n b_0={}\nb_1={}".format(b[0],b[1]))
    
    plot_line(x,y,b)

if __name__=="__main__":
    main()    
