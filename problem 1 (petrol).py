cost = 0
petrol = input("what type of petrol do you want?")
litres = int(input("how many litres of petrol do you want?"))
if petrol == "unleaded":
    cost = 1.15 * litres
    elif petrol == "diesel":
    cost = 1.19 * litres
    elif petrol == "super_unleaded":
    cost = 1.18 * litres
    else print ("there was an error")
print ("£" cost)
