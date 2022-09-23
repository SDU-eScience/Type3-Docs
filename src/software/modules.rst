.. |dash-line| raw:: html

	<hr class="dash" align="left">

.. |nbsp| unicode:: U+00A0


Modules System
==============

Multiple versions of the same software are accessible using the `Lmod <https://www.tacc.utexas.edu/research-development/tacc-projects/lmod>`__ environment module system.

The module system makes it easy to specify which version you want to use and keeps everything consistent. There are also circumstances where one software program will have some environment setting or file that conflicts with a different program, and in many cases the module system can also help solve this problem.

Access modules
--------------

Most software packages available on the system can be found as a module. To see a list of available software run the command:

.. code-block:: console

	[testuser@frontend ~]$ module spider

.. tip::

	|dash-line| The following is a list of the modules and extensions currently available: |dash-line|

	Autoconf: Autoconf/2.69-GCCcore-10.2.0
	  Autoconf is an extensible package of M4 macros that produce shell scripts to automatically configure software source code packages. These scripts can adapt the packages to many kinds of
	  UNIX-like systems without manual user intervention. Autoconf creates a configuration script for a package from a template file that lists the operating system features that the package can
	  use, in the form of M4 macro calls.
	Automake: Automake/1.16.2-GCCcore-10.2.0
	  Automake: GNU Standards-compliant Makefile generator
	Autotools: Autotools/20200321-GCCcore-10.2.0
	  This bundle collect the standard GNU build tools: Autoconf, Automake and libtool

	|dash-line|

	To learn more about a package execute:

	$ module spider Foo

	where "Foo" is the name of a module.

	To find detailed information about a particular package you
	must specify the version if there is more than one version:

	$ module spider Foo/11.1

	|dash-line|

Note that the above list is not updated automatically. To get an updated list, rerun the command on the frontend node.
You can optionally specify a module name, and it will show you all available versions of module package, as shown in the example above.

.. note::

	You can also use the command ``module avail`` to get the list of available packages in a different format.

Load a module
-------------

To load a module, use the command: ``module load <module_name>``. The default version will automatically be loaded.

If you want a particular version, use instead: ``module load <module_name>/<module_version>``. For example:

.. code-block:: console

	[testuser@frontend ~]$ module list

.. tip::

	No modules loaded

.. code-block:: console

	[testuser@frontend ~]$ module load GCCcore/10.2.0

.. tip::

	Currently Loaded Modules:
	|nbsp| |nbsp|\1) GCCcore/10.2.0

Check active modules
--------------------

You can print the list of currently loaded modules with the command:

.. code-block:: console

	[testuser@frontend ~]$ module list


Unload a module
---------------

To unload a module, use the command: ``module unload <module_name>``. This command will automatically unload all the dependencies as well.

To unload everything, use:

.. code-block:: console

  [testuser@frontend ~]$ module purge

..
	Show hidden modules
	-------------------

	To make the module overview simpler, by default a lot of modules are hidden. The hidden modules are mostly libraries and dependencies that rarely are needed on their own. To also show the hidden modules, add the ``--show-hidden`` option to the ``module`` command.

	.. code-block:: console

	[testuser@frontend ~]$ module --show-hidden avail

Examine a module file
---------------------

If you want to see what the ``module`` command is doing to your environment, you can run ``module show <module_name>/<module_version>``. For example:

.. code-block:: console

	[testuser@frontend ~]$ module show GCCcore/11.3.0

.. tip::

	|dash-line| /opt/sys/easybuild/modules/all/Core/GCCcore/11.3.0.lua: |dash-line|

	help([[
	Description
	\===========
	The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
	as well as libraries for these languages (libstdc++, libgcj,...).

	More information
	\================
	\- Homepage: https://gcc.gnu.org/
	]])
	whatis("Description: The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
	as well as libraries for these languages (libstdc++, libgcj,...).")
	whatis("Homepage: https://gcc.gnu.org/")
	whatis("URL: https://gcc.gnu.org/")
	conflict("GCCcore")
	prepend_path("MODULEPATH","/opt/sys/easybuild/modules/all/Compiler/GCCcore/11.3.0")
	prepend_path("CMAKE_LIBRARY_PATH","/opt/sys/easybuild/software/GCCcore/11.3.0/lib64")
	prepend_path("CMAKE_PREFIX_PATH","/opt/sys/easybuild/software/GCCcore/11.3.0")
	prepend_path("LD_LIBRARY_PATH","/opt/sys/easybuild/software/GCCcore/11.3.0/lib64")
	prepend_path("MANPATH","/opt/sys/easybuild/software/GCCcore/11.3.0/share/man")
	prepend_path("PATH","/opt/sys/easybuild/software/GCCcore/11.3.0/bin")
	prepend_path("XDG_DATA_DIRS","/opt/sys/easybuild/software/GCCcore/11.3.0/share")
	setenv("EBROOTGCCCORE","/opt/sys/easybuild/software/GCCcore/11.3.0")
	setenv("EBVERSIONGCCCORE","11.3.0")
	setenv("EBDEVELGCCCORE","/opt/sys/easybuild/software/GCCcore/11.3.0/easybuild/Core-GCCcore-11.3.0-easybuild-devel")


Use modules in script
---------------------

The ``module`` command can also be used in scripts, such as Slurm `batch scripts <../batch/submit.html#writing-a-job-script>`__, as shown in the following example:

.. code-block:: bash

	#!/bin/bash
	#SBATCH -N 1 -n 64
	#SBATCH -p fat
	#SBATCH -t 01:00:00

	module purge
	module load <list_of_modules>

	# Add below some commands depending on the modules


Further reading
---------------

- `Lmode user guide <https://lmod.readthedocs.io/en/latest/010_user.html>`__
