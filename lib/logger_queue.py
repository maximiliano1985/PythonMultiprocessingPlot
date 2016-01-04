#!/usr/bin/env python

from multiprocessing import Queue
from logger import Logger

class LoggerQueue(Logger):
    def __init__(self, din = {}):
        self.dict = {'queue': Queue()}
        self.dict.update(din)
        super(LoggerQueue, self).__init__(self.dict)
        
    def init_communication(self):
        return None
    
    def close_communication(self):
        self.dict['queue'].put('close')
        print "[LOG] Transmission completed"
    
    def write_msg(self, msg):
        self.dict['queue'].put(msg)
        # msg format: [os.getpid(), i, time, avg[0], avg[1], avg[2]]