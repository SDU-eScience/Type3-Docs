Canceling Jobs
==============
You can cancel jobs with the ``scancel`` command.

To cancel a single job you can supply the ``jobid`` like so:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scancel <jobid>

You can cancel all jobs for the user ``testuser`` like so:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scancel -u <testuser>

With the -t option you can limit this to a particular ``JOB STATE CODE``. To cancel all jobs for user ``testuser`` with a ``JOB STATE CODE`` of ``PENDING``, use:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scancel -u <testuser> -t PENDING

For a full list of all available ``JOB STATE CODES`` please consult the manual of ``squeue`` with ``man squeue``:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man squeue

For additional information on how to use ``scancel`` please consult the appropriate manual with ``man``:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man scancel
