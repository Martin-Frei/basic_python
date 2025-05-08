# Slicing 

word = 'Python'
word2 = ' today'
word3 ='hello here i am'
vowels ='AaEeIiOoUu'

word5 = 'Python3'

print(word[::-1])                   # nohtyP
print(word[::2])                    # Pto

print(len(word))                    # 6
print(word+ word2)                  # Python today

print(word3.upper())                # HELLO HERE I AM
print(word.lower())                 # python
print(word3.title())                # Hello Here I Am
print(word3.capitalize())           # Hello here i am

word4 = ' Hello '
print(word4.strip())                # Hello
print(word4.lstrip())               # Hello
print(word4.rstrip())               #  Hello

print(word3.replace('here', 'there'))# hello there i am
# replace all 
print(word3.find('am'))             # 13
# find the first 
# print(word.find('a','e','i', 'o','u'))
TheVowles = sum(1 for char in word3 if char in vowels)
print(TheVowles)



print(word5.isalpha())              # False
print(word5.isdigit())              # False
print(word5.isalnum())              # True
print(" ".isspace())                # True

print(f'my Name is {word5} and it is beautiful {word2}')
# my Name is Python3 and it is beautiful today
print('my Name is {} and it is beautiful {}'.format(word5,word2))
# my Name is Python3 and it is beautiful today
print('my Name is {0} and it is beautiful {1} '.format(word5,word2))
# my Name is Python3 and it is beautiful today

palindrom = "otto"
print(palindrom[::-1])              # madam
print(palindrom == palindrom[::-1]) # True
print(word3)                        # hello here i am
print(word3[:-1:2])                 # hlohr
print(word3[::-2])                  # m  rholh
print(word3[::2])                   # hlohr  m


print(word3)
string = word3.split()              # split automaticly default with spaces
print(string)                       # String is now a list []
joined= " ".join(string)            # String is now a string again
print(joined)
joined2 = "-".join(string)          # String is now a hiphen seperatetd string again
print(joined2)
joined3 = "*".join(string)          # String is now a asterix seperatetd string again
print(joined3)


print("Zoo" < "apple")              # True, weil "Z" < "a" im Unicode
print("Apple" < "apple")            # True, weil "A" < "a"
print("apple" < "applepie")         # True


name = "Martin"
age = 53
print(f"My name is {name} and I am {age} years old.")
# My name is Martin and I am 53 years old.
print(f"In 10 years I will be {age + 10} years old.")
# In 10 years I will be 63 years old.

new_length=[]                       # empty list
new_list = word3.split()            # split word3 (= string!!) into new_list (= list!!)
for elem in new_list:               # looping trough the new_list 
    if len(elem)>3:                 # if the length of a elem (from new_list) greater tahn 3
        print(elem)                 # print elem
        new_length.append(elem)     # new_list appending the elem
print(new_list)                     # printing to check
print(new_length)
print(len(new_length))

