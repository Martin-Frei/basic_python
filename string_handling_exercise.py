
string1 = 'Today is a pretty day'
string2 = 'otto222'
string3 = "hello my name ist Martin object has no attributeww object has no attributew object has no attribute222 "
revers = string1[::-1]
print(revers)


print(string2 == string2[::-1])
print(string1 == string1[::-1])
print(string2[::-1])


count = 0
vowel = "a,e,i,o,u,A,E,I,O,U"
for elem in string1:
    if elem in vowel:
        count += 1        
print(count)        

vowel2 = vowel.replace(",", "-")
print(vowel2)

print(len(string1))

listnew = string3.split()
print(listnew)
print(len(listnew))



count = 0
for elem in listnew:
    if len(elem) >= 6:
        print(elem)
        count +=1        
        
print("Count is :" ,count)

print(string1.lower())
print(string1.upper())
print(string1.capitalize())
print(string1.title())
print(string1.swapcase())

print(string2)
print(string2.isalnum())
print(string2.isalpha())
print(string2.isdigit())
print(string2.isnumeric())

print(string1)
words =string1.split()
print(words)
newstring = " ".join(words)
print(newstring)