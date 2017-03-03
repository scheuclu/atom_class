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

TODO
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


