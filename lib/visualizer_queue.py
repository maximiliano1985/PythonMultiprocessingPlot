#!/usr/bin/env python
from multiprocessing import Queue

from visualizer import Visualizer

class VisualizerQueue(Visualizer):

    def __init__(self, din = {}):
        self.dict = {'queue'  : Queue()}
        self.dict.update(din)
        super(VisualizerQueue, self).__init__(self.dict)
    
    def init_communication(self):
        return None
    
    def close_communication(self):
        return None
        
    def read_msg(self):
        msg = self.dict['queue'].get()
        return msg
        # msg format: [os.getpid(), i, time, avg[0], avg[1], avg[2]]