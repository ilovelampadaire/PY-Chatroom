"""Module that checks if the handler text file exists or not from the check() function."""

import os

def check(exists_callback, not_found_callback):
    """
        Checks if the handling text file exists and uses function callbacks to send the output.
        exists_callback: Function that gets ran when the file exists.
        not_found_callback: Function that gets ran when the file doesn't exist.
    """
# Get the current working directory (root of the repository)
    root_directory = os.getcwd()

# Construct the path to the 'lib' directory
    lib_directory = os.path.join(root_directory, 'lib')

# Construct the path to the parent directory of 'lib' (which is the root directory in this case)
    outside_lib_directory = os.path.dirname(lib_directory)

# Construct the full path to the file 'handling.txt' outside of 'lib'
    file_path = os.path.join(outside_lib_directory, 'handling.txt')

# Check if the file exists
    if os.path.exists(file_path):
        print('File exists outside of lib.')
        exists_callback()
    else:
        print('File does not exist outside of lib.')
        not_found_callback()
