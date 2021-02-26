Submit Jobs
===========
Jobs can be submitted either with of the following commands: ``srun``, ``salloc`` or ``sbatch``

This page will cover the basics of writing a job script and how to submit it with ``sbatch``.

Writing a job script
-----------------------

A minimal job script would look something like this:

.. code-block:: console

   #!/bin/bash
   #SBATCH --account test00_gpu      # account
   #SBATCH --nodes 1                 # number of nodes
   #SBATCH --time 2:00:00            # max time (HH:MM:SS)

   for i in {1..10000}; do
   echo $RANDOM >> random.txt
   done

   sort random.txt

* The first line is a shebang interpreter directive, in this case the interpreter is the ``Bash shell``.
* After the shebang any sbatch directives are added. An sbatch directive begins with ``#SBATCH`` followed by the option you want to set. These options can be overriden at execution by supplying them directly to the ``sbatch`` command.
* If an additional ``#`` is prepended to the sbatch directive, it is ignored by Slurm.
* After the sbatch directives, the actual job code is added. This is the code that will be executed.
* For ease of use, write the content to a file that can be passed to ``sbatch`` (see 'Submitting a job script with sbatch' below - the examples assume the filename '``jobscript.sh``')

In the above example, the code appends the value of the $RANDOM variable into a textfile called random.txt, it then prints them in order with the ``sort`` command.

Job script tips
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Walltime --time: Set the maximum wall time as low as possible enables Slurm to possibly pack your job on idle nodes currently waiting for a large job to start.
* Nodes --nodes: If your job can be flexible, use a range of the number of nodes needed to run the job, e.g.--nodes=2-4. In this case your job starts running when at least 2 nodes are available. If at that time 3 or 4 nodes are available, your job gets all of them.
* Tasks per node, --ntasks-per-node: Use this to select how many MPI ranks you want per node, e.g., 128 if you want one rank per cpu core

Additional notes for job scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You do not need to specify any of the following in your job scripts:

* Partition: The partition is automatically derived from the account you use, e.g., test00_fat implies the partition fat.
* Memory use, e.g., --mem or --mem-per-spu: By default you get all the RAM on the nodes you are running.

Submitting a job script with sbatch
------------------------------------
You can submit a job script with the ``sbatch`` command like so:

.. code-block:: console

   [user@fe-ac-02 ~]$ sbatch jobscript.sh

To add additional options, or to override options specified in the job script, add the new values to sbatch when submitting the job script.

In the below example, the ``--time`` option is passed to ``sbatch`` when submitting the job, setting the limit on the total run time of the job allocation to 4 hours:

.. code-block:: console

   [user@fe-ac-02 ~]$ sbatch --time 4:00:00 jobscript.sh

For more information about ``sbatch`` and to see a list of all the available options, use the ``man`` command:

.. code-block:: console

   [user@fe-ac-02 ~]$ man sbatch
