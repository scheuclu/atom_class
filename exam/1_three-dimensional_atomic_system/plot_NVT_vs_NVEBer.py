#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../../")

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray

import matplotlib.mlab as mlab



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

    cellnums=[str(item.strip().split()[0]) for item in open('./scriptinput/cellnums').readlines()]
    atomnums=[str(item.strip()) for item in open('./scriptinput/cellnums2atoms').readlines()]
    dampvals=[str(item.strip()) for item in open('./scriptinput/dampvals').readlines()]
    print(cellnums)
    print(atomnums)
    print(dampvals)

    thermostats    =['NVT','NVEBer']
    thermostatnames=['Nose-Hoover','NVE+Berendsen']
    quantities   =['PotEng',                      'Press',         'Density',            'Temp',           'KinEng',                    'TotEng']
    quantitynames=['Potential Energy [Kcal/mole]','Pressure [atm]','Density [gram/cm^3]','Temperature [K]','Kinetic Energy [Kcal/mole]','Total Energy [Kcal/mole]']

    for dampval in dampvals:
        for quantity,quantityname in zip(quantities,quantitynames):
            varianceavals=[]
            for cellnum,atomnum in zip(cellnums,atomnums):
                outfile = './plots/NVT_vs_NVEBer/hist_'+quantity+'_damp'+dampval+'_atomnum'+atomnum+'.png'
                for ensemble,ensemblename in zip(thermostats,thermostatnames):

                    infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
########################
                    array=cut_nparray(ydata)
                    s = np.std(array)
                    m = np.mean(array)
                    if s!=0:
                        x1=min(array)
                        x2=max(array)+(max(array)-min(array))*0.5
                        x=np.linspace(x1,x2,1000)
                        y=mlab.normpdf(x,m,s)
                        lineplot= plt.plot(x,y,'--')
                        c1 = lineplot[0].get_color()
                    else:
                        c1='k'

                    relvar = relvariance_nparray(cut_nparray(ydata))
                    varianceavals.append(relvar)
                    n, bins, patches = plt.hist(cut_nparray(ydata), 30,color=c1, histtype='step', normed=1, stacked=True, fill=False,label="ensemble: "+ensemble+'\n$\mu$={:.2E}'.format(m)+"\n$\sigma$={:.2E}".format(s))
                    plt.xlabel(quantityname)
                    plt.ylabel('PDF-value')
                    plt.title('Equilibriated distribution of '+quantityname)
##############################3
                    # relvar = relvariance_nparray(cut_nparray(ydata))
                    # varianceavals.append(relvar)
                    # plt.plot(time,ydata,label="ensemble: "+ensemble+" rel. var.:"+"{:.2E}".format( relvar ))
                    # plt.xlabel('Time[fs]')
                    # plt.ylabel(quantityname)
                plt.legend(loc='upper right')
                plt.title('Distribution of '+quantityname+', Tdamp='+dampval+'[fs]')
                print("\033[92m"+outfile+"\033[00m\n")
                plt.savefig(outfile,format='png')
                plt.close()


    for dampval in dampvals:
        for quantity,quantityname in zip(quantities,quantitynames):
            varianceavals=[]
            outfilevar = './plots/NVT_vs_NVEBer/variance_'+quantity+'_damp'+dampval+'.png'
            for cellnum,atomnum in zip(cellnums,atomnums):
                outfile = './plots/NVT_vs_NVEBer/'+quantity+'_damp'+dampval+'_atomnum'+atomnum+'.png'
                for ensemble,ensemblename in zip(thermostats,thermostatnames):

                    infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

                    relvar = relvariance_nparray(cut_nparray(ydata))
                    varianceavals.append(relvar)
                    plt.plot(time,ydata,label="ensemble: "+ensemble+" rel. var.:"+"{:.2E}".format( relvar ))
                    plt.xlabel('Time[fs]')
                    plt.ylabel(quantityname)
                plt.legend(loc='lower right')
                plt.title('Convergence '+quantityname+', Tdamp='+dampval+'[fs]')
                print("\033[92m"+outfile+"\033[00m\n")
                plt.savefig(outfile,format='png')
                plt.close()


    for dampval in dampvals:
        for quantity,quantityname in zip(quantities,quantitynames):
            outfilevar = './plots/NVT_vs_NVEBer/variance_'+quantity+'_damp'+dampval+'.png'
            for ensemble,ensemblename in zip(thermostats,thermostatnames):
                varianceavals=[]
                for cellnum,atomnum in zip(cellnums,atomnums):
                    
                    infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
                    relvar = relvariance_nparray(cut_nparray(ydata))
                    varianceavals.append(relvar)
                plt.xlabel('# of atoms')
                plt.ylabel('relative variance')
                plt.title(quantityname+' under '+ensemblename)
                plt.plot(atomnums,varianceavals,'-o',label=ensemble)
            plt.legend(loc='upper right')
            print("\033[92m"+outfilevar+"\033[00m\n")
            plt.savefig(outfilevar,format='png')
            plt.close()


