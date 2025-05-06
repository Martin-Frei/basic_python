# Slicing 

word = 'Python'
word2 = ' today'
word3 ='hello here i am'


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







