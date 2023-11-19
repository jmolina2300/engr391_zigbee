#!/usr/bin/env python3
##
# Display app
#
# This module plots the data from the sensor data file 
#
##

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import reader
import numpy as np
from statistics import stdev
from statistics import mean
import globals

data_file_name = globals.DATA_FILE_NAME
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

n_readings = 25
x_axis = [i for i in range(n_readings)]
all_lines = []

def get_limits(values):

    # Compute a 2-point moving range to obtain the UNPL and LNPL
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

def animate(i):
    
    try:
        with open(data_file_name, 'rb') as f:
            all_lines = reader.read_last_n_lines(f,n_readings)
    except IOError:
        print('Data file not found')
        return


    values = []
    for eachLine in all_lines:
        if len(eachLine)>1:
            # Retrieve data value from each line
            time,value = eachLine.split(',')
            values.append(float(value))
    
    
    # Create graph limits based on the data we currently have
    cl,unpl,lnpl = get_limits(values)
    
    
    ax.clear()
    
    # Plot the center line (average) and the actual values
    ax.set_ylim(lnpl,unpl)
    ax.plot(x_axis, cl, linestyle='--')
    ax.plot(x_axis, values)
    
    plt.ylabel('Temperature')
    
    


def main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    
    # Set the window size on startup
    print ('matplotlib backend:', plt.get_backend())
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    #manager.resize(600,400)
    
    plt.show()
    print("done")

if __name__ == "__main__" :
    main()
