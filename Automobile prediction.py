import numpy as np
import matplotlib.pyplot as plt
import csv


def estimate_coef(x,y):
    n=np.size(x)
    mean_x=np.mean(x)
    mean_y=np.mean(y)
    mean_xy=np.mean(x*y)
    mean_xx=np.mean(x*x)
    #ss_xy=np.sum(y*x-n*mean_x*mean_y)
    #ss_xx=np.sum(x*x-n*mean_x*mean_x)
    ss_xy=mean_x*mean_y-mean_xy
    ss_xx=mean_x*mean_x-mean_xx
    c_1=ss_xy/ss_xx
    c_0=mean_y - c_1*mean_x
    return(c_0,c_1)

def plot_line(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_prediction=b[0] + b[1]*x
    plt.plot(x,y_prediction,color="g")
    plt.xlabel('Engine_size')
    plt.ylabel('Price')
    plt.show()

def pred_err(x,y,b):
    y_pred=b[0]+b[1]*x
    pred=((y-y_pred)/y)*100
    return np.mean(pred)


def main():
    #x=np.array([65.04851,63.25094,64.95532,65.75250,61.13723,63.02254])
    #y=np.array([59.77827,63.21404,63.34242,62.79238,64.28113,64.24221])
    #file=open("E:\Programming\Python\Learning\Automobile.csv","r")
    #f=file.read()
    #m=f.split(",")
    #with open('E:\Programming\Python\Learning\Automobile.csv', newline='') as f:
    # m = csv.reader(f)
    #m=[]
    # for x in f:
    #    m.append(x.split(','))
        #m.append(x.split(',')[1])
    #file.close()
    #print(m)

    #eng_size = []
    #price = []

    #for d in csv.DictReader(open('E:\Programming\Python\Learning\Automobile.csv'), delimiter='\t'):
        #eng_size.append(int(d["Engine_size"]))
        #price.append(int(d["Price"]))

    f=open("E:\Programming\Python\Learning\Datasets\Automobile.csv","r")    
    csv_f=csv.reader(f)

    p=[]
    q=[]

    for row in csv_f:
        p.append(float(row[0]))
        q.append(float(row[1]))
    x=np.array(p)    
    y=np.array(q)

    s=float(input("Enter the size of the Engine:"))
    
       
    #print(x)   
    b=estimate_coef(x,y)
    print("The estimated price is ",b[0]+b[1]*s)
   
    print("Estimated coefficients:\nb_0 = {} \
		\nb_1 = {}".format(b[0], b[1]))

    print("The prediction error rate is ",abs(pred_err(x,y,b))    )

    plot_line(x,y,b)

if __name__ == "__main__":
    main()
