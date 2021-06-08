# script to demonstrate how to find patterns in text using regular expressions
# following ATBSWP Ch7

# mo - Match Object

# %%
import re

# %%
# re.compile creates a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')

# the regex object's search() method searches the string it is passes for any match
mo = phoneNumRegex.search('My number is 415-666-4321')
print('Phone number found: ' + mo.group())


# %%
# creating groups in the regex

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search("My mate's number is 345-987-2345")
print('Group 1 is: ' + mo.group(1))
print('Group 2 is: ' + mo.group(2))
print('Group 0 is: ' + mo.group(0))
print('Everything: ' + mo.group())


# %%
# to get all the groups at once, use groups() (plural)
mo.groups()


# %%
areaCode, mainNumber = mo.groups()
print('The area code is: ' + areaCode)
print('The main number is: ' + mainNumber)


# %%
# use pipes to match multiple groups

# The pipe operator | works as an OR statement
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Robin')
print('Our hero is: ' + mo1.group())

# if multiple match, the first is selected
mo2 = heroRegex.search('Tina Fey and Batman')
print('Now our hero is: ' + mo2.group())



# %%
# pipes can also help to match more than one pattern
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print("We're talking about the " + mo.group())
print('The unknown was that it would be the ' + mo.group(1) + ' part of the bat')


# %%
# optional matching with ?

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
mo1.group()

# the (wo)? part is optional

# %%
mo2 = batRegex.search('The adventures of Batwoman')
mo2.group()


# %%
# using the phone number example earlier...
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 543-767-1235')
print('Number found: ' + mo1.group())

mo2 = phoneRegex.search('My number is now 987-3456')
print('Number found: ' + mo2.group())


# %%
# match zero or more with *

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
mo1.group()

# %%
mo2 = batRegex.search('The adventures of Batwoman')
mo2.group()

# %%
mo3 = batRegex.search('The adventures of Batwowowowoman')
mo3.group()


# %%
# match 1 or more with +

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
mo1.group()

# %%
mo2 = batRegex.search('The adventures of Batwowowoman')
mo2.group()

# %%
mo3 = batRegex.search('The adventures of Batman')
mo3 == None


# %%
# repetitions with braces {}

# These are both the same -
# (Ha){3}
# (Ha)(Ha)(Ha)

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()


# %%
mo2 = haRegex.search('Ha')
mo2 == None


# %%
# greedy and non-greedy matching
# greedy matching matches on the longest possible string,
# non-greedy on the shortest possible string.
# for non-greedy, add a ? after the braces

greedyRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyRegex.search('HaHaHaHaHa')
mo1.group()

# %%
nongreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyRegex.search('HaHaHaHaHa')
mo2.group()


# %%
# findall finds everything, whereas search returns the first match
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 345-765-1234 Work: 765-789-7654')
mo.group()

# %%
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # no groups
phoneNumRegex.findall('Cell: 345-765-1234 Work: 765-789-7654')

# there are no groups in the regex, so findall will return a list of strings
# %%
# if there are groups in the regex then findall returns a list of tuples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # no groups
phoneNumRegex.findall('Cell: 345-765-1234 Work: 765-789-7654')


# %%
# character classes go in square brackets []
# there are also some shorthand codes for common character classes

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, blah blah')
# %%

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

# %%
# the caret character creates a negative class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')


# %%
# caret and dollar signs indicate that a match must occur at 
# the beginning or end of searched text

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')

# %%
beginsWithHello.search('He said Hello') == None

# %%
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
# %%
endsWithNumber.search('Your number is forty two') == None

# %%
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567')

# %%
wholeStringIsNum.search('2354vb456') == None
# %%
wholeStringIsNum.search('2354 456') == None


# %%
# wildcard character - .
# a . will matching anything but a new line

atRegex = re.compile(r'.at')
atRegex.findall('The cat sat in the that hat')

# %%
# .* matches everything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
# %%
mo.group(2)

# %%
# .* uses greedy mode. Use ? to make it non-greedy

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()

# %%
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

# %%
# use re.DOTALL to allow . to match new lines
noNewLineRegex = re.compile('.*')
noNewLineRegex.search('Serve the public trust.\nProtect the innocent.').group()

# %%
NewLineRegex = re.compile('.*', re.DOTALL)
NewLineRegex.search('Serve the public trust.\nProtect the innocent.').group()


# %%
# case sensitive matching
# use re.IGNORECASE or re.I to make regex case insensitive

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop').group()


# %%
# substituting strings using sub
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave documents to Agent Simon')

# %%
# enter text from group with sub
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice knew Agent Simon was a double agent.')

# %%
# complex regex can be split up over multiple lines to make it easier to follow

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|.ext)\s*\d{2,5})?)')

# use re.VERBOSE to break it up over multiple lines with comments...

# %%
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|.ext)\s*\d{2,5})?    # extension
)''', re.VERBOSE)

# %%
# use | to combine second arguments (re can only take one second argument)

someRegexValue = re.compile('foo', re.IGNORECASE| re.DOTALL | re.VERBOSE)