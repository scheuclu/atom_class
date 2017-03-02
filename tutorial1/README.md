# Tutorial 1
[up directory](../README.md)
## Usage
In order to use this scripts, please set the following environment variables:
### LAMMPSBIN
Pointing to your lmp_mpi binary
### LOG2TXT
Pointing to log2txt.py from the LAMMPS/tools folder

You can set an environment variable like this:
```{r, engine='bash', count_lines}
export LAMMPSBIN=/home/scheuclu/programs/lammps/src/lmp_mpi
export LOG2TXT=/home/scheuclu/programs/lammps/tools/python/log2txt.py
```
Make sure a working version of Python 2.x is installed on your system.

## Structure

This directory contains the LAMMPS input files. For the equilibriation tasks, where many diffrerent parameter combinations have to be run, the inputfiles are templated. Shell scripts thatn loop over different values for timestep and damping parameters and create actual input files with them, that are then run with lammps.

### [./scriptinput](./scriptinput)
Contains the files [dampvals](./scriptinput/dampvals), [numsteps](./scriptinput/numsteps), [numsteps](./scriptinput/numsteps) and [outfreqs](./scriptinput/outfreqs)
```diff
- These files control the automatic input file generation. If you want to used different parameters for timestep, dampin-values, etc., just change these files and re-run the run-scripts.
```


### [./logfiles](logfiles)
Contains all log-files from all LAMMPS runs. In particular it contains a seperate logfile for each timestep damping-parameter combination.

### [./results](results)
The postprocess scripts run over the logfiles and extract data that will be plotted. This extractionis done via log2txt.py from the LAMMPS tools library. Each extracted dataset will be stored in this folder.

### [./plots](plots)
This folder contains the .png-plots created by postprocess.sh
In particular, the following subfolder exist:

####   [./plots/NVT](./plots/NVT)
Contains the convergence plots of all thmermodynamic properties over time in the NVT ensemble.
####   [./plots/Ber](./plots/NVT)
Contains the convergence plots of all thmermodynamic properties over time with the Berendesen thermostat.
####   [./plots/dampstudy](./plots/dampstudy)
Contains plots of the dependence of convergence properties on the damping parameter for all thmermodynamic properties.
####   [./plots/NVTvsBer](./plots/NVTvsBer)
Contains plots that directly compare the convergence of NVT vs Berendsen for all thermodynamic properties.
####   [./plots/syssize](./plots/syssize)
Contains plots that anaylze the dependency of the relaive varaince with respect to the system size for all quantities of interest.

####   [./plots/NPT](./plots/NPT)
Contains the convergence plots for the NPT ensemble. at constant pressure at temperature.


## Files

### [./clean.sh](./clean.sh)
Removes all output and postprocessing files from previous runs.

### [./run_minimize.sh](./run_minimize.sh)
Runs the minimization process to determine the lattice constant. The result value is printed to the terminel in green.

### [./run_NVT.sh](run_NVT.sh)
Runs the Equilibrium with NVT ensemble. The script automatically loops over different values for the timestep and the damping parameter. For each run, a seperate logfile is writtten to [logfiles](./logfiles), and dump is stored to [dump](dump).

### [./run_Ber.sh](run_Ber.sh)
Runs the Equilibrium with Berendesen thermostat and NVE ensemle. The script automatically loops over different values for the timestep and the damping parameter. For each run, a seperate logfile is writtten to [logfiles](./logfiles), and dump is stored to [dump](dump).

### [./run_syssize.sh](run_syssize.sh)
Performs equilibrium simulations with NVT ensemble for all the problem sizes(cell numbers per direction) specified in [./scriptinput/cellnums](./scriptinput/cellnums). The atom-numbers corresponding to that system size are stores in [./scriptinput/cellnums2atoms](./scriptinput/cellnums2atoms).
The results are stored in logfiles.

### [./postprocess_NVT.sh](postprocess_NVT.sh)
Loops over all the input-files created by the run script for the NVT ensemble, and creates a plot of every possible quatity in that logfile plotted  over simulation time. Every plottitle contains the relative variance of that data.
The plots are stored in [./plots/NVT](./plots/NVT)

### [./postprocess_Ber.sh](postprocess_Ber.sh)
Loops over all the input-files created by the run script for the Ber ensemble, and creates a plot of every possible quatity in that logfile plotted  over simulation time. Every plottitle contains the relative variance of that data.
The plots are stores in [./plots/Ber](./plots/Ber)

### [./postprocess_NVT_vs_Ber.sh](./postprocess_NVT_vs_Ber.sh)
Creates plots that directly compare the convergence in time between NVT and Berendese/NVE. The plots are written to [./plots/NVTvsBer](./plots/NVTvsBer).

### [./postprocess_syssize.sh](./postprocess_syssize.sh)
Creates plots plots that show the dependence on the relative variance of all thermodynamic quantities with respect to system size(# of atoms).
The results are stored in [./plots/syssize](./plots/syssize)


### [./postprocess_NPT.sh](./postprocess_NPT.sh)
Creates the plots for the MD-NPT equilibrium.
Plots are stores in [./plots/NPT](./plots/NPT)

