System Description
==================

The system consists of four compute nodes, a frontend node for accessing the system, and an IBM Elastic Storage system.

**Summary**

* Compute nodes: 14
* CPU cores: 1792
* Memory: 27 TiB
* Storage: 1 PiB
* Interconnect: 100 Gbps Infiniband EDR

**Compute nodes**

4x Lenovo ThinkSystem SR645

* 4096 GB DDR4-2400 LRDIMM
* 2x AMD EPYC 7742 64-Core @ 2.25Ghz
* 480 GB SSD
* 7.68 TB NVMe (only two nodes)


10x Dell PowerEdge R6525

* 1024 GB DDR4-2933
* 2x AMD EPYC 7713 64-Core @ 2.0Ghz
* 480 GB SSD

**Frontend**

Lenovo ThinkSystem SR645

* 128 GB DDR4-2933
* 2x AMD EPYC 7282 16-Core @ 2.8Ghz
* 480 GB SSD
