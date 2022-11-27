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
timestampsA = []
timestampsB = []
total_arrival = 0
total_depart = 0
total_system = 0

"""
Global Poisson Generator
"""
def generate_poisson():
    return np.random.poisson(lam=5)

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
        return f"The ride,'{self.name}', has {self.ridetime} minutes riding time, {self.ridecapacity} seats, and {self.vehiclecount} vehicles."

"""
Operations
"""

def enqueue(ride: RollerCoaster, env: simpy.Environment, servers: simpy.Resource):
    while True:
        yield env.timeout(np.random.choice(IAT, 1, IATprob))
        people_count = 0
        people_count = generate_poisson()
        print('%d rider(s) arrives at %d' % (people_count,env.now))
        timestampsA.append(env.now[0])
        print("!!! Arrival Time Log: ",timestampsA)
        global total_arrival, total_system, queued
        queued.append(people_count)
        print("!!! Queue Log:",queued)
        total_arrival = total_arrival + people_count
        print("- total arrivals:     ",total_arrival)
        total_system = total_system + people_count
        print("- total in the system:",total_system)
        env.process(rideoperate(ride, env, servers))

def rideoperate(ride: RollerCoaster, env: simpy.Environment, servers: simpy.Resource):
    with servers.request() as req:
        yield req
        global total_depart, total_system
        out = get_total_seat(ride.ridecapacity)
        total_depart += out
        print("+ Ride starts and is released from the station")
    
        print("- total depart: ",total_depart)
        total_system -= out
        print("- total in the system:",total_system)
        yield env.timeout(ride.ridetime_seconds + np.random.choice(ServiceTime, 1, ServiceTimeProb))
        timestampsB.append(env.now[0])
        print("!!! Departure Time Log: ",timestampsB)
        print("+ Ride ends and docks at the station at %d" % env.now)
        print("...Current riders departs from the vehicle...")

def get_total_seat(ride_capacity: int):
    global queued
    total_seats = 0
    idx = 0
    for i in range(len(queued)):
        idx += 1
        if total_seats + queued[i] > ride_capacity:
            queued[i] -= ride_capacity - total_seats
            total_seats = ride_capacity
            break
        total_seats += queued[i]
    queued = queued[idx:]
    return total_seats

def get_time_sys(arr, dep):
    for a, d in zip(arr, dep):
        yield d - a


"""
Simulation
"""
env = simpy.Environment()

ride1 = RollerCoaster(env, "Mark1", 90, 12, 2)

servers = simpy.Resource(env, capacity=ride1.vehiclecount)

env.process(enqueue(ride1, env, servers))

env.run(until=600)

sys_time = list(get_time_sys(timestampsA, timestampsB))
expected_sys_time = sum(sys_time) / len(sys_time)

print("----------------------------------------")
print(ride1)
print("The expected system time: ", expected_sys_time,"seconds")
print("----------------------------------------")