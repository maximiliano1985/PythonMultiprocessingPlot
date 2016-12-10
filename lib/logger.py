#!/usr/bin/env python

from multiprocessing.connection import Client
import time
import os
from serial_simulator import simulator

class Logger(object):
    def __init__( self, din = {} ):
        self.dict = {
            'portname'        : '/dev/tty.usbserial-A601NO4K',
            'baudrate'        : 57600,
            'timeout_sec'     : 1,
            'sampling_time_ms': 5,
            'plotting_time_ms': 100,
            'n_data_sim'      : 4000,
            'verbose'         : False,
        }
        self.dict.update(din)
        
        # Simulate a logging at a predetermined sampling rate
        print "[LOG] Initialised simulation mode"
        self.ser = simulator(self.dict['n_data_sim'], self.dict['sampling_time_ms'])
       
        # Info on process used for data logging
        print "[IPC-C] Client process ID ", os.getpid()
        
        self.init_communication()
        self.__run__()
        self.close_communication()
        
    
    def init_communication(self):
        # Open the client-side of the communication for MultiProcessing
        print "[IPC-C] Opening client socket ... ",
        address = ('localhost', 6000)
        self.conn = Client(address)
        print "done!"
    
    def close_communication(self):
        # Tell to the server the data transfer is done
        self.conn.send('close')
        print "[IPC-C] Closing client ... ",
        # Close the client-side of the communication
        self.conn.close()
        print "done!"
    
    def write_msg(self, msg):
        self.conn.send( msg )
        
    def __run__(self):
        # Some initializations
        send_data = False
        avg       = [0, 0, 0]
        n         = 1
        time      = 0
        
        max_data = self.dict['n_data_sim']
            
        for i in range(1,max_data):
            # Read the data from the serial communication
            self.ser.log_data(self.dict['verbose'])
            
            # Calculate elapsed time from the sensor
            time = (time + self.ser.meas_ts_ms*1e-3) # (s)
            
            # Check if average or send data
            if n == round(self.dict['plotting_time_ms']/self.dict['sampling_time_ms']):
                send_data = True
            else:
                send_data = False
            
            # Average the data during a time span DT.
            # DT is chosen accordingly to the refresh rate of the plots (~100 ms)
            if send_data == False:
                # Calculate the cumulative average
                for j in range(0,3):
                    avg[j] = (avg[j]*(n-1)+self.ser.raw_data_A[j])/n
                    
                n = n+1
            else:
                msg = [os.getpid(), i, time, avg[0], avg[1], avg[2]]
                
                #print "Logger sent ", msg
                self.write_msg(msg)
                
                avg = [0, 0, 0]
                n   = 1
        
    
if __name__=='__main__':
    l = Logger( {'sampling_time_ms': 5, 'plotting_time_ms': 100} )

    
    
    