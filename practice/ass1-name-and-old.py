# Write a short program that asks the user for their **name and age**. Afterwards, print **how long their name is and when they were born**. Example of the expected below:

import datetime

today = datetime.datetime.now()
currentYear = today.year

name = input('What is your name? ')
age = input('How old are you? ')
nameLength = len(name)
birthYear = currentYear - int(age)
print(
    f'Heloo, {name}! Your name has {nameLength} letters and you were born in {birthYear}.')
