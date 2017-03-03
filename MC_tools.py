#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

from relative_variance import cut_nparray


#I use only the second (converged) half to compute the variance
def variance_nparray(data):
    red_data=cut_nparray(data)
    N=len(red_data)
    mean=1/N*sum(red_data)
    return 1/N*sum( (red_data-mean)*(red_data-mean) )

def autocovariance(data):
    N=len(data)
    data_avg=np.average(cut_nparray(data))
    result=[]
    for j in range(N):
        sum=0
        for i in range(N-j):
            sum=sum+(data[i]-data_avg)*(data[i+j]-data_avg)
        var=variance_nparray(cut_nparray(data))
        sum=1/var*1/(N-j)*sum
        result.append(sum)
    return result


if __name__ == "__main__":

    colnum = 1
    infile='./tutorial3/results/gcmc/equi_Press_trans0.1_damp20000.txt'
    data=np.loadtxt(infile, delimiter=' ', usecols=(colnum,), unpack=True, dtype=float)


    print(variance_nparray(data))
    print(autocovariance(data))
    res=autocovariance(data)
    plt.plot(range(len(res)),res)
    plt.show()




