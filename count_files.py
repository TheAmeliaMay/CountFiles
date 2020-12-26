import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help="Directory To Count Files", required=True)
args = parser.parse_args()

path = args.directory
files = next(os.walk(path))
file_count = len(files[2])
print('There are {} files.'.format(file_count))
input('Hit any key to exit...')
