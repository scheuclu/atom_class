#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plotsimple.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":
  if len(sys.argv)!=6:
      print("Invalid syntax")
      sys.exit(-1)

  infile =sys.argv[1]
  outfile=sys.argv[2]
  nameX  =sys.argv[3]
  nameY  =sys.argv[4]
  title  =sys.argv[5]

  data  = np.genfromtxt(infile,  delimiter=' ',
          skip_header=0,skip_footer=0,names=[nameX,nameY])
  xdata=data[nameX]
  ydata=data[nameY]
  ydata_avg=np.average(cut_nparray(ydata))
  plt.plot(xdata,ydata)
  plt.plot(xdata,ydata*0+ydata_avg,'--')
  plt.xlabel(nameX)
  plt.ylabel(nameY)

  relvar=relvariance_nparray(ydata)

  plt.title(title+" (rel. var.: "+"{:.2E}".format(relvar)+")")

  plt.savefig(outfile,format='png',dpi=200)
  plt.close()

  print("Plot successfully written to: "+str(outfile))

