#!/usr/bin/env python3
##
# Display app
#
# This module plots the data from the sensor data file 
#
##

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import test_reader

data_file_name = 'sensor_data.txt'
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animate(i):
    #file_data = open(data_file_name,"r").read()
    #dataArray = file_data.split('\n')
    dataArray = []
    with open(data_file_name, 'rb') as f:
        dataArray = test_reader.read_last_20_lines(f)

    if len(dataArray) < 1:
        print('no dataFile')
        return

    
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
    #manager.resize(*manager.window.minsize())
    manager.resize(600,400)
    
    plt.show()
    print("done")

if __name__ == "__main__" :
    main()
