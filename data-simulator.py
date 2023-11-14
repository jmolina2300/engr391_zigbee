#!/usr/bin/env python3
##
# Random sensor data generator
#
##

import random
import time
from math import floor

num_points = 100
file_name = 'sensor_data.txt'


def write_data(f) :
    for i in range(0, num_points):
        line = generate_line(i)
        f.write(line)

def generate_line(timestamp):
    rnd = floor(random.gauss(66, 5))
    line = str(timestamp) + ',' + str(rnd) + '\n'
    return line

def generate_file_data():
    print('Generating',num_points,'points...')
    with open(file_name, 'w') as f:
        write_data(f)
        
def main():
    counter = 0
    while (1):
        with open(file_name, 'a+') as f:
            line = generate_line(counter)
            f.write(line)
            print(line,end='')
        
        time.sleep(1)
        counter += 1
        

if __name__ == "__main__" :
    main()
