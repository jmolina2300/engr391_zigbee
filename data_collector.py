#!/usr/bin/env python3
import sys
import serial
import time
import globals
from datetime import datetime
from utils import file_exists


out_file_name = globals.DATA_FILE_NAME
device = '/dev/ttyUSB0'


def valid_identity(identity) :
    result = False
    for letter in identity:
        if letter == 0:
            result = False
    
    if len(identity) < 32:
        result = True
    
    return result

def create_new_csv_file(file_name):
    # If the file is new, then we need to put the header at the top
    with open(file_name, 'w') as f:
        f.write('timestamp,value\n')
        print('Created new file ' + file_name)


def update_csv_file():
    pass

    

def main():
    if len(sys.argv) < 2:
        print('Usage: data-collector-app <DEVICE_NAME>')
        quit(1)
    device = sys.argv[1]

    # Open the serial device file
    ser = serial.Serial(device, 9600, timeout=1) 
    ser.flush()
    
    # If we couldn't open the device, then exit
    if not device:
        print('Failed to open device ' + device)
        quit()
    
    print('Listening for data on device ' + device + '...')

    while True:
        # read in one good line from serial port
        line = serial_device.readline().decode('ascii').rstrip()
        pieces = line.split(',')
        
        # Verify the data before writing it
        if len(pieces) < 2:
            continue
        
        identity = pieces[0]
        if not valid_identity(identity) :
            continue
        
        # Assign the output file name as the identity (whatever it is)
        out_file_name = identity + ".csv"

        # If the file doesn't exist, then create it and add the header
        if (not file_exists(out_file_name)):
            create_new_csv_file(out_file_name)
        
        
        # Construct the actual line that will be saved to a file
        value = float(pieces[1])
        timestamp = datetime.now().isoformat()
        line = timestamp + ',' + str(value) + '\r\n'
        
        # Write the data to a file
        with open(out_file_name, 'a+') as f:
            f.write(line)
            print(line,end='')
            
        time.sleep(0.5)

if __name__ == '__main__':
    main()
