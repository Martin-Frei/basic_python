# List is ordered and mutabel collection of different data types
# List could also be a nested list 
# List is index ordered
#  Methoden for List []

my_list = [ 'appel', 'orange','banana', 'kiwi' ]
my_list2 = ['tomato','cucumber','leek', 'onion']
my_numbers = [4,5,6,1,2,3,7,8,9]


# Hinzufügen
my_list.append('lemone')
print(my_list)  
#Output ['appel', 'orange', 'banana', 'kiwi', 'lemone']

my_list.insert(2,'pear')
print(my_list)  
# Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone']

my_list.extend(my_list2)
print(my_list)  
# Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone', 'tomato', 'cucumber', 'leek', 'onion']

# Entfernen

my_list.remove('tomato')
print(my_list)
#Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone', 'cucumber', 'leek', 'onion']

my_list.remove('cucumber')
print(my_list)
#Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone', 'leek', 'onion']

print('new List is here')
list_new =['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone', 'cucumber', 'leek', 'onion','appel']
print(list_new)
list_new.remove('appel')
print(list_new)

my_list.pop(6)
print(my_list)
#Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone', 'onion']

element = my_list.pop(6)
print(my_list)
# Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone']
print(element)
# Output onion    ==> without []  !!

my_list3 = ['apple', 'banana', 'kiwi']
my_list3.clear()
print(my_list3)
# Output: []


#Suchen und finden
count = my_list.count('appel')
print(count)
# Output 1

element2 = my_list.index('lemone')
print(my_list)
# Output ['appel', 'orange', 'pear', 'banana', 'kiwi', 'lemone']
print(element2)
# Output 5 

if 'tomato' in my_list:
    my_list.remove('tomato')

try:
    my_list.remove('appel')
    print("Element is removed from List")
    print(my_list)
except ValueError:
    print("Element is not in List")
    # Output Element is removed from List
    # Output ['banana', 'kiwi', 'lemone', 'orange', 'pear'] 
    
try:
    my_list.remove('cucumber')
    print("Element is removed from List")
except ValueError:
    print("Element is not in List")
    # Output Element is not in List
    
print('banana' in my_list)  
# Output: True
print('tomato' in my_list)  
# Output: False
    
    
# Sortieren und Umkehren
my_list.sort()
print(my_list)
# Output ['appel', 'banana', 'kiwi', 'lemone', 'orange', 'pear']

my_new_list2 = sorted(my_list2)
print(my_new_list2)
# Output ['cucumber', 'leek', 'onion', 'tomato']

my_numbers2 = sorted(my_numbers)
print(my_numbers)
# Output [4, 5, 6, 1, 2, 3, 7, 8, 9]
print(my_numbers2)
# Output [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_numbers2.reverse()
print(my_numbers2)
# Output [9, 8, 7, 6, 5, 4, 3, 2, 1]


# Längen und Summen
length = len(my_list)
print(length)
# Output 6

length2 = len(my_list2)
print(length2)
# Output 4

length3 = len(my_numbers)
print(length3)
# Output 9

quadrate = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
summe = sum(quadrate)
print(summe)
# Output 385


# List Slicing
part_of_list = my_list[ 1:4]
print(part_of_list)
# Output ['banana', 'kiwi', 'lemone']

part_of_quadrate = quadrate[3:5]  
print(part_of_quadrate)
# Output[16, 25]

part_of_quadrate2 = quadrate[-3:]  
print(part_of_quadrate2)
# Output[64, 81, 100]

last_of_quadrate = quadrate[-1]  
print(last_of_quadrate)
# Output[100]


# Kopieren und Referenzen
list2 = my_list2  # only a second referenz for my_list2
# changes in list2 change my_list2 also

list2 = my_list2.copy() # This is a real copy of my_list2
# changes in list2 only changes in list2 not in my_list2


# Iterieren und kombinieren
for index, fruit in enumerate(my_list):
    print(index, fruit)
# Output:
# 0 appel
# 1 banana
# 2 kiwi
# 3 lemone
# 4 orange
# 5 pear

num_list = [1,2,3,4,5,6]
for fruit, number in zip(my_list, num_list ):
    print(fruit, number)

# Output
# appel 1
# banana 2
# kiwi 3
# lemone 4
# orange 5
# pear 6


quadrate = [ x**2 for x in range(1, 11)]
print(quadrate)
# Output  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  
# Output [2, 4, 6, 8, 10]    

import this

print(dir([]))
print(dir())
print(dir({}))

# print(help([]))
# print(help())
print(help({}))

