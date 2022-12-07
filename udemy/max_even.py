def highest_even(list):
    even_list = []
    for item in list:
        if item % 2 == 0:
            even_list.append(item)
    return max(even_list)


print(highest_even([10, 2, 3, 4, 8, 11, 12, 20, 13, 54]))
