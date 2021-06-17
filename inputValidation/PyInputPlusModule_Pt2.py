# Part 2 - PyInputPlus module

# pyinputplus functions will automatically reprompt the 
# user for as long as they don't enter a valid input.

# %%
import pyinputplus as pyip

# %%
response = pyip.inputNum()

# enter 42 where prompted
# %%
response
# %%
# prompt the type of input (standard)
response = input('Enter a number:')

# %%
# prompt the type of input (pyip)
response = pyip.inputInt(prompt = 'Enter a number: ')

# %%
# numeric input functions inputNum() inputInt() inputFloat() have 
# min max greaterThan and lessThan keyword arguements.

response = pyip.inputNum(prompt='Enter number: ', min=4)

# %%
response = pyip.inputNum(prompt='Enter number: ', greaterThan=4)

# %%
response = pyip.inputNum(prompt='Enter number: ', min=4, lessThan=10)

# %%
# blank input isn't allowed by default, it must be specified
# use this if the input is optional.
response = pyip.inputNum(blank=True)

# %%
# limit and timeout stop the program from asking after a specified number 
# of tries or amount of time.

response = pyip.inputNum(limit=2)

# %%
response = pyip.inputNum(timeout=5)

# %%
# passing a default value means the function will return the default
# value instead of raising an exception.

response = pyip.inputNum(limit=2, default='No response')

# enter a couple of non-numeric inputs, then -
response

# %%
# regex can be used to specify if a value is allowed or not
# for example, to allow roman numerals as input -
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|X|C|D|M)+', r'zero'])

# enter XLII

# %%
# you can also block some inputs using regex strings
response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# %%
# if both allow and block are specified, allow overrides block
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

# %%
# custom inputs can be created
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addsUpToTen)

# input 123
# input 235

# %%
response

# %%
