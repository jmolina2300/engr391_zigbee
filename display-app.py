#!/bin/env python3
##
# Data Plotter
#
# This module plots the data from the data file 
#
##

import matplotlib.pyplot as plt
import matplotlib.animation as animation


data_file_name = 'sensor_data.txt'
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animate(i):
    file_data = open(data_file_name,"r").read()
    dataArray = file_data.split('\n')
    time = []
    distance = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            time.append(float(x))
            distance.append(float(y))
            

    ax.clear()
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    ax.plot(time,distance)

def Main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    print("done")

Main()
