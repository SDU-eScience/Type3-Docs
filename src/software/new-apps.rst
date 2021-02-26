.. |br| raw:: html

	<br>

.. |nbsp| unicode:: U+00A0

Install New Software
====================

New software can be installed using `EasyBuild <https://easybuild.io/>`__.

EasyBuild is a software build and installation framework written in Python, which allows to deploy and manage (scientific) applications on High Performance Computing systems. The `EasyBuild` module is load by default when the user access the front-end node:

.. code-block:: console

	$ module list

.. tip::

 Currently Loaded Modules:
  \1) EasyBuild/4.3.2


TODO: comment about easyconfig files. Easyconfig files are used to specify the version, dependencies and build parameters of the software.


Searching for software
----------------------

To search for preloaded easyconfig files, use the option ``--search`` (or ``-S``), for example:

.. code-block:: console

	$  eb -S '^Python-3.6.6-*'

.. tip::

 == found valid index for /opt/sys/easybuild/software/EasyBuild/4.3.2/easybuild/easyconfigs, so using it...
 CFGS1=/opt/sys/easybuild/software/EasyBuild/4.3.2/easybuild/easyconfigs/p/Python
 |br|
 |nbsp|\* $CFGS1/Python-3.6.6-foss-2018b.eb
 |br|
 |nbsp|\* $CFGS1/Python-3.6.6-fosscuda-2018b.eb
 |br|
 |nbsp|\* $CFGS1/Python-3.6.6-intel-2018b.eb
 |br|
 |nbsp|\* $CFGS1/Python-3.6.6-iomkl-2018b.eb

List of installed toolchains
----------------------------

Installing software
-------------------

It is possible to check all the dependencies defined in a particular software easyconfig file by executing the eb command with the option ``--dry-run`` (or ``-D``). For example:

.. code-block:: console

	$ eb GROMACS-2018-foss-2018a.eb -D

.. tip::

 ...

Further reading
---------------

- `EasyBuild user guide <https://docs.easybuild.io/en/latest/>`__