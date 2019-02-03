import numpy as np
import matplotlib.pyplot as plt
import csv

def estimate_coef(x,y):
    mean_x=np.mean(x)
    mean_y=np.mean(y)
    mean_xx=np.mean(x*x)
    mean_xy=np.mean(x*y)
    ss_xy=mean_x*mean_y-mean_xy
    ss_xx=mean_x*mean_x-mean_xx
    c_1=ss_xy/ss_xx
    c_0=mean_y-c_1*mean_x
    return (c_0,c_1)

def pred_err(x,y,b):
    y_pred=b[0]+b[1]*x
    pred=((y-y_pred)/y)*100
    return np.mean(pred)
       

def plot_line(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_pred=b[0]+b[1]*x
    plt.plot(x,y_pred,color="g")
    plt.xlabel("Annual Fee for Franchise")
    plt.ylabel("Startup Fee for Franchise")
    plt.show()
    


def main():
    f=open("E:\Programming\Python\Learning\Datasets\Pizza_franchise.csv","r")
    csv_f=csv.reader(f)
    p=[]
    q=[]

    for i in csv_f:
        p.append(int(i[0]))
        q.append(int(i[1]))
    x=np.array(p)    
    y=np.array(q)

    m=int(input("Enter the Annual Franchise fee:"))

    b=estimate_coef(x,y)
    print("The Estimated startup fee for a Franchise is ",b[0]+b[1]*m)

    print("Estimated Coefficients:\nb_0={}\nb_1={}".format(b[0],b[1]))
    print("The prediction error rate is ",abs(pred_err(x,y,b))    )

    plot_line(x,y,b)

if __name__ == "__main__":
    main()

