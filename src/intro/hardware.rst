System Description
==================

The system consists of 34 compute nodes, a frontend node for accessing the system, and an IBM Elastic Storage system.

**Summary**

* Compute nodes: 34
* CPU cores: 4352
* Memory: 58 TiB
* Storage: 1 PiB
* Interconnect: 100 Gbps InfiniBand EDR

**Compute nodes**

4x Lenovo ThinkSystem SR645 (called **hm1** in Slurm)

* 4096 GB DDR4-2400 LRDIMM
* 2x AMD EPYC 7742 64-Core @ 2.25Ghz
* 480 GB SSD
* 7.68 TB NVMe (only two nodes)

10x Dell PowerEdge R6525 (called **hm2** in Slurm)

* 1024 GB DDR4-2933
* 2x AMD EPYC 7713 64-Core @ 2.0Ghz
* 480 GB SSD

20x Lenovo ThinkSystem SR645 V3 (called **hm3** in Slurm)

* 1536 GB DDR5-4800
* 2x AMD EPYC 9534 64-Core @ 2.45Ghz
* 480 GB SSD

**Frontend**

Lenovo ThinkSystem SR645

* 128 GB DDR4-2933
* 2x AMD EPYC 7282 16-Core @ 2.8Ghz
* 480 GB SSD

**Network**

The InfiniBand network is configured as a fat tree, with the compute nodes being connected to two different leaf switches.
The **hm1** and **hm2** nodes are connected to the first leaf switch and the **hm3** nodes are connected to the second one.
The connection between the two leaf switches is oversubscribed, which means that jobs requiring high network throughput
should be `restricted to nodes <../batch/submit.html#node-types>`__ on the same switch. Slurm will automatically try to select
nodes on the same switch, but it will not force it.
