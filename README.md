# PYTHON: multiprocess log and visualization

### Introduction

In this repository are provided two examples for managing the multi-processes in Python. The goal is to have a process that simulates the acquisition of data from a sensor at a high rate *ts*, and outputs to a visualizer process the averaged values at a lower rate, that is a multiple of *ts*. In the default examples the log is done every *5 ms*, and the average is output every *100 ms* since the latter is the maximum refresh rate of the plotter.


***

### Included software

multiproc_poolQUEUE
========================
The processes are run through a **pool** and the inter-process communication is done through a shared **queue**.

multiproc_processIPC
========================
Tthe processes are run through as two **Process instances** and the inter-process communication is done through a **UDP-like socket**