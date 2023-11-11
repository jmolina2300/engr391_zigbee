#!/usr/bin/env python3
##
# Random sensor data generator
#
##

import random
from math import floor

num_points = 100
file_name = 'fake_data.txt'


def write_data(f) :
    for i in range(0, num_points):
        rnd = floor(random.gauss(66, 5))
        line = str(i) + ',' + str(rnd) + '\n'
        f.write(line)

def main():
    print('Generating',num_points,'points...')
    with open(file_name, 'w') as f:
        write_data(f)
        

if __name__ == "__main__" :
    main()
