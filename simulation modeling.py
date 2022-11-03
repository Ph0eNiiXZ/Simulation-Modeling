class RollerCoasterInfo:
    def __init__(self, name, ridetime):
        self.name = name
        self.time = ridetime/60
    
    def __str__(self):
        return f"The ride, {self.name}, has {self.time} minutes riding time."

ride1 = RollerCoasterInfo("Phoenix", 180)
print(ride1.name)
print(ride1.time)
print(ride1)