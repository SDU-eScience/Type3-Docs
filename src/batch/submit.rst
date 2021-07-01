.. |br| raw:: html

   <br>

Submit Jobs
===========
Jobs can be submitted with either one of the following commands: ``srun``, ``salloc`` or ``sbatch``.

This page will cover the basics of writing a job script and how to submit it with ``sbatch``.


Writing a job script
-----------------------
A minimal job script would look something like this:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --nodes 1                 # number of nodes
   #SBATCH --ntasks-per-node 1       # number of cores per node
   #SBATCH --time 2:00:00            # max time (HH:MM:SS)

   for i in {1..10000}; do
   echo $RANDOM >> random.txt
   done

   sort random.txt

|br|

* The first line is a shebang interpreter directive, in this case the interpreter is the *Bash* shell environment.
* After the shebang all sbatch directives are added. An sbatch directive begins with ``#SBATCH`` followed by the option you want to set. These options can be overridden at execution by supplying them directly to the ``sbatch`` command.
* If an additional ``#`` is prepended to the sbatch directive, it is ignored by Slurm.
* After the sbatch directives, the actual job code is added. This is the code that will be executed.
* For ease of use, write the content to a file that can be passed to ``sbatch`` (see `Submitting a job script <#submitting-a-job-script>`__ below - the examples assume the filename ``jobscript.sh``)

In the above example, the code appends the value of the ``$RANDOM`` variable into a textfile called ``random.txt``, it then prints them in order with the ``sort`` command.

.. note::

   On this system Slurm is configured to allow multiple simultaneous jobs on the same node. For example, if your job only needs 32 cores, then the remaining cores can be used to run another job at the same time. For this reason, make sure you correctly specify how many cores your job will need.


Useful directives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The list below describes some of the most commen directives used in a job script. For a more detailed list of options, look at the `official documentation <https://slurm.schedmd.com/sbatch.html>`__.

* Use ``--time`` to set the wall time. Setting the maximum wall time as low as possible will allow Slurm to schedule your job on idle nodes currently waiting for a larger job to start.
* Use ``--nodes`` to set the number of required nodes. If your job can be flexible, use a range of the number of nodes needed to run the job, such as ``--nodes=2-4``. In this case your job starts running when at least 2 nodes are available. If at that time 3 or 4 nodes are available, then your job gets all of them.
* Use ``--ntasks-per-node`` to define the number of necessary MPI processes, for example 128 if you want a single process per core.
* Use ``--mem`` to define how much memory is needed per node. By default you will be assigned 32 GB of memory per allocated core. Please do not request more than what is needed for the job to run.
* Use ``--account`` to define the resource billing account. When left unspecified, then your default account is used. For this reason, this option is only relevant if you are part of multiple projects.
* Use ``--exclusive`` to request exclusive access to the entire node. This will ensure that no other job is running on the node at the same time as your job. With this option you will be billed for the entire node, even if you are only using a subset of the cores.
* Use ``--requeue`` to automatically requeue the job if it either fails or is being preempted by a higher priority job.


Additional notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You do not need to specify any of the following in your job scripts:

* Partition: The default partition is automatically chosen when your job is submitted.


Scavenger jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The cluster is configured to allow so-called *scavenger* jobs to run free-of-charge when there are available resources. However, these jobs will be preempted (killed) as soon as a normal priority job needs the resources. To run a scavenger job add the following directive to your job script.

.. code-block:: bash

   #SBATCH --qos=scavenger

If you want to automatically reschedule your scavenger jobs upon preemption, use the ``--requeue`` directive described above.


MPI jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For MPI jobs you should use a combination of ``--nodes`` and ``--ntasks-per-node`` to get the number of nodes and MPI processes per node that you want. Both of these variables have a default value of one. If using Intel MPI, check `here <intelmpi.html>`__.

.. code-block:: bash

   #!/bin/bash
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

   [testuser@fe-ac-02 ~]$ sbatch jobscript.sh

|br|
To add additional options, or to override options specified in the job script, add the new values to sbatch command when submitting the job script.

In the following example, the ``--time`` option is passed to ``sbatch`` command when submitting the job. This will set the limit on the total run time of the job allocation to 4 hours.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ sbatch --time 4:00:00 jobscript.sh

|br|
For more information about ``sbatch`` and to see a full list of the available options, consult the manual.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man sbatch
