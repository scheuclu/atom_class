
#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.path.append("../../")

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray


def red_ydata(ydata,boxsize,quantity):
    N=2048
    V=boxsize*boxsize*boxsize
    sigma=3.65
    if quantity=='Density':
        return ydata*N/V*pow(sigma,3)
    else:
        return ydata

def print_red(temprange,outdir):
    print("asdasd")
    sys.exit(-1)
    kb=1.380648e-26#[kJ/K]
    eps=0.3228
    outfile = outdir+'/red_'+quantity+'.png'
    values = []
    temperatures = [t*kb/eps for t in temprange]
    print(temperatures)
    for temp in temperatures:
        infile = './results/phasetrans/temp'+str(temp)+'_Density.txt'
        print(infile)
        time  = np.loadtxt(infile, delimiter=' ', usecols=(0,), unpack=True, dtype=float)
        ydata = np.loadtxt(infile, delimiter=' ', usecols=(1,), unpack=True, dtype=float)

        Lxdata = np.loadtxt(infileLx, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
        boxsize = np.average(cut_nparray(Lxdata))

        # ydatared=red_ydata(ydata,boxsize,quantity)
        ydatared=ydata
        ydataredavg=np.average(cut_nparray(ydatared))
        values.append(ydatared)

    plt.plot(temperatures,values,'-o')
    plt.xlabel('Reduced temperature')
    plt.ylabel('Reduced Density')
    print("\033[92m"+outfile+"\033[00m\n")
    plt.savefig(outfile,format='png')
    plt.close()
    return;


if __name__ == "__main__":
    print_red('./plots/phasetrans',range(26,231,1) )
    print_red('./plots/phasetrans/detail1',range(125,140,1) )
    print_red('./plots/phasetrans/detail2',range(174,182,1) )
