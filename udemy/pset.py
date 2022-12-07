def pset(list):
    res = []
    for index in reversed(range(len(list))):
        newlist = list[:index] + list[index+1:]

        result = pset(newlist)
        for item in result:
            if item not in res:
                res.append(item)
    res.append(list)
    return res

# pset([1, 2, 3]) -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


print(pset([1, 2, 3]))
