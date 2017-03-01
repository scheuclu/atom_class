#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

from relative_variance import relvariance_nparray



#assuming the follwowing input format
#plotsimple.py filename1.txt filename2.txt plotfilename.png xname yname data1name data2name plottitle

if __name__ == "__main__":
  if len(sys.argv)!=9:
      print("Invalid syntax")
      sys.exit(-1)

  infile1 =sys.argv[1]
  infile2 =sys.argv[2]
  outfile=sys.argv[3]
  nameX  =sys.argv[4]
  nameY  =sys.argv[5]
  name1  =sys.argv[6]
  name2  =sys.argv[7]
  title  =sys.argv[8]

  data1  = np.genfromtxt(infile1,  delimiter=' ',
          skip_header=0,skip_footer=0,names=[nameX,nameY])
  data2  = np.genfromtxt(infile2,  delimiter=' ',
          skip_header=0,skip_footer=0,names=[nameX,nameY])
  xdata1 =data1[nameX]
  xdata2 =data2[nameX]
  ydata1=data1[nameY]
  ydata2=data2[nameY]

  relvar1=relvariance_nparray(ydata1)
  relvar2=relvariance_nparray(ydata2)
  plt.plot(xdata1,ydata1,label=name1+" (rel. var.: "+"{:.2E}".format(relvar1)+")")
  plt.plot(xdata2,ydata2,label=name2+" (rel. var.: "+"{:.2E}".format(relvar2)+")")
  plt.xlabel(nameX)
  plt.ylabel(nameY)
  plt.legend(loc = 'lower right')
  # relvar=relvariance_nparray(ydata)

  plt.title(title)

  plt.savefig(outfile,format='png',dpi=200)
  plt.close()

  print("Plot successfully written to: "+str(outfile))

