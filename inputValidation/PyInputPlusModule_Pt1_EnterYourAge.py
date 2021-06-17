# this script follows along to the Input Validation chapter 
# in ATBSWP
# 2021-06-11

# Input validation code makes sure entered values are formatted properly

# For example - enter your age program.

# %%
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}.')

# This isn't a great way to do input validation because you have to think of every scenario and
# manually write in an exception. You could miss certain cases. 

# PyInputPlus module helps with this.

# Go to Part 2!
# %%
