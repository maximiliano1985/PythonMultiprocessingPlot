#!/usr/bin/env python

import matplotlib
#matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
import time



class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        self.Dt_max = 10  #(secs) time span of the plot
        self.fancyPlot = True # does a more beautiful plot (but slows the animation)
        
        self.t = np.asarray([])
        self.x = np.asarray([])
        self.y = np.asarray([])
        self.z = np.asarray([])
        
        self.fig = plt.figure()

        self.ax1 = self.fig.add_subplot(1, 2, 1)
        self.ax2 = self.fig.add_subplot(3, 2, 2)
        self.ax3 = self.fig.add_subplot(3, 2, 4)
        self.ax4 = self.fig.add_subplot(3, 2, 6)

        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')
        self.line1_History = Line2D([], [], color='black')
        self.ax1.add_line(self.line1_History)
        self.ax1.set_xlim(-400, 400)
        self.ax1.set_ylim(-800, 800)
        self.ax1.set_aspect('equal', 'datalim')
        
        self.ax2.grid(True)
        self.ax2.set_xlabel('t')
        self.ax2.set_ylabel('x')
        self.line2_History = Line2D([], [], color='black')
        self.ax2.add_line(self.line2_History)
        self.ax2.set_ylim(-400, 400)
        self.ax2.set_xlim(0, self.Dt_max+1)
        
        self.ax3.grid(True)
        self.ax3.set_xlabel('t')
        self.ax3.set_ylabel('y')
        self.line3_History = Line2D([], [], color='black')
        self.ax3.add_line(self.line3_History)
        self.ax3.set_ylim(-400, 400)
        self.ax3.set_xlim(0, self.Dt_max+1)
        
        self.ax4.grid(True)
        self.ax4.set_xlabel('t')
        self.ax4.set_ylabel('z')
        self.line4_History = Line2D([], [], color='black')
        self.ax4.add_line(self.line4_History)
        self.ax4.set_ylim(-400, 400)
        self.ax4.set_xlim(0, self.Dt_max+1)
        
        if self.fancyPlot == True:
            self.line1_Trace = Line2D([], [], color='red', linewidth=2)
            self.line1_NowMarker = Line2D([], [], color='red', marker='o', markeredgecolor='r')
            self.ax1.add_line(self.line1_Trace)
            self.ax1.add_line(self.line1_NowMarker)
            
            self.line2_Trace = Line2D([], [], color='red', linewidth=2)
            self.line2_NowMarker = Line2D([], [], color='red', marker='o', markeredgecolor='r')
            self.ax2.add_line(self.line2_Trace)
            self.ax2.add_line(self.line2_NowMarker)
            
            self.line3_Trace = Line2D([], [], color='red', linewidth=2)
            self.line3_NowMarker = Line2D( [], [], color='red', marker='o', markeredgecolor='r')
            self.ax3.add_line(self.line3_Trace)
            self.ax3.add_line(self.line3_NowMarker)
            
            self.line4_Trace = Line2D([], [], color='red', linewidth=2)
            self.line4_NowMarker = Line2D( [], [], color='red', marker='o', markeredgecolor='r')
            self.ax4.add_line(self.line4_Trace)
            self.ax4.add_line(self.line4_NowMarker)


        
    def draw_frame(self, ary):
        self.t = np.append(self.t, ary[0])
        self.x = np.append(self.x, ary[1])
        self.y = np.append(self.y, ary[2])
        self.z = np.append(self.z, ary[3])
        
        i          = len(self.t)
        head       = i - 1
        head_len   = 1  #(secs) time span of the NowMarker data trace
        
        i          = i-1
        time_now   = self.t[i]
        Dt = 0.01
        if len(self.t) > 1:
            Dt = self.t[-1] - self.t[-2]
        if Dt == 0:
            Dt = 0.01
              
        time_past  = time_now - head_len
        i_past     = max(0, int((time_now-self.Dt_max)/Dt))
        head_slice = (self.t > time_past) & (self.t < time_now+Dt/2)
        #print head_slice, ", ", self.t, ", ", time_past, ", ", time_now
        #print "x ", self.x[head_slice], ", y ", self.y[head_slice]
        print ary
        
        self.line1_History.set_data(self.x[:i], self.y[:i])
        self.line2_History.set_data(self.t[i_past:i], self.x[i_past:i])
        self.line3_History.set_data(self.t[i_past:i], self.y[i_past:i]) 
        self.line4_History.set_data(self.t[i_past:i], self.z[i_past:i])
        
        if self.fancyPlot == True:
            self.line1_Trace.set_data(self.x[head_slice], self.y[head_slice])
            self.line1_NowMarker.set_data(self.x[head], self.y[head])
            self.line2_Trace.set_data(self.t[head_slice], self.x[head_slice])
            self.line2_NowMarker.set_data(self.t[head], self.x[head])
            self.line3_Trace.set_data(self.t[head_slice], self.y[head_slice])
            self.line3_NowMarker.set_data(self.t[head], self.y[head])
            self.line4_Trace.set_data(self.t[head_slice], self.z[head_slice])
            self.line4_NowMarker.set_data(self.t[head], self.z[head])
            self._drawn_artists = [self.line1_History, self.line1_Trace, self.line1_NowMarker,
                                   self.line2_History, self.line2_Trace, self.line2_NowMarker,
                                   self.line3_History, self.line3_Trace, self.line3_NowMarker,
                                   self.line4_History, self.line4_Trace, self.line4_NowMarker]
        else:
            self._drawn_artists = [self.line1_History, self.line2_History,
                                   self.line3_History, self.line4_History]
                                   
        if time_now > self.Dt_max:
            self.ax2.set_xlim(time_now-self.Dt_max,time_now+1.0)
            self.ax3.set_xlim(time_now-self.Dt_max,time_now+1.0)
            self.ax4.set_xlim(time_now-self.Dt_max,time_now+1.0)
        
        #self.fig.canvas.draw()
        #self.fig.canvas.start_event_loop(0.00001)
        #plt.show(block=False)
        #self.fig.canvas.draw_idle()
        #self.fig.canvas.flush_events()
        
        plt.pause(0.001)
        #plt.draw()
        #self.fig.canvas.flush_events()
        

        
    def new_frame_seq(self):
        self.ax2.set_xlim(0, self.Dt_max+1)
        self.ax3.set_xlim(0, self.Dt_max+1)
        self.ax4.set_xlim(0, self.Dt_max+1)
        return iter(range(len(self.t)))


    def _init_draw(self):
        lines = []
        if time_now > self.Dt_max:
            lines = [self.line1_History, self.line1_Trace, self.line1_NowMarker,
                                   self.line2_History, self.line2_Trace, self.line2_NowMarker,
                                   self.line3_History, self.line3_Trace, self.line3_NowMarker,
                                   self.line4_History, self.line4_Trace, self.line4_NowMarker]
        else:
            lines = [self.line1_History, self.line2_History,self.line3_History, self.line4_History]
        
        for l in lines:
            l.set_data([], [])
            


if __name__ == '__main__':
    ani = SubplotAnimation()
    #ani.save(filename='sim.mp4',fps=30,dpi=300)
    #plt.show()
    for i in range(1,1000):
        msg = [i/2.0, i/2.0+0.25, i/2.0+0.5, i/2.0+0.75]
        ani.draw_frame( msg )