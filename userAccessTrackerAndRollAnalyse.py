userList = [
    ("Alice", "Developer", "Germany"),
    ("Bob", "Tester", "Pakistan"),
    ("Charlie", "Project Manager", "Italy"),
    ("David", "Analyst", "Spain"),
    ("Eva", "Designer", "Germany"),
    ("Farhan", "Developer", "Pakistan"),
    ("Gina", "Tester", "Italy"),
    ("Hugo", "Project Manager", "Spain"),
    ("Ines", "Analyst", "Germany"),
    ("Junaid", "Designer", "Pakistan"),
    ("Karl", "Developer", "Italy"),
    ("Lina", "Tester", "Spain"),
    ("Maria", "Project Manager", "Germany"),
    ("Naseer", "Analyst", "Pakistan"),
    ("Oskar", "Designer", "Italy"),
    ("Paula", "Developer", "Spain"),
    ("Qasim", "Tester", "Germany"),
    ("Rosa", "Project Manager", "Pakistan"),
    ("Stefan", "Analyst", "Italy"),
    ("Tariq", "Designer", "Spain"),
    ("Ursula", "Developer", "Germany"),
    ("Viktor", "Tester", "Pakistan"),
    ("Walter", "Project Manager", "Italy"),
    ("Xenia", "Analyst", "Spain"),
    ("Yusuf", "Designer", "Germany"),
    ("Zara", "Developer", "Pakistan")
]

# while True:
#     name = input("Enter your Name: ").strip()
#     roll = input("Enter your Roll: ").strip()
#     country = input("Enter your Country: ").strip() 
    
#     userList.append((name, roll, country))
    
#     print(name, roll, country, "is successfully added")
#     breaking = input("Add one more User?? y/n:  ").lower()
#     if breaking == "n":
#         break
        
print(userList)  
  
countrySet = set()
for user in userList:
    countrySet.add(user[2])
    
print("country visited", countrySet)

for count in userList:
    pakistan = 0
    germany = 0
    italy = 0
    spain = 0
    if count(user[2]) == "Pakistan":
        pakistan +=1
    elif count(user[2]) == "Germany":
        germany +=1
    elif count(user[2]) == "Italy":
        italy +=1
    else:
        spain += 1 
        
        
print(pakistan,germany,italy,spain)

    
