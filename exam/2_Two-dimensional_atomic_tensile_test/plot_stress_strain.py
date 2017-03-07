#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../../")

from relative_variance import relvariance_nparray, cut_nparray
from MC_tools import variance_nparray, autocovariance 



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

    infile = './results/stress_strain.txt'
    outfilex = './plots/stressx_strain.png'
    outfiley = './plots/stressy_strain.png'
    outfilez = './plots/stressz_strain.png'
    strain   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
    stressx  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    stressy  = np.loadtxt(infile, delimiter=' ', usecols=(2,), unpack=True, dtype=float)
    stressz  = np.loadtxt(infile, delimiter=' ', usecols=(3,), unpack=True, dtype=float)

    plt.plot(strain,stressx)
    plt.xlabel('strain in x-direction [-]')
    plt.ylabel('Stress in x-direction [GPa]')
    plt.title('Stress-strain relation')
    plt.savefig(outfilex,format='png')
    plt.close()

    plt.plot(strain,stressy)
    plt.xlabel('Strain in x-direction [-]')
    plt.ylabel('Stress in y-direction [GPa]')
    plt.title('Stress-strain relation')
    plt.savefig(outfiley,format='png')
    plt.close()
