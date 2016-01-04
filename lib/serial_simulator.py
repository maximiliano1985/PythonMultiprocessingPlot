#!/usr/bin/env python

import os
import time
import numpy as np
import random

class simulator:
    def __init__(self, nData = 10000, samplingTime_ms = 100):
        self.pid        = os.getpid()
        self.meas_ts_ms = samplingTime_ms
        self.x_sim      = [0]*nData
        self.y_sim      = [0]*nData
        self.z_sim      = [0]*nData
        
        for i in range(1, nData):
            self.x_sim[i] = 230*np.cos(2 * np.pi * (i*samplingTime_ms) / 10000.) + random.gauss(0, 80)
            self.y_sim[i] = 230*np.sin(2 * np.pi * (i*samplingTime_ms) / 10000.) + random.gauss(0, 80)
            self.z_sim[i] = 120*np.cos(2 * np.pi * (i*samplingTime_ms) / 5000.)
            
            
        
    def log_data(self, verbose = False):
        # Simulate a deterministic logging
        #a = time.time()
        time.sleep(self.meas_ts_ms/1e3)
        #print "DT ",  time.time() - a
        
        self.raw_data_A = [self.x_sim.pop(0), self.y_sim.pop(0), self.z_sim.pop(0)]
        if verbose:
            print self.raw_data_A


if __name__=='__main__':
    numData = 100
    sim = simulator(numData, samplingTime_ms = 20)
    for i in range(1, numData):
        sim.log_data(verbose = True)
    