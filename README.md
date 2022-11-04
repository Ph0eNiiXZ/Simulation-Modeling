# **Rollercoaster Queueing Simulation**
## **Process Overview**
- people will first be checked off their corresponding type of queue to enter 
- people enter the corresponding queue
- people wait for the ride
- special pass gets prioritized
- people enter ride until capacity is filled
- ride starts
- ride ends and people exits the system

## **Probability distribution tables**

|Time between arrivals (seconds) |   Probability|
|--------------------------------|--------------|
|                            5   |   0.5        |
|                            10  |   0.2        |
|                            15  |   0.1        |
|                            20  |   0.075      |
|                            25  |   0.075      |
|                            25+ |   0.05       |

|Ride service time (seconds)|Probability|
|---|---|
|180|0.6|
|190|0.2|
|200|0.1|
|210|0.05|
|220|0.025|
|220+|0.025|

> Note that **ride service time** includes the **actual ride time** and the  **service time** for when finished riders exits and new riders enters the vehicle

## **To do**

1. generate arrival time with a uniform distribution
2. random 1-10 and distributed along the corresponding probability
3. using normal distribution, generate and randomize the number of people (between 1-10) that will enter the system correspondingly at a point of time




## **What to find**
- min-max-mean of the queue length
- distribution of queue length throughout a selected period of time 
