"""
Created on 03 November 2022 16:46:56

@author: Jirapit Sripitak
"""

import simpy
import numpy as np

"""
Probability Distribution Tables
"""
IAT = [10,20,30,40,50,60]
IATprob = [0.35,0.25,0.15,0.15,0.075,0.025]
ServiceTime = [30,35,40,45,50,55,60]
ServiceTimeProb = [0.6,0.2,0.1,0.05,0.025,0.015,0.01]

"""
Global Settings
"""
queued = []
on_ride = []
total_arrival = 0
total_depart = 0
total_system = 0
docking_time = 10

"""
Global Poisson Generator
"""
def generate_poisson():
    return np.random.poisson(lam=4)

"""
Rollercoaster Informations
"""
class RollerCoaster:
    def __init__(self, env, name, ridetime_seconds, ridecapactiy, vehiclecount):
        self.env = env
        self.name = name
        self.ridetime = int(ridetime_seconds/60)
        self.ridetime_seconds = ridetime_seconds
        self.ridecapacity = ridecapactiy
        self.vehiclecount = vehiclecount
    
    def __str__(self):
        return f"The ride,'{self.name}', has {self.ridetime} minutes riding time,{self.ridecapacity} seats, and {self.vehiclecount} vehicles."

"""
Operations
"""

current_queue = 0

def enqueue(ride: RollerCoaster, env: simpy.Environment, servers: simpy.Resource):
    while True:
        yield env.timeout(np.random.choice(IAT, 1, IATprob))
        people_count = 0
        people_count = generate_poisson()
        print('%d rider(s) arrives at %d' % (people_count,env.now))
        global total_arrival, total_system, current_queue
        current_queue += people_count
        total_arrival = total_arrival + people_count
        print("- total arrivals:     ",total_arrival)
        total_system = total_system + people_count
        print("- total in the system:",total_system)
        queued.append(people_count)
        print("!!! Queue Log:",queued)
        if current_queue > ride.ridecapacity:
            env.process(rideoperate(ride, env, servers))
            current_queue -= ride.ridecapacity

def rideoperate(ride: RollerCoaster, env: simpy.Environment, servers: simpy.Resource):
    with servers.request() as req:
        yield req
        print("+ Ride starts and is released from the station")
        yield env.timeout(ride.ridetime_seconds + np.random.choice(ServiceTime, 1, ServiceTimeProb))
        print("- Ride ends and docks at the station at %d" % env.now)
        print("...Current riders departs from the vehicle...")

"""
Simulation
"""
env = simpy.Environment()

ride1 = RollerCoaster(env, "Phoenix", 90, 10, 2)

servers = simpy.Resource(env, capacity=ride1.vehiclecount)

env.process(enqueue(ride1, env, servers))

env.run(until=180)