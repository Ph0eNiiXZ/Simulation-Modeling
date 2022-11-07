# **Rollercoaster Queueing Simulation**
## **Process & Overview**
- ride opens
- people may start entering the queue
- the ride starts operating once there is enough people in the queue to fill in a ride's capacity
- if there is more than one vehicle, the next vehicle will take 10 seconds to dock the station after the preceding vehicle was released
- when a vehicle is stationed, if there are riders on the vehicle they shall exit the system and the people enqueued shall enter the vehicle
- once a vehicle finishes the ride according to the given ridetime, it checks if station is empty; if it is empty, the vehicle will dock instantly. if it is not the vehicle will wait at the waiting station until it is empty again
- and the processes repeats

## **Probability Distribution Tables**

|Time between arrivals (seconds) |   Probability|
|--------------------------------|--------------|
|                            10  |   0.35       |
|                            20  |   0.25       |
|                            30  |   0.15       |
|                            40  |   0.15       |
|                            50  |   0.075      |
|                            60  |   0.025      |

> Let the number of people that will arrive along the time between arrivals be generated and randomized using  **Poisson Distribution** (lambda = 4)

|Ride service time (seconds)|Probability|
|---|---|
|30|0.6|
|35|0.2|
|40|0.1|
|45|0.05|
|50|0.025|
|55|0.015|
|60|0.01|

> Note that the **ride service time** excludes the **actual ride time**. It is for the  **service time** for when finished riders **exits** and new riders **enters** the vehicle at the station.
