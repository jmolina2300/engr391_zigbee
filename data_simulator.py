#!/usr/bin/env python3
##
# Random sensor data generator
#
##

import random
import time
from datetime import datetime
import sys
from utils import file_exists
from math import floor



"""
    generate_line()
	
    Generates one line of random data with an ISO8601 timestamp
"""
def generate_line():
	rnd = floor(random.gauss(66, 5))
	timestamp = datetime.now().isoformat()
	line =  timestamp + ',' + str(rnd) + '\r\n'
	return line


"""
    create_new_sensor_file()

    Creates a new file with the CSV header using the sensor identity
"""
def create_new_sensor_file(identity, new_file_name):
	print('Creating new file',new_file_name)
	with open(new_file_name, 'w') as f:
		csv_header = identity + ',values\r\n'
		f.write(csv_header)


def main():
	if len(sys.argv) < 2:
		print('Usage: ./data_simulator.py SENSOR_IDENTITY')
		quit()
	
	# Get the sensor identity from the command line
	identity = sys.argv[1]
	sensor_file_name = identity + '.csv'
	

	while (1):
		# If the file doesn't exist, create it
		if not file_exists(sensor_file_name):
			create_new_sensor_file(identity, sensor_file_name)

		# Append a new line of random data to the file
		with open(sensor_file_name, 'a+') as f:
			line = generate_line()
			f.write(line)
			print(line,end='')

		time.sleep(1)
		

if __name__ == "__main__" :
	main()
