#---------------- Challenges 1 ----------------#

#---------------- Part 1 ----------------#
#List []: ordered, mutable, duplicates.
#Set {}: unordered, mutable, no duplicates.
#Tuple (): ordered, imutable (cannot add/remove elements), duplicates.
#Dictonary[ key ]: unordered, mutable, no duplicate keys.

fruit_List = ['banana', 'apple', 'orange', 'banana', 'pineapple']
fruit_Set  = {'banana', 'apple', 'orange', 'banana', 'pineapple'}
fruit_Tuple= ('banana', 'apple', 'orange', 'banana', 'pineapple')
fruit_Dict = {10: 'banana', 20: 'apple', 30: 'orange', 40: 'banana', 20: 'pineapple'}
fruit_Dict2 = {'banana': 10, 'apple': 20, 'orange': 30, 'banana': 40, 'pineapple': 20}

print('## This is the export of each group ##')
print(f'fruit_List:  {fruit_List}')
print(f'fruit_Set:   {fruit_Set}')
print(f'fruit_Tuple: {fruit_Tuple}')
print(f'fruit_Dict:  {fruit_Dict}')
print(f'fruit_Dict2: {fruit_Dict2}')

#---------------- Part 2 ----------------#

def myCount(list, item):
    count = 0
    for fruit_item in list:
        if fruit_item == item:
            count += 1
    return count

def myCountDictByValue(dict, value):
    count = 0
    for myKey, myValue in dict.items():
        if myValue == value:
            count += 1
    return count

def myCountDictByKey(dict, key):
    count = 0
    for myKey, myValue in dict.items():
        if myKey == key:
            count += 1
    return count


fruit_List = ['banana', 'apple', 'orange', 'banana', 'pineapple']
fruit_Set  = {'banana', 'apple', 'orange', 'banana', 'pineapple'}
fruit_Tuple= ('banana', 'apple', 'orange', 'banana', 'pineapple')
fruit_Dict = {10: 'banana', 20: 'apple', 30: 'orange', 40: 'banana', 20: 'pineapple'}
fruit_Dict2 = {'banana': 10, 'apple': 20, 'orange': 30, 'banana': 40, 'pineapple': 20}

#For List
print(f'bag of fruits of type_{type(fruit_List)}')
for item in fruit_List:
    count = myCount(fruit_List, item)
    print('- counted ', count, 'x', item)
    
#For Set
print(f'bag of fruits of type_{type(fruit_Set)}')
for item in fruit_Set:
    count = myCount(fruit_Set, item)
    print('- counted ', count, 'x', item)
    
#For Tuple
print(f'bag of fruits of type_{type(fruit_Tuple)}')
for item in fruit_Tuple:
    count = myCount(fruit_Tuple, item)
    print('- counted ', count, 'x', item)

#For Dict
print(f'bag of fruits of type_{type(fruit_Dict)}')
for key, value in fruit_Dict.items():
    count = myCountDictByValue(fruit_Dict, value)
    print('- counted ', count, 'x', value)

#For Dict2
print(f'bag of fruits of type_{type(fruit_Dict2)}')
for key, value in fruit_Dict2.items():
    count = myCountDictByKey(fruit_Dict2, key)
    print('- counted ', count, 'x', key)