#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../")

from relative_variance import relvariance_nparray, cut_nparray
from MC_tools import variance_nparray, autocovariance 



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

  translatevals=[float(item.strip()) for item in open('./scriptinput/translatevals').readlines()]
  dampvals=[str(item.strip()) for item in open('./scriptinput/dampvals').readlines()]

  for quantity in ['PotEng','Press','Temp','KinEng','TotEng']:
      for translateval in translatevals:
          outfile = './plots/autocov/'+quantity+'_trans'+str(translateval)+'.png'
          print(outfile)
          variancearray=[]
          for dampval in dampvals:
              infile='./results/gcmc/equi_'+quantity+'_trans'+str(translateval)+'_damp'+dampval+'.txt'
              ydata=np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
              xdata=np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
              autocov=autocovariance(ydata)
              plt.plot(xdata,autocov,label=dampval)
          plt.xlabel('Time')
          plt.ylabel('autocovariance')
          plt.title(quantity+'_tans'+str(translateval))
          plt.legend()
          plt.savefig(outfile,format='png')
          plt.close()
