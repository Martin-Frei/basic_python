print(35/6)
print(3.14*10)
print(10+41)
print(10%4)
print(5**2)
print(5+9)*(15-7)


print("=== AND ===")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("1 and 2:", 1 and 2)                 # 2 (beides truthy → letzter Wert)
print("0 and 5:", 0 and 5)                 # 0 (0 ist falsy → sofort zurück)

print("\n=== OR ===")
print("True or False:", True or False)     # True
print("0 or 5:", 0 or 5)                   # 5 (0 ist falsy → zweiter Wert)
print("'' or 'Hello':", '' or 'Hello')     # Hello
print("[] or [1, 2]:", [] or [1, 2])       # [1, 2]

print("\n=== NOT ===")
print("not True:", not True)               # False
print("not 0:", not 0)                     # True (0 ist falsy)
print("not 'text':", not 'text')           # False ('text' ist truthy)
print("not []:", not [])                   # True (leere Liste = falsy)

print("\n=== Kombiniert ===")
x = 5
y = 0

if x and not y:
    print("x is truthy and y is falsy → Bedingung erfüllt")
else:
    print("Bedingung nicht erfüllt")