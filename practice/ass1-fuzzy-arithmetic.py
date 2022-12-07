# onsider all natural numbers up to (and including) 30.
# Print out for each number whether it is a **multiple of 3, of 5, of both or none**.

naturalNum = list(range(1, 31, 1))
for i in naturalNum:
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} is a multiple of 3 and 5')
    elif i % 3 == 0:
        print(f'{i} is a multiple of 3')
    elif i % 5 == 0:
        print(f'{i} is a multiple of 5')
    else:
        print(f'{i} is none')
