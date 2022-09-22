.. |br| raw:: html

   <br>

Use of Intel MPI
===========================

When you compile a program on the system, you can choose to use the Intel Compiler and the associated Intel MPI implementation. These tools can be loaded via the `module system <../software/modules.html>`__:

.. code-block:: console

   [testuser@frontend ~]$ module load intel/2022a


When your program is compiled with Intel MPI you need to use the associated ``mpirun`` command to launch the program in your Slurm job script, instead of ``srun``. This is due to lack of proper PMIx support in Intel MPI, which is normally used by Slurm for launching MPI jobs. The following is an example of a job script that uses Intel MPI to launch a program.

.. code-block:: bash

   #!/bin/bash
   #SBATCH --nodes 2
   #SBATCH --ntasks-per-node 128
   #SBATCH --time 2:00:00

   module load intel/2022a
   mpirun /path/to/your_program [program options]
