"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

import os

print(f'Arguments: {len(sys.argv)}')
print(f'Argument List: {str(sys.argv)}')

# Print out the OS platform you're using:
print(f'Windows Version: {sys.version}')

# Print out the version of Python you're using:
print(f'Python Version: {sys.version_info}')


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'Current Process ID: {os.getpid()}')

# Print the current working directory (cwd):
print(f'PWD: {os.getcwd()}')

# Print out your machine's login name
print(f"Machine's login name: {os.getlogin()}")