# Exercise : Check for duplicates in list without using set:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
