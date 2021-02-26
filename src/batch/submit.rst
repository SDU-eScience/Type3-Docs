Submit Jobs
===========
Jobs can be submitted with either one of the following commands: ``srun``, ``salloc`` or ``sbatch``.

This page will cover the basics of writing a job script and how to submit it with ``sbatch``.


Writing a job script
-----------------------
A minimal job script would look something like this:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --account myaccount       # account
   #SBATCH --nodes 1                 # number of nodes
   #SBATCH --time 2:00:00            # max time (HH:MM:SS)

   for i in {1..10000}; do
   echo $RANDOM >> random.txt
   done

   sort random.txt

* The first line is a shebang interpreter directive, in this case the interpreter is the *Bash* shell environment.
* After the shebang any sbatch directives are added. An sbatch directive begins with ``#SBATCH`` followed by the option you want to set. These options can be overriden at execution by supplying them directly to the ``sbatch`` command.
* If an additional ``#`` is prepended to the sbatch directive, it is ignored by Slurm.
* After the sbatch directives, the actual job code is added. This is the code that will be executed.
* For ease of use, write the content to a file that can be passed to ``sbatch`` (see 'Submitting a job script with sbatch' below - the examples assume the filename '``jobscript.sh``')

In the above example, the code appends the value of the $RANDOM variable into a textfile called random.txt, it then prints them in order with the ``sort`` command.


Job script tips
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Use ``--time`` to set the wall time. Setting the maximum wall time as low as possible will allow Slurm to schedule your job on idle nodes currently waiting for a larger job to start.
* Use ``--nodes`` to set the number of required nodes. If your job can be flexible, use a range of the number of nodes needed to run the job, such as ``--nodes=2-4``. In this case your job starts running when at least 2 nodes are available. If at that time 3 or 4 nodes are available, then your job gets all of them.
* Use ``--ntasks-per-node`` to define the number of necessary MPI processes, for example 128 if you want a single process per core.


Additional notes for job scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You do not need to specify any of the following in your job scripts:

* Partition: The default partition is automatically chosen from your associated slurm account.
* Memory: By default you get all the memory on the nodes you are using.


MPI jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For MPI jobs you should use a combination of ``--nodes`` and ``--ntasks-per-node`` to get the number of nodes and MPI processes per node that you want. Both of these variables have a default value of one. If using Intel MPI, see the relevant section in the menu.

.. code-block:: bash

   #!/bin/bash
   #SBATCH --account myaccount       # account
   #SBATCH --nodes 2                 # number of nodes
   #SBATCH --ntasks-per-node 128     # number of MPI tasks per node
   #SBATCH --time 2:00:00            # max time (HH:MM:SS)

   echo Running on "$(hostname)"
   echo Available nodes: "$SLURM_NODELIST"
   echo Slurm_submit_dir: "$SLURM_SUBMIT_DIR"
   echo Start time: "$(date)"

   # Load the modules used when compiling the application
   module purge
   module load foss/2020a

   # Start a total of 2*128 MPI processes
   srun my-mpi-application -i input.txt -o output.txt

   echo Done.


Submitting a job script
--------------------------------
You can submit a job script with the ``sbatch`` command like this:

.. code-block:: console

   [user@fe-ac-02 ~]$ sbatch jobscript.sh

To add additional options, or to override options specified in the job script, add the new values to sbatch command when submitting the job script.

In the example below, the ``--time`` option is passed to ``sbatch`` command when submitting the job. This will set the limit on the total run time of the job allocation to 4 hours.

.. code-block:: console

   [user@fe-ac-02 ~]$ sbatch --time 4:00:00 jobscript.sh

For more information about ``sbatch`` and to see a full list of the available options, use the ``man`` pages.

.. code-block:: console

   [user@fe-ac-02 ~]$ man sbatch
