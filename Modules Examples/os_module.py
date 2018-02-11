import os
from datetime import datetime
print(os.getcwd())

os.chdir('/Users/Luis/Desktop')

print(os.getcwd())

# print(os.listdir())

# two ways of creating a directory
# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2')

# print(os.listdir())

# remove directories
# os.rmdir('OS-Demo-2')
# os.removedirs('OS-Demo-2/Sub-dir-1')

# rename files
# os.rename('test.txt', 'demo.txt')

# Info about a file
# print(os.stat('demo.txt').st_size)
# mod_time = os.stat('demo.txt').st_mtime

# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('/Users/Luis/Desktop'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()
print(os.environ.get('Home'))
# file_path = os.path.join(os.environ.get('Home'), 'test.txt')
print(os.path.basename('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
