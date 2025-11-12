# Importing the module random
import random

# Setting input from user to the variable 'species' for use later
species = input('Enter whether you are Human, Elf, or Dwarf: ')

# Conditional statements for if the species is 'Human', 'Elf' or 'Dwarf' and otherwise prints disbelief
if species == 'Human':
    print('Human! Very cool.')
elif species == 'Elf':
    print('Do you really have pointy ears?')
elif species == 'Dwarf':
    print('Are you a fan of the art deco period?')
else:
    print("That sounds made up, I don't believe you!")

# generates a random number between 0 and 100, assigns it to the variable x, then prints the number
x = random.randint(0, 100)
print(x)
