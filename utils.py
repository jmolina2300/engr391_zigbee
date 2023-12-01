"""
Shared utility functions for the project

"""
import os

def file_exists(file):
    exists = False
    try:
        with open(file, 'rb') as f:
            exists = True
            
    except IOError:
        pass
        
    return exists


def read_last_n_lines(f,n) :
    
    lines = []
    linecount = 0
    file_offset = os.SEEK_END
    
    # Start out seeking backwards by 2 bytes
    offset = -2
    while (linecount < n):
    
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