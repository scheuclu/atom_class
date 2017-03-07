#!/usr/bin/python3
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import sys
import numpy as np

sys.path.append("../../")

from relative_variance import relvariance_nparray
from relative_variance import cut_nparray



#assuming the follwowing input format
#plot_syssize_dependence.py filename.txt filename.png xname yname plottitle

if __name__ == "__main__":

    Nb = 6.022*pow(10,23)
    kb = 1.38065*pow(10,-26) #[KJ/K]
    m  = 0.083798*5324/Nb
    infile_E = './results/CV/NVT_TotEng.txt'
    infile_T = './results/CV/NVT_Temp.txt'


    Evals = np.loadtxt(infile_E, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    Evals = cut_nparray(Evals)

    Tvals = np.loadtxt(infile_T, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    Tvals = cut_nparray(Tvals)

    Evals=Evals*5324/(Nb)*4.184*0.0837 #conversion to KJoule

    Eavg=np.average(Evals)
    Tavg=np.average(Tvals)

    Cv=(np.average(Evals*Evals)-Eavg*Eavg)/(kb*Tavg*Tavg)
    print("Cv = "+str(Cv))



    
    infile_Ep = './results/CV/NVT_plus_TotEng.txt'
    infile_Em = './results/CV/NVT_minus_TotEng.txt'
    infile_Tp = './results/CV/NVT_plus_Temp.txt'
    infile_Tm = './results/CV/NVT_minus_Temp.txt'


    Evalsp = np.loadtxt(infile_Ep, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    Evalsp = cut_nparray(Evalsp)

    Evalsm = np.loadtxt(infile_Em, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    Evalsm = cut_nparray(Evalsm)

    Tvalsp = np.loadtxt(infile_Tp, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    Tvalsp = cut_nparray(Tvalsp)

    Tvalsm = np.loadtxt(infile_Tm, delimiter=' ', usecols=(1,), unpack=True, dtype=float)
    Tvalsm = cut_nparray(Tvalsm)


    Eavgm=np.average(Evalsm)
    Eavgp=np.average(Evalsp)
    Tavgm=np.average(Tvalsm)
    Tavgp=np.average(Tvalsp)
    print(Eavgp)
    print(Eavgm)
    print(Tavgp)
    print(Tavgm)


    print("Cv_fd ="+str((Eavgp-Eavgm)/(Tavgp-Tavgm)*4.19/0.083798*1/5324))

