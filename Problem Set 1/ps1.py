###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    start = time.time()
    cowList = []
    trip = []
    wholeTrip = []

    for key, value in cows.items():
        temp = [key,value]
        cowList.append(temp)
    

    cowList.sort(key=lambda x: x[1], reverse = True)
    
    flattenedWholeTrip = [item for sublist in wholeTrip for item in sublist]
    #Cada Loop es un viaje:
    while len(flattenedWholeTrip) < len(cowList):
        
        print("es menor?")
        print(str(len(flattenedWholeTrip) ) + " <? " + str(len(cowList)))
        trip = []
        spaceAvailable = limit

        #recorro la lista ordenada y subo las vacas que entran.
        for i in range(len(cowList)):
            
            if cowList[i][1] <= spaceAvailable and cowList[i][0] not in flattenedWholeTrip:
                trip.append(cowList[i][0])
                spaceAvailable -= cowList[i][1]
            print(str(i) + " --> " + str(spaceAvailable)+ " --> " + str(trip))


        #Cargo el trip a la lista de viajes
        wholeTrip.append(trip)
        #Actualizo flattenedWholeTrip para ver si cumple la condicion del While
        flattenedWholeTrip = [item for sublist in wholeTrip for item in sublist]

    
    end = time.time()
    print(end - start)         
    return wholeTrip


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #start = time.time()
    cowList = []
    allTrips = []

    for key, value in cows.items():
        temp = (key,value)
        cowList.append(temp)
    
    for item in (get_partitions(cowList)):
        allTrips.append(item)
    
    weights = []
    weight = 0
    setOfTripsToArrange = []
    
    #Los ordeno por cantidad de viajes en cada set, de menor a mayor:
    #el 6 del principio significa que entraron 6 vacas en un viaje
    allTrips.sort(key=len)
    #los ordeno por cantidad de vacas en solo un viaje. Si uno hizo
    #un viaje de 5 y otro de 1 PERO otro hizo uno de 4 y otro de 2,
    #tiene prioridad el primero. 
    allTrips.sort(key=lambda t: len(t[0]), reverse = True)
    #El Codigo para ver todo esto es:
    #==============================================================================
    #         for setOfTrips in allTrips:
    #         for trip in setOfTrips:
    #             lista.append(len(trip))
    #         print(lista)
    #         lista = []
    #==============================================================================    
        
    
    #Recorro los setOfTrips
    for setOfTrips in allTrips:
        #Dentro de cada trip, recorro las vacas y sumo los pesos
        #print("Set of trips is: ")
        #print(setOfTrips)
        for trip in setOfTrips:
            for cow in trip:
                weight += cow[1]
            #print()
            #print(str(trip) + " weighs:    " + str(weight))
            weights.append(weight)
            #Deespues de recorrer todas las vacas reseteo weight
            weight = 0
        #Si el peso es mayor, paso al siguiente setOfTrips y reseto weights
        if max(weights) > limit:
            weights = []
            continue
        #Sino, guardo mi respuesta y corto el loop principal
        else:
            setOfTripsToArrange = setOfTrips
            break
    #print("setOfTripsToArrange")  
    #print(setOfTripsToArrange)
    
    result = []
    cowNameTrip = []
    
    #Transformo los tuples en strings
    for trip in setOfTripsToArrange:
        for cow in trip:
            cowName = cow[0]
            cowNameTrip.append(cowName)
        result.append(cowNameTrip)
        cowNameTrip = []
    
    #end = time.time()
    
    return result
        

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print("cows is :" + str(cows))

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


