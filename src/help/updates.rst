System Updates
===============
On this page you can find a list of changes to the system, which might affect how users interact with the system.

September 2022
--------------
All machines have been reinstalled with AlmaLinux 8.6 and the system has been expanded with 10 additional nodes. Because of the new Linux distribution, the entire module system has also been rebuilt. If you are missing any modules, contact our service desk and we will get them installed again.

Notable changes include:

* The module system is now using a hierarchical structure. Before loading a module you now have to load the associated toolchain. You can still use ``module spider`` to see all the available modules and this command will also tell which dependencies you have to load together with the module. Simply running ``module avail`` will show the available toolchains, but it will not show the modules using that toolchain, until the toolchain has been loaded.
* The new nodes only have 1 TB of memory and by default you will only reserve 8 GB of memory per allocated core. For this reason it is important to specify the amount of memory you need in your Slurm job scripts. Use the ``--mem-per-core`` directive set the memory requirements. Please only request the amount of memory that you actually need, such that the nodes can be properly utilised.
* If you previously compiled your own software on the system, then you will have to recompile it before running your new jobs.
* The module systems on Hippo and Abacus are now different, so for those using both system, you will now need separate job scripts for the two systems.
