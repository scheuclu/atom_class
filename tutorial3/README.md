# Tutorial 2
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

The simulation series is scripted and runs automatically when calling [./run_equi_mcmc.sh](./run_equi_mcmc.sh).
The siumlation series parameters are specified via the files in [./scriptinput](./scriptinput).

The turorial is organized in the following folder
### [./logfiles](./logfiles)
Directory where all the LAMMPS logfiles are written to.

### [./results](./results)
All the data-files that are extracted from log-files are stores here.

### [./plots](./plots)
All the plots, created from the data-files in results are stored here.

### [./scriptinput](./scriptinput)
Contains the files that controll the simulation series parameters.

## Files

### [./run_equi_mcmc.sh](./run_equi_mcmc.sh)
Runs all the simulations. For my purpose, all simulations are submitted as batchjobs to a cluster. You probably need to change that one line in order to run in locally on your machine.

### [./postprocess_equi_gcmc.sh](./posprocess_equi_gcmc.sh)
Does all the postprocessing. In particular, the following plot series are created:

#### [./plots/gcmc](./plots/gcmc)
Contains time equilibrium plots of all qunatities for all trail-step sizes and all damping paramters. This folder does not contain anay comparative plots

#### [./plots/gcmc_dampstudy](./plots/gcmc_dampstudy)
Compairs equilibriation for different damping parameters in one plot.

#### [./plots/autocov](./plots/autocov)
Shows the autocovariance of all quantities over time.

