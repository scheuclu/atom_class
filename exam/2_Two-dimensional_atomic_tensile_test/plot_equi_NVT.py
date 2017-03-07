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
    kb=1.380648e-26#[kJ/K]
    eps=0.3228

    quantities   =['Lx','Temp','Density', 'PotEng', 'KinEng', 'TotEng', 'Press']
    quantitynames=['Box-size[$\AA$]', 'Temperature [K]', 'Density [gramm/cm^3]', 'Potential Energy [kcal/mole]', 'Kinetic Energy [kcal/mole]', 'Total Energy [kcal/mole]', 'Pressure [atm]'   ]
    pdampvals=[str(item.strip()) for item in open('./scriptinput/pdamp').readlines()]
    tdampvals=[str(item.strip()) for item in open('./scriptinput/Tdamp').readlines()]

    for quantity, quantityname in zip(quantities,quantitynames):
        for pdamp in pdampvals:
            outfile='./plots/equi/dampstudy/NVT_'+quantity+'_pdamp'+pdamp+'.png'
            for tdamp in tdampvals:
                infile = './results/equi/NVT_'+quantity+'_'+pdamp+'_'+tdamp+'.txt'
                print(infile)
                time  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
                plt.plot(time,ydata,label='$T_{damp}='+tdamp+'$')
            plt.xlabel('Time [fs]')
            plt.ylabel(quantityname)
            plt.legend(loc='center right')
            print("\033[92m"+outfile+"\033[00m\n")
            plt.title(quantityname+' convergence at $P_{damp}='+pdamp+'$')
            plt.savefig(outfile,format='png')
            plt.close()


        for tdamp in tdampvals:
            outfile='./plots/equi/dampstudy/NVT_'+quantity+'_tdamp'+tdamp+'.png'
            for pdamp in pdampvals:
                infile = './results/equi/NVT_'+quantity+'_'+pdamp+'_'+tdamp+'.txt'
                print(infile)
                time  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
                plt.plot(time,ydata,label='$P_{tamp}='+pdamp+'$')
            plt.xlabel('Time [fs]')
            plt.ylabel(quantityname)
            plt.legend(loc='center right')
            print("\033[92m"+outfile+"\033[00m\n")
            plt.title(quantityname+' convergence at $T_{damp}='+tdamp+'$')
            plt.savefig(outfile,format='png')
            plt.close()




        # outfile = './plots/phasetrans/'+quantity+'.png'
        # outfilered = './plots/phasetrans/red_'+quantity+'.png'
        # values = []
        # valuesred = []

        # temperatures = range(26,231,1)
        # temperaturesred = [t*kb/eps for t in temperatures]
        # for temp in temperatures:
            # infile = './results/phasetrans/temp'+str(temp)+'_'+quantity+'.txt'
            # infileLx = './results/phasetrans/temp'+str(temp)+'_Lx.txt'
            # print(infile)
            # outfiletemp = './plots/phasetrans/convergence/temp'+str(temp)+'_'+quantity+'.png'

            # time  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
            # ydata = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
            # Lxdata = np.loadtxt(infileLx, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

            # boxsize = np.average(cut_nparray(Lxdata))

            # ydataavg=np.average(cut_nparray(ydata))
            # values.append(ydataavg)

            # ydatared=red_ydata(ydata,boxsize,quantity)
            # ydataredavg=np.average(cut_nparray(ydatared))
            # valuesred.append(ydatared)

            # # plt.plot(time,ydata)
            # # plt.xlabel('Time [fs]')
            # # plt.ylabel(quantityname)
            # # print("\033[92m"+outfiletemp+"\033[00m\n")
            # # plt.savefig(outfiletemp,format='png')
            # # plt.close()
        # plt.plot(temperatures,values,'-')
        # plt.xlabel('Temperature [K]')
        # plt.ylabel(quantityname)
        # plt.grid()
        # print("\033[92m"+outfile+"\033[00m\n")
        # plt.savefig(outfile,format='png')
        # plt.close()

        # plt.plot(temperaturesred,valuesred,'-')
        # plt.xlabel('Reduced temperature')
        # plt.ylabel("Reduced "+quantity)
        # plt.grid()
        # print("\033[92m"+outfilered+"\033[00m\n")
        # plt.savefig(outfilered,format='png')
        # plt.close()





        # #detail1
        # outfile = './plots/phasetrans/detail1/'+quantity+'.png'
        # outfilered = './plots/phasetrans/detail1/red_'+quantity+'.png'
        # values = []
        # valuesred = []
        # temperatures = range(120,140,1)
        # temperaturesred = [t*kb/eps for t in temperatures]
        # for temp in temperatures:
            # infile = './results/phasetrans/temp'+str(temp)+'_'+quantity+'.txt'
            # print(infile)
            # time  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
            # ydata = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
            # ydataavg=np.average(cut_nparray(ydata))
            # values.append(ydataavg)

            # ydatared=red_ydata(ydata,boxsize,quantity)
            # ydataredavg=np.average(cut_nparray(ydatared))
            # valuesred.append(ydatared)

        # plt.plot(temperatures,values,'-o')
        # plt.xlabel('Temperature [K]')
        # plt.ylabel(quantityname)
        # plt.grid()
        # temperatures = range(25,231,1)
        # print("\033[92m"+outfile+"\033[00m\n")
        # plt.savefig(outfile,format='png')
        # plt.close()

        # plt.subplots()
        # plt.plot(temperaturesred,valuesred,'-o')
        # plt.xlabel('Reduced temperature')
        # plt.ylabel("Reduced "+quantity)
        # plt.grid()
        # print("\033[92m"+outfilered+"\033[00m\n")
        # plt.savefig(outfilered,format='png')
        # plt.close()


        # #detail2
        # outfile = './plots/phasetrans/detail2/'+quantity+'.png'
        # outfilered = './plots/phasetrans/detail2/red_'+quantity+'.png'
        # values = []
        # valuesred = []
        # temperatures = range(174,182,1)
        # temperaturesred = [t*kb/eps for t in temperatures]
        # for temp in temperatures:
            # infile = './results/phasetrans/temp'+str(temp)+'_'+quantity+'.txt'
            # print(infile)
            # time  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
            # ydata = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
            # ydataavg=np.average(cut_nparray(ydata))
            # values.append(ydataavg)

            # ydatared=red_ydata(ydata,boxsize,quantity)
            # ydataredavg=np.average(cut_nparray(ydatared))
            # valuesred.append(ydatared)

        # plt.plot(temperatures,values,'-o')
        # plt.xlabel('Temperature [K]')
        # plt.ylabel(quantityname)
        # plt.grid()
        # temperatures = range(25,231,1)
        # print("\033[92m"+outfile+"\033[00m\n")
        # plt.savefig(outfile,format='png')
        # plt.close()

        # plt.plot(temperaturesred,valuesred,'-')
        # plt.xlabel('Reduced temperature')
        # plt.ylabel("Reduced "+quantity)
        # plt.grid()
        # print("\033[92m"+outfilered+"\033[00m\n")
        # plt.savefig(outfilered,format='png')
        # plt.close()

        # valuesred=[]
