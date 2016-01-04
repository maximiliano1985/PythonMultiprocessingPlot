#!/usr/bin/env python
import multiprocessing as mp
import sys
sys.path.insert(0, './lib')
import logger_queue
import visualizer_queue

if __name__=='__main__':
    
   
    
    manager = mp.Manager()
    queue   = manager.Queue()
    pool    = mp.Pool(2)
    
    args_logger     = {'queue': queue}
    args_visualizer = {'queue': queue}

    pool.apply_async(visualizer_queue.VisualizerQueue, (args_visualizer,))
    pool.apply_async(logger_queue.LoggerQueue        , (args_logger    ,))
    
    pool.close()
    pool.join()