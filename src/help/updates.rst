System Updates
===============
On this page you can find a list of changes to the system, which might affect how users interact with the system.


October 2023
--------------
All machines have been updated to AlmaLinux 8.8 and the system has been expanded with 20 additional nodes. If you experience any issues, please contact our service desk.

Notable changes include:

* The compute nodes are now connected to two different Infiniband switches. The ``hm1`` and ``hm2`` nodes are connected to the first switch, while the ``hm3`` nodes are connected to the second one. Because the connection between the two switches is oversubscribed, if your compute job requires high network throughput, you should restrict which nodes are being used.
* We have had some issues with people running CPU intensive programs on the frontend, which is slowing down the frontend for everybody. For this reason CPU and memory resources are now constrained on the frontend, such that no single user can use all available resources.


September 2022
--------------
All machines have been reinstalled with AlmaLinux 8.6 and the system has been expanded with 10 additional nodes. Because of the new Linux distribution, the entire module system has also been rebuilt. If you are missing any modules, contact our service desk and we will get them installed again.

Notable changes include:

* The module system is now using a hierarchical structure. Before loading a module you now have to load the associated toolchain. You can still use ``module spider`` to see all the available modules and this command will also tell which dependencies you have to load together with the module. Simply running ``module avail`` will show the available toolchains, but it will not show the modules using that toolchain, until the toolchain has been loaded.
* The new nodes only have 1 TB of memory and by default you will only reserve 8 GB of memory per allocated core. For this reason it is important to specify the amount of memory you need in your Slurm job scripts. Use the ``--mem-per-cpu`` directive set the memory requirements. Please only request the amount of memory that you actually need, such that the nodes can be properly utilised.
* If you previously compiled your own software on the system, then you will have to recompile it before running your new jobs.
* The module systems on Hippo and Abacus are now different, so for those using both system, you will now need separate job scripts for the two systems.
