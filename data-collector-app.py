#!/usr/bin/env python3
import serial
import time
from datetime import datetime


out_file_name = 'sensor_data.txt'
device = '/dev/ttyS0'



def main():
    # Open the serial device file
    ser = serial.Serial(device, 9600, timeout=1) 
    ser.flush()
    
    # If we couldn't open the device, then exit
    if not device:
        print('Failed to open device ' + device)
        quit()
    
    print('Listening for data on device ' + device + '...')

    while True:
        # read in the raw line from serial port
        line = ser.readline().decode('utf-8').rstrip()
        pieces = line.split(',')
        
        # Verify the data before writing it
        if len(pieces) < 2:
            continue
        
        # Construct the actual line that will be saved to a file
        value = pieces[1]
        currdate = datetime.now().isoformat()
        line = currdate + ',' + value + '\n'
        
        # Write the data to a file
        with open(out_file_name, 'a+') as f:
            f.write(line)
            print(line,end='')
            
        time.sleep(0.5)

if __name__ == '__main__':
    main()
