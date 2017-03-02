#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../")

from relative_variance import relvariance_nparray



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

  cellnums=[int(item.strip()) for item in open('./scriptinput/cellnums').readlines()]
  atomnums=[int(item.strip()) for item in open('./scriptinput/cellnums2atoms').readlines()]
  print(cellnums)
  print(atomnums)

  for quantity in ['PotEng','Press','Temp','KinEng','TotEng']:
      outfile = './plots/syssize/NVT_'+quantity+'.png'
      print(outfile)
      variancearray=[]
      for cellnum, atomnum in zip(cellnums,atomnums):
          infile = './results/NVT_convergence_syssize_'+quantity+'_'+str(cellnum)+'.txt'
          data  = np.genfromtxt(infile,  delimiter=' ',
                  skip_header=0,skip_footer=0,names=['Time',quantity])
          xdata = data['Time']
          ydata = data[quantity]
          relvar = relvariance_nparray(ydata)
          variancearray.append(relvar)
      plt.plot(atomnums,variancearray,'-o')
      for x,y in zip(atomnums,variancearray):
          plt.text(x,y,"{:.4E}".format(y))
      plt.xlabel('number of atoms')
      plt.ylabel('relative variance of '+quantity)
      plt.title('relative variance of '+quantity+' over #atoms')
      plt.savefig(outfile,format='png',dpi=200)
      plt.close()
