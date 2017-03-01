# Atomistic modeling of materials
This repository holds all lecture, exercise and exam materials for the "Atomistic Modeling of Materials" class at TU-Munich.
## Usage
In order to use this scripts, please set the following environment variables:
### LAMMPSBIN
Pointing to your lmp_mpi binary
### LOG2TXT
Pointing to log2txt.py from the LAMMPS/tools folder

You can set an environment variable like this:
```{r, engine='bash', count_lines}
export LAMMPSBIN=/home/scheuclu/programs/lammps/src/lmp_mpi
export LOG@TXT=/home/scheuclu/programs/lammps/tools/python/log2txt.py
```
Make sure a working version of Python 2.x is installed on your system.

## Structure
Just like the the class, the repository is oragnized in the folders [lecture](lecture), [exercise](exercise), tutorials[1](tutorial1) [2](tutorial2) [3](tutorial3) [4](tutorial4).

Additionally, folder [exam](exam) holds all input-data and results used for the exam, folder [report](report) stores the final report written in LaTeX.

## Contents of Tutorials

### [Tutorial 1](tutorial1/README.md)
### [Tutorial 2](tutorial2/README.md)
### [Tutorial 3](tutorial3/README.md)
### [Tutorial 4](tutorial4/README.md)

