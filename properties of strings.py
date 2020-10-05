mystring = ("lancaster")
times = 0
letter = input("input the letter you want to check")
for index in range (0 ,len(mystring) - 1):
    if mystring[index] == "letter":
        times = times + 1
print ("no of times",letter,"appears:",times)
