#!/usr/bin/env python
from multiprocessing import Process
import sys
sys.path.insert(0, './lib')
import logger
import visualizer


if __name__=='__main__':

    args_logger = {'sampling_time_ms': 5, 'plotting_time_ms': 100}
    
    p1 = Process(target = visualizer.Visualizer )
    p1.start()
    
    p2 = Process(target = logger.Logger, args=(args_logger,) )
    p2.start()
    
    
    