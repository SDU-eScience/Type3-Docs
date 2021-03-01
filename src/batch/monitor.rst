Monitor Jobs
============
You can monitor your jobs with the ``squeue`` and ``scontrol`` commands.

Listing jobs
-------------------------
You can list all jobs for ``testuser`` like this:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ squeue -u testuser

The ``-t`` option will allow you to filter which jobs are listed by their job state code. Examples of states are ``RUNNING`` and ``PENDING`` and they can be used like this:

.. code-block:: console

   [testuser@fe-ac-02 ~]$ squeue -u <testuser> -t RUNNING
   [testuser@fe-ac-02 ~]$ squeue -u <testuser> -t PENDING

For a full list of possible job states, please consult the manual.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man squeue

List detailed job information
--------------------------------------------
The ``scontrol`` command can be used to show detailed job information.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ scontrol show jobid -dd <jobid>

This information could be valuable when troubleshooting. For additional information, please consult the manual.

.. code-block:: console

   [testuser@fe-ac-02 ~]$ man scontrol

Below is an example from the manual of a detailed job description as returned by ``scontrol``.

.. code-block:: text

   JobId=71701 Name=hostname
             UserId=da(1000) GroupId=da(1000)
             Priority=66264 Account=none QOS=normal WCKey=*123
             JobState=COMPLETED Reason=None Dependency=(null)
             TimeLimit=UNLIMITED Requeue=1 Restarts=0 BatchFlag=0 ExitCode=0:0
             SubmitTime=2010-01-05T10:58:40 EligibleTime=2010-01-05T10:58:40
             StartTime=2010-01-05T10:58:40 EndTime=2010-01-05T10:58:40
             SuspendTime=None SecsPreSuspend=0
             Partition=debug AllocNode:Sid=snowflake:4702
             ReqNodeList=(null) ExcNodeList=(null)
             NodeList=snowflake0
             NumNodes=1 NumCPUs=10 CPUs/Task=2 ReqS:C:T=1:1:1
             MinCPUsNode=2 MinMemoryNode=0 MinTmpDiskNode=0
             Features=(null) Reservation=(null)
             OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
