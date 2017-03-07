#!/usr/bin/python3
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import sys
import numpy as np

sys.path.append("../../")

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

    cellnums=[str(item.strip().split()[0]) for item in open('./scriptinput/cellnums').readlines()]
    atomnums=[str(item.strip()) for item in open('./scriptinput/cellnums2atoms').readlines()]
    dampvals=[str(item.strip()) for item in open('./scriptinput/dampvals').readlines()]
    print(cellnums)
    print(atomnums)
    print(dampvals)

    quantities   =['Lx','PotEng','Density','Press','KinEng','Temp','TotEng']
    quantitynames=['Box-size[$\AA$]','Potential Energy [Kcal/mole]','Density [grams/mole]', 'Pressure [atm]', 'Kinetic Energy [Kcal/mole]', 'Temperature [K]', 'Total Energy [Kcal/mole]']

    for sim in ['equi','NVT']:
        for quantity, quantityname in zip(quantities,quantitynames):
            infile = './results/CV/'+sim+'_'+quantity+'.txt'
            outfile = './plots/CV/'+sim+'_'+quantity+'.png'
            time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
            ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
            plt.plot(time,ydata,label='simulation')
            avg = np.average(cut_nparray(ydata))
            plt.plot(time,ydata*0+avg,'g--',label='avg. value:{:.2E}'.format(avg))
            plt.ylabel(quantityname)
            plt.xlabel('Time [fs]')
            plt.legend(loc='lower right')
            plt.title('Equilibriation of '+quantityname)
            plt.savefig(outfile,format='png')
            plt.close()


            outfile = './plots/CV/hist_'+sim+'_'+quantity+'.png'
            n, bins, patches = plt.hist(cut_nparray(ydata), 50, histtype='step', normed=1, stacked=True, fill=False,label='simulation results')
            array=cut_nparray(ydata)
            s = np.std(array)
            m = np.mean(array)
            if s!=0:
                x1=min(array)
                x2=max(array)
                x=np.linspace(x1,x2,1000)
                y=mlab.normpdf(x,m,s)
                plt.plot(x,y,'g--',label='$\mu$={:.2E}'.format(m)+"\n$\sigma$={:.2E}".format(s))
            plt.xlabel(quantityname)
            plt.ylabel('PDF value')
            plt.title('Histogram of equilibriated '+quantityname)
            plt.legend(loc='upper left')
            plt.savefig(outfile,format='png')
            plt.close()
