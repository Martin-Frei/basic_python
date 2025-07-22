class device():
    def __init__(self,name,isOn):
        self.name = name
        self.isOn = isOn
        
    def __str__(self):
        return f"{self.name} is {self.isOn}"
    
class computer(device):
    def __init__(self,name,isOn, cpu):
        super().__init__(name,isOn)
        self.cpu = cpu
    
    def __str__(self):
        return f"{self.name} is {self.isOn} and run with {self.cpu}"
    
class lamp(device):
    def __init__(self,name,isOn,wattage):
        super().__init__(name,isOn)
        self.wattage = wattage
    
    def __str__(self):
        return f"{self.name} is {self.isOn} and need {self.wattage} watt"
    
device1 = device("stoven","off")
computer1 = computer("Amiga", "on", "286er") 
lamp1 = lamp("Lamp", "off", 100 )  

print(device1)
print(computer1)
print(lamp1)