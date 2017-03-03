#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plotsimple.py filename1.txt filename2.txt plotfilename.png xname yname data1name data2name plottitle

if __name__ == "__main__":
  if len(sys.argv)!=11:
      print("Invalid syntax")
      sys.exit(-1)

  infile1 =sys.argv[1]
  infile2 =sys.argv[2]
  infile3 =sys.argv[3]
  outfile=sys.argv[4]
  nameX  =sys.argv[5]
  nameY  =sys.argv[6]
  name1  =sys.argv[7]
  name2  =sys.argv[8]
  name3  =sys.argv[9]
  title  =sys.argv[10]

  data1  = np.genfromtxt(infile1,  delimiter=' ',
          skip_header=0,skip_footer=0,names=[nameX,nameY])
  data2  = np.genfromtxt(infile2,  delimiter=' ',
          skip_header=0,skip_footer=0,names=[nameX,nameY])
  data3  = np.genfromtxt(infile3,  delimiter=' ',
          skip_header=0,skip_footer=0,names=[nameX,nameY])
  xdata1 =data1[nameX]
  xdata2 =data2[nameX]
  xdata3 =data3[nameX]
  ydata1=data1[nameY]
  ydata2=data2[nameY]
  ydata3=data3[nameY]

  ydata1_avg=np.average(cut_nparray(ydata1))
  ydata2_avg=np.average(cut_nparray(ydata2))
  ydata3_avg=np.average(cut_nparray(ydata3))

  relvar1=relvariance_nparray(cut_nparray(ydata1))
  relvar2=relvariance_nparray(cut_nparray(ydata2))
  relvar3=relvariance_nparray(cut_nparray(ydata3))
  
  plt.plot(xdata1,ydata1,'r',label=name1+" (rel. var.: "+"{:.2E}".format(relvar1)+", avg="+"{:.2E}".format(ydata1_avg)+")")
  plt.plot(xdata2,ydata2,'g',label=name2+" (rel. var.: "+"{:.2E}".format(relvar2)+", avg="+"{:.2E}".format(ydata2_avg)+")")
  plt.plot(xdata3,ydata3,'b',label=name3+" (rel. var.: "+"{:.2E}".format(relvar3)+", avg="+"{:.2E}".format(ydata3_avg)+")")
  plt.plot(xdata1,ydata1*0+ydata1_avg,'r')
  plt.plot(xdata2,ydata2*0+ydata2_avg,'g')
  plt.plot(xdata3,ydata3*0+ydata3_avg,'b')
  plt.xlabel(nameX)
  plt.ylabel(nameY)
  plt.legend(loc = 'lower right',fontsize=10)

  plt.title(title)

  plt.savefig(outfile,format='png',dpi=200)
  plt.close()

  print("Plot successfully written to: "+str(outfile))

