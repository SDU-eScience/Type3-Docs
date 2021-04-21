.. |br| raw:: html

   <br>

Use of Intel MPI
===========================

When you compile a program on the system, you can choose to use the Intel Compiler and the associated Intel MPI implementation. These tools can be loaded via the `module system <../software/modules.html>`__:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ module load intel/2020b

|br|
When your program is compiled with Intel MPI you need to use the associated ``mpirun`` command to launch the program in your Slurm submit scripts instead of ``srun``. This is due to lack of proper integration between Intel MPI and Slurm in our system. The following is an example of a submit script that uses Intel MPI to launch a program.

.. code-block:: bash

   #!/bin/bash
   #SBATCH -N 1 -n 64
   #SBATCH -p fat
   #SBATCH -t 01:00:00

   module load intel/2020b
   mpirun /path/to/your_program [program options]
