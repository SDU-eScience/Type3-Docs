.. |dash-line| raw:: html

	<style>
	hr.dash {
  		border: 1px dashed black;
  		width: 100%
	}
	</style>

	<hr class="dash">

.. |nbsp| unicode:: U+00A0

.. |br| raw:: html

	<br>

.. |ellipsis| raw:: html

	<object style="font-size:30px;font-weight:700;">&#x22EE;</object>

Modules System
==============

Multiple versions of the same software are installed using the `Lmod <https://www.tacc.utexas.edu/research-development/tacc-projects/lmod>`__ enviromental modules system. 

The modules system makes it very easy to specify which version you want to use and keeps everything consistent. There are also circumstances where one software program will have some environment setting or file that conflicts with a different program, and also has modules that help solve this problem.

Access modules
--------------

Most software packages available on Type 3 can be found as a module. To see a list of available software run the command:

.. code-block:: console

	[testuser@fe-ac-02 ~]$ module spider

.. tip:: 

  |br|

  |dash-line|

  The following is a list of the modules and extensions currently available:

  |dash-line|

  Autoconf: Autoconf/2.69-GCCcore-10.2.0
    Autoconf is an extensible package of M4 macros that produce shell scripts to automatically configure software source code packages. These scripts can adapt the packages to many kinds of
    UNIX-like systems without manual user intervention. Autoconf creates a configuration script for a package from a template file that lists the operating system features that the package can
    use, in the form of M4 macro calls.

  Automake: Automake/1.16.2-GCCcore-10.2.0
    Automake: GNU Standards-compliant Makefile generator

  Autotools: Autotools/20200321-GCCcore-10.2.0
    This bundle collect the standard GNU build tools: Autoconf, Automake and libtool

  Bison: Bison/3.3.2, Bison/3.7.1-GCCcore-10.2.0, Bison/3.7.1
    Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR (GLR) parser employing LALR(1) parser tables.

  |ellipsis|

  |dash-line|

  To learn more about a package execute:

  $ module spider Foo

  where "Foo" is the name of a module.

  To find detailed information about a particular package you
  must specify the version if there is more than one version:

  $ module spider Foo/11.1

  |dash-line|

Note that the list above is not updated automatically. To get an updated list, rerun the command on the frontend node.
You can optionally specify a package name, and it will show you all available versions of that package, as shown in the example above.

.. note::

    You can also use the command ``module avail`` to get the list of available packages in a different format.
	 
Load a module
-------------

To load a module, use the command: ``module load <module_name>``. The default version will get loaded. 

If you want a particular version, use instead: ``module load <module_name>/<module_version>``. For example:

.. code-block:: console

	[testuser@fe-ac-02 ~]$ module list

.. tip::

	No modules loaded

.. code-block:: console

	[testuser@fe-ac-02 ~]$ module load GCCcore/10.2.0

.. tip::
	
  |br|
  Currently Loaded Modules:
  |br|
  |nbsp| \1) GCCcore/10.2.0

Check active modules
--------------------

You can print the list of currently loaded modules with the command:

.. code-block:: console

  [testuser@fe-ac-02 ~]$ module list


Unload a module
---------------

To unload a module, use the command: ``module unload <module_name>``. To unload everything, use:  ``module purge``.

.. note::

	``module unload``  automatically unloads all the dependencies.

Examine a module file
---------------------

If you want to see what the ``module`` command is doing to your environment, you can run ``module show <module_name>/<module_version>``. For example:

.. code-block:: console

	[testuser@fe-ac-02 ~]$ module show GCCcore/10.2.0

.. tip::

  |br|
  |dash-line|     
  /opt/sys/easybuild/modules/compiler/GCCcore/10.2.0.lua:
  |br|
  |dash-line|
  |br|
  help([[
  |br|
  Description
  |br|
  \===========
  |br|
  The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
  |br|
  |nbsp|\as well as libraries for these languages (libstdc++, libgcj,...).
  |br|
  |br|
  More information
  |br|
  \================
  |br|
  |nbsp|\- Homepage: https://gcc.gnu.org/
  |br| 
  ]])
  |br|
  whatis("Description: The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
  |br|
  |nbsp|\as well as libraries for these languages (libstdc++, libgcj,...).")
  |br|
  whatis("Homepage: https://gcc.gnu.org/")
  |br|
  whatis("URL: https://gcc.gnu.org/")
  |br|
  conflict("GCCcore")
  |br|
  prepend_path("CMAKE_LIBRARY_PATH","/opt/sys/easybuild/software/GCCcore/10.2.0/lib64")
  |br|
  prepend_path("CMAKE_PREFIX_PATH","/opt/sys/easybuild/software/GCCcore/10.2.0")
  |br|
  prepend_path("LD_LIBRARY_PATH","/opt/sys/easybuild/software/GCCcore/10.2.0/lib")
  |br|
  prepend_path("LD_LIBRARY_PATH","/opt/sys/easybuild/software/GCCcore/10.2.0/lib64")
  |br|
  prepend_path("MANPATH","/opt/sys/easybuild/software/GCCcore/10.2.0/share/man")
  |br|
  prepend_path("PATH","/opt/sys/easybuild/software/GCCcore/10.2.0/bin")
  |br|
  prepend_path("XDG_DATA_DIRS","/opt/sys/easybuild/software/GCCcore/10.2.0/share")
  |br|
  setenv("EBROOTGCCCORE","/opt/sys/easybuild/software/GCCcore/10.2.0")
  |br|
  setenv("EBVERSIONGCCCORE","10.2.0")
  |br|
  setenv("EBDEVELGCCCORE","/opt/sys/easybuild/software/GCCcore/10.2.0/easybuild/GCCcore-10.2.0-easybuild-devel")


Using modules in script
-----------------------

The ``module`` command can be used in script, e.g. Slurm `batch scripts <../batch/submit.html#writing-a-job-script>`__, as in the following example:

.. code-block:: bash

	#! /bin/bash 

	#SBATCH options 
	#SBATCH ... 

	module purge 
	module load <list_of_modules> 

	... 

	# Add below some commands depending on the modules


Further reading
---------------

- `Lmode user guide <https://lmod.readthedocs.io/en/latest/010_user.html>`__




