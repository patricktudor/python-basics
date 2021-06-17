# script following along to ATBSWP Ch 9 - creating folders
# 2021-06-11

# %%
import os

# %%
os.makedirs('C:\\delicious\\walnut\\waffles')

# %%
from pathlib import Path

Path(r'C:/Users/ptudor/Documents/spam').mkdir()

# mkdir() can only make one directory at a time. 
# Unlike makedirs which can make as many as needed.

# %%
# absolute and relative filepaths

# to check if a path is absolute or not
Path.cwd()

# %%
Path.cwd().is_absolute()

# %%
Path('spam/bacon/eggs').is_absolute()

# %%
# put Path.cwd() / infront of a relative path to get an absolute path

Path.cwd() / Path('my/relative/path')

# %%
# to get an string of the absolute path of the arguement
os.path.abspath('.')

# %%
os.path.abspath('.\\GitHub')

# %%
# another way to check if path is absolute
os.path.isabs('.')

# %%
os.path.isabs(os.path.abspath('.'))

# %%
# to get a relative file path
os.path.relpath('C:\\Windows', 'C:\\')

# %%
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')

# '..' allows you to return to the parent folder

# %%
# to extract specific attributes of a path

p = Path('C:/Users/ptudor/Documents/spam.txt')
# %%
p.anchor
# %%
p.parent
# %%
p.name
# %%
p.stem
# %%
p.suffix
# %%
p.drive

# %%
# the parents attribute evaluates to the ancestor folders of 
# a Path object with an integer index

Path.cwd().parents[1]

# %%
# File sizes and folder contents

# to find out the size of a file in bytes
os.path.getsize('C:\\Users\\ptudor\\Documents\\PostOffices2000.png')

# %%
os.listdir('C:\\Users\\ptudor\\Documents\\Work Notes')
# %%

# to get the total size of a folder -
totalsize = 0
for filename in os.listdir('C:\\Users\\ptudor\\Documents\\Work Notes'):
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Users\\ptudor\\Documents\\Work Notes', filename))
print(totalsize)

# %%
