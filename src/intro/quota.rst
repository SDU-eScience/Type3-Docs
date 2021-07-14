.. |myquota| raw:: html

   <br>
   Account &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quota &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Available &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Used
   <br>
   --------------------------------------------------------------------
   <br>
   testproject &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 64512 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 64444 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.11%
   <br>
   <br>
   Filesystem &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Quota &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Available &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Used
   <br>
   --------------------------------------------------------------------
   <br>
   /home/testuser &nbsp;&nbsp;&nbsp;&nbsp; 100 GB &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 96 GB &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.48%
   <br>
   /work/testproject &nbsp; 25 TB &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 25 TB &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.00%



Resources
==================
All users and projects have associated quotas on resources, such as disk space and CPU time. Everyone can use the ``myquota`` command to get a simple overview of the resources they have available.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ myquota

.. tip::

 |myquota|


For each associated project, this command shows the number of core-hours available for computation, and the amount of disk space used in the project's work folder.

When appending the ``-l`` option to the command, it will show (in percentage) how many core-hours each user in the project has consumed. This is primarily useful for PIs to keep track of how the resources are being spent.

.. note::

	All users will have 100 GB of space in their personal home folder.
