car = {
    "brand" : "Ford",
    "model": "Mustang",
    "year" : 1964
}

x = car.values()
print(x)
car["year"] = 2020
print(x)

car["color"] ="red"
print(x)

print(car.items())

for elem in car:
    print(elem)
    
for elem in car.values():
    print(elem)
    
for key, value in car.items():
    print(key , value)
    
carNew = car.copy()

carNew2 = dict(car)


myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Karl",
        "year": 2004
    }
}

print(myFamily)


for x, obj in myFamily.items():
    print(x)
    for y in obj:
        print(y +':', obj[y])