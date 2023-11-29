"""
Shared utility functions for the project

"""

def file_exists(file):
    exists = False
    try:
        with open(file, 'rb') as f:
            exists = True
            
    except IOError:
        pass
        
    return exists