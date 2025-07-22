# with Copilot
# This code demonstrates the use of classes and inheritance in Python.
# It defines a base class `device` and two derived classes `computer` and `lamp`.
# Each class has its own attributes and a string representation method. 


# class device:
#     def __init__(self, name, isOn):
#         self.name = name
#         self.isOn = isOn

#     def __str__(self):
#         return f"{self.name} is {self.isOn} ."

# class computer(device):
#     def __init__(self, name, isOn, cpu):
#         super().__init__(name, isOn)
#         self.cpu = cpu

#     def __str__(self):
#         return f"{self.name} with {self.cpu} CPU is {self.isOn} ."

# class lamp(device):
#     def __init__(self, name, isOn, wattage):
#         super().__init__(name, isOn)
#         self.wattage = wattage

#     def __str__(self):
#         return f"{self.name} with {self.wattage}W is {self.isOn} ."
    
# device1 = device("Generic Device", "on")
# computer1 = computer("Gaming PC", "on", "Intel i9")     
# lamp1 = lamp("Desk Lamp", "off", 60)

# print(device1)
# print(computer1)
# print(lamp1)

# oop polymorphism example
# def print_device_info(device):
#     print(device)   
    
class device():
    def __init__(self,name,isOn):
        self.name = name
        self.isOn = isOn
        
    def __str__(self):
        return f"{self.name} is {self.isOn}"
    
class computer(device):
    def __init__(self,name,isOn,cpu):
        super().__init__(self,name,isOn)
        self.cpu = cpu
    
    def __str__(self):
        return f"{self.name} is {self.isOn} and run with {self.cpu}"
    
class lamp(device):
    def __init_(self,name,isOn,wattage):
        super().__init__(self, name,isOn)
        self.wattage = wattage
    
    def __str__(self):
        return f"{self.name} is {self.isOn} and need {self.wattage} watt"
    
device1 = device("stoven","off")
computer1 = computer("Amiga", "on", "286er") 
lamp1 = lamp("Lamp", "off", 100 )  

print(device1)
print(computer1)
print(lamp1)