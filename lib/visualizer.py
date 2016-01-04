#!/usr/bin/env python
from multiprocessing.connection import Listener
import os
import time

class Visualizer(object):
    
    def __init__(self, din = {}):
        import plotter
        
        self.dict = {
            'plotter': plotter.SubplotAnimation(),
        }
        self.dict.update(din)
        
        print "[IPC-S] Server process ID ", os.getpid()
        self.init_communication()
        self.__run__()
     
     
    def init_communication(self):
        print "[IPC-S] Opening Server socket ... ",
        address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
        self.listener = Listener(address)
        print "done!"
    
        print "[IPC-S] Waiting Client ... ",
        self.conn = self.listener.accept()
        print 'connection accepted from', self.listener.last_accepted
        
    def close_communication(self):
        print "[IPC-S] Closing interprocess communication ... ",
        self.conn.close()
        self.listener.close()
        print "done!"
        
    def read_msg(self):
        return self.conn.recv()
        
         
    def __run__(self):
        while True:
            msg = self.read_msg()
            # msg format: [os.getpid(), i, time, avg[0], avg[1], avg[2]]
            
            # Process the message
            if msg == 'close':
                self.close_communication()
                break
            
            procID  = msg[0]
            counter = msg[1]
            logTime = msg[2]
            avg     = msg[3:]
            #print os.getpid(), "--- Recived ", msg, " ||| avg ", avg, " ||| counter ", counter
            
            # Plot the data
            self.dict['plotter'].draw_frame([logTime, avg[0], avg[1], avg[2]] ) # plots a point every 100 ms
        
        
if __name__=='__main__':
    v = Visualizer()
        
