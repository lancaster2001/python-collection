fee = 3
cost = 0
miles = int(input("how many miles did you do?"))
miles = miles - 1
cost_for_miles = 2 * miles
passengers = int(input("how many passengers is there?"))
if passengers > 4:
    passengers = passengers - 4
elif passengers <= 4:
        passengers = 0
cost_for_passengers = 2 * passengers
cost = cost + fee + cost_for_miles + cost_for_passengers

time = int(input("is the time between 8am and 8pm? 1=yes 0=no"))
if time == 1:
    print (cost)
elif time == 0:
    cost = cost * 2
    print (cost)
