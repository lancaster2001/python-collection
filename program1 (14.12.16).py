print ("type ""0"" to stop")
total = 0
print("total =", total)
number = int(input("input a number"))
while number > 0:
    total = total + number
    print ("total =", total)
    number = int(input("input a number"))
    print ("number =", number)
print (total)
