Canceling Jobs
==============
You can cancel jobs with the ``scancel`` command.

To cancel a single job you can supply the ``<jobid>`` as the argument:

.. code-block:: console

   [user@frontend ~]$ scancel <jobid>

You can cancel all jobs for the user ``<user>`` with the ``-u`` option:

.. code-block:: console

   [user@frontend ~]$ scancel -u <user>

With the ``-t`` option you can limit this to a particular job state. To cancel all jobs for ``<user>`` with the job state ``PENDING``, simply use:

.. code-block:: console

   [user@frontend ~]$ scancel -u <user> -t PENDING

For a full list of possible job states, please consult the manual:

.. code-block:: console

   [user@frontend ~]$ man squeue

Similarly, for additional information on how to use ``scancel``, please consult the associated manual:

.. code-block:: console

   [user@frontend ~]$ man scancel
