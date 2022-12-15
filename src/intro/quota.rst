Resources
==================
All users and projects have associated quotas on resources, such as disk space and CPU time. Everyone can use the ``myquota`` command to get a simple overview of the resources they have available.

.. code-block:: console

	[testuser@frontend ~]$ myquota

.. tip::

	Account                     Quota               Available           Used
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	testproject                 64512               62842               2.59%


	Filesystem                  Quota               Available           Used
	\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
	/home/testuser              100 GiB             93 GiB              6.57%
	/work/testproject           25 TiB              24 TiB              0.00%


For each associated project, this command shows the number of core-hours available for computation, and the amount of disk space used in the project's work folder.

When appending the ``-l`` option to the command, it will show (in percentage) how many core-hours each user in the project has consumed. This is primarily useful for PIs to keep track of how the resources are being spent.

.. note::

	All users will have 100 GB of space in their personal home folder.

Default project
------------------
If you are part of multiple projects you can use the interactive command ``set_default_project`` to select the default project used when when submitting Slurm jobs.

.. code-block:: console

	[testuser@frontend ~]$ set_default_project

.. tip::
	You are part of the following projects:

	\1. project1                    (default)
	\2. project2

	Select new default project (1): 2
	Setting new default project: project2
