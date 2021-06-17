# script following along to ATBSWP Ch 9 - reading and writing files
# 2021-06-11

# %%

from pathlib import Path

# %%
# folders can be specified in Path to make sure the correct path operators (\ or /)
# are used for the operating system. 
# Windows = \
# macOS = /
# linux = /

Path('spam', 'bacon', 'eggs')

# %%
str(Path('spam', 'bacon', 'eggs'))

# %%
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Pat', filename))

# %%
# it's a good idea to always use forward slashes in your paths (see pg. 203)

# using / to join paths - the following 3 lines all result in the same path

Path('spam') / 'bacon' / 'eggs'

# %%
Path('spam') / Path('bacon/eggs')

# %%
Path('spam') / Path('bacon', 'eggs')

# %%
# it makes joining paths a lot easier and safer. For example, the following -
homeFolder = r'C:\Users\Pat'
subFolder = 'spam'
homeFolder + '\\' + subFolder

# %%
'\\'.join([homeFolder, subFolder])

# can instead be created by -
homeFolder = Path('C:/Users/Pat')
subFolder = Path('Spam')
homeFolder / subFolder

# %%
str(homeFolder / subFolder)