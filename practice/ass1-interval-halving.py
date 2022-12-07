# Write a program that asks the user to choose a number from 1 to 1000
# and then tries to guess that number by halving the search interval.
# Concretely, the user is prompted after each wrong guess of the program
# to reveal if their choice is higher or lower than the previous guess
# and then halves again the next subinterval.

# Make sure the program stops when the maximum number of possible halving
# steps is reached (what is this number?). Also make sure you handle unallowed
# user inputs accordingly.

# Here is an example of how the program would react, if the user thought of **523**:

# ```
# Think of a number from 1 to 1000
# Have you thought of 500? y/n: n
# Is it lower or higher than 500? l/h: h
# Have you thought of 750? y/n: n
# Is it lower or higher than 750? l/h: l
# Have you thought of 625? y/n: n
# Is it lower or higher than 625? l/h: l
# Have you thought of 562? y/n: n
# Is it lower or higher than 562? l/h: l
# Have you thought of 531? y/n: n
# Is it lower or higher than 531? l/h: l
# Have you thought of 515? y/n: n
# Is it lower or higher than 515? l/h: h
# Have you thought of 523? y/n: y
# Yeah, I guessed correctly in 7 steps!
# ```


from math import log2
import time

a, b = 1, 1000  # interval margins
counter = 1    # counts the number of guesses
maxSteps = 10
print("Think of a number from 1 to 1000")
time.sleep(1)  # wait 1 second before proceeding

while True:
    # Calculate the middle of the range
    middleRange = int((a+b)/2)

    # Ask if this is correct
    clientAnswer = input(f'Have you thought of {middleRange}? y/n:')
    if clientAnswer == 'y':
        print(f'Yeah, I guessed correctly in {counter} steps!')
        break
    else:
        # Calculate new range based on the no answer
        askLowerOrHigher = input(
            f'Is it lower or higher than {middleRange}? l/h:')
        if askLowerOrHigher == 'h':
            a = middleRange
        else:
            b = middleRange
    # Check if we reached the max steps
    if counter == maxSteps:
        print('Sorry, I could not guess your number')
        break
    counter += 1
