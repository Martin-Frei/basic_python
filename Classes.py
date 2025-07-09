

class sellMeat:
    def __init__ (self,meat, price):
        self.meat = meat
        self.price = price
        
    def __str__(self):
        return f"The price of {self.meat} is {self.price} Euro"

meat1 = sellMeat("Beef", 12.00)
print(meat1.meat)
print(meat1.price)
print(meat1)


def chek_day(day):
    match day:
        case "monday":
            print(" Beginn of the week 😩")
        case "Freitag":
            print("Near weekend 😎")
        case "Samstag" | "Sonntag":
            print("weekend! 🎉")
        case _ :
            print("A normaly day")


from datetime import datetime

class toDoList:
    def __init__(self,dateTime):
        self.dateTime = dateTime
        
    def __str__(self):
        return f"The time of this task is {self.dateTime}"

class addTask(toDoList):
    def __init__(self, headline, task, dateTime = None):
        dateTime = datetime.now().strftime("%Y-%m-%d %H:%M")
        super().__init__(dateTime)
        self.headline = headline
        self.task = task
        
    def __str__(self):
        return f"{self.dateTime}: {self.headline}: {self.task}"
    
    
        
        
task1 = addTask("Lern Python", "inheritance")
print(task1)
task2 = addTask("learning Python", "Topic: inheritance", "2023-12-01 14:00" )
print(task2)