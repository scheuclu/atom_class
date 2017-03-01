#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np



#assuming the follwowing input format
#relative.py filename.txt columnindex

def relvariance_nparray(data):
    N=len(data)
    relvar = (1/N*sum(data*data)-pow(1/N*sum(data),2))/pow(1/N*sum(data),2)
    return relvar


if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Invalid syntax")
        sys.exit(-1)

    infile =sys.argv[1]
    colnum =int(sys.argv[2])

    data=np.loadtxt(infile, delimiter=' ', usecols=(colnum,), unpack=True, dtype=float)

    relvar = relvariance_nparray(data)

    print("\033[92mRelative variance of dataset: "+str(relvar)+"\033[00m")

    # write to outputfile if specified
    if len(sys.argv)==4:
        outfile=sys.argv[3]
        with open(outfile,'w') as f:
            f.write(str(relvar))



