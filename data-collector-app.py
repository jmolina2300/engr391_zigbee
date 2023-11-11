#!/usr/bin/env python3
import serial
import time


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
        # read in the line from serial port
        line = ser.readline().decode('utf-8').rstrip()
        line = line + '\n'
        
        # Verify the data before writing it
        if len(line) < 2:
            continue
        
        # Write the data to a file
        with open(out_file_name, 'a+') as f:
            f.write(line)
            print(line,end='')
            
        time.sleep(0.5)

if __name__ == '__main__':
    main()
