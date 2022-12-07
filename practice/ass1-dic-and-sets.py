# Print the answers to the following questions **by manipulating the given dictionary of sets**.

prog_skills = {'Chris': {'C#', 'Java'},
               'Laura': {'Python', 'C++', 'JavaScript'},
               'Paula': {'Java', 'Python'}}

print('What languages can Paula code in?')
print('Paula can code in {}.'.format(prog_skills['Paula']))

print('How many languages can Laura code in?')
print('Laura codes in {} languages.'.format(len(prog_skills['Laura'])))

print('What language do both Chris and Paula master?')
print('They both code in {}'.format(
    prog_skills['Chris'].intersection(prog_skills['Paula'])))
