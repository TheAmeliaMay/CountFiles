import os

path = input('Directory to count files in: ')
files = next(os.walk(path))
file_count = len(files[2])
print('There are {} files.'.format(file_count))
input('Hit any key to exit...')