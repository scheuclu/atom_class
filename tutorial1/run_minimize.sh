LAMMPS=/home/lscheuch/Downloads/lammps-17Nov16/src/lmp_mpi


$LAMMPS < in.argon.equilibrium

#greping the result file for the lattice constant
printf "\033[92m"
grep -E 'Lattice constant \(Angstroms\) = [-+]?[0-9]+\.?[0-9]+' log.argon.equilibrium |xargs echo
printf "\033[00m"
