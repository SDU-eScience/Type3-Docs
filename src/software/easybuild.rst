.. |nbsp| unicode:: U+00A0

Easybuild
=========

All compilers, libraries and software available on the system are installed and configured with `EasyBuild <https://easybuild.io/>`__.

EasyBuild is a software build and installation framework written in Python, which allows to deploy and manage several scientific applications and tools on HPC systems.

The EasyBuild module is loaded by default when the user accesses the frontend node.

.. code-block:: console

	[testuser@frontend ~]$ module list

.. tip::

	Currently Loaded Modules:
	|nbsp| |nbsp|\1) EasyBuild/4.3.2


The dependencies and build parameters of each software release are specified in the corresponding EasyBuild `easyconfigs files <https://github.com/easybuilders/easybuild-easyconfigs>`__.

Searching for software
----------------------

To search for all available easyconfig files, use the option ``--search`` (or ``-S``). For example:

.. code-block:: console

	[testuser@frontend ~]$ eb -S '^Python-3.6.6'

.. tip::
	CFGS1=/opt/sys/easybuild-easyconfigs/easybuild/easyconfigs/p/Python
	* $CFGS1/Python-3.6.6-foss-2018b.eb
	* $CFGS1/Python-3.6.6-fosscuda-2018b.eb
	* $CFGS1/Python-3.6.6-intel-2018b.eb
	* $CFGS1/Python-3.6.6-iomkl-2018b.eb


Each file specifies the installation parameters for a particular `compiler toolchain <compilers.html>`__.


Installing new software
-----------------------

The ``eb`` command is used to install new software from the corresponding easyconfig file.
To check the software dependencies, run the ``eb`` command with the option ``--dry-run`` (or ``-D``). For example:

.. code-block:: console

	[testuser@frontend ~]$ eb Python-3.8.6-GCCcore-10.2.0.eb -D

.. tip::

	== temporary log file in case of crash /tmp/eb-9rE3Ix/easybuild-yWJqtE.log
	== found valid index for /opt/sys/easybuild/software/EasyBuild/4.3.2/easybuild/easyconfigs, so using it...
	== found valid index for /opt/sys/easybuild/software/EasyBuild/4.3.2/easybuild/easyconfigs, so using it...
	Dry run: printing build status of easyconfigs and dependencies
	CFGS=/opt/sys/easybuild/software/EasyBuild/4.3.2/easybuild/easyconfigs
	|nbsp|\* [x] $CFGS/m/M4/M4-1.4.18.eb (module: M4/1.4.18)
	|nbsp|\* [x] $CFGS/b/Bison/Bison-3.7.1.eb (module: Bison/3.7.1)
	|nbsp|\* [x] $CFGS/b/Bison/Bison-3.3.2.eb (module: Bison/3.3.2)
	|nbsp|\* [x] $CFGS/z/zlib/zlib-1.2.11.eb (module: zlib/1.2.11)
	|nbsp|\* [x] $CFGS/h/help2man/help2man-1.47.4.eb (module: help2man/1.47.4)
	|nbsp|\* [x] $CFGS/f/flex/flex-2.6.4.eb (module: flex/2.6.4)
	|nbsp|\* [x] $CFGS/b/binutils/binutils-2.35.eb (module: binutils/2.35)
	|nbsp|\* [x] $CFGS/g/GCCcore/GCCcore-10.2.0.eb (module: GCCcore/10.2.0)
	...
	|nbsp|\* [ ] $CFGS/g/GMP/GMP-6.2.0-GCCcore-10.2.0.eb (module: GMP/6.2.0-GCCcore-10.2.0)
	|nbsp|\* [ ] $CFGS/p/Python/Python-3.8.6-GCCcore-10.2.0.eb (module: Python/3.8.6-GCCcore-10.2.0)
	== Temporary log file(s) /tmp/eb-9rE3Ix/easybuild-yWJqtE.log* have been removed.
	== Temporary directory /tmp/eb-9rE3Ix has been removed.

All the dependencies marked with ``[x]`` are already installed on the system and can be loaded with the corresponding module.

The software and the missing dependencies can be installed using the option ``--robot`` (or ``-r``):

.. code-block:: console

	[testuser@frontend ~]$ eb Python-3.8.6-GCCcore-10.2.0.eb -r

The additional option ``--debug`` (or ``-d``) can be used to enable debug log mode. More options are reported `here <https://docs.easybuild.io/en/latest/version-specific/help.html>`__.

By default EasyBuild will install the software in ``$HOME/easybuild/software`` and the corresponding module file in ``$HOME/easybuild/modules/all``. The path of the module file is automatically added to ``$MODULEPATH``, once the EasyBuild module is loaded.

The user can also specify a different installation path for a particular software and the corresponding module using the option ``--installpath`` (or, more specifically,  ``--installpath-software`` and ``--installpath-modules``). In this case the new module path must be added with the command:  ``module use <new_module_path>``.

An overview of the default EasyBuild configuration settings can be displayed with the command:

.. code-block:: console

	[testuser@frontend ~]$ eb --show-config

.. tip::

	#
	# Current EasyBuild configuration
	# (C: command line argument, D: default value, E: environment variable, F: configuration file)
	#
	buildpath      (E) = /home/testuser/easybuild/build
	containerpath  (E) = /home/testuser/easybuild/containers
	installpath    (E) = /home/testuser/easybuild
	packagepath    (E) = /home/testuser/easybuild/packages
	prefix         (E) = /home/testuser/easybuild
	repositorypath (E) = /home/testuser/easybuild/ebfiles_repo
	robot-paths    (E) = /opt/sys/easybuild-easyconfigs/easybuild/easyconfigs
	sourcepath     (E) = /home/testuser/easybuild/sources


Further reading
---------------

- `EasyBuild user guide <https://docs.easybuild.io/en/latest/>`__
