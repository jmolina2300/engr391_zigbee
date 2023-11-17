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

data_file_name = 'sensor_data.txt'
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

n_readings = 25
x_axis = [i for i in range(n_readings)]
all_lines = []

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
            
    
    ax.clear()
    #plt.xlabel('Time')
    plt.ylabel('Temperature')
    ax.plot(x_axis, values)


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
