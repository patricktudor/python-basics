# Web Scraping guide from ATBSWP
# 2021-07-08

# %%

# opening a web page
import webbrowser
webbrowser.open('http://inventwithpython.com')

# %%
# downloading from a web page

import requests

# example - get text of entire romeo and juliet play
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

# %%
# check that the request for the page succeeded
res.status_code == requests.codes.ok

# %%
len(res.text)

# %%
print(res.text[:250])

# %%
# Another way to check for errors is to raise and exception
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()

# %%
# if you don't want to crash the program you can use try
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# %%
# saving downloaded files to the hard drive
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb') # need to use write-binary (wb) mode, even if txt
for chunk in res.iter_content(100000): 
    playFile.write(chunk)

playFile.close()

# %%
# HTML

