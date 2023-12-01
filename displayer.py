#!/usr/bin/env python3
##
# Display app
#
# This module plots the data from the sensor data file 
#
##

import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from utils import read_last_n_lines
from utils import file_exists
from statistics import stdev
from statistics import mean
import globals

data_file_name = ""

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

n_readings = 25
x_axis = [i for i in range(n_readings)]
all_lines = []

# Compute limits using a 2-point moving range
def get_limits_mR(values):
    k = 2
    mR = [0 for i in range(0,len(values) - k + 1)]
    for i in range(0,len(mR)-1):
        mR[i] = abs(values[i]-values[i+1])
    
    mRbar = mean(mR)
    
    xbar = mean(values)
    cl = [xbar for i in range(0,n_readings)]
    unpl = xbar + (3*mRbar)/1.128
    lnpl = xbar - (3*mRbar)/1.128
    return cl,unpl,lnpl

# Compute limits using mean and +/- 3 sigma
def get_limits_3sig(values):
    avg = mean(values)
    cl = [avg for i in range(0,n_readings)]
    ul = avg + 3*stdev(values)
    ll = avg - 3*stdev(values)
    return cl,ul,ll


def animate(i, data_file_name):
    
    try:
        with open(data_file_name, 'rb') as f:
            all_lines = read_last_n_lines(f,n_readings)
    except IOError:
        print('Data file not found:',data_file_name)
        return


    values = []
    for eachLine in all_lines:
        if len(eachLine)>1:
            # Retrieve data value from each line
            time,value = eachLine.split(',')
            values.append(float(value))
    
    
    # Create graph limits based on the data we currently have
    cl,unpl,lnpl = get_limits_3sig(values)
    
    
    ax.clear()
    
    # Plot the center line (average) and the actual values
    ax.set_ylim(lnpl,unpl)
    ax.plot(x_axis, cl, linestyle='--')
    ax.plot(x_axis, values,color='blue')
    
    plt.ylabel('Temperature')
    
"""
get_file_to_monitor

  Sets the file to be continuously monitored for changes and displayed
  on the plot.

"""
def get_file_to_monitor():
    return sys.argv[1]




def main():
    if len(sys.argv) < 2:
        print('Usage: display-app <file.csv>')
        quit(1)
    
    data_file_name = get_file_to_monitor()
    if not file_exists(data_file_name) :
        print('No such data file:',data_file_name)
        quit(1)

    
    """
      Animate the plot

      Inputs: 

        fig - the figure to animate
        animate - function to call to animate the figure
        interval - interval in milliseconds between each animation
        fargs - arguments passed to the animate function
    """
    ani = animation.FuncAnimation(fig, animate, interval=1000, fargs=(data_file_name, ))
    
    # Set the window size on startup
    print ('matplotlib backend:', plt.get_backend())
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    #manager.resize(600,400)
    
    plt.show()
    print("done")

if __name__ == "__main__" :
    main()
