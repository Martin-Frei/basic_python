
# Ordered : Elemnts have a fixed orer
# immutabel cannot changed after creation 
# Allows Duolicates Same values can repeat 
# can store different dada types 
# can contain other tulpes 
# can be sued as dictinnary key if elementare immutabel 
# more lightwigth than lists 


t = 1 , 2 , 3
a,b,c = t 
print(a,b,c)

# # Packing
# t = 1, 2, 3

# # Unpacking
# a, b, c = t
# print(a, b, c)
a, *b,c = t
print(a,b,c)