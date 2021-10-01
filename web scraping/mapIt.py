#! python3
# mapIt.py - Launches a map in the browser using an address from
# the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '. join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.co.uk/maps/place/' + address)

# NOTES
# sys.argv variable stores a list of the program filename (first element) 
# and command line arguments