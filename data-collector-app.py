#!/bin/env python3
import serial
import time


out_file_name = 'sensor_data.txt'
device = '/dev/ttyS0'



if __name__ == '__main__':

    # if connected via serial Pin(RX, TX)
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
        #numbers = line.split(',')
        if len(line) < 2:
            continue
        
        # Convert the string data into integers
        #sensor_time = str(numbers[0])
        #sensor_value = str(numbers[1])
        
        #print(sensor_time,sensor_value)
        
        
        # Write the data to a file
        with open(out_file_name, 'a+') as f:
            f.write(line)
            print(line,end='')
            
        time.sleep(0.5)
        

            
            

