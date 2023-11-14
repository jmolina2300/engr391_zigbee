##
# Test reading only the last 20 lines of a data file
##

import os

data_file_name = 'sensor_data.txt'

def read_last_20_lines(f) :
    
    lines = []
    linecount = 0
    file_offset = os.SEEK_END
    
    # Start out seeking backwards by 2 bytes
    offset = -2
    while (linecount < 20):
    
        try:
            f.seek(offset, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            
            # If we got here, then we found a line. Save it.
            linecount += 1
            line = f.readline().decode()
            line = line.rstrip('\n')
            lines.append(line)
            
            # back up by however many bytes just read
            offset -= len(line)
        except OSError: # In case of a one line file
            f.seek(0)
    
    lines.reverse()

    return lines

def test_read_last_20_lines():
    with open(data_file_name, 'rb') as f:
        lines = read_last_20_lines(f)
        
        print(lines)
        print('Lines read:',len(lines))