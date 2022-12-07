list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('The sum of list is:', sum(list_numbers))


range_numbers = range(0, 11)
print('The sum of list range is:', sum(range_numbers))


counter = 0
for i in list_numbers:
    counter = counter + i
    print(counter)
