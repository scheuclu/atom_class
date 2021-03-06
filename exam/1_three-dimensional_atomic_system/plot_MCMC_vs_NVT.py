#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../../")

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

    # cellnums=[str(item.strip().split()[0]) for item in open('./scriptinput/cellnums').readlines()]
    # atomnums=[str(item.strip()) for item in open('./scriptinput/cellnums2atoms').readlines()]
    dampvals=[str(item.strip()) for item in open('./scriptinput/dampvals').readlines()]
    # print(cellnums)
    # print(atomnums)
    print(dampvals)

    thermostats    =['NVTstep','MCMC']
    thermostatnames=['Nose-Hoover MD','MCMC']
    quantities   =['PotEng',                      'Press',         'Temp',           'KinEng',                    'TotEng']
    quantitynames=['Potential Energy [Kcal/mole]','Pressure [atm]','Temperature [K]','Kinetic Energy [Kcal/mole]','Total Energy [Kcal/mole]']

    for dampval in dampvals:
        for quantity,quantityname in zip(quantities,quantitynames):
                varianceavals=[]
                outfile = './plots/MCMC_vs_NVT/'+quantity+'_damp'+dampval+'.png'
                for ensemble,ensemblename in zip(thermostats,thermostatnames):

                    infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum5'
                    print(infile)
                    
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

                    relvar = relvariance_nparray(cut_nparray(ydata))
                    varianceavals.append(relvar)
                    plt.plot(time,ydata,label="ensemble: "+ensemble+" rel. var.:"+"{:.2E}".format( relvar ))
                    plt.xlabel('Step number')
                    plt.ylabel(quantityname)
                plt.legend(loc='lower right')
                plt.title('Convergence '+quantityname+', Tdamp='+dampval+'[fs]')
                print("\033[92m"+outfile+"\033[00m\n")
                plt.savefig(outfile,format='png')
                plt.close()

    for dampval in dampvals:
        for quantity,quantityname in zip(quantities,quantitynames):
                varianceavals=[]
                outfile = './plots/MCMC_vs_NVT/hist_'+quantity+'_damp'+dampval+'.png'
                for ensemble,ensemblename in zip(thermostats,thermostatnames):

                    infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum5'
                    print(infile)
                    
                    ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
                    n, bins, patches = plt.hist(cut_nparray(ydata), 30,normed=True, histtype='step', stacked=True, fill=False, label=ensemblename)

                    plt.xlabel(quantityname)
                    plt.ylabel('PDF value')
                plt.legend(loc='upper right')
                plt.title('Histogram '+quantityname+', Tdamp='+dampval+'[fs]')
                print("\033[92m"+outfile+"\033[00m\n")
                plt.savefig(outfile,format='png')
                plt.close()

