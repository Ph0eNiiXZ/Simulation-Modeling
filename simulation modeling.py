import random
import simpy

RANDOM_SEED = 69
SIM_TIME = 100

random.seed(RANDOM_SEED)
env = simpy.Environment()

class RollerCoasterInfo:
    def __init__(self, env, name, ridetime, ridecapactiy, vehiclecount):
        self.env = env
        self.name = name
        self.ridetime = int(ridetime/60)
        self.ridecapacity = ridecapactiy
        self.number_of_vehicles = vehiclecount
        self.time = simpy.Store(env)
    
    def __str__(self):
        return f"The ride,'{self.name}', has {self.ridetime} minutes riding time."

ride1 = RollerCoasterInfo("env", "Phoenix", 180, 12, 2)
print(ride1)
