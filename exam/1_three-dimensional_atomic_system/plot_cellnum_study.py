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

  thermostats    =['NVT','NVEBer']
  thermostatnames=['Nose-Hoover','NVE+Berendsen']
  quantities   =['PotEng',                      'Press',         'Temp',           'KinEng',                    'TotEng']
  quantitynames=['Potential Energy [Kcal/mole]','Pressure [atm]','Temperature [K]','Kinetic Energy [Kcal/mole]','Total Energy [Kcal/mole]']

  for ensemble, ensemblename in zip(thermostats,thermostatnames):
      for dampval in dampvals:
          for quantity,quantityname in zip(quantities,quantitynames):
              varianceavals=[]
              outfile = './plots/cellnum_study/'+ensemble+'_'+quantity+'_damp'+dampval+'.png'

              for cellnum,atomnum in zip(cellnums,atomnums):

                  infile  = './results/'+ensemble+'/'+quantity+'_damp'+dampval+'_cellnum'+cellnum
                  print(infile)
                  
                  time   = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
                  ydata   = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

                  relvar = relvariance_nparray(cut_nparray(ydata))
                  varianceavals.append(relvar)
                  # plt.plot(time,ydata,label="cellnum: "+cellnum+" rel. var.:"+"{:.2E}".format( relvar ))
                  # plt.xlabel('Time[fs]')
                  # plt.ylabel(quantityname)
              # plt.legend(loc='lower right')
              # plt.savefig(outfile,format='png')
              # plt.close()
              if ensemble=='NVT':
                 plt.loglog(atomnums,varianceavals,'b-o',label=quantityname)
                 temp=[1/float(k) for k in atomnums]
                 # i=int(len(temp)/2)
                 # tempi=temp[i]
                 # tempnew=[j-tempi+varianceavals[i] for j in temp]
                 plt.loglog(atomnums,temp,'b--',label='y~1/x')
              else:
                 plt.plot(atomnums,varianceavals,'-o')
              plt.xlabel('# of atoms')
              plt.ylabel('relative variance of '+quantityname)
              plt.legend(loc='lower left')
              plt.savefig(outfile,format='png')
              print("\033[92m"+outfile+"\033[00m\n")
              plt.close()



      # print(outfile)
      # variancearray=[]
      # for cellnum, atomnum in zip(cellnums,atomnums):
          # infile = './results/NVT_convergence_syssize_'+quantity+'_'+str(cellnum)+'.txt'
          # data  = np.genfromtxt(infile,  delimiter=' ',
                  # skip_header=0,skip_footer=0,names=['Time',quantity])
          # xdata = data['Time']
          # ydata = data[quantity]
          # relvar = relvariance_nparray(ydata)
          # variancearray.append(relvar)
      # plt.plot(atomnums,variancearray,'-o')
      # for x,y in zip(atomnums,variancearray):
          # plt.text(x,y,"{:.4E}".format(y))
      # plt.xlabel('number of atoms')
      # plt.ylabel('relative variance of '+quantity)
      # plt.title('relative variance of '+quantity+' over #atoms')
      # plt.savefig(outfile,format='png',dpi=200)
      # plt.close()
