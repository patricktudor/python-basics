#! python3
# downloadXkcd.py - Downloads every XKCD comic

# %%

import requests
import os
import bs4

# %%

url = 'https://xkcd.com/'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the url of the image
    # the <img> element is inside a <div> element with id="comic"
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find the image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')  # get 'src' attribute from <img> element
        # Download the image
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

    # Save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')



# %%
