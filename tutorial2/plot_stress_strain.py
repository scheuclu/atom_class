#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../")

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

    densities_red=[]
    kineng_red    =[]
    temprange    =range(25,305,5)
    infile = './results/stress_strain.txt'
    data  = np.genfromtxt(infile,  delimiter=' ',
       skip_header=1,skip_footer=0,names=['strain','pxx','pyy','pzz'])
    strain=data['strain']
    pxx   =data['pxx']
    pyy   =data['pyy']
    pzz   =data['pzz']
    
    plt.plot(strain,pxx)
    plt.xlabel('Strain')
    plt.ylabel('pxx')
    plt.savefig('./plots/pxx_over_strain.png',format='png')
    plt.close()

    plt.plot(strain,pyy)
    plt.xlabel('Strain')
    plt.ylabel('pyy')
    plt.savefig('./plots/pyy_over_strain.png',format='png')
    plt.close()

    plt.plot(strain,pzz)
    plt.xlabel('Strain')
    plt.ylabel('pzz')
    plt.savefig('./plots/pzz_over_strain.png',format='png')
    plt.close()
