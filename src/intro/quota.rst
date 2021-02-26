Resources
==================
All users and projects have associated quotas on resources, such as disk space and CPU time. Everyone can use the ``myquota`` command to get a simple overview of the resources they have available.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ myquota

   Account             Quota               Available           Used
   --------------------------------------------------------------------
   testproject         64512               64444               0.11%


   Filesystem          Quota               Available           Used
   --------------------------------------------------------------------
   /home/testuser      100 GB              96 GB               3.48%
   /work/testproject   25 TB               25 TB               0.00%


For each associated project, this command shows the number of core-hours available for computation, and the amount of disk space used in the project's work folder. All users will also have 100 GB of space in their personal home folder.
