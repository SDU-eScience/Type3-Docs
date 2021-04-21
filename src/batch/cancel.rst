.. |br| raw:: html

   <br>

Canceling Jobs
==============
You can cancel jobs with the ``scancel`` command.

To cancel a single job you can supply the ``jobid`` as the argument:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scancel <jobid>

|br|
You can cancel all jobs for the user ``testuser`` with the ``-u`` option:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scancel -u testuser

|br|
With the ``-t`` option you can limit this to a particular job state. To cancel all jobs for ``testuser`` with the job state ``PENDING``, simply use:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scancel -u testuser -t PENDING

|br|
For a full list of possible job states, please consult the manual:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man squeue

|br|
Similarly, for additional information on how to use ``scancel``, please consult the associated manual:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man scancel
