# script following along to ATBSWP Ch 9 - current working directory
# 2021-06-11

# %%
from pathlib import Path
import os

# %%
Path.cwd()

# %%
# the os module can change the cwd
os.chdir('C:/Users/ptudor/Documents')

Path.cwd()

# %%
# it will throw an error if a folder doesn't exist
os.chdir('C:/ThisFolderDoesntExist')

# %%
# to ge the home directory
Path.home()
