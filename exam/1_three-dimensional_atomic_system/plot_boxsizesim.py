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

    cellnums=[str(item.strip().split()[0]) for item in open('./scriptinput/cellnums').readlines()]
    atomnums=[str(item.strip()) for item in open('./scriptinput/cellnums2atoms').readlines()]
    dampvals=[str(item.strip()) for item in open('./scriptinput/dampvals').readlines()]
    print(cellnums)
    print(atomnums)
    print(dampvals)

    thermostats    =['NPT']
    thermostatnames=['NPT with Nose-Hover']
    quantities   =['Lx']
    quantitynames=['Box-size[$\AA$]']

    for ensemble, esemblename in zip(thermostats,thermostatnames):
        for quantity, quantityname in zip(quantities,quantitynames):
            for dampval in dampvals:
                varianceavals=[]
                outfile = './plots/boxsizesim/'+ensemble+'_'+quantity+'_damp'+dampval+'.png'
                for cellnum,atomnum in zip(cellnums,atomnums):

                    infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata   = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

                    yavg = np.average(cut_nparray(ydata))
                    plt.plot(time,ydata,label=atomnum+" atoms, avg.:{:.2E}".format( yavg ))
                    plt.xlabel('Time[fs]')
                    plt.ylabel(quantityname)
                    plt.title(quantityname+' over time for '+esemblename+', Tdamp='+dampval)

                plt.legend(loc='lower right')
                print("\033[92m"+outfile+"\033[00m\n")
                fig = plt.gcf()
                fig.set_size_inches(8, 10)
                plt.gca().set_ylim([0,700])
                plt.savefig(outfile,format='png')
                plt.close()

    for ensemble, esemblename in zip(thermostats,thermostatnames):
        for quantity, quantityname in zip(quantities,quantitynames):
            for dampval in dampvals:
                varianceavals=[]
                outfile = './plots/boxsizesim/boxmod_'+ensemble+'_'+quantity+'_damp'+dampval+'.png'
                for cellnum,atomnum in zip(cellnums,atomnums):

                    infile  = './results/'+ensemble+'/boxmod_'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata   = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

                    yavg = np.average(cut_nparray(ydata))
                    plt.plot(time,ydata,label=atomnum+" atoms, avg.:{:.2E}".format( yavg ))
                    plt.xlabel('Time[fs]')
                    plt.ylabel(quantityname)
                    plt.title(quantityname+' over time for '+esemblename+', Tdamp='+dampval)

                plt.legend(loc='lower right')
                print("\033[92m"+outfile+"\033[00m\n")
                fig = plt.gcf()
                fig.set_size_inches(8, 10)
                plt.gca().set_ylim([0,700])
                plt.savefig(outfile,format='png')
                plt.close()


    #plot histograms
    for ensemble, esemblename in zip(thermostats,thermostatnames):
        for quantity, quantityname in zip(['Press','Temp'],['Pressure[atm]','Temperature [K]']):
            for dampval in dampvals:
                variancevals=[]
                outfile = './plots/boxsizesim/boxmod_'+ensemble+'_'+quantity+'_damp'+dampval+'.png'
                for cellnum,atomnum in zip(['5','7','8','11'],['500','1372','2048','5324']):
                # for cellnum,atomnum in zip(cellnums,atomnums):

                    infile  = './results/'+ensemble+'/boxmod_'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata   = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

                    relvar = relvariance_nparray(cut_nparray(ydata))
                    variancevals.append(relvar)
                    # n, bins, patches = plt.hist(ydata, 50, normed=1)
                    n, bins, patches = plt.hist(ydata, 16, histtype='step', stacked=True, fill=False,label='# of atoms:'+atomnum)
                    # plt.plot(time,ydata,label=atomnum+" atoms, rel. var.:{:.2E}".format( relvar ))
                    plt.xlabel('Pressure[atm]')
                    plt.ylabel('occurences')
                    plt.title(quantityname+' histogram '+esemblename+', Tdamp='+dampval)

                plt.legend(loc='upper right')
                print("\033[92m"+outfile+"\033[00m\n")
                fig = plt.gcf()
                # fig.set_size_inches(8, 10)
                plt.savefig(outfile,format='png')
                plt.close()

                variancevals = []
                for cellnum,atomnum in zip(cellnums,atomnums):
                    infile  = './results/'+ensemble+'/boxmod_'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    ydata   = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
                    relvar = relvariance_nparray(cut_nparray(ydata))
                    variancevals.append(relvar)

                plt.loglog(atomnums,variancevals,'-bo',label='simulation data')
                plt.loglog(atomnums,[1/float(i) for i in atomnums],'--b',label='y~1/x')
                plt.xlabel("# of atoms")
                plt.ylabel("relative variance of "+quantityname)
                plt.legend(loc='lower left')
                plt.title('relative variance for Tdamp='+dampval+'[fs]')
                outfile="./plots/boxsizesim/relvar_"+quantity+"_damp"+dampval+".png"
                plt.savefig(outfile,fomat='png')
                plt.close()




    scalefacs=[8.983,8.983,9.0,9.0,9.0,9.0,8.998,8.997]
    # plot density over atomnum
    for ensemble, esemblename in zip(thermostats,thermostatnames):
        for quantity, quantityname in zip(['Density'],['Density[gramm/cm^3]']):
            for dampval in dampvals:
                avgvals=[]
                outfile = './plots/boxsizesim/boxmod_'+ensemble+'_'+quantity+'_damp'+dampval+'.png'
                for cellnum,atomnum,scalefac in zip(cellnums,atomnums,scalefacs):
                # for cellnum,atomnum in zip(cellnums,atomnums):

                    celllength=float(cellnum)*5.9*scalefac*1e-8
                    print(celllength)
                    density=(float(atomnum)*83.798)/(6.022*1e23*pow(float(celllength),3))

                    # infile  = './results/'+ensemble+'/boxmod_'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                    print(infile)
                    
                    # time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                    # ydata   = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
                    # avgvar = np.average(cut_nparray(ydata))
                    # avgvals.append(relvar)
                    avgvals.append(density)
                plt.plot(atomnums,avgvals,'-ob',label='simulation')
                plt.plot(atomnums,[0.003749 for a in atomnums],'--b',label='reference value')
                plt.xlabel('# of atoms')
                plt.legend(loc='lower right')
                print("\033[92m"+outfile+"\033[00m\n")
                plt.gca().set_ylim([0.00365,0.0038])
                plt.savefig(outfile,format='png')
                plt.close()

