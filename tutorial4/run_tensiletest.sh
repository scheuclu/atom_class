#export LAMMPSBIN=/home/lscheuch/Downloads/lammps-17Nov16/src/lmp_mpi
#readarray -t timesteps < ./scriptinput/timesteps
#readarray -t dampvals < ./scriptinput/dampvals
#readarray -t numsteps < ./scriptinput/numsteps
#readarray -t translatevals < ./scriptinput/translatevals

CURDIR=$(pwd)

mpirun -np 2 ${LAMMPSBIN} < in.tensiletest

