.. |dash-line| raw:: html

	<style>
	hr.dash {
  		border: 1px dashed black;
  		width: 100%
	}
	</style>

	<hr class="dash">

.. |br| raw:: html

	<br>

.. |ellipsis| raw:: html

	<object style="font-size:30px;font-weight:700;">&#x22EE;</object>

Modules System
==============

Multiple versions of the same software are installed using the `lmod <https://www.tacc.utexas.edu/research-development/tacc-projects/lmod>`__ enviromental mudules system. 

The modules system makes it very easy to specify which version you want to use and keeps everything consistent. There are also circumstances, where one software program will have some environment setting or file that conflicts with a different program, and also has modules that help solve this problem.

Access modules
--------------

Most software packages available on ABACUS2.0 can be found as a module. To see a list of available software run the command module spider.

Note that the list below is not updated automatically. To get an updated list, rerun the command on the frontend node:

.. code-block:: console

	$ module spider

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

You can optionally specify a package name, and it will show you all available versions of that package, as shown above.
	 
Load a module
-------------

To load a module, use the command module load modulename. The default version will get loaded. If you want a particular version, use ``module load <module_name>/<module_version>``, e.g.:

.. code-block:: console

	$ module list

.. tip::

	No modules loaded

.. code-block:: console

	$ module load GCCcore/10.2.0

.. tip::
	
	|br|

	Currently Loaded Modules:

  	\1) GCCcore/10.2.0
    
Unload a module
---------------

To unload a module, use the command: ``module unload <module_name>``. To unload everything, use: ``module purge``.

.. note::

	``module unload`` automatically unloads dependencies.


Examine a module file
---------------------

If you want to see what the ``module`` command is doing to your environment, you can run: ``module show <module_name>/<module_version>``, e.g.:

.. code-block:: console

	module show GCCcore/10.2.0

Using modules in script
-----------------------

The ``module`` command can be used in script, e.g. SLURM batch scripts:

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




