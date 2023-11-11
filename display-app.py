#!/usr/bin/env python3
##
# Display app
#
# This module plots the data from the sensor data file 
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


def main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    
    # Set the window size on startup
    print ('matplotlib backend:', plt.get_backend())
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    
    plt.show()
    print("done")

if __name__ == "__main__" :
    main()
