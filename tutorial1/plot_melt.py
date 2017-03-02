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

    for temp in temprange:
        infile='./results/NPT_melt_Density_temp'+str(temp)
        data  = np.genfromtxt(infile,  delimiter=' ',
            skip_header=0,skip_footer=0,names=['Time','Density'])
        ydata = data['Density']
        dens_avg=np.average(cut_nparray(ydata))
        densities_red.append(dens_avg)

        infile='./results/NPT_melt_KinEng_temp'+str(temp)
        data  = np.genfromtxt(infile,  delimiter=' ',
            skip_header=0,skip_footer=0,names=['Time','KinEng'])
        ydata = data['KinEng']
        kineng_avg=np.average(cut_nparray(ydata))
        kineng_red.append(kineng_avg)


    plt.plot(temprange,densities_red,'-')
    plt.xlabel('Temperature [K]')
    plt.ylabel('Density')
    plt.title('Density over temperature')
    plt.gca().grid(True)
    plt.savefig('./plots/melt/NPT_Density_over_Temp.png',format='png',dpi=200)
    plt.close()

    plt.plot(temprange,kineng_red,'-')
    plt.xlabel('Temperature [K]')
    plt.ylabel('Kinetic Energy')
    plt.title('Kinetic Energy over Temperature')
    plt.gca().grid(True)
    plt.savefig('./plots/melt/NPT_KinEng_over_Temp.png',format='png',dpi=200)
