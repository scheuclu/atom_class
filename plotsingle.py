#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plotsimple.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":
  if len(sys.argv)!=8:
      print("Invalid syntax")
      sys.exit(-1)

  infile =sys.argv[1]
  outfile=sys.argv[2]
  nameX  =sys.argv[3]
  nameY  =sys.argv[4]
  title  =sys.argv[5]
  special=sys.argv[6]
  dovar  =sys.argv[7]

  xdata  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
  ydata  = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
  plt.plot(xdata,ydata)


  ydata_max=np.max(cut_nparray(ydata))
  if special=='final':
    finalval=ydata[-1]
    plt.text(xdata[int(len(xdata)/2)],finalval,'Final value: '+"{:.2E}".format(finalval),color='green')
    plt.plot(xdata,ydata*0+finalval,'--g')
  elif special=='avg':
    ydata_avg=np.average(ydata)
    plt.text(xdata[int(len(xdata)/2)],ydata_max,'Avergage :'+"{:.2E}".format(ydata_avg),color='green')
    plt.plot(xdata,ydata*0+ydata_avg,'--g')
  elif special=='redavg':
    ydata_avg=np.average(cut_array(ydata))
    plt.text(xdata[int(len(xdata)/2)],ydata_max,'Avergage :'+"{:.2E}".format(ydata_avg),color='green')
    plt.plot(xdata,ydata*0+ydata_avg,'--g')
  elif special=='none':
    1+1
  else:
    print('Invalid annotater!')
    sys.exit(-1)


  plt.xlabel(nameX)
  plt.ylabel(nameY)

  if dovar=='True':
    relvar=relvariance_nparray(ydata)
    plt.title(title+" (rel. var.: "+"{:.2E}".format(relvar)+")")
  else:
    plt.title(title)

  plt.savefig(outfile,format='png',dpi=200)
  plt.close()

  print("Plot successfully written to: "+str(outfile))

