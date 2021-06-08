# the pyperclip module allows you to copy text to clipboard and then paste it

# %%
import pyperclip

pyperclip.copy('Hello, world!')
pyperclip.paste()

# %%
pyperclip.copy('This text can be anything. When something is copied in, the clipboard contents changes.')
pyperclip.paste()


# %%
# and, more practically, anything that is copied using CTRL+C will be copied - try it!
pyperclip.paste()
