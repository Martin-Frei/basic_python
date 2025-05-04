integer1 = 20
float1 = 10.3
name1= "Hello" 
name2 ="World"
'''
print("Addition: ",integer1 + float1)
print("Subtraction: ",integer1 - float1)
print("Multiplication: ",integer1 * float1)
print("Division: ",integer1 / float1)
print("Reminder: ",integer1 % float1)
print("Floor Devision: ",integer1 //float1)
print("Power of 2 : ",integer1 **float1)

'''
'''
if not integer1 % 2:  
    print('Even')
else:
    print('odd')    

if integer1 % 2:
    print('Odd')
else:
    print('Even')
    
if float1 != 0 and (integer1 / float1) > 0:
    print(integer1 / float1)
else:
    print('Choose bigger than ZERO!')
'''

'''
# integer1 = 20
# float1 = 10.3  


print(float1 and integer1 )     # I get 20 because every variable is True
print(integer1 and float1)      # I get 10.3 because every variabl is True

print(0 or integer1 or float1)  # I get 20 because short circuit evaluation
print(integer1 or float1)       # I get 20 because short circuit evaluation
print(integer1 and float1)      # I get 10.3 because th last one is True
print([] or float1)             # i get the first True

print(not[1,2,3])               # I get False because List is truthy (contains Elements)
print(not 0)                    # I get True because Zero is falsy Value, opposit is True
print(not True)                 # I get False because Two is truthy, opposit is False

'''

# name1= "Hello" 
# name2 ="World"

string1 = "Hello World, how are you??"
 
if name1 in string1:
     print(name1, ' is in ', string1)
else:
    print( name1, ' is not present')
    
    
print(len(name1))
print(len(name2))
print(len(string1))
 
list1 = [1,2,3,4,5,6,7,8,9,0]
# print(len(integer1))          # Integer have noch len function
# print(len(float1))            # Integer have noch len function

print(len(list1))

print(len(str(abs(integer1))))
print(len(str(abs(float1))))
print(str(abs(integer1)))
print(str(abs(float1)))