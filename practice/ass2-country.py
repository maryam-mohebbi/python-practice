# Copy the file *country_info.txt* from the lecture folder into the same folder as this notebook. Take a look inside the file to understand the data.

# Write a program that reads the file and stores all the country information in a suitable data structure.

# Afterwards, ask the user to enter a country name. Based on the user input, return the capital and currency of that country. The user should be prompted to enter a new country until they type in **quit**. In case the input is not a country name in your data structure, notify the user accordingly and ask them to enter a new valid country. Below is an example of the output:

# ```python
# Please enter the name of a country: Germany
# The capital of Germany is Berlin. Their currency is Euro.
# Please enter the name of a country: Romania
# The capital of Romania is Bucharest. Their currency is Romanian leu.
# Please enter the name of a country: LaLaLand
# Sorry, I do not understand the input...
# Please enter the name of a country: quit

# ```

input_filename = 'country_info.txt'
countries = {}

# Open file and store data in a suitable format
with open(input_filename) as country_file:

    # Your code here
    for line in country_file:
        data = line.split('|')
        key = data[0].lower()
        if key == 'country' or key == '':
            continue
        countries[key] = {'name': data[0],
                          'currency': data[6].strip(), 'capital': data[1]}

    # Interact with the user as in the example output above
while True:

    # Your code here
    user_input = input('Please enter the name of a country: ')
    user_input = user_input.lower()
    if user_input == 'quit':
        break
    if user_input in countries.keys():
        name = countries[user_input]['name']
        capital = countries[user_input]['capital']
        currency = countries[user_input]['currency']
        print(
            f'The capital of {name} is {capital}. Their currency is {currency}.')
    else:
        print('Sorry, I do not understand the input...')
