def checkDriverAge():
    age = input('What is your age?: ')
    if age.isdigit():
        if int(age) < 18 or int(age) > 70:
            print('Sorry, you cannot drive this car. Powering off')
        elif int(age) > 18 and int(age) <= 70:
            print('Powering On. Enjoy the ride!')
        else:
            print('Congratulations on your first year of driving. Enjoy the ride!')
    else:
        print('Not defined')


checkDriverAge()
# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.
